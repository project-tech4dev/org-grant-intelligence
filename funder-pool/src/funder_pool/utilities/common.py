"""Shared assembly for every utility: in_sangam, scoring, ingest queue, validation and writing outputs."""
import json
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd

from ..core import config, ids, matching, report, sangam, schema, scoring
from ..core.paths import DATA
from ..core.provenance import Ledger, write_csv


@dataclass
class Build:
    """Accumulates one utility's rows. Funders are keyed by funder_id."""
    category: str
    pool: dict[str, dict] = field(default_factory=dict)
    signals: dict[str, dict] = field(default_factory=dict)
    review: list[dict] = field(default_factory=list)
    drops: list[dict] = field(default_factory=list)
    ledger: Ledger = field(default_factory=Ledger)

    def __post_init__(self):
        cfg = (config.load_yaml("aliases.yaml") or {}).get(self.category) or {}
        self.canonical = {matching.normalise(a): canon for canon, al in cfg.items() for a in [canon, *al]}

    def fid(self, name: str) -> str:
        return ids.funder_id(matching.normalise(self.canonical.get(matching.normalise(name), name)), self.category)

    def candidates(self) -> dict[str, str]:
        """{key: name} over every funder name and alias, key = 'funder_id||n'. Use with key.split('||')[0]."""
        out = {}
        for fid, r in self.pool.items():
            for i, n in enumerate([r["name"], *r["aliases"]]):
                out[f"{fid}||{i}"] = n
        return out

    def add_funder(self, name: str, *, source_key: str, **fields) -> str:
        """Create or extend a funder. Lists (aliases, sources, notes) are merged; first non-blank scalar wins."""
        canon = self.canonical.get(matching.normalise(name))
        if canon and canon != name and not fields.get("funder_id"):
            fields["aliases"] = [name, *(fields.get("aliases") or [])]
            name = canon
        fid = fields.pop("funder_id", None) or self.fid(name)
        row = self.pool.setdefault(fid, {"funder_id": fid, "category": self.category, "name": name,
                                         "aliases": [], "sources": [], "notes": []})
        if source_key not in row["sources"]:
            row["sources"].append(source_key)
        for a in fields.pop("aliases", []) or []:
            if a and a != row["name"] and a not in row["aliases"]:
                row["aliases"].append(a)
        note = fields.pop("notes", "")
        if note and note not in row["notes"]:
            row["notes"].append(note)
        for k, v in fields.items():
            if v not in (None, "") and not row.get(k):
                row[k] = v
        return fid

    def add_alias(self, fid: str, alias: str) -> None:
        row = self.pool[fid]
        if alias and alias != row["name"] and alias not in row["aliases"]:
            row["aliases"].append(alias)

    def drop(self, name: str, source_key: str, reason: str) -> None:
        self.drops.append({"name": name, "source_key": source_key, "reason": reason})

    def queue(self, fid: str, issue: str, candidates: str = "", action: str = "") -> None:
        code = schema.issue_enum(issue)  # schema enum; the detail goes into suggested_action
        detail = "" if issue == code else issue
        self.review.append({"funder_id": fid, "issue": code, "candidates": candidates,
                            "suggested_action": f"{detail}: {action}" if detail and action else (detail or action),
                            "decision": ""})


def by_source_best(values: dict[str, float], preference: list[str]) -> tuple[float | None, str, bool]:
    """Pick india_usd_best by preference order. Never sums. sources_disagree if any two known values differ >50%."""
    known = {k: v for k, v in values.items() if v is not None and not pd.isna(v)}
    best, used = None, ""
    for k in preference:
        if k in known:
            best, used = known[k], k
            break
    if best is None and known:
        used = sorted(known)[0]
        best = known[used]
    # single-year lower bounds (keys ending _1yr) are not comparable with window totals
    vals = [v for k, v in known.items() if v > 0 and not k.endswith("_1yr")]
    disagree = len(vals) > 1 and max(vals) > 1.5 * min(vals)
    return best, used, disagree


def finalize(b: Build, outdir_name: str, *, value_col: str, bins: list[float], unit: str,
             size_col: str = "total_giving_usd_5y", notes: list[str] | None = None,
             extra_signal_cols: list[str] | None = None) -> dict[str, pd.DataFrame]:
    """Compute in_sangam, score, write all outputs to data/<outdir_name>/. Returns the frames."""
    out = DATA / outdir_name
    funders, sangam_src = sangam.load()
    pool_rows = []
    for fid, r in sorted(b.pool.items()):
        r = dict(r)
        names = [r["name"], *r["aliases"]]
        st, hit = "no", ""
        for n in names:
            s, h = sangam.status(n, funders, r.get("cin", ""))
            if s == "yes" or (s == "related" and st == "no"):
                st, hit = s, h
            if st == "yes":
                break
        r["in_sangam"] = st
        if hit:
            r["notes"] = [*r["notes"], f"Sangam match: {hit} ({Path(sangam_src).name})"]
        r["aliases"] = "|".join(r["aliases"])
        r["sources"] = "|".join(sorted(r["sources"]))
        r["notes"] = "; ".join(r["notes"])
        pool_rows.append(r)
    pool = schema.conform(pd.DataFrame(pool_rows), schema.POOL).fillna("")

    sig = pd.DataFrame([{"funder_id": fid, **b.signals.get(fid, {})} for fid in pool["funder_id"]])
    for c in ("india_evidence_status",):
        sig[c] = sig.get(c, pd.Series("unknown", index=sig.index)).fillna("unknown").replace("", "unknown")
    scored = scoring.score(sig, b.category)
    if "india_usd_by_source" in scored.columns:
        scored["india_usd_by_source"] = scored["india_usd_by_source"].map(
            lambda d: json.dumps(d, sort_keys=True) if isinstance(d, dict) and d else "")
    weight_keys = list(config.category_weights(b.category).keys())
    signals = schema.conform(scored, schema.SIGNALS)
    keep_extra = [c for c in dict.fromkeys([*(extra_signal_cols or []), *weight_keys])
                  if c in signals.columns and c not in schema.SIGNALS]
    signals = signals[schema.SIGNALS + keep_extra]
    signals = signals.sort_values("rank_in_category").reset_index(drop=True)

    joined = pool.merge(signals, on="funder_id", how="left")
    iq = joined[joined["in_sangam"] != "yes"].copy()
    iq["notes"] = np.where(iq["in_sangam"] == "related", "related to a Sangam funder: " + iq["notes"].astype(str), iq["notes"])
    ingest = schema.conform(iq, schema.INGEST_QUEUE)[schema.INGEST_QUEUE].sort_values("rank_in_category")

    review = pd.DataFrame(b.review, columns=schema.REVIEW_QUEUE).drop_duplicates()
    review = review.sort_values(["issue", "funder_id"], kind="stable")
    drops = pd.DataFrame(b.drops, columns=["name", "source_key", "reason"]).sort_values(["source_key", "name"], kind="stable")
    evidence = b.ledger.evidence_df()
    sources = b.ledger.sources_df()

    problems = schema.duplicate_ids(pool) + schema.validate(pool, schema.POOL) + schema.validate(signals, schema.SIGNALS)
    if problems:
        raise ValueError("validation failed: " + "; ".join(problems[:20]))

    for name, df in [("pool", pool), ("signals", signals), ("review_queue", review), ("evidence", evidence),
                     ("sources_log", sources), ("ingest_queue", ingest), ("drop_log", drops)]:
        write_csv(df, out / f"{name}.csv")
    md = report.distribution_report(joined, b.category, value_col=value_col, bins=bins, unit=unit,
                                    size_col=size_col, notes=notes)
    (out / "distribution_report.md").write_text(md + "\n")
    return {"pool": pool, "signals": signals, "review_queue": review, "evidence": evidence,
            "sources_log": sources, "ingest_queue": ingest, "drop_log": drops, "joined": joined}

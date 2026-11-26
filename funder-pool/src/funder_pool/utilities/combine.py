"""Phase 7: merge the five utilities, flag cross-category duplicates, write data/combined/.

Rankings stay within each category: scores use different signals per category and are not comparable across them.
Cross-category duplicates are linked (column also_in) and sent to review; rows are never merged automatically,
because the category decides which help file and signals apply.
"""
from collections import defaultdict

import pandas as pd
from rapidfuzz import fuzz

from ..core import matching, report as rpt, schema
from ..core.paths import DATA
from ..core.provenance import write_csv

UTILS = {"western": "western_funders", "indian_csr": "indian_csr", "hni_family": "hni_family",
         "government_india": "government_india", "bilateral_multilateral": "bilateral_multilateral"}
SMALL = ["western", "hni_family", "government_india", "bilateral_multilateral"]  # fuzzy-matched against each other
OUT = DATA / "combined"


def _read(util: str, name: str) -> pd.DataFrame:
    p = DATA / util / f"{name}.csv"
    return pd.read_csv(p, dtype=str, keep_default_na=False) if p.exists() else pd.DataFrame()


def _names(row) -> list[str]:
    return [row["name"]] + [a for a in row["aliases"].split("|") if a]


def _stem_close(a: str, b: str) -> bool:
    sa, sb = matching.stem(a), matching.stem(b)
    return bool(sa and sb) and fuzz.token_sort_ratio(sa, sb) >= 90


def cross_category(pool: pd.DataFrame) -> list[dict]:
    """Pairs of rows in different categories that look like the same organisation."""
    pairs = {}
    # 1. shared external identifier
    for col in schema.IDENTIFIERS:
        sub = pool[pool[col] != ""]
        for v, g in sub.groupby(col):
            if g["category"].nunique() > 1:
                ids = sorted(g["funder_id"])
                for i, a in enumerate(ids):
                    for b in ids[i + 1:]:
                        pairs[(a, b)] = f"same {col} {v}"
    # 2. same normalised name or alias (all categories, including the 33k CSR companies)
    by_norm = defaultdict(set)
    for r in pool.to_dict("records"):
        for n in _names(r):
            by_norm[matching.normalise(n)].add(r["funder_id"])
    cat = dict(zip(pool["funder_id"], pool["category"]))
    for n, fids in by_norm.items():
        fids = sorted(fids)
        for i, a in enumerate(fids):
            for b in fids[i + 1:]:
                if cat[a] != cat[b]:
                    pairs.setdefault((a, b), f"same normalised name '{n}'")
    # 3. fuzzy and acronym matches among the smaller categories
    small = pool[pool["category"].isin([UTILS[u] for u in SMALL])]
    names = {r["funder_id"]: r["name"] for r in small.to_dict("records")}
    for r in small.to_dict("records"):
        others = {k: v for k, v in names.items() if cat[k] != r["category"]}
        dec, cands = matching.match(r["name"], others)
        if dec in {"acronym", "fuzzy", "ambiguous"}:
            for c in cands[:3]:
                if dec != "acronym" and not _stem_close(r["name"], c.name):
                    continue  # only 'foundation' in common ('UMA Foundation' vs 'UNM Foundation')
                a, b = sorted([r["funder_id"], c.key])
                pairs.setdefault((a, b), f"name match ({dec}, score {c.score:.0f})")
    return [{"funder_id_a": a, "funder_id_b": b, "evidence": why} for (a, b), why in sorted(pairs.items())]


def build() -> dict:
    pools, sigs, queues, reviews, logs, drops, missing = [], [], [], [], [], [], []
    for util, category in UTILS.items():
        p = _read(util, "pool")
        if p.empty:
            missing.append(util)
            continue
        pools.append(p)
        sigs.append(_read(util, "signals"))
        q = _read(util, "ingest_queue")
        queues.append(q)
        for name, acc in (("review_queue", reviews), ("sources_log", logs), ("drop_log", drops)):
            df = _read(util, name)
            if not df.empty:
                df.insert(0, "category", category)
                acc.append(df)
    pool = pd.concat(pools, ignore_index=True)
    sig = pd.concat(sigs, ignore_index=True)
    pool_all = schema.conform(pool.merge(sig, on="funder_id", how="left"), schema.POOL + schema.SIGNALS[1:])

    pairs = cross_category(pool)
    also = defaultdict(list)
    for p in pairs:
        also[p["funder_id_a"]].append(p["funder_id_b"])
        also[p["funder_id_b"]].append(p["funder_id_a"])
    pool_all["also_in"] = pool_all["funder_id"].map(lambda f: "|".join(sorted(also.get(f, []))))
    info = pool_all.set_index("funder_id")
    cross = pd.DataFrame(pairs)
    if not cross.empty:
        for side in ("a", "b"):
            cross[f"category_{side}"] = cross[f"funder_id_{side}"].map(info["category"])
            cross[f"name_{side}"] = cross[f"funder_id_{side}"].map(info["name"])
            cross[f"money_origin_{side}"] = cross[f"funder_id_{side}"].map(info["money_origin_draft"])
        cross["decision"] = ""
        cross = cross[["funder_id_a", "category_a", "name_a", "money_origin_a", "funder_id_b", "category_b",
                       "name_b", "money_origin_b", "evidence", "decision"]]

    iq = pd.concat(queues, ignore_index=True)
    iq["also_in"] = iq["funder_id"].map(lambda f: "|".join(sorted(also.get(f, []))))
    iq["_r"] = pd.to_numeric(iq["rank_in_category"], errors="coerce")
    iq = iq.sort_values(["category", "_r"], kind="stable").drop(columns="_r")
    review = pd.concat(reviews, ignore_index=True) if reviews else pd.DataFrame()
    if not cross.empty:
        xr = pd.DataFrame({"category": "cross_category", "funder_id": cross["funder_id_a"], "issue": "ambiguous_match",
                           "candidates": cross["funder_id_b"],
                           "suggested_action": "same organisation in two categories? " + cross["evidence"]
                                               + ": keep the category whose help file fits; link or drop the other",
                           "decision": ""})
        review = pd.concat([review, xr], ignore_index=True)
    sources = pd.concat(logs, ignore_index=True)
    drop_log = pd.concat(drops, ignore_index=True) if drops else pd.DataFrame()

    OUT.mkdir(parents=True, exist_ok=True)
    write_csv(pool_all, OUT / "pool_all.csv")
    write_csv(iq, OUT / "ingest_queue.csv")
    write_csv(cross if not cross.empty else pd.DataFrame(columns=["funder_id_a", "funder_id_b"]),
              OUT / "cross_category_matches.csv")
    report = _report(pool_all, iq, cross, sources, missing)
    (OUT / "distribution_report.md").write_text(report)
    _workbook(pool_all, iq, review, cross, sources, drop_log, report)
    return {"pool_all": pool_all, "ingest_queue": iq, "review": review, "cross": cross, "sources_log": sources}


def _md(df: pd.DataFrame) -> str:
    return rpt._table(df.astype(str).values.tolist(), [str(c) for c in df.columns])


def _report(pool_all, iq, cross, sources, missing) -> str:
    lines = ["# Combined funder pool: distribution report", "",
             "Ranks are within each category. Scores are not comparable across categories. Priority bands are blank by design.", ""]
    if missing:
        lines += [f"Not built: {', '.join(missing)}", ""]
    t = pool_all.groupby("category").agg(funders=("funder_id", "size"),
                                         known_positive=("india_evidence_status", lambda s: (s == "known_positive").sum()),
                                         unknown=("india_evidence_status", lambda s: (s == "unknown").sum()),
                                         in_sangam_yes=("in_sangam", lambda s: (s == "yes").sum()),
                                         in_sangam_related=("in_sangam", lambda s: (s == "related").sum()),
                                         linked_cross_category=("also_in", lambda s: (s != "").sum()))
    t["ingest_queue"] = iq.groupby("category").size()
    lines += ["## Funders by category", "", _md(t.reset_index()), ""]
    lines += [f"Cross-category candidate duplicates: {len(cross)} pairs (cross_category_matches.csv; also in review.xlsx).", ""]
    st = sources.groupby(["category", "status"]).size().unstack(fill_value=0)
    lines += ["## Sources by status", "", _md(st.reset_index()), ""]
    gaps = sources[sources["status"] != "used"][["category", "source_key", "status", "reason"]].drop_duplicates()
    lines += ["## Sources not used", "", _md(gaps), ""]
    lines += ["## Per-category reports", ""] + [f"- data/{u}/distribution_report.md" for u in UTILS]
    return "\n".join(lines) + "\n"


def _workbook(pool_all, iq, review, cross, sources, drop_log, report) -> None:
    from openpyxl.utils import get_column_letter
    path = OUT / "review.xlsx"
    readme = pd.DataFrame({"README": [
        "Funder pool review workbook (research output; nothing is loaded into Sangam).",
        "ingest_queue: ranked within each category, excluding funders already in Sangam. Fill priority_band yourself.",
        "review_queue: fill the decision column (all categories, plus cross-category duplicate checks).",
        "cross_category: the same organisation may sit in two categories; choose one.",
        "pool_all: every funder with its signals. sources_log: what each source gave or why it was not used.",
        "Ranks are within category; scores are not comparable across categories. Unknown India giving is not zero.",
    ]})
    sheets = {"README": readme, "ingest_queue": iq.assign(priority_band=""), "review_queue": review,
              "cross_category": cross, "pool_all": pool_all, "sources_log": sources, "drop_log": drop_log}
    with pd.ExcelWriter(path, engine="openpyxl") as xw:
        for name, df in sheets.items():
            df.to_excel(xw, sheet_name=name, index=False)
            ws = xw.sheets[name]
            ws.freeze_panes = "A2"
            if len(df.columns):
                ws.auto_filter.ref = ws.dimensions
            for i, col in enumerate(df.columns, 1):
                width = min(60, max(10, int(df[col].astype(str).str.len().quantile(0.9)) if len(df) else 10, len(str(col)) + 2))
                ws.column_dimensions[get_column_letter(i)].width = width

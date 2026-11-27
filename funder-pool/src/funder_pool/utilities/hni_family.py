"""hni_family: Indian HNIs, family foundations and private or public charitable trusts.
Help file: docs/funder-sources/hni-family-foundations.md.

Sources:
- hurun_india (M8): data/manual/hurun_india_philanthropy_list_YYYY.{csv,xlsx}. A PDF must be converted to a table
  first. Columns are matched loosely (rank, name, foundation, donation, five-year total, cause, city).
  Only name, rank, amount, cause, foundation and city are kept (hard rule 8).
- oecd_india / manual_seed: seeds/domestic_oecd_annex_b_and_later.csv, family/private foundations only.
- Sangam partial seed: rows typed private_foundation or hni (roster only; in_sangam comes out as yes).
Rule: rank by the foundation where one exists; the donor is an alias of it (trap 3).
"""
import re

import pandas as pd

from ..core import config, matching, sangam
from ..core.paths import DATA, MANUAL, SEEDS
from ..core.provenance import file_hash, local_file_meta
from .common import Build, finalize

CATEGORY = "hni_family"
HURUN_URL = "https://www.hurunindia.com/"
DOMESTIC_TYPES = {"private_foundation", "hni"}
CSR_ROUTED = "routed to indian_csr (corporate foundation)"

COLS = {  # pool field -> regex over the file's column names
    "rank": r"^rank",
    "name": r"^(name|donor|philanthropist)",
    "foundation": r"foundation|trust|vehicle",
    "donation": r"donation|amount|giving.*(fy|year|crore)|crore",
    "five_year": r"five|5.?y",
    "cause": r"cause",
    "city": r"city",
}


def _cols(df: pd.DataFrame) -> dict[str, str]:
    out = {}
    for k, pat in COLS.items():
        for c in df.columns:
            if c in out.values():
                continue
            if re.search(pat, str(c).strip().lower()):
                if k == "donation" and re.search(COLS["five_year"], str(c).lower()):
                    continue
                out[k] = c
                break
    return out


def _num(v) -> float | None:
    try:
        return float(re.sub(r"[^\d.]", "", str(v)) or "x")
    except ValueError:
        return None


def _hurun_files() -> list:
    if not MANUAL.exists():
        return []
    return sorted(p for p in MANUAL.glob("hurun_india_philanthropy_*") if p.suffix.lower() in (".csv", ".xlsx", ".pdf", ".html"))


TRANSCRIBED = "hurun_transcribed.csv"
PHIL_VEHICLE = re.compile(r"foundation|trust|philanthrop|charit|institutions|initiative|endowment|society|mission|"
                          r"fund\b|seva|sangh", re.I)
FAMILY = re.compile(r"\s*(&|and)\s+(family|families)\s*$", re.I)
PARTIAL = re.compile(r"personal donation|woman's share", re.I)  # not the donor's total giving


def _donor_key(donor: str) -> str:
    """'A.M. Naik' and 'AM Naik' -> 'am naik' (runs of single letters joined); '& family' dropped."""
    out, run = [], ""
    for t in matching.normalise(FAMILY.sub("", donor)).split():
        if len(t) == 1:
            run += t
            continue
        if run:
            out.append(run)
            run = ""
        out.append(t)
    return " ".join(out + ([run] if run else []))


class _Corporate:
    """Corporate foundations and companies: indian_csr's pool (built first) and Sangam corporate rows.
    A Hurun donor giving through one stays an individual linked to it (trap 2). A vehicle is corporate when its
    normalised name is one of these, its stem starts a CSR company's stem ('Adani Foundation' -> 'Adani Agri
    Fresh Limited'), or it names a group ('Bajaj Group Trust'). Wrong calls are visible in the review queue."""

    def __init__(self):
        self.names: dict[str, str] = {}
        self.stems: dict[str, list[list[str]]] = {}
        p = DATA / "indian_csr" / "pool.csv"
        companies = list(pd.read_csv(p, dtype=str, keep_default_na=False, usecols=["name"])["name"]) if p.exists() else []
        funders, _ = sangam.load()
        companies += [n for f in funders if f.funder_type in sangam.CORPORATE_TYPES for n in [f.name, *f.aliases]]
        for n in companies:
            self.names[matching.normalise(n)] = n
            st = matching.stem(n).split()
            if st:
                self.stems.setdefault(st[0], []).append(st)

    def __call__(self, vehicle: str) -> bool:
        if matching.normalise(vehicle) in self.names or re.search(r"\bgroup\b", vehicle, re.I):
            return True
        vs = matching.stem(vehicle).split()
        return bool(vs) and any(st[:len(vs)] == vs for st in self.stems.get(vs[0], []))


def _resolve(b: Build, donor: str, vehicle: str, corporate: "_Corporate", donors: dict[str, str]) -> tuple[str, str]:
    """(funder_id, how) for one Hurun donor. Same donor across editions -> same funder."""
    key = _donor_key(donor)
    if key not in donors:  # 'Susmita Bagchi' (women's share) inside 'Susmita & Subroto Bagchi': one gift
        kt = set(key.split())
        inside = {f for k, f in donors.items()
                  if len(kt) >= 2 and len(k.split()) >= 2 and (kt <= set(k.split()) or set(k.split()) <= kt)}
        if len(inside) == 1:
            donors[key] = inside.pop()
    if key in donors:
        fid = donors[key]
        b.add_alias(fid, donor)
        if vehicle and PHIL_VEHICLE.search(vehicle) and b.pool[fid]["funder_type_draft"] == "private_foundation":
            b.add_alias(fid, vehicle)
        return fid, "seen before"
    is_corp = bool(vehicle) and corporate(vehicle)
    if vehicle and PHIL_VEHICLE.search(vehicle) and not is_corp:
        found = {f: r["name"] for f, r in b.pool.items() if r["funder_type_draft"] == "private_foundation"}
        dec, cands = matching.match(vehicle, found)
        if dec in {"exact", "fuzzy", "acronym"}:  # 'K Chittilapiily Foundation' (source typo) -> existing row
            fid = cands[0].key
            b.add_alias(fid, vehicle)
            b.add_alias(fid, donor)
            if "hurun_india" not in b.pool[fid]["sources"]:
                b.pool[fid]["sources"].append("hurun_india")
        else:
            fid = b.add_funder(vehicle, source_key="hurun_india", aliases=[donor],
                               funder_type_draft="private_foundation", money_origin_draft="domestic")
        how = "foundation as published"
    else:
        # no private vehicle: is there a foundation in the pool carrying the donor's name? (Shiv Nadar Foundation)
        core = key.split()
        hits = [f for f, r in b.pool.items() if r["funder_type_draft"] == "private_foundation" and len(core) >= 2
                and matching.normalise(r["name"]).split()[:len(core)] == core]
        if len(hits) == 1:
            fid = hits[0]
            b.add_alias(fid, donor)
            if "hurun_india" not in b.pool[fid]["sources"]:
                b.pool[fid]["sources"].append("hurun_india")
            how = "donor name matches foundation"
        else:
            fid = b.add_funder(donor, source_key="hurun_india", funder_type_draft="hni", money_origin_draft="domestic")
            how = "individual"
        if vehicle:
            kind = "corporate foundation or company (indian_csr / Sangam)" if is_corp else "company as published"
            note = f"gives through {vehicle}: {kind}"
            if note not in b.pool[fid]["notes"]:
                b.pool[fid]["notes"].append(note)
            if is_corp:
                b.queue(fid, f"Hurun donor gives through corporate vehicle '{vehicle}'", "indian_csr",
                        "linked, not merged (trap 2): keep the individual here, the vehicle in indian_csr")
    donors[key] = fid
    return fid, how


def _load_hurun(b: Build) -> dict[str, dict]:
    """Returns {fid: {year: {...}}} and adds funders. Logs each file.
    PDFs (web-page printouts) are read through data/manual/hurun_transcribed.csv: the tables were transcribed
    in-session (2026 tables are images) with a table reference per row. Ages are not transcribed (rule 8)."""
    files = _hurun_files()
    pdfs = [p for p in files if p.suffix.lower() == ".pdf"]
    tr = MANUAL / TRANSCRIBED
    if not files:
        b.ledger.log_source("hurun_india", "EdelGive Hurun India Philanthropy List (M8)", HURUN_URL, "manual_file",
                            "blocked", reason="M8 not supplied; Hurun's full list is manual. hni_family holds the OECD "
                                              "and Sangam seeds only until it arrives.")
        return {}
    per: dict[str, dict] = {}
    donors: dict[str, str] = {}
    corporate = _Corporate()
    for p in files:
        if p.suffix.lower() == ".html":
            if any(q.stem == p.stem for q in pdfs):
                b.ledger.log_source("hurun_india", f"Hurun list (saved web page) {p.name}", f"file://{p.name}",
                                    "manual_file", "skipped", reason="superseded by the PDF of the same edition")
                continue
            txt = p.read_text(errors="ignore")
            if not re.search(r"<table|rank", txt, re.I) or "Nadar" not in txt:
                b.ledger.log_source("hurun_india", f"Hurun list (saved web page) {p.name}", f"file://{p.name}",
                                    "manual_file", "blocked", reason="saved page is the site shell only; the list "
                                    "loads by script and is not in the file. Needs a CSV/XLSX/PDF of the table")
            continue
        if p.suffix.lower() == ".pdf":
            continue  # read below through the transcription
        if p.name == TRANSCRIBED:
            continue
        _load_table_file(b, p, per, donors, corporate)

    if pdfs and not tr.exists():
        for p in pdfs:
            b.ledger.log_source("hurun_india", f"Hurun list PDF {p.name}", f"file://{p.name}", "manual_file", "skipped",
                                reason=f"tables not yet transcribed to {TRANSCRIBED}")
        return per
    if not pdfs:
        return per
    t = pd.read_csv(tr, dtype=str, keep_default_na=False)
    tm = local_file_meta(tr, url=f"file://{tr.name}")
    metas = {p.name: local_file_meta(p, url=f"file://{p.name}") for p in pdfs}
    t = t[t["source_file"].isin(metas)]
    for p in pdfs:
        sub = t[t["source_file"] == p.name]
        m = metas[p.name]
        b.ledger.log_source("hurun_india", f"EdelGive Hurun India Philanthropy List: {p.stem} (web page PDF, M8)",
                            m["url"], "manual_file", "used" if len(sub) else "skipped",
                            reason="" if len(sub) else f"no rows in {TRANSCRIBED}",
                            retrieved_at=m["retrieved_at"], file_hash=m["file_hash"], rows_read=len(sub),
                            terms_checked="no",
                            notes=f"web article printout: named tables only (top 10, women, new entrants, donors "
                                  f">= INR 50 Cr), not the full list; via {TRANSCRIBED} ({tm['file_hash'][:19]})")
    t = t.assign(_amt=t["donation_inr_cr"].map(_num), _five=t["five_year_inr_cr"].map(_num),
                 _ed=t["edition"].astype(int), _row=range(2, len(t) + 2))
    t["_part"] = t["table_title"].str.contains(PARTIAL)
    groups = sorted(t.groupby(["_ed", "name"]), key=lambda kv: (-kv[0][0], bool(kv[1]["_part"].all()), kv[0][1]))
    for (ed, name), g in groups:
        vehicle = next((v for v in g["company_or_foundation"] if v.strip() not in ("", "-")), "").strip()
        fid, how = _resolve(b, name.strip(), vehicle, corporate, donors)
        part = g["table_title"].str.contains(PARTIAL)
        amts = sorted({float(a) for a in g.loc[~part, "_amt"] if pd.notna(a)})
        partial_only = not amts
        if partial_only:  # only a personal-capacity or women's-share figure: a lower bound on total giving
            amts = sorted({float(a) for a in g.loc[part, "_amt"] if pd.notna(a)})
        amt = amts[-1] if amts else None
        if len(amts) > 1:
            b.queue(fid, f"Hurun {ed} tables disagree for {name}: {amts}", "", "check the PDF; the highest is used")
        five = next((float(x) for x in g["_five"] if pd.notna(x)), None)
        cause = next((c for c in g["cause"] if c.strip() not in ("", "-")), "")
        city = next((c for c in g["city"] if c.strip()), "")
        rank = next((r for r, n in zip(g["table_rank"], g["table_title"]) if r and re.search(r"cr|top 10$", n, re.I)), "")
        if city and f"city as published: {city}" not in b.pool[fid]["notes"]:
            b.pool[fid]["notes"].append(f"city as published: {city}")
        y = per.setdefault(fid, {}).setdefault(ed, {"amt": None, "five": None, "names": []})
        if y["names"] and not partial_only:  # two published names on one funder in one edition: never add them (could be the same money)
            b.queue(fid, f"Hurun {ed}: {y['names'] + [name]} resolve to one funder", "",
                    "same donor under two names, or two donors through one foundation? the larger amount is used")
        y["names"].append(name)
        if amt is not None and (y["amt"] is None or amt > y["amt"]):
            y["amt"] = amt
        y["five"] = five if five is not None else y["five"]
        src = g["source_file"].iloc[0]
        b.ledger.add_evidence(funder_id=fid, year_or_period=f"FY{ed - 1}-{str(ed)[-2:]}",
                              measure=f"Hurun donation ({name}; tables {'/'.join(sorted(set(g['table_no'])))}"
                                      + (f"; rank {rank}" if rank else "") + ")",
                              amount=amt if amt is not None else "", currency="INR crore",
                              basis="donation in FY as published (includes own institutions)"
                                    + ("; lower bound: personal or women's-share figure only" if partial_only else ""),
                              purpose_text=cause, recipient_country="IN", source_key="hurun_india",
                              source_url=metas[src]["url"], retrieved_at=metas[src]["retrieved_at"],
                              file_hash=metas[src]["file_hash"],
                              row_ref=f"{TRANSCRIBED}:" + ",".join(map(str, g["_row"])))
    return per


def _load_table_file(b: Build, p, per: dict, donors: dict, corporate) -> None:
    """A CSV or XLSX of the full list (one edition per file, year in the file name)."""
    year = int(re.search(r"(\d{4})", p.stem).group(1))
    df = pd.read_excel(p, dtype=str) if p.suffix.lower() == ".xlsx" else pd.read_csv(p, dtype=str)
    df = df.fillna("")
    cm = _cols(df)
    meta = local_file_meta(p, url=f"file://{p.name}")
    b.ledger.log_source("hurun_india", f"EdelGive Hurun India Philanthropy List {year} (M8)", meta["url"],
                        "manual_file", "used", retrieved_at=meta["retrieved_at"], file_hash=meta["file_hash"],
                        rows_read=len(df), terms_checked="no", notes=f"columns used: {cm}")
    if "name" not in cm:
        b.queue("", f"Hurun {year}: no name column found", "|".join(df.columns), "rename columns")
        return
    fy = f"FY{year - 1}-{str(year)[-2:]}"  # the list published in Nov YYYY covers FY(YYYY-1)-YY
    for i, r in enumerate(df.to_dict("records")):
        donor = str(r[cm["name"]]).strip()
        if not donor:
            continue
        fnd = str(r.get(cm.get("foundation", ""), "")).strip()
        fnd = "" if fnd.lower() in ("", "-", "na", "n/a", "none") else fnd
        amt = _num(r.get(cm.get("donation", ""), ""))
        five = _num(r.get(cm.get("five_year", ""), ""))
        cause = str(r.get(cm.get("cause", ""), "")).strip()
        city = str(r.get(cm.get("city", ""), "")).strip()
        rank = str(r.get(cm.get("rank", ""), "")).strip()
        fid, _ = _resolve(b, donor, fnd, corporate, donors)
        if city and f"city as published: {city}" not in b.pool[fid]["notes"]:
            b.pool[fid]["notes"].append(f"city as published: {city}")
        per.setdefault(fid, {})[year] = {"amt": amt, "five": five}
        b.ledger.add_evidence(funder_id=fid, year_or_period=fy, measure=f"Hurun donation (rank {rank})",
                              amount=amt if amt is not None else "", currency="INR crore",
                              basis="donation in FY as published (includes own institutions)",
                              purpose_text=cause, recipient_country="IN", source_key="hurun_india",
                              source_url=meta["url"], retrieved_at=meta["retrieved_at"],
                              file_hash=meta["file_hash"], row_ref=f"{p.name}:{i + 2}")


def build() -> dict:
    b = Build(CATEGORY)
    hurun = _load_hurun(b)

    # OECD domestic seed: family and private foundations only; CSR rows belong to indian_csr
    seed_p = SEEDS / "domestic_oecd_annex_b_and_later.csv"
    sm = local_file_meta(seed_p)
    seed = pd.read_csv(seed_p, dtype=str, keep_default_na=False)
    b.ledger.log_source("oecd_india", "OECD India's Private Giving (2019) Annex B and Third Edition sample",
                        f"file://seeds/{seed_p.name}", "manual_file", "used", retrieved_at=sm["retrieved_at"],
                        file_hash=sm["file_hash"], rows_read=len(seed),
                        notes="2019 Annex B rows via seed; M4 (2022) PDF has no organisation list")
    b.ledger.log_source("manual_seed", "Package seeds", f"file://seeds/{seed_p.name}", "manual_file", "used",
                        retrieved_at=sm["retrieved_at"], file_hash=sm["file_hash"], rows_read=len(seed))
    for i, r in seed.iterrows():
        name, t = r["Clean name"], r["Draft funder_type"]
        oecd_t = r["OECD type (as printed)"]
        if t.startswith("csr") or oecd_t in ("CSR", "Corporate Foundation"):
            continue  # indian_csr seeds; not logged as drops here
        if name == "EdelGive Foundation":
            b.drop(name, "manual_seed", CSR_ROUTED + "; in Sangam as corporate_foundation, #324 review as intermediary")
            continue
        fid = b.add_funder(name, source_key="manual_seed", funder_type_draft="private_foundation",
                           money_origin_draft="domestic", notes=r["Note"])
        if t in ("review", "other"):
            b.queue(fid, f"OECD type '{oecd_t}', draft '{t}'", "private_foundation|intermediary|csr_foundation",
                    "confirm funder_type_draft")
        b.ledger.add_evidence(funder_id=fid, year_or_period=r["Seen in"], measure="named in OECD list (roster)",
                              basis="roster listing, no amount", source_key="oecd_india",
                              source_url=f"file://seeds/{seed_p.name}", retrieved_at=sm["retrieved_at"],
                              file_hash=sm["file_hash"], row_ref=f"{seed_p.name}:{i + 2}")

    # Sangam partial seed (issue #324 types): domestic private foundations and HNIs. It carries the domestic/foreign
    # judgement that the M11 export lacks (M11 has no country), so it stays the roster source for Sangam rows.
    sp = SEEDS / "sangam_existing_funders_partial.csv"
    spm = local_file_meta(sp)
    sdf = pd.read_csv(sp, dtype=str, keep_default_na=False)
    for i, r in sdf.iterrows():
        if r["funder_type_as_listed_in_324"] not in DOMESTIC_TYPES:
            continue
        t = r["funder_type_as_listed_in_324"]
        fid = b.add_funder(r["name"], source_key="manual_seed", funder_type_draft=t, money_origin_draft="domestic")
        b.ledger.add_evidence(funder_id=fid, year_or_period="", measure="listed in Sangam (issue #324)",
                              basis="roster listing, no amount", source_key="manual_seed",
                              source_url=f"file://seeds/{sp.name}", retrieved_at=spm["retrieved_at"],
                              file_hash=spm["file_hash"], row_ref=f"{sp.name}:{i + 2}")
    # M11 export: family trusts are domestic by type; private_foundation rows may be foreign (no country in M11),
    # so those not named by a domestic source get money_origin unknown and go to review
    funders, src = sangam.load()
    if src.endswith("sangam_funders_export.csv"):
        from pathlib import Path
        mm = local_file_meta(Path(src))
        names = {fid: r["name"] for fid, r in b.pool.items()}
        b.ledger.log_source("sangam_export", "Sangam funders export (M11)", mm["url"], "manual_file", "used",
                            retrieved_at=mm["retrieved_at"], file_hash=mm["file_hash"], rows_read=len(funders),
                            notes="used for in_sangam and for family trusts and private foundations")
        before = set(b.pool)
        for f in funders:
            if f.funder_type in ("family_trust", "family_trust_network"):
                b.add_funder(f.name, source_key="sangam_export", funder_type_draft="private_foundation",
                             money_origin_draft="domestic", aliases=f.aliases,
                             notes=f"Sangam type {f.funder_type}")
            elif f.funder_type == "private_foundation":
                form = sangam.foreign_form(f)
                if form:  # foreign legal form: western_funders takes it (western._sangam_foreign)
                    b.drop(f.name, "sangam_export", f"routed to western_funders (foreign legal form '{form}')")
                    continue
                dec, _ = matching.match(f.name, names)
                fid = b.add_funder(f.name, source_key="sangam_export", funder_type_draft="private_foundation",
                                   money_origin_draft="unknown", aliases=f.aliases)
                # named by a domestic source if add_funder merged it into an existing row (alias map) or it matched
                named = fid in names or dec != "none"
                if named:
                    b.pool[fid]["money_origin_draft"] = "domestic"
                else:  # M11 has no country and no foreign legal form: confirm it is Indian
                    b.queue(fid, "Sangam private_foundation; no domestic source names it", "hni_family|western_funders",
                            "confirm it is Indian; if foreign, remove here (Phase 7 dedupe also checks western)")

        for fid in sorted(set(b.pool) - before):
            b.ledger.add_evidence(funder_id=fid, year_or_period="", measure="listed in Sangam export (M11)",
                                  basis="roster listing, no amount", source_key="sangam_export", source_url=mm["url"],
                                  retrieved_at=mm["retrieved_at"], file_hash=mm["file_hash"], row_ref=Path(src).name)

    # OECD PP4D Third Edition Annex B (M3), India rows that are family or private foundations
    annex = MANUAL / "oecd_third_edition_annex_b.csv"
    if annex.exists():
        am = local_file_meta(annex, url="file://oecd_pp4d_third_edition_report.pdf#AnnexB")
        adf = pd.read_csv(annex, dtype=str, keep_default_na=False)
        names = {fid: r["name"] for fid, r in b.pool.items()}
        hits = 0
        for i, r in adf[adf["country"] == "India"].iterrows():
            dec, cands = matching.match(r["name"], names)
            if dec not in {"exact", "acronym", "fuzzy"}:
                continue
            hits += 1
            fid = cands[0].key
            if "oecd_philanthropy" not in b.pool[fid]["sources"]:
                b.pool[fid]["sources"].append("oecd_philanthropy")
            b.ledger.add_evidence(funder_id=fid, year_or_period="2020-2023", measure="in OECD PP4D Third Edition sample",
                                  basis="roster listing (Annex B), no amount", recipient_country="IN",
                                  source_key="oecd_philanthropy", source_url=am["url"], retrieved_at=am["retrieved_at"],
                                  file_hash=am["file_hash"], row_ref=f"{annex.name}:{i + 2}")
        b.ledger.log_source("oecd_philanthropy", "OECD PP4D Third Edition, Annex B (M3, extracted from the report PDF)",
                            am["url"], "manual_file", "used", retrieved_at=am["retrieved_at"], file_hash=am["file_hash"],
                            rows_read=int((adf["country"] == "India").sum()),
                            notes=f"India rows matched to hni_family funders: {hits}; companies are left to indian_csr")

    b.ledger.log_source("foundation_site", "Foundation websites and annual reports", "", "download", "skipped",
                        reason="help file: enrich after the roster exists (later phase)")

    # signals
    years = sorted({y for d in hurun.values() for y in d})
    last5 = years[-5:]
    for fid, r in b.pool.items():
        h = hurun.get(fid, {})
        with_amt = [y for y in h if h[y].get("amt") is not None]
        latest = h[max(with_amt)] if with_amt else {}
        five = next((h[y]["five"] for y in sorted(h, reverse=True) if h[y].get("five") is not None), None)
        b.signals[fid] = {
            "annual_giving_latest": latest.get("amt"),
            "five_year_giving_total": five,
            "list_appearances_5y": sum(1 for y in last5 if y in h) if years else None,
            "has_named_foundation": r["funder_type_draft"] == "private_foundation",
            "funds_ngos_externally": None,  # unknown until foundation sites are read
            "ingest_readiness": 1 if h else 0,
            # domestic giving is India giving by definition: a Hurun donation is a known positive amount;
            # an OECD/Sangam roster listing names the funder as an Indian giver, without an amount
            "india_evidence_status": "known_positive",
            "india_inr_crore_latest": latest.get("amt"),
        }
        if not h:
            b.queue(fid, "no giving amount (roster only)", "", "supply M8 or read the annual report")

    bins = config.thresholds()["distribution_bins_inr_crore_for_indian_sources"]
    notes = ["M8 (Hurun list) not supplied: the pool is the OECD domestic seed plus the Sangam partial seed only."
             if not hurun else f"Hurun editions read: {', '.join(map(str, years))}. The PDFs are printouts of Hurun's "
             "web article: only the featured tables (top 10, women, new entrants, professional managers, donors of "
             "INR 50 Cr or more). A donor missing from an edition may still be on that year's full list, so "
             "list_appearances_5y is a lower bound.",
             "Hurun amounts are donations in the FY, including to the donor's own institutions; not grants to NGOs.",
             "Donor and foundation are one funder; the donor is an alias. Individuals without a foundation are typed hni.",
             "Legal flag: names are personal data under India's DPDP Act; publicly-available exemption is unsettled "
             "for third-party lists. Add to legal review.",
             "Priority bands are blank by design."]
    return finalize(b, "hni_family", value_col="annual_giving_latest", bins=bins, unit="INR crore",
                    size_col="annual_giving_latest", notes=notes,
                    extra_signal_cols=["annual_giving_latest", "five_year_giving_total", "list_appearances_5y",
                                       "has_named_foundation", "funds_ngos_externally"])

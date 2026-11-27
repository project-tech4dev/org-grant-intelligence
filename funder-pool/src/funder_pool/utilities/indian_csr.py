"""indian_csr: Indian companies and corporate foundations spending under Section 135.
Help file: docs/funder-sources/indian-csr.md.

M10: data/manual/mca_csr_export_FY*.csv, the National CSR Data Portal "Dynamic CSR Report" export (project rows:
company, FY, PSU/Non-PSU, state, district, sector, sub-sector, amount spent in INR crore). Used when present.
Fallback: data/manual/CSRAnalytics-Report-FY-2014-2025.xlsx (user-approved stand-in, origin and licence unverified).
"""
import re
from collections import defaultdict

import pandas as pd

from ..core import config, fx, matching, sangam
from ..core.paths import CACHE, MANUAL, SEEDS
from ..core.provenance import file_hash, local_file_meta
from .common import Build, finalize

CATEGORY = "indian_csr"
WINDOW_FYS = ["2021-22", "2022-23", "2023-24", "2024-25"]  # FY2025-26 not yet filed
LAST3 = WINDOW_FYS[-3:]
XLSX = "CSRAnalytics-Report-FY-2014-2025.xlsx"
NEC = {"", "nec/ not mentioned", "nan", "-", "none"}
PORTAL = "https://csr.gov.in/content/csr/global/master/home/ExploreCsrData/dynamic-csr-report-search.html.html"


def _num(v) -> float:
    try:
        return float(str(v).strip().replace(",", ""))
    except ValueError:
        return float("nan")


def load_csranalytics(path) -> tuple[pd.DataFrame, str]:
    """Read the window sheets once; cache as CSV keyed by file hash (deterministic reruns)."""
    h = file_hash(path)
    cache = CACHE / f"csranalytics_{h.split(':')[1][:16]}.csv"
    if cache.exists():
        return pd.read_csv(cache, dtype=str, keep_default_na=False), h
    frames = []
    for fy in WINDOW_FYS:
        df = pd.read_excel(path, sheet_name=fy, dtype=str, keep_default_na=False, engine="openpyxl")
        df.columns = [c.strip() for c in df.columns]
        # second 'State' column is the project state
        cols = list(df.columns)
        if cols.count("State") == 2:
            i = len(cols) - 1 - cols[::-1].index("State")
            cols[i] = "Project_State"
            df.columns = cols
        df["_sheet"], df["_row"] = fy, range(2, len(df) + 2)
        frames.append(df)
    out = pd.concat(frames, ignore_index=True)
    CACHE.mkdir(parents=True, exist_ok=True)
    out.to_csv(cache, index=False)
    return out, h


def load_mca(paths) -> tuple[pd.DataFrame, str]:
    """Official Dynamic CSR Report export(s). Maps to the columns the build uses. The company's FY spend is the sum of
    its project rows in that FY (one source, one filing; not a cross-source sum)."""
    frames = []
    for p in paths:
        df = pd.read_csv(p, dtype=str, keep_default_na=False)
        df.columns = [c.strip() for c in df.columns]
        df["_row"], df["_sheet"] = range(2, len(df) + 2), p.name
        frames.append(df)
    df = pd.concat(frames, ignore_index=True)
    df["Year"] = df["Financial Year"].str.replace("FY", "").str.strip()
    df = df[df["Year"].isin(WINDOW_FYS)].copy()
    df["Amount_Spent_INR_Cr"] = df["Project Amount Spent (In INR Cr.)"]
    amt = df["Amount_Spent_INR_Cr"].map(_num).fillna(0)
    df["CSR Spent"] = amt.groupby([df["Company Name"].str.strip().str.lower(), df["Year"]]).transform("sum").astype(str)
    df["Development_Sector_s"] = df["CSR Development Sector"]
    df["CSR_Project_s"] = df["CSR Sub Development Sector"]
    df["Class"], df["Listing Status"], df["State"] = df["PSU/Non-PSU"], "", ""
    return df, "|".join(file_hash(p) for p in paths)


def _stem(name: str) -> str:
    n = matching.normalise(name)
    return re.sub(r"\b(foundation|trust|charitable|society|csr)\b", "", n).strip()


def build() -> dict:
    b = Build(CATEGORY)
    path = MANUAL / XLSX
    official = sorted(MANUAL.glob("mca_csr_export_FY*.csv")) if MANUAL.exists() else []
    src_name = XLSX
    if official:
        df, h = load_mca(official)
        src_name = official[0].name
        meta = local_file_meta(official[0], url=f"file://{src_name}")
        h = meta["file_hash"] if len(official) == 1 else h
        b.ledger.log_source("mca_csr", "National CSR Data Portal, Dynamic CSR Report export (M10)", PORTAL,
                            "manual_file", "used", retrieved_at=meta["retrieved_at"], file_hash=h, rows_read=len(df),
                            terms_checked="no", notes="project rows FY" + "..FY".join([WINDOW_FYS[0], WINDOW_FYS[-1]])
                            + "; company FY spend = sum of its project rows")
        if path.exists():
            b.ledger.log_source("csranalytics", "CSRAnalytics Report FY2014-2025 (stand-in)", f"file://{XLSX}",
                                "manual_file", "skipped", reason="superseded by the official M10 export")
    elif not path.exists():
        b.ledger.log_source("mca_csr", "CSR data (M10 or CSRAnalytics stand-in)", PORTAL, "manual_file", "blocked",
                            reason="no M10 export and no CSRAnalytics file in data/manual/")
        df, h = pd.DataFrame(), ""
    else:
        df, h = load_csranalytics(path)
        meta = local_file_meta(path, url=f"file://{XLSX}")
        b.ledger.log_source("mca_csr", "CSRAnalytics Report FY2014-2025 (user-approved stand-in for M10)", meta["url"],
                            "manual_file", "used", retrieved_at=meta["retrieved_at"], file_hash=h, rows_read=len(df),
                            terms_checked="no",
                            notes="origin and licence unverified; appears to mirror csr.gov.in; sheets " + ",".join(WINDOW_FYS))

    companies: dict[str, dict] = {}
    if len(df):
        df["spent"] = df["CSR Spent"].map(_num)
        df["proj_spent"] = df["Amount_Spent_INR_Cr"].map(_num)
        df["sector"] = df["Development_Sector_s"].str.strip()
        df["norm"] = df["Company Name"].map(matching.normalise)
        for norm, g in df.groupby("norm", sort=True):
            per_fy = g.groupby("Year")["spent"].max().to_dict()  # company figure repeats on each project row
            if not any(per_fy.get(fy, 0) > 0 for fy in LAST3):
                b.drop(g["Company Name"].iloc[-1], "mca_csr", "cost filter: no CSR spend in FY2022-23..FY2024-25")
                continue
            latest = g[g["Year"] == max(g["Year"])]
            name = latest["Company Name"].iloc[0].strip()
            fid = b.add_funder(name, source_key="mca_csr", funder_type_draft="csr_company", money_origin_draft="domestic",
                               india_csr_draft="true", aliases=sorted(set(g["Company Name"].str.strip()) - {name}),
                               notes=", ".join(x for x in (latest["Class"].iloc[0], latest["Listing Status"].iloc[0],
                                                          latest["State"].iloc[0]) if str(x).strip()))
            b.pool[fid]["country"] = "IN"
            lp = latest[(latest["CSR_Project_s"].str.strip().str.lower().map(lambda x: x not in NEC))
                        | (latest["proj_spent"] > 0)]
            sectors = {s for s in g["sector"].str.lower() if s not in NEC}
            last3 = [per_fy.get(fy) for fy in LAST3]
            known = [v for v in last3 if v is not None and not pd.isna(v)]
            usd5 = 0.0
            for fy, v in per_fy.items():
                if pd.isna(v):
                    continue
                y = int(fy[:4])
                usd5 += fx.to_usd(v * 1e7, "INR", y)[0]
                first = g[g["Year"] == fy].iloc[0]
                usd, rate, src = fx.to_usd(v * 1e7, "INR", y)
                b.ledger.add_evidence(funder_id=fid, year_or_period=f"FY{fy}", measure="CSR spent (company total)",
                                      amount=v, currency="INR crore", amount_usd=round(usd, 2), fx_rate=rate,
                                      fx_source=f"{src} ({y})", basis="spent, as reported", recipient_country="IN",
                                      source_key="mca_csr", source_url=f"file://{src_name}#{fy}",
                                      retrieved_at=meta["retrieved_at"], file_hash=h,
                                      row_ref=f"{src_name}:{first['_row']}")
            projects_with_amount = int((lp["proj_spent"] > 0).sum())
            b.signals[fid] = {
                "india_evidence_status": "known_positive",
                "india_inr_crore_5y": round(sum(v for v in per_fy.values() if not pd.isna(v)), 4),
                "india_usd_5y": round(usd5, 2),
                "csr_spend_3y_average": round(sum(known) / len(LAST3), 4),  # missing year counts as 0 spend filed
                "project_count": len(lp),
                "india_grants_count_5y": int(((g["CSR_Project_s"].str.strip().str.lower().map(lambda x: x not in NEC))
                                              | (g["proj_spent"] > 0)).sum()),
                "theme_breadth": len(sectors),
                "themes": "|".join(sorted(sectors)[:8]),
                "last_india_year": "FY" + max(k for k, v in per_fy.items() if v and v > 0),
                "ingest_readiness": 3 if projects_with_amount else (2 if sectors else 1),
                "evidence_quality": 2,
            }
            companies[fid] = {"name": name, "norm": norm, "spend": b.signals[fid]["csr_spend_3y_average"],
                              "projects": " ".join(g["CSR_Project_s"].str.lower().unique()[:200])}

    # ---- foundations (seed + Sangam partial), linked to parent companies ----
    seed_p = SEEDS / "domestic_oecd_annex_b_and_later.csv"
    sm = local_file_meta(seed_p)
    seed = pd.read_csv(seed_p, dtype=str, keep_default_na=False)
    sang, _ = sangam.load()
    fnd = [(r["Clean name"] or r["Organisation (as printed)"], "seed", i) for i, r in seed.iterrows()
           if r["Draft funder_type"] == "csr_foundation"]
    fnd += [(f.name, "sangam", None) for f in sang
            if getattr(f, "funder_type", "") in ("csr_foundation", "corporate_foundation")]  # M11 uses corporate_foundation
    by_stem = defaultdict(list)
    for fid, c in companies.items():
        by_stem[_stem(c["name"])].append(fid)
    comp_names = {fid: c["name"] for fid, c in companies.items()}
    for name, src, row in fnd:
        st = _stem(name)
        self_fid = b.fid(name)
        exact = [f for f in by_stem.get(st, []) if f != self_fid]
        parents = exact or [fid for s, fids in by_stem.items() if s and st and s.startswith(st + " ")
                            for fid in fids if fid != self_fid]
        fid = b.add_funder(name, source_key="manual_seed", funder_type_draft="csr_foundation",
                           money_origin_draft="domestic", india_csr_draft="true", country="IN",
                           notes="from package seed" if src == "seed" else "listed in Sangam (M11 export or partial seed)")
        if fid in companies:
            b.queue(fid, "foundation also files CSR as a company", "", "confirm funder_type_draft")
        if parents:
            best = max(parents, key=lambda f: companies[f]["spend"])
            b.pool[fid]["parent_name"] = companies[best]["name"]
            b.signals.setdefault(best, {})["has_foundation_arm"] = True
            if len(parents) > 1 and not exact:
                b.queue(fid, "several candidate parent companies", "|".join(comp_names[p] for p in parents[:5]),
                        "confirm parent_name")
        else:
            b.queue(fid, "parent company not found in CSR data", "", "set parent_name by hand")
        b.ledger.add_evidence(funder_id=fid, year_or_period="", measure="corporate foundation (roster)",
                              source_key="manual_seed", source_url=sm["url"], retrieved_at=sm["retrieved_at"],
                              file_hash=sm["file_hash"], row_ref=f"{seed_p.name}:{row + 2}" if row is not None else "sangam partial seed",
                              basis="roster listing, no amount")
        if fid not in companies:
            b.signals.setdefault(fid, {}).update({"india_evidence_status": "known_positive" if parents else "unknown",
                                                   "ingest_readiness": 1, "evidence_quality": 0})
    # seed companies not found with spend
    for i, r in seed.iterrows():
        if r["Draft funder_type"] != "csr_company":
            continue
        nm = r["Clean name"] or r["Organisation (as printed)"]
        dec, cands = matching.match(nm, comp_names)
        if dec in {"exact", "acronym", "fuzzy"}:
            fid = cands[0].key
            b.add_alias(fid, r["Organisation (as printed)"])
            if "manual_seed" not in b.pool[fid]["sources"]:
                b.pool[fid]["sources"].append("manual_seed")
        else:
            b.drop(nm, "manual_seed", "cost filter: no CSR spend found for FY2022-23..FY2024-25 under this name"
                   + (f" (possible: {', '.join(c.name for c in cands[:3])})" if cands else ""))
    annex = MANUAL / "oecd_third_edition_annex_b.csv"
    if annex.exists():
        am = local_file_meta(annex, url="file://oecd_pp4d_third_edition_report.pdf#AnnexB")
        adf = pd.read_csv(annex, dtype=str, keep_default_na=False)
        hits = 0
        for i, r in adf[adf["country"] == "India"].iterrows():
            dec, cands = matching.match(r["name"], comp_names)
            if dec not in {"exact", "acronym", "fuzzy"}:
                continue
            fid = cands[0].key
            hits += 1
            if "oecd_philanthropy" not in b.pool[fid]["sources"]:
                b.pool[fid]["sources"].append("oecd_philanthropy")
            b.ledger.add_evidence(funder_id=fid, year_or_period="2020-2023", measure="in OECD PP4D Third Edition sample",
                                  basis="roster listing (Annex B), no amount", recipient_country="IN",
                                  source_key="oecd_philanthropy", source_url=am["url"], retrieved_at=am["retrieved_at"],
                                  file_hash=am["file_hash"], row_ref=f"{annex.name}:{i + 2}")
        b.ledger.log_source("oecd_philanthropy", "OECD PP4D Third Edition, Annex B (M3, extracted from the report PDF)",
                            am["url"], "manual_file", "used", retrieved_at=am["retrieved_at"], file_hash=am["file_hash"],
                            rows_read=int((adf["country"] == "India").sum()),
                            notes=f"India rows matched to CSR companies: {hits}")
    b.ledger.log_source("manual_seed", "Package seed domestic_oecd_annex_b_and_later.csv", sm["url"], "manual_file", "used",
                        retrieved_at=sm["retrieved_at"], file_hash=sm["file_hash"], rows_read=len(seed), terms_checked="n/a")
    for k, reason in [("oecd_india", "M4 supplied (Taking stock, 2022) but the PDF has no organisation list; "
                                     "2019 Annex B used via seed"),
                      ("company_site", "later phase: crawl only for funders being enriched"),
                      ("brsr", "not researched (help file section 9)")]:
        b.ledger.log_source(k, k, "", "manual_file" if k == "oecd_india" else "download", "skipped", reason=reason)

    # has_foundation_arm is only known where a link was found; everyone else stays unknown (not False)

    bins = config.thresholds()["distribution_bins_inr_crore_for_indian_sources"]
    notes = [("Data: National CSR Data Portal Dynamic CSR Report export (M10), project rows summed per company and FY."
              if official else
              "Data: CSRAnalytics Report FY2014-2025 (user-approved stand-in for M10; origin and licence unverified)."),
             "Window FY2021-22 to FY2024-25 (FY2025-26 not yet filed). Pool filter: CSR spend > 0 in FY2022-23..FY2024-25.",
             "csr_spend_3y_average = mean of the last three FYs, INR crore; a year with no filing counts as 0.",
             "No CIN in the CSR data, so company-to-Sangam matching is by name only.",
             "Corporate foundations are separate funders linked by parent_name (never merged).",
             "Percentile scoring compresses the top: with ~32k small filers, any company above ~5 crore sits near the top "
             "percentile for spend. Consider raising the spend weight or using log spend after reading this.",
             "Priority bands are blank by design."]
    return finalize(b, "indian_csr", value_col="csr_spend_3y_average", bins=bins, unit="INR crore",
                    size_col="csr_spend_3y_average", notes=notes,
                    extra_signal_cols=["csr_spend_3y_average", "project_count", "theme_breadth", "has_foundation_arm",
                                       "evidence_quality"])

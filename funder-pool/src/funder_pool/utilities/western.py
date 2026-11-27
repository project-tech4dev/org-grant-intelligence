"""western_funders: foreign private philanthropy. Help file: docs/funder-sources/western-funders.md."""
import math
import re
from collections import defaultdict

import pandas as pd
from rapidfuzz import fuzz

from ..core import config, matching, sangam, themes
from ..core.paths import MANUAL, RAW, SEEDS
from ..core.provenance import local_file_meta
from ..sources import iati, iati_summary
from .common import Build, by_source_best, finalize

CATEGORY = "western_funders"
START, END, RECENT = "2021-04-01", "2026-03-31", "2023-04-01"  # FY2021-22..FY2025-26; recent = last 3 FYs
IATI_URL = iati.BASE + "/{kind}.csv?recipient-country=IN"

WESTERN_TYPES = {"60": "private_foundation", "21": "international_agency", "22": "international_agency",
                 "23": "international_agency", "24": "international_agency", "70": "other", "71": "other",
                 "73": "other", "80": "other", "90": "other"}
ROUTED_TYPES = {"10", "11", "15", "30", "40"}  # government, multilateral, PPP -> bilateral_multilateral
# Funding-org refs that identify official donors whatever org type a publisher typed: OECD DAC multilateral and
# bilateral codes (XM-DAC-*, bare numeric DAC codes such as 44000) and government registries (GB-GOV-*, *-GOV-*).
MULTI_REF = re.compile(r"^(XM-DAC-|XM-OCHA|\d{3,6}$|[A-Z]{2}-GOV-)", re.I)
# Indian legal forms seen on funding orgs without a ref: "Pvt", "Private Limited", "(India)" companies, Tata trusts.
INDIAN_FORM = re.compile(r"\b(pvt|private limited)\b|\bindia\)?\s*(pvt|private|ltd|limited)\b|\bTata Trusts?\b|"
                         r"\bSir (Dorabji|Ratan) Tata\b", re.I)
US_INTERMEDIARIES = ["American India Foundation", "Give2Asia", "Charities Aid Foundation America",
                     "Tides Foundation", "GlobalGiving Foundation"]
COUNTRY = {"United States": "US", "Netherlands": "NL", "United Kingdom": "GB", "Switzerland": "CH",
           "United States / India": "US"}
PREF = {"US": ["irs_990pf", "oecd_philanthropy", "iati", "manual_seed_1yr"],
        "GB": ["threesixtygiving", "oecd_philanthropy", "iati", "manual_seed_1yr"]}
PREF_OTHER = ["oecd_philanthropy", "iati", "manual_seed_1yr"]


def _ids_from_ref(ref: str) -> dict:
    out = {"iati_org_id": ref}
    if ref.startswith("US-EIN-"):
        out["ein"] = ref[7:].replace("-", "")
    elif ref.startswith("GB-CHC-"):
        out["uk_charity_no"] = ref[7:]
    elif ref.startswith("NL-RSIN-"):
        out["rsin"] = ref[8:]
    return out


def _country(ref: str) -> str:
    head = ref.split("-")[0] if ref else ""
    return head if len(head) == 2 and head.isalpha() and head not in {"XM", "XI", "XB"} else ""


def _seeds(b: Build) -> dict[str, dict]:
    """Seed funders and their dated India figures. Returns {fid: {'seed_usd': float|None, 'status': str}}."""
    sp, ep = SEEDS / "international_seed.csv", SEEDS / "evidence_by_year.csv"
    sm, em = local_file_meta(sp), local_file_meta(ep)
    seed = pd.read_csv(sp, dtype=str, keep_default_na=False)
    ev = pd.read_csv(ep, dtype=str, keep_default_na=False)
    info = {}
    for i, r in seed.iterrows():
        fid = b.add_funder(r["Funder"], source_key="manual_seed", country=COUNTRY.get(r["Based in"], ""),
                           funder_type_draft=r["Draft funder_type"] or "review", money_origin_draft="foreign",
                           india_csr_draft="false", notes=f"seed: {r['Evidence level']}")
        level = r["Evidence level"].lower()
        positive = "amount found" in level or "named" in level
        info[fid] = {"status": "known_positive" if positive else "unknown", "seed_usd": None, "seed_period": "", "seed_year": 0}
        if positive:
            b.ledger.add_evidence(funder_id=fid, year_or_period=r["Period"], measure="India giving named (seed)",
                                  basis=r["Evidence level"], recipient_country="IN",
                                  purpose_text=r["India evidence retrieved"][:200], source_key="manual_seed",
                                  source_url=r["Source"].split(";")[0].strip() or sm["url"],
                                  retrieved_at=sm["retrieved_at"], file_hash=sm["file_hash"], row_ref=f"{sp.name}:{i + 2}")
    names = {fid: b.pool[fid]["name"] for fid in info}
    for i, r in ev.iterrows():
        dec, cands = matching.match(r["Funder"], names)
        if dec not in {"exact", "acronym", "fuzzy"}:
            continue
        fid = cands[0].key
        amt = float(r["Amount (USD million)"]) * 1e6
        period = r["Year or period"]
        b.ledger.add_evidence(funder_id=fid, year_or_period=period, measure=r["Measure"], amount=amt,
                              currency="USD", amount_usd=amt, basis=r["Basis"], recipient_country="IN",
                              source_key="manual_seed", source_url=r["Source"] or em["url"],
                              retrieved_at=em["retrieved_at"], file_hash=em["file_hash"], row_ref=f"{ep.name}:{i + 2}")
        info[fid]["status"] = "known_positive"
        yr = int(period.replace("FY", "")[:4]) if period.replace("FY", "")[:4].isdigit() else 0
        # single-year figure inside the window: a lower bound for the 5-year total (never summed with other sources)
        if yr >= 2021 and "-" not in period.replace("FY", "") and yr > info[fid]["seed_year"]:
            info[fid].update(seed_usd=amt, seed_period=period, seed_year=yr)
    for k, (p, m) in {"international_seed": (sp, sm), "evidence_by_year": (ep, em)}.items():
        b.ledger.log_source("manual_seed", f"Package seed {p.name}", m["url"], "manual_file", "used",
                            retrieved_at=m["retrieved_at"], file_hash=m["file_hash"],
                            rows_read=len(seed) if k == "international_seed" else len(ev), terms_checked="n/a")
    return info


ISO2 = {"United States": "US", "United Kingdom": "GB", "Netherlands": "NL", "Switzerland": "CH", "France": "FR",
        "Germany": "DE", "Italy": "IT", "Spain": "ES", "Belgium": "BE", "Luxembourg": "LU", "Portugal": "PT",
        "Denmark": "DK", "Sweden": "SE", "Norway": "NO", "Finland": "FI", "Austria": "AT", "Ireland": "IE",
        "Canada": "CA", "Australia": "AU", "Japan": "JP", "Korea": "KR", "Singapore": "SG", "Qatar": "QA",
        "United Arab Emirates": "AE", "Saudi Arabia": "SA", "Türkiye": "TR", "Brazil": "BR", "Mexico": "MX",
        "Colombia": "CO", "China (People's Republic of)": "CN", "Hong Kong, China": "HK", "South Africa": "ZA",
        "Nigeria": "NG", "Kenya": "KE", "Panama": "PA", "Guatemala": "GT", "Zimbabwe": "ZW", "Togo": "TG"}
DOMESTIC_SECONDARY = {"China (People's Republic of)", "Mexico"}


def _annex_b(b: Build) -> None:
    """OECD PP4D Third Edition Annex B (M3): foreign organisations as roster entries. India giving stays unknown."""
    p = MANUAL / "oecd_third_edition_annex_b.csv"
    if not p.exists():
        return
    am = local_file_meta(p, url="file://oecd_pp4d_third_edition_report.pdf#AnnexB")
    df = pd.read_csv(p, dtype=str, keep_default_na=False)
    names = {fid: r["name"] for fid, r in b.pool.items()}
    added = matched = 0
    for i, r in df.iterrows():
        if r["country"] == "India":
            continue  # Indian organisations belong to indian_csr and hni_family
        if r["country"] in DOMESTIC_SECONDARY and r["survey_respondent"] == "No":
            # cost filter: listed only through national secondary data on domestic giving (OECD Box 2.2 for Mexico;
            # China Foundation Center data); these report no cross-border giving
            b.drop(r["name"], "oecd_philanthropy", f"cost filter: {r['country']} organisation listed from national "
                                                   "secondary data on domestic giving (Annex B col C = No)")
            continue
        dec, cands = matching.match(r["name"], names)
        if dec in {"exact", "acronym", "fuzzy"}:
            fid = cands[0].key
            b.add_alias(fid, r["name"])
            if "oecd_philanthropy" not in b.pool[fid]["sources"]:
                b.pool[fid]["sources"].append("oecd_philanthropy")
            matched += 1
        else:
            fid = b.add_funder(r["name"], source_key="oecd_philanthropy", country=ISO2.get(r["country"], ""),
                               funder_type_draft="review", money_origin_draft="foreign", india_csr_draft="false",
                               notes="" if r["country"] in ISO2 else f"country as printed: {r['country']}")
            added += 1
        b.ledger.add_evidence(funder_id=fid, year_or_period="2020-2023", measure="in OECD PP4D Third Edition sample",
                              basis=f"roster listing (Annex B), no amount; survey respondent {r['survey_respondent']}",
                              source_key="oecd_philanthropy", source_url=am["url"], retrieved_at=am["retrieved_at"],
                              file_hash=am["file_hash"], row_ref=f"{p.name}:{i + 2}")
    b.ledger.log_source("oecd_philanthropy", "OECD PP4D Third Edition, Annex B (M3, extracted from the report PDF)",
                        am["url"], "manual_file", "used", retrieved_at=am["retrieved_at"], file_hash=am["file_hash"],
                        rows_read=len(df), notes=f"foreign rows: {matched} matched existing funders, {added} added")


def _sangam_foreign(b: Build) -> None:
    """Sangam export (M11) private foundations with a foreign legal form (hni_family routes them here).
    M11 has no country, so country stays blank; India giving stays unknown unless another source counts it."""
    funders, src = sangam.load()
    if not src.endswith("sangam_funders_export.csv"):
        return
    from pathlib import Path
    mm = local_file_meta(Path(src))
    names = {fid: r["name"] for fid, r in b.pool.items()}
    hits = []
    for f in funders:
        form = sangam.foreign_form(f)
        if f.funder_type != "private_foundation" or not form:
            continue
        dec, cands = matching.match(f.name, names)
        if dec in {"exact", "acronym", "fuzzy"}:
            fid = cands[0].key
            for a in [f.name, *f.aliases]:
                b.add_alias(fid, a)
            if "sangam_export" not in b.pool[fid]["sources"]:
                b.pool[fid]["sources"].append("sangam_export")
        else:
            fid = b.add_funder(f.name, source_key="sangam_export", aliases=f.aliases,
                               funder_type_draft="private_foundation", money_origin_draft="foreign",
                               india_csr_draft="false", notes=f"listed in the Sangam export; foreign legal form '{form}'")
        hits.append(f.name)
        b.ledger.add_evidence(funder_id=fid, year_or_period="", measure="listed in Sangam export (M11)",
                              basis="roster listing, no amount", source_key="sangam_export", source_url=mm["url"],
                              retrieved_at=mm["retrieved_at"], file_hash=mm["file_hash"], row_ref=Path(src).name)
    b.ledger.log_source("sangam_export", "Sangam funders export (M11)", mm["url"], "manual_file", "used",
                        retrieved_at=mm["retrieved_at"], file_hash=mm["file_hash"], rows_read=len(funders),
                        notes=f"used for in_sangam, and as roster for foreign-form private foundations: {len(hits)}")


TS_REGISTRY = "https://registry.threesixtygiving.org/data.json"
UK_PUBLIC_PREFIXES = ("GB-GOV-", "GB-LAE-", "GB-LAS-", "GB-LANI-", "GB-PLA-", "GB-UKPRN-", "GB-NHS-")


def _threesixty_rows():
    """India rows from the cached 360Giving files; cached to data/cache keyed on the download log."""
    import hashlib
    from ..core.paths import CACHE
    from ..sources import threesixty
    logp = threesixty.DIR / "_download_log.csv"
    if not logp.exists():
        return None, None
    key = hashlib.sha256(logp.read_bytes()).hexdigest()[:16]
    cp = CACHE / f"threesixty_india_{key}.csv"
    if cp.exists():
        return pd.read_csv(cp, dtype=str, keep_default_na=False), logp
    df = threesixty.india_rows()
    CACHE.mkdir(parents=True, exist_ok=True)
    df.to_csv(cp, index=False)
    return pd.read_csv(cp, dtype=str, keep_default_na=False), logp


def _threesixty(b: Build, sig, by_src, unresolved) -> None:
    from ..core import fx
    from ..sources import threesixty
    rows, logp = _threesixty_rows()
    if rows is None:
        b.ledger.log_source("threesixtygiving", "360Giving data registry", TS_REGISTRY, "download", "skipped",
                            reason="registry files not yet downloaded (python -m funder_pool.sources.threesixty)")
        return
    log = pd.read_csv(logp, dtype=str, keep_default_na=False)
    used = log[log["status"].isin(["used", "cached"])]
    hashes = {f: local_file_meta(threesixty.DIR / f)["file_hash"] for f in rows["file"].unique()} if len(rows) else {}
    lm = local_file_meta(logp, url=TS_REGISTRY)
    counted = text_only = 0
    no_fx: dict[str, int] = {}
    resolved: dict[tuple, str] = {}
    text_by_funder: dict[str, int] = defaultdict(int)
    for r in rows.to_dict("records"):
        date = r["award_date"][:10]
        funder = r["funder"].strip()
        fref = r["funder_id"].strip()
        if fref.upper().startswith(UK_PUBLIC_PREFIXES):
            b.drop(funder, "threesixtygiving", f"out of scope: UK public body ({fref}); not private philanthropy")
            continue
        if r["match"] == "text":
            text_by_funder[funder] += 1
            text_only += 1
            continue
        if not (START <= date <= END):
            continue
        try:
            amt = float(r["amount"])
        except ValueError:
            continue
        yr = int(date[:4])
        cur = (r["currency"] or "GBP").upper()
        try:
            usd, _, fxs = fx.to_usd(amt, cur, min(yr, 2025))
        except KeyError:
            no_fx[cur] = no_fx.get(cur, 0) + 1
            continue
        ids = {"uk_charity_no": fref[7:]} if fref.startswith("GB-CHC-") else {}
        if (funder, fref) in resolved:
            fid = resolved[(funder, fref)]
        else:
            fid = None
        names = {} if fid else {f: x["name"] for f, x in b.pool.items()}
        by_no = {x.get("uk_charity_no"): f for f, x in b.pool.items() if x.get("uk_charity_no")}
        if fid:
            pass
        elif ids and ids["uk_charity_no"] in by_no:
            fid = by_no[ids["uk_charity_no"]]
            b.add_alias(fid, funder)
        elif b.fid(funder) in b.pool:
            fid = b.add_funder(funder, source_key="threesixtygiving", **ids)
        else:
            dec, cands = matching.match(funder, names)
            if dec in {"exact", "acronym", "fuzzy"}:
                fid = cands[0].key
                b.add_alias(fid, funder)
                b.add_funder(funder, source_key="threesixtygiving", funder_id=fid, **ids)
            else:
                fid = b.add_funder(funder, source_key="threesixtygiving", country=_country(fref) or "GB",
                                   funder_type_draft="review", money_origin_draft="foreign", india_csr_draft="false",
                                   **ids)
                b.queue(fid, "funder_type_draft needs review (360Giving publisher)", fref, "set funder_type_draft")
                if dec == "ambiguous":
                    b.queue(fid, "ambiguous match", "|".join(c.name for c in cands), "merge if same organisation")
        resolved[(funder, fref)] = fid
        s = sig[fid]
        by_src[fid]["threesixtygiving"] = round(by_src[fid].get("threesixtygiving", 0) + usd, 2)
        if date >= RECENT:
            s["_ts_3y"] = s.get("_ts_3y", 0) + usd
        s["_ts_grants"] = s.get("_ts_grants", 0) + 1
        s.setdefault("_ts_recips", set()).add(r["recipient"].strip().lower())
        s["last_india_year"] = max(s.get("last_india_year", ""), date[:4])
        s["india_evidence_status"] = "known_positive"
        th = themes.from_text(r["title"] + " " + r["description"]) or themes.override(f"360:{r['identifier']}")
        if th:
            s.setdefault("_themes", defaultdict(float))[th] += usd
        else:
            unresolved[f"360:{r['identifier']}"] = (r["title"] + " " + r["description"])[:300]
        s["_ready"] = max(s.get("_ready", 0), 3)
        s["_quality"] = max(s.get("_quality", 0), 2)
        b.ledger.add_evidence(
            funder_id=fid, year_or_period=date, measure="360Giving grant, India recipient or beneficiary",
            amount=amt, currency=cur, amount_usd=round(usd, 2), fx_source=fxs,
            basis="amount awarded" + ("" if r["recipient_country"].lower() in {"india", "in"}
                                      else "; recipient outside India, beneficiary location India"),
            recipient_name=r["recipient"], recipient_country="IN", purpose_text=r["title"][:200],
            source_key="threesixtygiving", source_url=r["url"], retrieved_at=lm["retrieved_at"],
            file_hash=hashes.get(r["file"], ""), row_ref=f"{r['identifier']} | {r['file']}:{r['row']}")
        counted += 1
    for fid, s in sig.items():
        if "_ts_recips" in s:
            s["india_grants_count_5y"] = s.get("india_grants_count_5y", 0) + s["_ts_grants"]
            s["india_recipients_distinct_5y"] = s.get("india_recipients_distinct_5y", 0) + len(s.pop("_ts_recips"))
    for funder, n in sorted(text_by_funder.items()):
        fid = b.fid(funder)
        if fid in b.pool:
            b.queue(fid, f"360Giving: {n} grants mention India only in title/description (not counted)", "",
                    "check whether these are India grants")
    b.ledger.log_source("threesixtygiving", "360Giving data registry (publisher files, India filter applied locally)",
                        TS_REGISTRY, "download", "used", retrieved_at=lm["retrieved_at"],
                        file_hash=f"{len(used)} files, see evidence rows", rows_read=len(rows),
                        terms_checked="open licences per publisher (mostly CC-BY / OGL); attribution kept in evidence",
                        notes=f"{counted} India grants counted in window {START}..{END}; {text_only} text-only mentions "
                              f"not counted; {(log['status'].str.startswith('skipped')).sum()} files past the 0.95 GB cap; "
                              f"{(log['status'].str.startswith('blocked')).sum()} files failed"
                              + (f"; not counted for missing FX rate: {no_fx}" if no_fx else ""))


IRS_URL = "https://www.irs.gov/charities-non-profits/form-990-series-downloads"


_WEB = re.compile(r"^(https?://)?(www\.)?[a-z0-9-]+(\.[a-z0-9-]+)+(/\S*)?$", re.I)


def _web(v: str) -> str:
    """990-PF website box, kept only if it looks like a web address (filers also enter emails, N/A and notes)."""
    v = (v or "").strip()
    return v.lower() if "@" not in v and _WEB.match(v) else ""


def _stem_close(a: str, b: str) -> bool:
    sa, sb = matching.stem(a), matching.stem(b)
    return bool(sa and sb) and fuzz.token_sort_ratio(sa, sb) >= 90


def _irs(b: Build, sig, by_src, unresolved) -> None:
    """990-PF Part XV. Pool filter (help file section 4): filers with at least one foreign-address grant in a tax
    period ending inside the window. India = recipient foreign address country IN. A filer with foreign grants but none
    to India has grantee-level data showing no India grant: known_zero, unless another source shows India giving."""
    from ..sources import irs990
    rets, grants = irs990.load()
    if rets.empty:
        b.ledger.log_source("irs_990pf", "IRS Form 990-PF XML (TEOS)", IRS_URL, "download", "skipped",
                            reason="bulk files not yet downloaded or extracted (scripts/download_irs.sh; "
                                   ".venv/bin/python -I scripts/extract_irs.py)")
        return
    n_files = rets["zip"].nunique()
    rets = rets[(rets["tax_period_end"] >= START) & (rets["tax_period_end"] <= END)]
    # one return per filer and tax period: the latest filed (amended returns get higher object ids)
    rets = rets.sort_values("object_id").drop_duplicates(["ein", "tax_period_end"], keep="last")
    grants = grants[grants["object_id"].isin(set(rets["object_id"]))].drop_duplicates(["object_id", "grant_no"]).copy()
    grants["usd"] = pd.to_numeric(grants["amount"], errors="coerce").fillna(0.0).astype(float)
    meta = irs990.zip_meta()
    period = rets.set_index("object_id")["tax_period_end"].to_dict()
    member = rets.set_index("object_id")["member"].to_dict()
    foreign = grants[grants["country"] != "US"]
    keep = sorted(set(foreign["ein"]))
    rets = rets[rets["ein"].isin(keep)]
    by_ein = {r.get("ein"): f for f, r in b.pool.items() if r.get("ein")}
    # filers are matched by name only against funders from the other sources (filers dedupe among themselves by EIN)
    names = {f: r["name"] for f, r in b.pool.items()}
    compact = defaultdict(list)
    for f, n in names.items():
        compact[matching.normalise(n).replace(" ", "")].append(f)
    rets_by = dict(tuple(rets.groupby("ein")))
    grants_by = dict(tuple(grants[grants["ein"].isin(keep)].groupby("ein")))
    counted = zero = added = 0
    for ein in keep:
        rr = rets_by[ein].sort_values("tax_period_end")
        last = rr.iloc[-1]
        name = " ".join(x for x in (last["name"], last["name2"]) if x).strip() or f"EIN {ein}"
        if ein in by_ein:
            fid = by_ein[ein]
            b.add_alias(fid, name)
        else:
            dec, cands = matching.match(name, names)
            squeezed = compact.get(matching.normalise(name).replace(" ", ""), [])
            if dec not in {"exact", "acronym"} and len(squeezed) == 1:  # 'WAL-MART FOUNDATION' = 'Walmart Foundation'
                dec, cands = "exact", [matching.Candidate(squeezed[0], names[squeezed[0]], 100, "exact")]
            # a fuzzy hit is queued only when the distinctive words agree, not just 'foundation'
            cands = [c for c in cands if dec in {"exact", "acronym"} or _stem_close(name, c.name)]
            if dec in {"exact", "acronym"}:
                fid = cands[0].key
                b.add_alias(fid, name)
                b.pool[fid]["ein"] = b.pool[fid].get("ein") or ein
                if "irs_990pf" not in b.pool[fid]["sources"]:
                    b.pool[fid]["sources"].append("irs_990pf")
            else:
                fid = b.add_funder(name, source_key="irs_990pf", country="US", ein=ein,
                                   website=_web(last["website"]),
                                   funder_type_draft="private_foundation", money_origin_draft="foreign",
                                   india_csr_draft="false", notes="990-PF filer with foreign grants")
                added += 1
                if dec in {"fuzzy", "ambiguous"} and cands:
                    b.queue(fid, "possible match with an existing funder (990-PF name)",
                            "|".join(c.name for c in cands[:3]), "merge if same organisation (check EIN)")
            by_ein[ein] = fid
        s = sig[fid]
        g = grants_by[ein]
        india = g[g["country"] == "IN"]
        s["_irs_total"] = s.get("_irs_total", 0.0) + float(pd.to_numeric(rr["grants_paid"], errors="coerce").fillna(0).sum())
        indirect = g[g["country"] == "US"]
        if len(indirect):
            b.queue(fid, "990-PF grants to US intermediaries that may re-grant to India (indirect, not counted)",
                    f"USD {indirect['usd'].sum():,.0f} to " + "; ".join(sorted(set(indirect["recipient"]))[:3]),
                    "keep as indirect; do not count as India giving")
        if india.empty:
            top = g[g["country"] != "US"].sort_values(["usd", "object_id", "grant_no"], ascending=[False, True, True]).iloc[0]
            s["_irs_zero"] = True
            b.ledger.add_evidence(
                funder_id=fid, year_or_period=f"tax periods to {rr['tax_period_end'].max()}",
                measure=f"990-PF Part XV: {len(g[g['country'] != 'US'])} foreign-address grants in window, none to India "
                        "(largest shown)", amount=top["usd"], currency="USD", amount_usd=top["usd"],
                basis="grants paid in tax year", recipient_name=top["recipient"], recipient_country=top["country"],
                purpose_text=top["purpose"][:200], source_key="irs_990pf", source_url=IRS_URL,
                retrieved_at=meta.get(top["zip"], {}).get("retrieved_at", ""),
                file_hash=meta.get(top["zip"], {}).get("file_hash", ""),
                row_ref=f"{top['zip']}:{member[top['object_id']]} grant {top['grant_no']}")
            zero += 1
            continue
        usd = round(float(india["usd"].sum()), 2)
        by_src[fid]["irs_990pf"] = usd
        s["_irs_3y"] = round(float(india.loc[india["object_id"].map(period) >= RECENT, "usd"].sum()), 2)
        s["_irs_grants"] = len(india)
        s["_irs_recips"] = india["recipient"].str.lower().str.strip().nunique()
        s["last_india_year"] = max(s.get("last_india_year", ""), india["object_id"].map(period).max()[:4])
        s["india_evidence_status"] = "known_positive"
        s["_ready"] = max(s.get("_ready", 0), 3)
        s["_quality"] = max(s.get("_quality", 0), 2)
        for x in india.to_dict("records"):
            th = themes.from_text(x["purpose"]) or themes.override(f"990:{x['object_id']}:{x['grant_no']}")
            if th:
                s.setdefault("_themes", defaultdict(float))[th] += x["usd"]
            elif x["purpose"]:
                unresolved[f"990:{x['object_id']}:{x['grant_no']}"] = x["purpose"][:300]
            m = meta.get(x["zip"], {})
            b.ledger.add_evidence(
                funder_id=fid, year_or_period=f"tax period ending {period[x['object_id']]}",
                measure="990-PF Part XV grant paid, recipient address in India", amount=x["usd"], currency="USD",
                amount_usd=x["usd"], basis="grants paid in tax year", recipient_name=x["recipient"],
                recipient_country="IN", recipient_state=x["province"], purpose_text=x["purpose"][:200],
                source_key="irs_990pf", source_url=IRS_URL, retrieved_at=m.get("retrieved_at", ""),
                file_hash=m.get("file_hash", ""), row_ref=f"{x['zip']}:{member[x['object_id']]} grant {x['grant_no']}")
            counted += 1
    b.ledger.log_source("irs_990pf", "IRS Form 990-PF XML (TEOS), Part XV grants paid", IRS_URL, "download", "used",
                        retrieved_at=min((m["retrieved_at"] for m in meta.values()), default=""),
                        file_hash=f"{len(meta)} zips, see evidence rows", rows_read=len(rets),
                        terms_checked="public domain",
                        notes=f"{n_files} zips extracted; tax periods ending {START}..{END}; {len(keep)} filers with "
                              f"foreign-address grants kept ({added} new to the pool); {counted} India grants counted; "
                              f"{zero} filers with foreign grants and none to India (known_zero unless another source "
                              "shows India giving)")


def build() -> dict:
    b = Build(CATEGORY)
    seed_info = _seeds(b)
    _annex_b(b)
    _sangam_foreign(b)
    seed_names = {fid: b.pool[fid]["name"] for fid in seed_info}
    sig: dict[str, dict] = defaultdict(dict)
    by_src: dict[str, dict] = defaultdict(dict)
    unresolved: dict[str, str] = {}

    # ---- IATI ----
    pages = iati.cached_pages("activity") + iati.cached_pages("transaction")
    if pages:
        act = iati.load("activity")
        pubs, hashes, skips = iati_summary.summarise(START, END, RECENT)
        confirmed = iati_summary.confirmed_india_activities
        pub_acts = act.groupby(act["reporting-org-ref"].str.strip().where(act["reporting-org-ref"].str.strip() != "",
                                                                          act["reporting-org"].str.strip()))["iati-identifier"].apply(set).to_dict()
        last_update = max(p.stat().st_mtime for p in pages)
        meta0 = local_file_meta(pages[0])
        # publishers with India activities but no in-window transactions are kept (never drop on unknown)
        for r in act[["reporting-org-ref", "reporting-org", "reporting-org-type-code"]].drop_duplicates().itertuples(index=False):
            key = (r[0] or r[1]).strip()
            if key and key not in pubs:
                pubs[key] = iati_summary.Publisher(r[0].strip(), r[1].strip(), r[2].strip())
        for key, p in sorted(pubs.items()):
            name = p.name or p.ref
            if p.type_code in ROUTED_TYPES:
                b.drop(name, "iati", f"routed to bilateral_multilateral (reporting-org type {p.type_code})")
                continue
            if p.ref.upper().startswith("IN-") or p.type_code == "72":
                b.drop(name, "iati", "out of scope: Indian-registered publisher (domestic categories cover it)")
                continue
            ftype = WESTERN_TYPES.get(p.type_code, "review")
            dec, cands = matching.match(name, seed_names) if b.fid(name) not in b.pool else ("exact", [])
            if b.fid(name) in b.pool:
                fid = b.add_funder(name, source_key="iati", **_ids_from_ref(p.ref))
            elif dec in {"exact", "acronym", "fuzzy"}:
                fid = cands[0].key
                b.add_alias(fid, name)
                b.add_funder(name, source_key="iati", funder_id=fid, **_ids_from_ref(p.ref))
            else:
                fid = b.add_funder(name, source_key="iati", country=_country(p.ref), funder_type_draft=ftype,
                                   money_origin_draft="foreign", india_csr_draft="false", **_ids_from_ref(p.ref))
                if dec == "ambiguous":
                    b.queue(fid, "ambiguous match to seed funder", "|".join(c.name for c in cands),
                            "merge if same organisation")
            if p.type_code in {"70", "71", "73", "90", ""}:
                b.queue(fid, f"funder_type_draft needs review (IATI org type {p.type_code or 'blank'})", "",
                        "set funder_type_draft")
            s = sig[fid]
            if p.usd_5y > 0:
                by_src[fid]["iati"] = round(by_src[fid].get("iati", 0) + p.usd_5y, 2)
                s["iati_usd_3y"] = s.get("iati_usd_3y", 0) + p.usd_3y
                s["india_grants_count_5y"] = s.get("india_grants_count_5y", 0) + len(p.activities)
                s["india_recipients_distinct_5y"] = s.get("india_recipients_distinct_5y", 0) + len(p.receivers)
                s["last_india_year"] = max(s.get("last_india_year", ""), p.last_year)
                s["india_evidence_status"] = "known_positive"
                if p.typed_usd > 0:
                    s["_ngo"] = s.get("_ngo", 0) + p.ngo_usd
                    s["_typed"] = s.get("_typed", 0) + p.typed_usd
                for th, v in p.theme_usd.items():
                    s.setdefault("_themes", defaultdict(float))[th] += v
                for (aid, fy), e in sorted(p.evidence.items()):
                    b.ledger.add_evidence(
                        funder_id=fid, year_or_period=fy, measure="IATI disbursement+expenditure to India",
                        amount=round(e["usd"], 2), currency="USD", amount_usd=round(e["usd"], 2),
                        fx_source=e.get("fx", ""),
                        basis="disbursement+expenditure, current USD" + (", India % share applied" if e["multi"] else ""),
                        recipient_name=e["receiver"], recipient_country="IN", purpose_text=e["purpose"],
                        source_key="iati", source_url=f"https://d-portal.org/q.html?aid={aid}",
                        retrieved_at=meta0["retrieved_at"], file_hash=hashes[e["rows"][0].split(":")[0]],
                        row_ref=f"{aid} | " + ";".join(e["rows"][:5]) + (" ..." if len(e["rows"]) > 5 else ""))
            else:
                india_aids = sorted(pub_acts.get(key, set()) & confirmed)
                if india_aids:  # confirmed-India activity exists, but no spend in window: positive, amount unknown
                    s.setdefault("india_evidence_status", "known_positive")
                    s.setdefault("_note", "IATI India activity, no disbursement in window")
                    aid = india_aids[0]
                    row = act[act["iati-identifier"] == aid].iloc[0]
                    b.ledger.add_evidence(funder_id=fid, year_or_period=row["start-actual"] or row["start-planned"],
                                          measure="IATI India activity (no in-window spend)", recipient_country="IN",
                                          purpose_text=row["title"][:200], source_key="iati",
                                          source_url=f"https://d-portal.org/q.html?aid={aid}",
                                          retrieved_at=meta0["retrieved_at"], file_hash=hashes[row["_page"]],
                                          row_ref=f"{aid} | {row['_page']}:{row['_row']} (+{len(india_aids) - 1} more)")
                else:
                    s.setdefault("_note", "IATI activities list India only within multi-country scope (not counted)")
            if p.indirect_usd > 0:
                b.queue(fid, "spend to US intermediary (indirect, not counted)", f"USD {p.indirect_usd:,.0f}",
                        "keep as indirect; do not count as India giving")
                s.setdefault("_note2", "indirect: part of India-tagged spend goes via a US intermediary (not counted)")
            if p.unsplit_usd > 0:
                b.queue(fid, "multi-country IATI spend without India % (not counted)",
                        f"USD {p.unsplit_usd:,.0f}", "leave uncounted unless publisher splits by country")
            s["_ready"] = max(s.get("_ready", 0), 2)
            s["_quality"] = max(s.get("_quality", 0), 1)
            unresolved.update(p.unresolved_purposes)
        b.ledger.log_source("iati", "IATI Datastore Classic (activity + transaction CSV, recipient-country=IN)",
                            IATI_URL.format(kind="transaction"), "api", "used",
                            retrieved_at=meta0["retrieved_at"], file_hash=f"{len(hashes)} pages, see evidence rows",
                            rows_read=len(act), terms_checked="publisher licences vary",
                            notes=f"window {START}..{END}; spend = transaction types 3+4; multi-country w/o % not counted; "
                                  "skip counts (org type, reason): " + "; ".join(f"{k[0]}/{k[1]}={v}" for k, v in sorted(skips.items())))
    else:
        b.ledger.log_source("iati", "IATI Datastore Classic", IATI_URL.format(kind="activity"), "api", "skipped",
                            reason="no cached pages; run python -m funder_pool.sources.iati")

    # ---- Funding orgs named in other publishers' India activities (no amount attributable) ----
    if pages:
        fund_cols = ["participating-org (Funding)", "participating-org-ref (Funding)", "participating-org-type-code (Funding)"]
        named = defaultdict(set)
        act_by_id = act.set_index("iati-identifier")
        for r in act[fund_cols + ["iati-identifier"]].to_dict("records"):
            ns = r[fund_cols[0]].split(";")
            rs = r[fund_cols[1]].split(";")
            ts = r[fund_cols[2]].split(";")
            for j, n in enumerate(ns):
                t = ts[j].strip() if j < len(ts) else ""
                ref = rs[j].strip() if j < len(rs) else ""
                if (n.strip() and t in {"60", "70", "71", "73", "21"} and not ref.upper().startswith("IN-")
                        and r["iati-identifier"] in confirmed):
                    named[(n.strip(), ref, t)].add(r["iati-identifier"])
        for (n, ref, t), aids in sorted(named.items()):
            if MULTI_REF.match(ref):
                b.drop(n, "iati", f"routed to bilateral_multilateral (Funding org ref {ref})")
                continue
            if not ref and INDIAN_FORM.search(n):
                b.drop(n, "iati", "out of scope: Indian-registered company or trust (domestic categories cover it)")
                continue
            existing = b.candidates()
            cid = {k: {"iati_org_id": b.pool[k.split("||")[0]].get("iati_org_id", "")} for k in existing}
            dec, cands = matching.match(n, existing, ids={"iati_org_id": ref}, candidate_ids=cid)
            by_ref = {r.get("iati_org_id"): f for f, r in b.pool.items() if r.get("iati_org_id")}
            if ref and ref in by_ref:
                fid = by_ref[ref]
                b.add_alias(fid, n)
            elif b.fid(n) in b.pool:
                fid = b.add_funder(n, source_key="iati")
            elif dec in {"id", "exact", "acronym", "fuzzy"}:
                fid = cands[0].key.split("||")[0]
                b.add_alias(fid, n)
            else:
                fid = b.add_funder(n, source_key="iati", country=_country(ref), funder_type_draft=WESTERN_TYPES.get(t, "review"),
                                   money_origin_draft="foreign", india_csr_draft="false",
                                   notes="named as Funding org in another publisher's India activity", **(_ids_from_ref(ref) if ref else {}))
            s = sig[fid]
            s.setdefault("india_evidence_status", "known_positive")
            s["_funded_activities"] = s.get("_funded_activities", 0) + len(aids)
            aid = sorted(aids)[0]
            row = act_by_id.loc[aid]
            b.ledger.add_evidence(funder_id=fid, year_or_period=row["start-actual"] or row["start-planned"],
                                  measure="named as Funding org on IATI India activity (amount not attributable)",
                                  recipient_name=row["reporting-org"], recipient_country="IN", purpose_text=row["title"][:200],
                                  source_key="iati", source_url=f"https://d-portal.org/q.html?aid={aid}",
                                  retrieved_at=meta0["retrieved_at"], file_hash=hashes[row["_page"]],
                                  row_ref=f"{aid} | {row['_page']}:{row['_row']} (+{len(aids) - 1} more)")
            s["_ready"] = max(s.get("_ready", 0), 1)
            s["_quality"] = max(s.get("_quality", 0), 1)

    # ---- sources not yet available ----
    _irs(b, sig, by_src, unresolved)
    b.ledger.log_source("irs_990_sched_f", "IRS Form 990 Schedule F", "https://www.irs.gov/charities-non-profits/form-990-series-downloads",
                        "download", "skipped", reason="Schedule F Part II gives region only (South Asia) and no recipient names; "
                                                      "cannot confirm India. Files are downloaded with the 990-PF zips")
    b.ledger.log_source("irs_bmf", "IRS EO Business Master File extract (eo1 to eo4)",
                        "https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf",
                        "download", "skipped", reason="every pool entry from IRS is a 990-PF filer, so the foundation code adds "
                                                      "nothing to funder_type; files are in data/raw/irs_bmf for the import agent "
                                                      "(NTEE code, ruling date)", rows_read=0)
    m1 = sorted(MANUAL.glob("oecd_pp4d_crs*")) if MANUAL.exists() else []
    b.ledger.log_source("oecd_philanthropy", "OECD Private Philanthropy for Development (M1/M2/M3/M5/M6)",
                        "https://www.oecd-ilibrary.org/development/data/oecd-international-development-statistics/creditor-reporting-system-private-philanthropy-for-development-edition-2023_dd620077-en",
                        "manual_file", "blocked", reason="oecd-ilibrary returns 403 to scripts; M1, M2, M5, M6 (grant-level data) "
                                                         "not supplied. M3 (Annex B roster) is used; it has no amounts")
    _threesixty(b, sig, by_src, unresolved)

    # ---- signals ----
    for fid, info in seed_info.items():
        s = sig[fid]
        if info["status"] == "known_positive":
            s["india_evidence_status"] = "known_positive"
        if info["seed_usd"]:
            by_src[fid]["manual_seed_1yr"] = info["seed_usd"]
            s["_seed_period"] = info["seed_period"]
        s["_ready"] = max(s.get("_ready", 0), 1)
    for fid in b.pool:
        s = sig[fid]
        if "_irs_grants" in s:
            s["india_grants_count_5y"] = s.get("india_grants_count_5y", 0) + s["_irs_grants"]
            s["india_recipients_distinct_5y"] = s.get("india_recipients_distinct_5y", 0) + s["_irs_recips"]
        country = b.pool[fid].get("country", "")
        pref = PREF.get(country, PREF_OTHER)
        vals = by_src.get(fid, {})
        best, used, disagree = by_source_best(vals, pref)
        s["india_usd_by_source"] = vals
        s["india_usd_best"] = best
        s["source_preference_used"] = used
        s["sources_disagree"] = disagree if len(vals) > 1 else ""
        s["india_usd_5y"] = best
        s["india_usd_3y"] = {"iati": s.get("iati_usd_3y"), "threesixtygiving": s.get("_ts_3y"),
                             "irs_990pf": s.get("_irs_3y")}.get(used)
        if s.get("_irs_total"):
            s["total_giving_usd_5y"] = round(s["_irs_total"], 2)
        if used == "manual_seed_1yr":
            b.pool[fid]["notes"].append(f"india_usd_5y is a single-year lower bound ({s.get('_seed_period')}, seed)")
        for k in ("_note", "_note2"):
            if s.get(k):
                b.pool[fid]["notes"].append(s[k])
        if s.get("_funded_activities"):
            b.pool[fid]["notes"].append(f"Funding org on {s['_funded_activities']} India IATI activities (amount not attributable)")
        if disagree:
            b.queue(fid, "sources disagree by >50%", str(vals), "check basis and period of each source")
        s["funds_ngos_share"] = round(s["_ngo"] / s["_typed"], 3) if s.get("_typed") else None
        th = s.get("_themes") or {}
        s["themes"] = "|".join(k for k, _ in sorted(th.items(), key=lambda kv: -kv[1])[:5])
        s["ingest_readiness"] = s.get("_ready", 0)
        s["evidence_quality"] = s.get("_quality", 0)
        s["recency_3y"] = s["india_usd_3y"]
        g, r = s.get("india_grants_count_5y"), s.get("india_recipients_distinct_5y")
        s["breadth_recipients_and_grants"] = (math.log1p(g or 0) + math.log1p(r or 0)) if (g or r) else None
        s["india_share_of_giving"] = (round(by_src[fid]["irs_990pf"] / s["_irs_total"], 4)
                                      if s.get("_irs_total") and "irs_990pf" in by_src.get(fid, {}) else None)
        s["india_share"] = s["india_share_of_giving"]
        if s.get("_irs_zero") and s.get("india_evidence_status") != "known_positive":
            s["india_evidence_status"] = "known_zero"
        s.setdefault("india_evidence_status", "unknown")
        if s["india_evidence_status"] == "unknown":
            b.queue(fid, "India giving unknown", "", "check OECD M1/M2 or IRS once available")

    # intermediaries trap: flag, never count
    for fid, r in b.pool.items():
        for name in [r["name"], *r["aliases"]]:
            if any(matching.normalise(name) == matching.normalise(x) for x in US_INTERMEDIARIES):
                r["notes"].append("indirect: US intermediary re-granting to India; grants TO it are not India giving")
    b.signals = {fid: {k: v for k, v in s.items() if not k.startswith("_") and k != "iati_usd_3y"} for fid, s in sig.items()}

    # cache unresolved purposes for in-session classification (config/theme_overrides.csv)
    if unresolved:
        from ..core.paths import CACHE
        CACHE.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(sorted(unresolved.items()), columns=["key", "purpose_text"]).to_csv(
            CACHE / "western_unresolved_purposes.csv", index=False)

    bins = config.thresholds()["distribution_bins_usd"]
    notes = [f"India window FY2021-22 to FY2025-26 ({START} to {END}); recent window from {RECENT}.",
             "india_usd_5y comes from one source per funder (india_usd_best); sources are never summed.",
             "IATI spend = disbursements + expenditure (types 3, 4). Multi-country activities without an India % are not counted.",
             "IRS 990-PF Part XV: India = recipient foreign address in India, tax periods ending in the window. "
             "total_giving_usd_5y and india_share_of_giving are filled for 990-PF filers only (grants paid, Part I line 25).",
             "990-PF filers with foreign grants but none to India are known_zero (grantee-level data), unless another "
             "source shows India giving. Grants to US intermediaries are flagged indirect and not counted.",
             "OECD grant data (M1, M2, M5, M6) not available; 360Giving total giving is not computed.",
             "Funders named only as Funding org in others' IATI activities have India evidence but no attributable amount.",
             "Priority bands are blank by design."]
    return finalize(b, "western", value_col="india_usd_5y", bins=bins, unit="USD", notes=notes,
                    extra_signal_cols=["recency_3y", "breadth_recipients_and_grants", "india_share_of_giving",
                                       "evidence_quality"])

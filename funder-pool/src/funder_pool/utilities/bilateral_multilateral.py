"""bilateral_multilateral: foreign government agencies and multilaterals.
Help file: docs/funder-sources/bilateral-multilateral.md.

- IATI publishers typed government (10, 11, 15), PPP (30) or multilateral (40); Indian (IN-) publishers are out of scope.
- india_usd_5y = commitments (type 2) by default; disbursements + expenditure (3, 4) are kept apart and used only
  when a publisher reports no commitments. The basis is recorded per funder.
- Donor and implementer (for example BMZ and GIZ) are separate funders linked by parent_name; never summed.
- Budget annex (Receipt Budget, external assistance) gives a roster of partners with no per-partner amounts here.
- CRS is not loaded; if it ever is, keep it in its own column and never add it to IATI.
"""
import re
from collections import Counter, defaultdict

import pandas as pd

from ..core import config, matching
from ..core.provenance import RobotsDisallowed, cached_fetch, local_file_meta
from ..sources import iati, iati_summary
from .common import Build, finalize

CATEGORY = "bilateral_multilateral"
START, END, RECENT = "2021-04-01", "2026-03-31", "2023-04-01"
BILATERAL_TYPES = {"10", "11", "15", "30", "40"}
IATI_URL = iati.BASE + "/{kind}.csv?recipient-country=IN"
ANNEX = {"2025-26": "https://indiabudget.gov.in/doc/rec/annex13.pdf",
         "2024-25": "https://indiabudget.gov.in/budget2024-25/doc/rec/annex13.pdf"}
HEADING = re.compile(r"^(?:\(?[a-z0-9]{1,3}[\).]\s*)([A-Z][A-Z0-9 ()&,.'/-]{3,}?):?$")
SKIP_HEADINGS = {"WORLD BANK GROUP"}


def _annex_partners() -> tuple[list[tuple[str, str, int]], dict | None, str]:
    """Partner headings from the latest Receipt Budget annex. Returns ([(name, section, line)], meta, error)."""
    import pdfplumber
    for fy, url in ANNEX.items():
        try:
            m = cached_fetch(url, "budget_annex", f"annex13_{fy}.pdf")
        except (RobotsDisallowed, Exception) as e:  # noqa: BLE001 - logged as blocked
            err = f"{type(e).__name__}: {e}"
            continue
        with pdfplumber.open(m["path"]) as pdf:
            text = "\n".join((pg.extract_text() or "") for pg in pdf.pages)
        out, section = [], ""
        for i, line in enumerate(text.split("\n")):
            line = line.strip()
            if "MULTILATERAL SOURCES" in line:
                section = "multilateral"
            elif "BILATERAL SOURCES" in line:
                section = "bilateral"
            mm = HEADING.match(line)
            if mm and section:
                name = mm.group(1).strip().rstrip(":").strip()
                if name not in SKIP_HEADINGS:
                    out.append((name.title().replace("(Ibrd)", "(IBRD)").replace("(Ida)", "(IDA)")
                                .replace("(Adb)", "(ADB)").replace("(Eib)", "(EIB)").replace("(Ndb)", "(NDB)")
                                .replace("(Aiib)", "(AIIB)").replace("(Ifad)", "(IFAD)").replace("Fedration", "Federation"),
                                section, i + 1))
        return out, {**m, "fy": fy}, ""
    return [], None, err


def _country(ref: str) -> str:
    head = ref.split("-")[0] if ref else ""
    return head if len(head) == 2 and head.isalpha() and head not in {"XM", "XI", "XB"} else ""


def build() -> dict:
    b = Build(CATEGORY)
    sig: dict[str, dict] = defaultdict(dict)
    pages = iati.cached_pages("activity") + iati.cached_pages("transaction")
    links: dict[str, Counter] = defaultdict(Counter)

    if pages:
        act = iati.load("activity")
        pubs, hashes, skips = iati_summary.summarise(START, END, RECENT)
        confirmed = iati_summary.confirmed_india_activities
        meta0 = local_file_meta(pages[0])
        pkey = act["reporting-org-ref"].str.strip().where(act["reporting-org-ref"].str.strip() != "",
                                                           act["reporting-org"].str.strip())
        pub_acts = act.groupby(pkey)["iati-identifier"].apply(set).to_dict()
        for r in act[["reporting-org-ref", "reporting-org", "reporting-org-type-code"]].drop_duplicates().itertuples(index=False):
            key = (r[0] or r[1]).strip()
            if key and key not in pubs:
                pubs[key] = iati_summary.Publisher(r[0].strip(), r[1].strip(), r[2].strip())
        # activities returned by the recipient-country=IN query with no activity-level country: India is on the
        # transactions (US publishers do this). Kept as unknown until transactions are read; never dropped.
        blank_acts = set(act.loc[act["recipient-country-code"].fillna("").str.strip() == "", "iati-identifier"])
        ref_to_fid: dict[str, str] = {}
        for key, p in sorted(pubs.items()):
            if p.type_code not in BILATERAL_TYPES:
                continue  # other publishers belong to western_funders (which logs the routing)
            name = p.name or p.ref
            if p.ref.upper().startswith("IN-"):
                b.drop(name, "iati", "out of scope: Indian government publisher (government_india covers it)")
                continue
            india_aids = pub_acts.get(key, set()) & confirmed
            blank_country = pub_acts.get(key, set()) & blank_acts
            if not (p.usd_5y or p.commit_5y or india_aids or blank_country):
                b.drop(name, "iati", "cost filter: no activity with recipient country India (multi-country only)")
                continue
            fid = b.add_funder(name, source_key="iati", iati_org_id=p.ref, country=_country(p.ref),
                               funder_type_draft="bilateral_multilateral", money_origin_draft="foreign",
                               india_csr_draft="false")
            if p.ref:
                ref_to_fid[p.ref] = fid
            s = sig[fid]
            s["_commit"] = s.get("_commit", 0) + p.commit_5y
            s["_commit3"] = s.get("_commit3", 0) + p.commit_3y
            s["_disb"] = s.get("_disb", 0) + p.usd_5y
            s["_disb3"] = s.get("_disb3", 0) + p.usd_3y
            s["_acts"] = s.get("_acts", set()) | p.activities | p.commit_activities | india_aids
            s["_ngo"] = s.get("_ngo", 0) + p.ngo_usd
            s["_typed"] = s.get("_typed", 0) + p.typed_usd
            s["last_india_year"] = max(s.get("last_india_year", ""), p.last_year)
            s["india_recipients_distinct_5y"] = s.get("india_recipients_distinct_5y", 0) + len(p.receivers)
            if p.usd_5y or p.commit_5y or india_aids:
                s["india_evidence_status"] = "known_positive"
            else:
                b.queue(fid, "India only at transaction level and no in-window India transactions read",
                        f"{len(blank_country)} activities", "check transactions once the IATI fetch is complete")
            for th, v in p.theme_usd.items():
                s.setdefault("_themes", defaultdict(float))[th] += v
            for (aid, fy), e in sorted(p.evidence.items()):
                b.ledger.add_evidence(
                    funder_id=fid, year_or_period=fy, measure="IATI disbursement+expenditure to India",
                    amount=round(e["usd"], 2), currency="USD", amount_usd=round(e["usd"], 2), fx_source=e.get("fx", ""),
                    basis="disbursement+expenditure, current USD" + (", India % share applied" if e["multi"] else ""),
                    recipient_name=e["receiver"], recipient_country="IN", purpose_text=e["purpose"],
                    source_key="iati", source_url=f"https://d-portal.org/q.html?aid={aid}",
                    retrieved_at=meta0["retrieved_at"], file_hash=hashes[e["rows"][0].split(":")[0]],
                    row_ref=f"{aid} | " + ";".join(e["rows"][:5]) + (" ..." if len(e["rows"]) > 5 else ""))
            if not p.evidence and (india_aids or p.commit_activities):
                aids = sorted(india_aids or p.commit_activities)
                aid = aids[0]
                row = act[act["iati-identifier"] == aid].iloc[0]
                b.ledger.add_evidence(funder_id=fid, year_or_period=row["start-actual"] or row["start-planned"],
                                      measure="IATI India activity (commitments only or no in-window spend)",
                                      amount=round(p.commit_5y, 2) if p.commit_5y else "", currency="USD" if p.commit_5y else "",
                                      amount_usd=round(p.commit_5y, 2) if p.commit_5y else "",
                                      basis="commitments in window, all activities" if p.commit_5y else "activity listing",
                                      recipient_country="IN", purpose_text=row["title"][:200], source_key="iati",
                                      source_url=f"https://d-portal.org/q.html?aid={aid}",
                                      retrieved_at=meta0["retrieved_at"], file_hash=hashes[row["_page"]],
                                      row_ref=f"{aid} | {row['_page']}:{row['_row']} (+{len(aids) - 1} more)")
            if p.unsplit_usd > 0:
                b.queue(fid, "multi-country IATI spend without India % (not counted)", f"USD {p.unsplit_usd:,.0f}",
                        "leave uncounted unless publisher splits by country")
            # donor links: government/multilateral Funding orgs on this publisher's India activities
            for aid in sorted(pub_acts.get(key, set()) & confirmed):
                rr = act.loc[act["iati-identifier"] == aid].iloc[0]
                ns = rr["participating-org (Funding)"].split(";")
                rs = rr["participating-org-ref (Funding)"].split(";")
                ts = rr["participating-org-type-code (Funding)"].split(";")
                for j, n in enumerate(ns):
                    n, ref = n.strip(), (rs[j].strip() if j < len(rs) else "")
                    t = ts[j].strip() if j < len(ts) else ""
                    if not n or ref == p.ref or matching.normalise(n) == matching.normalise(name):
                        continue
                    # implementer link only: a government agency funded by a government body of the same country
                    # (e.g. GIZ <- BMZ). Multilaterals' core donors are not parents.
                    if (p.type_code in {"10", "11", "15"} and t in {"10", "11", "15"}
                            and _country(p.ref) and _country(ref) == _country(p.ref)):
                        links[fid][(n, ref, t)] += 1
        b.ledger.log_source("iati", "IATI Datastore Classic (activity + transaction CSV, recipient-country=IN)",
                            IATI_URL.format(kind="transaction"), "api", "used", retrieved_at=meta0["retrieved_at"],
                            file_hash=f"{len(hashes)} pages, see evidence rows", rows_read=len(act),
                            terms_checked="publisher licences vary",
                            notes=f"window {START}..{END}; reporting-org types {sorted(BILATERAL_TYPES)}; "
                                  "commitments (2) kept apart from disbursement+expenditure (3, 4)")

        # donor <- implementer links (parent_name); donors not publishing themselves are added as roster funders
        for fid, cnt in sorted(links.items()):
            (n, ref, t), k = cnt.most_common(1)[0]
            parent = ref_to_fid.get(ref)
            if not parent:
                parent = b.add_funder(n, source_key="iati", iati_org_id=ref, country=_country(ref),
                                      funder_type_draft="bilateral_multilateral", money_origin_draft="foreign",
                                      india_csr_draft="false", notes="named as Funding org on another publisher's India activities")
                if ref:
                    ref_to_fid[ref] = parent
                sig[parent].setdefault("india_evidence_status", "known_positive")
                sig[parent]["_ready"] = max(sig[parent].get("_ready", 0), 1)
                b.ledger.add_evidence(funder_id=parent, measure="named as Funding org on IATI India activity (amount not attributable)",
                                      recipient_name=b.pool[fid]["name"], recipient_country="IN", source_key="iati",
                                      source_url=IATI_URL.format(kind="activity"), retrieved_at=meta0["retrieved_at"],
                                      file_hash=f"{len(hashes)} pages", row_ref=f"Funding org on {k} activities of {b.pool[fid]['iati_org_id']}")
            if parent == fid:
                continue
            b.pool[fid]["parent_name"] = b.pool[fid].get("parent_name") or b.pool[parent]["name"]
            b.pool[fid]["notes"].append(f"implements for {b.pool[parent]['name']} on {k} India activities; amounts never summed")
            if len(cnt) > 1:
                b.queue(fid, "several funding agencies on India activities", "|".join(x[0] for x, _ in cnt.most_common(5)),
                        "confirm parent_name")
    else:
        b.ledger.log_source("iati", "IATI Datastore Classic", IATI_URL.format(kind="activity"), "api", "skipped",
                            reason="no cached pages; run python -m funder_pool.sources.iati")

    # ---- Budget annex roster ----
    partners, am, err = _annex_partners()
    if am:
        b.ledger.log_source("budget_annex", f"Union Budget Receipt Budget {am['fy']}, Annex: External Assistance",
                            am["url"], "download", "used", retrieved_at=am["retrieved_at"], file_hash=am["file_hash"],
                            rows_read=len(partners), terms_checked="public document",
                            notes="partner headings only; amounts in the annex are aggregate, not per partner")
        cands = b.candidates()
        for name, section, line in partners:
            dec, cs = matching.match(name, cands)
            if dec in {"exact", "acronym", "fuzzy"}:
                fid = cs[0].key.split("||")[0]
                b.add_funder(name, source_key="budget_annex", funder_id=fid)
                b.add_alias(fid, name)
            else:
                label = f"Government of {name}" if section == "bilateral" else name
                fid = b.add_funder(label, source_key="budget_annex", funder_type_draft="bilateral_multilateral",
                                   money_origin_draft="foreign", india_csr_draft="false",
                                   notes=f"{section} partner in Union Budget external assistance annex; agency not yet resolved"
                                   if section == "bilateral" else f"{section} partner in Union Budget external assistance annex")
                if section == "bilateral":
                    b.queue(fid, "bilateral partner named as a country; agencies (e.g. JICA, KfW, AFD) may already be IATI funders",
                            "", "link to agency funders or merge")
            s = sig[fid]
            s.setdefault("india_evidence_status", "known_positive")
            s["_ready"] = max(s.get("_ready", 0), 1)
            s["_quality"] = max(s.get("_quality", 0), 1)
            b.ledger.add_evidence(funder_id=fid, year_or_period=f"FY{am['fy']}", measure="named India external assistance partner",
                                  basis="roster listing; loans and grants to Government of India", recipient_name="Government of India",
                                  recipient_country="IN", source_key="budget_annex", source_url=am["url"],
                                  retrieved_at=am["retrieved_at"], file_hash=am["file_hash"], row_ref=f"annex13_{am['fy']}.pdf:line {line}")
    else:
        b.ledger.log_source("budget_annex", "Union Budget Receipt Budget annex", ANNEX["2025-26"], "download", "blocked",
                            reason=err or "fetch failed")

    # ---- sources not loaded ----
    gz = [k for k in ref_to_fid if k in ("XM-DAC-5-7", "DE-1")] if pages else []
    b.ledger.log_source("giz", "GIZ project data / GIZ IATI publisher", "https://iatiregistry.org/publisher/about/giz",
                        "api", "used" if gz else "skipped",
                        reason="" if gz else "GIZ/BMZ not found among IATI India publishers in the cached pages",
                        notes="read through the IATI datastore (same data as the GIZ IATI publisher files); "
                              "giz.de project pages not scraped" if gz else "")
    b.ledger.log_source("devtracker", "FCDO DevTracker India page", "https://devtracker.fcdo.gov.uk/countries/in", "download",
                        "skipped", reason="DevTracker renders FCDO's own IATI data (GB-GOV-1 and partners), already read from "
                                          "the IATI datastore; reading both would double count")
    b.ledger.log_source("oecd_crs", "OECD Creditor Reporting System", "https://data-explorer.oecd.org/", "manual_file",
                        "skipped", reason="Data Explorer cloud copy of CRS stopped 1 Feb 2026; API not tested. IATI used "
                                          "for amounts; CRS would be a separate column, never added to IATI")
    b.ledger.log_source("other", "World Bank, ADB, UN and EU portals", "", "download", "skipped",
                        reason="not researched (help file section 9)")

    # ---- signals ----
    for fid in b.pool:
        s = sig[fid]
        commit, disb = s.get("_commit", 0), s.get("_disb", 0)
        if commit > 0:
            best, basis, recent = commit, "commitment", s.get("_commit3", 0)
        elif disb > 0:
            best, basis, recent = disb, "disbursement+expenditure", s.get("_disb3", 0)
        else:
            best, basis, recent = None, "", None
        s["india_usd_5y"] = best
        s["india_usd_3y"] = recent
        s["india_usd_best"] = best
        s["india_usd_by_source"] = {"iati": round(best, 2)} if best else {}
        s["source_preference_used"] = f"iati ({basis})" if basis else ""
        s["india_usd_commit_5y"] = round(commit, 2) if commit else None
        s["india_usd_disbursed_5y"] = round(disb, 2) if disb else None
        s["recency_3y"] = recent
        acts = s.get("_acts", set())
        s["activity_count"] = len(acts) if acts else None
        s["india_grants_count_5y"] = s["activity_count"]
        # blank (not zero) where the implementing org type is missing on every counted transaction
        s["ngo_channel_share"] = round(s["_ngo"] / s["_typed"], 3) if s.get("_typed") else None
        s["funds_ngos_share"] = s["ngo_channel_share"]
        th = s.get("_themes") or {}
        s["themes"] = "|".join(k for k, _ in sorted(th.items(), key=lambda kv: -kv[1])[:5])
        has_tx = bool(s.get("_disb") or s.get("_commit"))
        s["ingest_readiness"] = max(s.get("_ready", 0), 3 if s.get("_disb") else (2 if has_tx else 0))
        s["evidence_quality"] = max(s.get("_quality", 0), 2 if has_tx else 0)
        s.setdefault("india_evidence_status", "unknown")
        if basis == "disbursement+expenditure":
            b.pool[fid]["notes"].append("no commitments reported in window; india_usd_5y uses disbursement+expenditure")
    b.signals = {fid: {k: v for k, v in s.items() if not k.startswith("_")} for fid, s in sig.items() if fid in b.pool}

    bins = config.thresholds()["distribution_bins_usd"]
    notes = [f"Window FY2021-22 to FY2025-26 ({START} to {END}); recent window from {RECENT}.",
             "india_usd_5y = IATI commitments by default; disbursements are a separate column and used only where no "
             "commitments are reported (basis in source_preference_used).",
             "Donor and implementer are separate funders linked by parent_name; their amounts are never added.",
             "ngo_channel_share is blank where the implementing organisation type is missing.",
             "CRS not loaded. Budget annex partners are a roster without per-partner amounts.",
             "Expect low ngo_channel_share: most of this money goes to government and large partners.",
             "Priority bands are blank by design."]
    return finalize(b, "bilateral_multilateral", value_col="india_usd_5y", bins=bins, unit="USD", notes=notes,
                    extra_signal_cols=["india_usd_commit_5y", "india_usd_disbursed_5y", "recency_3y", "activity_count",
                                       "ngo_channel_share", "evidence_quality"])

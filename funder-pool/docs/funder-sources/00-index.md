# Funder sources: index and shared conventions

This folder tells you, and the future import agent, where each kind of funder data lives and how to read it. Read this file first, then the help file for the category you are working on.

## Routing

| Category | Help file | Draft funder_type values | Main source_key values | Manual files |
|---|---|---|---|---|
| Foreign private philanthropy | western-funders.md | private_foundation, intermediary, csr_foundation, csr_company, international_agency, other | oecd_philanthropy, irs_990pf, irs_990_sched_f, iati, threesixtygiving | M1 to M7, M12, M13 |
| Indian CSR | indian-csr.md | csr_company, csr_foundation | mca_csr, brsr, company_site | M3, M4, M7, M10, M11 |
| Indian HNIs and family foundations | hni-family-foundations.md | hni, private_foundation | hurun_india, oecd_india, foundation_site | M3, M4, M7, M8 |
| Indian government | government-india.md | government | ngo_darpan, nabard, ministry_site, parliament_qa | M9 |
| Foreign governments and multilaterals | bilateral-multilateral.md | bilateral_multilateral | iati, oecd_crs, devtracker, giz | M1 |

Facts sit in the help files. When code and a help file disagree, fix whichever is wrong and log it in CHANGELOG.md.

## The nine funder types (issue #324 proposal)

| Value | Label | Rolls up to |
|---|---|---|
| csr_company | Corporate, run by the company | Corporate |
| csr_foundation | Corporate, through its foundation | Corporate |
| private_foundation | Private or family foundation | Philanthropy |
| hni | Individual or giving network | HNI |
| intermediary | Re-granting fund or intermediary (includes community foundations and donor-advised fund sponsors) | Philanthropy |
| international_agency | International development or church agency | Philanthropy |
| bilateral_multilateral | Bilateral or multilateral donor | Govt. |
| government | Government or statutory body | Govt. |
| other | Other (lotteries, impact investors, anything that fits nowhere) | Other |

These values are draft labels in the pool. Sangam adopts them when issue #324 merges.

Related flags:
- **india_csr**: true only where the money counts as Section 135 spend, so the recipient needs CSR-1. False for every foreign funder. Review for Indian companies below the Section 135 thresholds.
- **money_origin**: foreign, domestic, mixed or unknown. Foreign-owned Indian subsidiaries need the FCRA foreign-source check noted in issue #324.
- **source_funder_type**: keep the source's own label (for example family, daf_sponsor, community) in notes for traceability.

## Rules shared by every category

1. **India giving is a signal.** It never decides whether a funder enters the pool.
2. **Unknown is not zero.** Use known_positive, known_zero (only with grantee-level data that shows no India grant) or unknown.
3. **Do not add across sources.** Keep one column per source. Choose the best value by the help file's source order.
4. **Identity.** Match on an external identifier first (EIN, UK charity number, RSIN, IATI ID, CIN), then on normalised name plus country. Send every ambiguous match to review_queue.csv. A company and its foundation are two funders linked by parent_name. A donor and the foundation they give through are one funder with an alias.
5. **Currency.** Keep the original amount and currency. Convert to USD at the annual average rate for the grant year and record the rate and its source. Indian sources stay in INR crore.
6. **Fiscal year.** Sangam uses Indian fiscal years (FYyyyy-yy, April to March). Map a grant to the Indian year containing its payment date, or the source period end when there is no date. Keep the original period in as_of.
7. **Provenance.** Every fact carries source_key, source_url, retrieved_at, file_hash and row_ref.
8. **Already in Sangam.** Mark yes, related or no. Exclude yes rows from ingest_queue.csv.

## Terms and legal notes

- Use official downloads and APIs, rate-limited and cached. Respect robots.txt. The OECD site blocked automated page fetches in testing, so expect manual downloads for some OECD files.
- Do not use Kindora for bulk extraction: its terms bar bulk extraction without a partner agreement. Candid, Daanveda and Stiftungssuche are paid and out of scope.
- Named individuals from public lists are allowed (user decision, 13 Nov 2026). Store name, rank, amount, cause, foundation and city as published, and nothing else. Legal flag: under India's DPDP Act a name is personal data, and the exemption for publicly available data is unsettled for lists compiled by a third party. Add this to the legal review that issue #324 already plans for FCRA.

## Export for the ingest agent

The Sangam ingest agent reads a versioned export instead of downloading and parsing the sources again. Build it after the utility builds and `combine`:

    .venv/bin/python -I scripts/export_for_ingest.py        # writes data/export/<YYYY-MM-DD>/

| Path | Contents |
|---|---|
| funders/<category>/ | pool, signals, evidence, sources_log for each of the five utilities |
| funders/combined/ | pool_all, ingest_queue, cross_category_matches |
| funders/combined/funder_pool_load.csv | One row per pool funder for a Sangam queue table (funder_pool): pool_funder_id, category, name, cin, rank_in_category, score_total, csr_spend_3y_avg_cr, in_sangam_at_load, ingest_status (pending; skipped where in_sangam is yes; needs_review where related), export_version, and signals (every other non-blank pool column as JSON). It does not copy the columns of Sangam's funders table: once a funder is ingested, funders is the source of truth. Built by core/pool_load.py. |
| grants/irs990_returns.csv.gz, irs990_grants.csv.gz | Every extracted 990-PF return and every foreign grant (plus US grants to India intermediaries), all years, with zip, retrieved_at and file_hash. Individual recipients appear only as 'individual recipient'. |
| grants/iati_activity.csv.gz, iati_transaction.csv.gz | IATI India activities and transactions, deduplicated as in sources/iati.py, with page and row for provenance |
| grants/oecd_annex_b.csv | OECD PP4D Third Edition Annex B organisation list. OECD grant-level data was blocked to scripts and is not included. |
| MANIFEST.json | Rows, bytes and sha256 per file, licences, git commit, build window, missing inputs |

Not exported: data/raw (re-downloadable), third-party files in data/manual (Hurun, CSRAnalytics, MCA, OECD PDFs) and the Sangam funder export. The grant tables are not windowed; apply the window in MANIFEST.json for India totals. Refresh monthly: `scripts/download_irs.sh` fetches only new IRS zips, the extract step reuses its cache for unchanged zips, then rebuild and export again. The data flows one way: this repo never writes to Sangam.

## Source keys

oecd_philanthropy, oecd_crs, irs_990pf, irs_990_sched_f, iati, threesixtygiving, uk_charity_commission, nl_anbi, hurun_india, oecd_india, foundation_site, company_site, mca_csr (already in Sangam), brsr, ngo_darpan, nabard, ministry_site, parliament_qa, devtracker, giz, fcra_disclosure, manual_seed.


*This document was structured and edited with AI assistance but the frameworks, insights, and approaches presented are the author's own.*

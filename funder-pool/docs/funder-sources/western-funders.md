# Help file: western funders (foreign private philanthropy)

## 1. Scope

Foreign foundations, corporate foundations and giving programs, intermediaries (community foundations, donor-advised fund sponsors, re-granting public charities), church and development agencies, lotteries and impact investors. Foreign governments and multilaterals go to bilateral-multilateral.md. money_origin is foreign and india_csr is false for every row.

Out of scope for bulk use: Candid, Daanveda, Stiftungssuche (paid) and Kindora (terms bar bulk extraction).

## 2. Where the data lives

| source_key | Source | Access | Format | Key fields | Refresh | Licence |
|---|---|---|---|---|---|---|
| oecd_philanthropy | OECD Private Philanthropy for Development: CRS dataset (Edition 2023), https://www.oecd-ilibrary.org/development/data/oecd-international-development-statistics/creditor-reporting-system-private-philanthropy-for-development-edition-2023_dd620077-en | Download link on the page (31.34 MB CSV). Try automated, else manual M1. | CSV, activity level, since 2009, 41 of the largest foundations | donor, year, recipient country, sector or purpose code, channel of delivery, project title and description, amounts (confirm columns after download) | Per edition | Free. Check OECD terms. |
| oecd_philanthropy | Third Edition data (2020 to 2023), https://oecd.org/development/philanthropy-centre/data | Manual M2. The Data Explorer limits downloads to 60 an hour. | Dashboard export | As above | Per edition | As above |
| oecd_philanthropy | Second Edition dataset (2016 to 2019, 205 organisations), https://search.oecd.org/development/philanthropy-centre/researchprojects | Manual M5 | xlsx | As above | Static | As above |
| oecd_philanthropy | First Edition dataset (2013 to 2015), same page | Manual M6, optional | xls | As above | Static | As above |
| oecd_philanthropy | Third Edition Annex B, 506 organisations | Manual M3 | Table | name, country, cross-border or domestic | Static | As above |
| irs_990pf | IRS Form 990 series XML (TEOS), https://www.irs.gov/charities-non-profits/form-990-series-downloads | Automated. The page lists monthly zips by year (2019 to 2026) and an index CSV per year. Index files are very large, so stream them. Page sizes are not shown, so check disk before downloading. | XML in zips plus index CSV | Filer EIN, name, tax period, return type. 990-PF Part XV grants: recipient name, address and country, amount, purpose. Assets and total grants paid. | Monthly | Public domain |
| irs_990_sched_f | Same files, Form 990 Schedule F Part II | Automated | XML | Grants to organisations outside the US by region (South Asia is a region, so India needs the address or name to confirm) | Monthly | Public domain |
| irs_bmf | EO Business Master File extract (foundation codes), linked from https://www.irs.gov/charities-non-profits/tax-exempt-organization-search-bulk-data-downloads | Automated | CSV | EIN, NTEE, foundation code | Monthly | Public domain |
| iati | IATI Datastore Classic, https://datastore.codeforiati.org/ (official Datastore, https://docs.datastore.iatistandard.org/en/latest/, needs an API key) | Automated | CSV or JSON | Reporting org, recipient country IN, activities, transactions, partner organisations | Continuous | Varies by publisher |
| threesixtygiving | 360Giving data registry, https://data.threesixtygiving.org/ (publisher files, filtered locally for India). GrantNav robots.txt disallows /search, /funders and /recipients, so GrantNav is not crawled. | Automated (registry files) | CSV or JSON | Funder, recipient, amount, date, location | Daily | Open licences with attribution |
| manual_seed | seeds/international_seed.csv and seeds/evidence_by_year.csv | In this package | CSV | Named funders with dated India figures | Static | n/a |

Phase 2 sources, not needed for the first run: UK Charity Commission register extract, Netherlands ANBI register, EU Funding and Tenders portal API. They add rosters and open calls, not India signals.

## 3. How to get the data

1. Automated: IRS, IATI and 360Giving. Cache every download under data/raw/ with its hash.
2. Try the OECD official download link. If it fails, add M1 to the request list and continue.
3. Ask the user for M2, M3 and M4 to M7 through manual/MANIFEST.md.
4. Confirm the 990-PF Part XV element names against the IRS e-file schema before parsing. Do not guess tag names. (Done 2026-11-26 against 2022 filings; the names are listed in src/funder_pool/sources/irs990.py and section 10.)

## 4. Pool filters (cost only)

- 990-PF: keep filers with at least one grant to a recipient outside the US in the last five tax years. Drop filers with no grants.
- IATI: keep non-government reporting organisations. Send government and multilateral publishers to bilateral-multilateral.
- OECD and 360Giving: keep all.
- Never drop a funder because India giving is unknown.

## 5. Signals and ranking

Weights are in config/weights.yaml (western_funders).

| Signal | How to compute |
|---|---|
| india_usd_5y, india_usd_3y | Sum of grants or activities with recipient country India inside the window, from the best source |
| india_grants_count_5y, india_recipients_distinct_5y | Count and distinct recipients |
| total_giving_usd_5y | OECD global rows, 990-PF total grants paid, 360Giving total |
| india_share | india_usd_5y divided by total_giving_usd_5y |
| funds_ngos_share | Share of India money to recipients classed as NGO. Classify recipients by name rules and OECD channel as ngo, government, university, multilateral or unknown. Unknown stays unknown. |
| ingest_readiness | 3 grantee-level lines with amounts, 2 project-level with country and sector, 1 profile only, 0 name only |
| evidence_quality | 2 grantee-level source with India in the address, 1 project-level with a country tag, 0 inferred |

Source preference for india_usd_best: US home country, irs_990pf then oecd_philanthropy then iati. UK home country, threesixtygiving then oecd_philanthropy then iati. Any other country, oecd_philanthropy then iati.

Theme mapping: draft config/theme_map.yaml in Phase 1 mapping OECD purpose codes and keyword rules to Schedule VII top-level themes, and ask the user to review it.

## 6. Field extraction and Sangam mapping

| Pool field | Source | Sangam target |
|---|---|---|
| name, aliases, country | All | funders.name, aliases |
| ein | 990 files, BMF | funders.external_ids.ein (pending) |
| iati_org_id | IATI | funders.external_ids.iati_org_id (pending) |
| funder_type_draft | BMF foundation code, OECD roster, name rules | funders.funder_type (pending #324) |
| grant lines to Indian recipients | 990-PF, IATI, 360Giving, OECD | funder_activity kind partner |
| totals and shares | All | metrics with funder_id |

## 7. Traps

1. Multi-country rows labelled "Developing countries, unspecified" are not India. Leave them out of india_usd and keep them in total giving.
2. US intermediaries re-grant to India (American India Foundation, Give2Asia, Charities Aid Foundation America, Tides Foundation, GlobalGiving Foundation). Grants to them show no India country. Flag them indirect, never count them as India giving.
3. The same money appears in several sources (a foundation's 990-PF and its OECD report). Do not sum.
4. OECD publishes only anonymised aggregates for foundations that do not disclose grantees. These are unknown, not zero.
5. Bases differ: commitments versus disbursements, constant versus current USD. Record the basis.
6. An Indian intermediary funded from abroad cannot re-grant foreign money under FCRA. Matters for matching later, not for the pool.
7. Two ranges are not the same: the OECD Third Edition covers 2020 to 2023, the IRS window is the last five tax years. Report the window used per funder.

## 8. Notes for the import agent

- Read seeds/international_seed.csv and evidence_by_year.csv for confirmed India figures.
- New funders enter as registry_status placeholder. Hidden is for funders with known_zero.
- Write amounts in INR with the original amount, currency and rate in notes until the columns exist (follow-up to issue #324).
- Do not write external_ids until that follow-up merges.
- Set source_key to the values in section 2.

## 9. Not yet researched

UK Charity Commission extract, Dutch ANBI, EU portal, Schedule F field list, OECD terms of use. (IRS file sizes and 990-PF element names: see section 10.)

## 10. Route as built (2026-11-25)

- sangam_export (M11): private_foundation rows with a foreign legal form, routed here from hni_family (Paul Hamlyn Foundation, Stiftung Childaid Network), are roster entries. Country is blank because M11 has none. India giving is unknown unless another source counts it.

- oecd_philanthropy: M1, M2, M5 and M6 (grant-level data) were not supplied, so OECD amounts are missing. M3, the Third Edition Annex B roster, is extracted from the report PDF. Foreign organisations join as roster entries with India giving unknown. Cost filter: China and Mexico rows where Annex B column C is "No" are dropped, because they come from national data on domestic giving.
- threesixtygiving: registry files are downloaded up to a 0.95 GB cap. India rows are those with Recipient Org:Country India, a Beneficiary Location country code IN, or a Beneficiary Location name India. Grants in the window are converted to USD with annual FX (2025 rates for 2026 awards) and counted as committed (amount awarded). Grants that mention India only in their text go to the review queue and are not counted. UK public bodies (GB-GOV, GB-LAE and similar) are out of scope.
- Themes: purposes that rules cannot map are written to data/cache/western_unresolved_purposes.csv. They are then classified in-session into config/theme_overrides.csv (key, theme), which the build reads.
- irs_990pf: used. scripts/download_irs.sh fetches the TEOS index CSV and XML zips for filing years 2022 to 2026 (about 19 GB, scripts/irs_urls.txt) into data/raw/irs_990pf/<year>/. `.venv/bin/python -I scripts/extract_irs.py` parses only returns the index marks RETURN_TYPE 990PF and caches one returns/grants/meta set per zip in data/cache/irs990/ (the zip hash is computed once there). Element paths, confirmed on 2022 filings: ReturnHeader/Filer/EIN, Filer/BusinessName/BusinessNameLine1Txt, ReturnHeader/TaxPeriodEndDt; IRS990PF/AnalysisOfRevenueAndExpenses/ContriPaidRevAndExpnssAmt (grants paid); IRS990PF/Form990PFBalanceSheetsGrp/TotalAssetsEOYFMVAmt; IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp (one per grant paid) with RecipientBusinessName or RecipientPersonNm, RecipientForeignAddress/CountryCd, GrantOrContributionPurposeTxt and Amt. Country codes are the IRS's own list (IN is India; UK, not GB, is the United Kingdom).
  - Window: returns whose tax period ends 2021-04-01 to 2026-03-31. One return per EIN and tax period (the highest object id, so an amended return replaces the original).
  - Pool filter: filers with at least one grant to a foreign address in the window. Filers with only US grants are not added.
  - India: grants with RecipientForeignAddress CountryCd IN, summed over the window as grants paid. A filer with foreign grants but none to India is known_zero (grantee-level data), unless another source shows India giving; its evidence row shows its largest foreign grant.
  - Indirect: US-address grants to recipients whose name suggests an India re-granter (India in the name, Give2Asia, CAF America, GlobalGiving, Tides) go to the review queue and are never counted.
  - total_giving_usd_5y: sum of grants paid (Part I line 25) over the window. india_share_of_giving: India grants over that total.
  - Matching: by EIN first, then exact, acronym or spacing-free name match ('WAL-MART FOUNDATION' = 'Walmart Foundation') against funders from the other sources. A fuzzy name match is added as a new funder and queued as a possible duplicate only when the names also agree without philanthropy words (foundation, trust, fund); otherwise short names such as 'UMA Foundation' and 'UNM Foundation' would match.
  - Five TEOS zips (2025 05A, 05B, 11B; 2026 05A, 05B) use Deflate64, which Python cannot read; those members are unpacked with the system unzip into a temporary folder. unzip reports a central-directory warning (exit 3) on them but extracts every member; each member's size is checked. Website is kept only if it looks like a web address (filers also enter emails).
  - Grants to individuals (RecipientPersonNm) are kept for the India total but stored as 'individual recipient' with no name or place (rule 8). Purposes the keyword rules cannot map are themed from config/theme_overrides.csv, key 990:{object_id}:{grant_no}.
  - Filers whose returns are on paper or not yet published (large foundations file late) have no row; their India giving stays with the other sources.
- irs_990_sched_f: skipped. Part II gives region only, with no recipient names.
- irs_bmf: skipped. Downloaded to data/raw/irs_bmf/ for the import agent (NTEE code, ruling date); all IRS pool entries are 990-PF filers, so the foundation code adds nothing here.


*This document was structured and edited with AI assistance but the frameworks, insights, and approaches presented are the author's own.*

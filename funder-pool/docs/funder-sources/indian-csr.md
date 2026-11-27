# Help file: Indian CSR funders

## 1. Scope

Indian companies and corporate foundations that spend under Section 135 of the Companies Act, 2013. funder_type is csr_company when the company runs the programme itself (for example public sector units such as BEML and BEL) and csr_foundation when it gives through its foundation. india_csr is true. money_origin is domestic, with a check for foreign-owned subsidiaries.

Sangam already ingests CSR data from the National CSR Data Portal (source_key mca_csr). This utility does not rebuild that ingest. It finds which CSR funders are not yet in Sangam and ranks them for seeding.

## 2. Where the data lives

| source_key | Source | Access | Format | Key fields | Refresh | Licence |
|---|---|---|---|---|---|---|
| mca_csr | National CSR Data Portal (MCA), company-wise CSR search, https://csr.gov.in/content/csr/global/master/home/ExploreCsrData/dynamic-csr-report-search.html.html | Manual M10 (the search sits behind a CAPTCHA) | Table export by financial year | Company, CIN, CSR spend, projects, sector, state, implementing agency | Annual | Public |
| oecd_india | OECD India's Private Giving (2019), Annex B: 50 domestic organisations, 2013 to 2017 | Provided in context/ and seeds/ | PDF, CSV | Name, type as printed, data type | Static | OECD |
| oecd_india | OECD Taking stock (2022): 183 organisations, 2016 to 2019 | Manual M4 | PDF | Roster in an annex (confirm) | Static | OECD |
| oecd_india | OECD Third Edition sample (506 organisations) | Manual M3 | Table | Name, country, flags | Static | OECD |
| company_site | Company CSR policy pages and annual reports | Automated, per company, after the roster exists | HTML, PDF | Project lists, themes, foundation link | Annual | Public |
| brsr | BSE and NSE Business Responsibility and Sustainability Reports | Not researched. Check whether they give CSR spend and project lists. | PDF, XBRL | Unknown | Annual | Public |
| manual_seed | seeds/domestic_oecd_annex_b_and_later.csv | In this package | CSV | 50 Annex B organisations plus three later mentions, with draft types | Static | n/a |

Not a funder source: the CSR-1 register of implementing agencies lists recipients.

## 3. How to get the data

1. Ask the user for M10 (one export per financial year, as many years as they can pull) and M11 (the Sangam funders export, read-only).
2. Read the seed CSV for the OECD rosters. Ask for M4 to add the 183-organisation list.
3. Crawl company sites only for funders you are enriching, in a later phase.

## 4. Pool filter (cost only)

Keep companies with CSR spend recorded in any of the last three financial years. Drop only on that ground.

## 5. Signals and ranking

Weights are in config/weights.yaml (indian_csr). India giving is always true here, so it is not a signal.

| Signal | How to compute |
|---|---|
| csr_spend_3y_average | Mean CSR spend in INR crore over the last three financial years |
| project_count | Projects in the latest financial year |
| theme_breadth | Distinct Schedule VII items among the projects |
| has_foundation_arm | A linked corporate foundation exists (CIN, annual report or name match) |
| ingest_readiness | 3 project-level lines with amounts on the portal, 2 themes and states only, 1 profile, 0 name only |
| evidence_quality | 2 portal data, 1 annual report, 0 inferred |

Funders with in_sangam yes are scored but excluded from ingest_queue.csv.

## 6. Field extraction and Sangam mapping

| Pool field | Sangam target |
|---|---|
| name, CIN | funders.name, funders.cin |
| parent_name | funders.parent_id (company is the parent of its foundation) |
| CSR spend by year | funder_csr_years and funder_csr_spend (existing mca_csr ingest; do not duplicate) |
| projects by state | funder_activity kind footprint |
| themes | funder_tags |

## 7. Traps

1. Section 135 applies to companies with net worth of Rs 500 crore or more, turnover of Rs 1,000 crore or more, or net profit of Rs 5 crore or more in a financial year. The required spend is 2 percent of average net profit of the preceding three years. Spend can differ from the requirement, and unspent amounts carry rules.
2. Foreign-owned Indian entities (in the 2019 OECD list: Deutsche Bank, JP Morgan, IBM India, Samsung India, Castrol India) spend Indian CSR money, but check the FCRA foreign-source question before setting money_origin.
3. Entities may have merged or been renamed since 2013 to 2017 (in the 2019 list: Cairn India, Bharti Infratel, IDFC, Indiabulls Housing Finance). Verify the current legal entity.
4. OECD printed "Reliance India Limited". Confirm the legal entity (likely Reliance Industries) before linking.
5. The 2019 report's text says 2 corporate and 4 family foundations, while Annex B shows 3 and 3. Keep Annex B's labels as printed.
6. A company and its foundation are two funders. Do not merge them.

## 8. Notes for the import agent

- Read the OECD seed CSV for draft types and in_sangam flags.
- Do not re-ingest what mca_csr already holds.
- Set india_csr true only after the legal check noted in issue #324 for foreign-owned entities.

## 9. Not yet researched

BRSR usefulness, the portal's export options and column names, and company site layouts.

## 10. Route as built (2026-11-25)

- mca_csr (M10): the user supplied the portal's Dynamic CSR Report export as one file (data/manual/mca_csr_export_FY2014-26.csv): one row per CSR project, FY2014-15 to FY2024-25. A company's CSR spend for a year is the sum of its project rows ("Project Amount Spent (In INR Cr.)"). Listing status and state are not in this export and stay blank. Class gives PSU or Non-PSU.
- csranalytics: a third-party compilation (CSRAnalytics-Report-FY-2014-2025.xlsx) is supported as a fallback. It is logged as skipped when the official M10 export is present.
- oecd_india, Taking stock 2022 (M4): supplied, but the PDF has no organisation annex. Logged as skipped.
- oecd_india, Third Edition (M3): the table is extracted from Annex B of the report PDF by `python -m funder_pool.sources.oecd_annex_b` (556 rows, not the 506 the manifest expected). India rows that match a CSR company add oecd_philanthropy to its sources, with an evidence row. They carry no amounts.
- M11 (Sangam export): corporate_foundation and csr_foundation rows are read as candidate CSR foundations and linked to parent companies by name.
- Ranking note: spend signals are percentile-scored, so the top of the list compresses. A company with much larger spend can rank just below one with a broader signal profile (for example HDFC Bank below Dr Reddy's).


*This document was structured and edited with AI assistance but the frameworks, insights, and approaches presented are the author's own.*

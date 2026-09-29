# Axis Bank Foundation — Registry Row

*Compiled from official ABF sources only (axisbankfoundation.org and ABF's own Annual Reports FY2014-15 through FY2025-26) — updated 2026-09-29. Scope: Axis Bank Foundation (the Trust) only. Axis Bank Limited's own CSR annexure, BRSR, CSR Impact Report, CSR Committee, CIN and bank-run projects have been removed per scope rules.*

---

## Changelog — 2026-09-29 (FY2025-26 Annual Report deep-read)

The ABF Annual Report 2025-26 (88 pp.) was downloaded and read in full. Key tables — "Sustainable Livelihood Programme Highlights" (p.18) and "Outreach 2018–2026" (p.76) — were checked against rendered page images, not only extracted text. Page numbers below are the report's printed page numbers.

**Headline FY2025-26 numbers (ABF AR2025-26, p.18)**

| Particulars | FY2023-24 | FY2024-25 | FY2025-26 |
|---|---|---|---|
| Spend (₹ crore, annual) | 154.00 | 231.96 | **352.92\*** |
| Households — annual | 3,85,343 | 3,87,467 | **7,12,879** |
| Households — Mission 4 Million (cumulative) | 16,82,062 | 20,46,247 | **27,59,126** |
| Projects — annual | 43 | 59 | **58** |
| States & UTs | 28 | 32 | **32** |
| Villages (cumulative) | 18,706 | 23,686 | **33,517** |

\* *Footnote printed in the report: "Includes funds disbursed by Axis Bank Limited."* This is the first year in which ABF's headline spend figure explicitly includes money disbursed by the Bank. The ABF-only share is **not disclosed**, and the report gives no Rural Livelihoods / Skill Development / Ecosystem Action split for FY2025-26. Under this file's ABF-only scope, the ₹352.92 cr figure is therefore flagged and should not be compared directly with earlier years.

**Changes made in this pass**
- `funder_csr_years`: FY2025-26 row added (flagged as above).
- `funder_csr_spend`: FY2025-26 recorded as "category split not published".
- `metrics`: FY2025-26 cumulative outreach figures added, covering 40+ indicators from p.76.
- **Error fixed:** "Water harvesting potential created" for FY2024-25 was labelled **litres**. The source (AR2024-25 p.62) says **cubic metres** (16.60 crore m³). Unit corrected.
- **Error fixed:** `reference_figures`. The FY2023-24 cost per household was shown as ≈₹39,977. ₹154.01 cr ÷ 3,85,343 is actually **≈₹3,997**, so the old value was 10× too high and the "anomaly" note was wrong. Corrected, and a FY2025-26 row added.
- `funder_partners`: full FY2025-26 list added — 47 SLP partners and 8 Axis Cares partners (p.84), plus year-on-year additions and drops.
- Co-funders FY2025-26 (p.16): **Axis Direct** is named for the first time (it appears to replace "Axis Securities Limited"; the report doesn't say so explicitly). Invoicemart (A.TReDS) is present again.
- `funder_locations` / `funder_footprints`: the FY2025-26 report is organised into **23 state/region chapters** (p.20). This is the first ABF document that names states at this level. Rows added.
- `leadership_note` / `contacts`: 8 trustees re-confirmed for FY2025-26, with updated titles for Dhruvi Shah and Vijay Mulbagal.
- `documents`: AR2025-26 `status` changed from `received` to `read`.

**New inconsistencies found (flagged, not resolved)**
1. **Cumulative household arithmetic:** FY2023-24 cumulative (16,82,062) + FY2024-25 annual (3,87,467) = 20,69,529. ABF reports 20,46,247 for FY2024-25, which is **23,282 lower**. The FY2025-26 step does add up exactly (20,46,247 + 7,12,879 = 27,59,126).
2. **Mission 4 Million target year:** "by 2031" (p.9, About ABF) vs "by 2030" (p.14, Dhruvi Shah bio). Both appear in the same report.
3. **FY2023-24 spend:** ₹154.00 cr in AR2025-26 (p.18) vs ₹154.01 cr in AR2023-24/AR2024-25. Treated as a rounding difference.
4. **Mission 2 Million / Outreach window:** the Outreach page is headed "Mission4Million … 2018 – 2026". This supports the "2018" start year in the existing launch-year inconsistency note.

---

**Schema audit pass (all Part A tables checked against AR2025-26)**

Every figure below was machine-checked against the report text. Pages 18 and 76 were also checked against page images.

| # | Table | What AR2025-26 added / fixed |
|---|---|---|
| 1 | `funders` | `as_of` → FY2025-26. `profile` keys updated: `flagship_program` (Mission 4 Million progress, 2030/2031 conflict), `funding_trend`, `grant_terms` (8 co-funders, impact-bond intent), `leadership_note`. `kabil_grant_status`: no mention of KABIL in AR2025-26. |
| 2 | `funder_identifiers` | Nothing new. The report prints no PAN, CSR-1, Darpan, registration number or FCRA number. |
| 3 | `credential_events` | 7 rows added: `reg_no registered 2006` (p.8) and `not_found` for pan/12a/80g/csr1/darpan/fcra. **Fixed an overclaim:** old rows said "10 Annual Reports reviewed", but only 5 were read in full. |
| 4 | `funder_tags` | 4 tags added with FY26 evidence (artisan livelihoods, climate resilience, youth employability, governance convergence). |
| 5 | `funder_locations` | 29 states/UTs now named. 15 new state rows and 14 existing rows given FY26 evidence. Gujarat upgraded `operates`→`funds`. `valid_from` filled from partner "since" years. Tripura and Arunachal added (Changlang district, NoDE). |
| 6 | `funder_csr_years` | FY2025-26 row. 6a/6c/6e/6f recorded as "not published", not 0. |
| 7 | `funder_csr_spend` | FY2025-26 total row: ₹3,529,200,000, 58 projects, flagged as including Axis Bank funds. No sector or state split is published. |
| 8 | `programs` | 14 new/updated rows with full columns incl. `details` JSON: NoDE, Abhisaran, NorthEast Edit, leadership pilot, Governance Toolkit, Communications is Capacity, Vikaasvaani/playbooks, migration study, climate-readiness, PPIA fellows, Development Practitioners' Training, Axis Cares, and Mission 4 Million / Health & Nutrition updates. |
| 9 | `funder_footprints` | 29 state rows, 373 district rows (name_as_printed, with LGD spelling and duplicate notes) and 77 block rows. |
| 10 | `funder_partners` | 47 SLP + 8 Axis Cares + 8 co-funder + 8 knowledge/government rows, with `partner_canonical`, `partner_kind`, program, and state-by-state "since" years. |
| 11 | `grants` | 20 case-study candidates with reach in `outcomes`. Start-year corrections for WOTR/SRIJAN/BRLF. |
| 14 | `contacts` | Trustee titles updated. No ABF staff below trustee named. |
| 15 | `metrics` | 46 cumulative + 22 state case-study + 17 other rows. |
| 16 | `documents` | AR2025-26 → `read`. |
| 18 | `reference_figures` | `kind` column added (was missing). 3 new rows: TN 89% smallholdings, CG ≥60% income growth, Kerala enterprise income. |
| 19 | `program_locations` | 64 FY26 rows (SLP ×29, Skill Development ×19, Health & Nutrition ×3, NoDE ×5, Towards the Northeast ×7, DPT ×1). **Fixed:** 8 old rows were missing `archive_url` or had a non-URL `source_url`. |
| 20 | `program_tags` | 5 rows added. |
| 21 | `grant_locations` | Candidate rows: named blocks tied to case-study partners. |
| 12/13/17/22–24 | `rfps`, `proposal_templates`, `news_mentions`, `rfp_*`, `template_items` | Nothing in AR2025-26 (no calls, forms or news). |

## Changelog — 2026-09-29 (earlier pass)

**(a) Added, per table**
- `funders`: single `source_url`, `archive_url` attempt logged (failed — see note).
- `funder_identifiers` / `credential_events`: portal-check attempts for NGO Darpan, FCRA online, MCA CSR-1, Income Tax 12A/80G — all logged with `check_blocked`/`not_found` and the exact URL + date checked, since none could be completed (captcha-gated or portal timeout).
- `funder_csr_years`: 3 new ABF-only rows (FY2022-23, FY2023-24, FY2024-25) built from ABF's own "Financial Highlights"/"Sustainable Livelihood Programme Highlights" tables across three separate ABF Annual Reports (2022-23, 2023-24, 2024-25 editions), cross-checked against each other. `section_135_applicable = No` on all three; `average_net_profit`/`prescribed_csr` left empty as instructed.
- `funder_csr_spend`: FY2020-21 and FY2021-22 category-level totals added (newly found in the ABF AR2022-23 3-year trend table), on top of FY2022-23–FY2024-25.
- `funder_locations`/`funder_footprints`: every individually-named ABF state re-sourced to an ABF-only document (no bank CSR Impact Report data); added new named states (Meghalaya, Nagaland, Mizoram — Northeast case studies) and precise district/block names (Khunti-Jharkhand, Narayanpet-Telangana, Ahmednagar & Beed-Maharashtra, Dahod & Panchmahal-Gujarat) found in ABF's own reports.
- `funder_partners`: full 46-partner FY2024-25 list + full 34-partner FY2023-24 list + full ~27-partner FY2022-23 list (with **real "Partner Since" years** for ~27 of them, and founder names) — all from ABF's own "Programme Partners" pages. 9 "Axis Cares" (employee-volunteering) partners per year also added, tagged separately from SLP grant partners.
- `programs`: descriptions (2-4 sentences) added to every row; `kind` changed to `programme` for Rural Livelihoods and Skill Development; Ecosystem Action added as a `programme` with `is_enabler=Yes`; all dates converted to YYYY-MM-DD or flagged `not_found`.
- `contacts`: added **Abhinav Sen** (Vice President, ABF — named in AR2024-25, `kind=programme`) and **Shubhanjali Roye** (Program Manager, CSR, ABF — LinkedIn, `kind=programme`, unverified).
- `metrics`: `method`, `is_self_reported`, `target`, `source_url`, `source_name`, `fetched_at`, `as_of` added to every row; Mission 4 Million target (4,000,000) added.
- `documents`: all 10 ABF Annual Reports (FY2014-15 through FY2025-26) now listed with real URLs.
- `news_mentions`: new table, 8 items found (short of the 10–20 target — see note in that section).
- `reference_figures`: new table — cost-per-household calculated figure, admin-overhead note.
- `program_tags`: new table, populated per the gap list's suggested tags.
- **New, material finding not previously in the file:** ABF's own Annual Reports give **three different, mutually inconsistent "Mission 2 Million launch year" claims** across primary ABF/Axis Bank sources — 2017 (AR2022-23, Munish Sharda's message), 2018 (AR2023-24 and AR2024-25 Outreach chapters, stated twice), and 2019 (Axis Bank's own official March 2025 press release announcing Mission 4 Million: "a commitment taken in 2019"). This is flagged wherever the date appears, rather than silently picking one value.

**(b) Removed**
- `funder_identifiers`: the `cin` row (Axis Bank Ltd's, not ABF's).
- `funder_tags`: the inferred "Financial Inclusion" tag; "secondary (historical)" replaced with `secondary` + `valid_to` + note.
- `funder_csr_years`: all 4 Axis Bank Ltd rows and the Bank's CSR Committee table.
- `funder_csr_spend`: the Aspirational-District BRSR table; the 5 bank-direct project rows (Financial Literacy, Mobile Vans, Heart Surgeries, Mid-Day Meal, DilSe).
- `programs`: Financial Inclusion & Literacy and Healthcare & Humanitarian Relief themes and their 5 bank-run projects.
- `funder_partners` / `grants`: CSC Academy, Sri Sathya Sai Health & Education Trust, Akshaya Patra Foundation, Sunbird Trust (all bank-direct, not ABF).
- `program_locations`/`funder_footprints`: the 6 bank-CSR-theme district lists (Education/Environment/Financial Inclusion/Health/Sports/Humanitarian), and the Heart Surgeries/Mid-Day Meal/DilSe location rows.
- `documents`: 5 Axis Bank Ltd documents + the "Axis Bank Limited CSR Policy" placeholder row.
- `contacts`: the 4 Bank CSR Committee members and `csr@axisbank.com`.
- All "(historical)" role suffixes — replaced with a valid enum value + `note`/`valid_to`.
- The Gujarat/Dahod `funds` row — replaced with `operates` + caveat (see `funder_locations`).
- The stray reference to a nonexistent "official CSR Policy PDF" and "earlier Part D" in the `rfps` note.

**(c) Still not found, with what was checked and where**
- **PAN, CSR-1 number, NGO Darpan ID, exact trust registration number**: not found. Checked ABF's own Annual Reports (FY2014-15 through FY2024-25, all downloaded and reviewed for a financial-statements/audit section — none of the 10 reports publish a full audited income-and-expenditure statement or these ID numbers); attempted ngodarpan.gov.in NPO Directory search (blocked by mandatory CAPTCHA, not solvable via automated session, checked 2026-09-29); attempted fcraonline.nic.in (page timed out repeatedly, checked 2026-09-29); attempted mca.gov.in CSR-1 data page (HTTP 403 Access Denied, checked 2026-09-29). No Income Tax e-Filing "Verify 12A/80G" public lookup tool exists that accepts a name search without the organisation's own PAN — not completable without that PAN.
- **A full, ABF-published named list of all 32 states and 300 districts**: not found. Checked ABF Annual Report 2024-25 "Outreach" chapter (pp. 62–65) and AR2023-24/AR2022-23 equivalents — all three publish only the aggregate counts (32 states, 300 districts, 775 blocks), never an itemised list. ABF's own materials only name individual states/districts via case studies (captured in `funder_locations`/`funder_footprints` below).
- **A dedicated ABF income-and-expenditure statement (audited accounts)** distinct from the narrative Annual Report: not found in any of the 10 ABF Annual Reports downloaded and reviewed page-by-page in this pass.
- **`archive_url`**: `fetch_url`-based attempts at web.archive.org "Save Page Now" and the Wayback availability API both failed (HTTP 520 / timeout / unparseable JSON). **Succeeded on retry via the browser tool** for 3 pages: the ABF Overview page, the Board of Trustees page, and the Financials Overview page (all archived 2026-09-29 — see their rows in `funders`/`funder_locations`/`documents` above). Most other rows in this file still show "Not found" for `archive_url` — only these 3 were attempted with the browser tool given time constraints; the rest were left as `fetch_url`-only attempts (failed).
- **10–20 news items**: only 8 found in the time available (see `news_mentions`). More likely exist on ABF's LinkedIn page and in regional press not indexed by the search tool used.

---

## `funders` table — field values

| Column | Value | Notes |
|---|---|---|
| **id** | *(auto — assigned by database)* | Do not type |
| **slug** | `axis-bank-foundation` | |
| **name** | **Axis Bank Foundation** | Registered Public Trust; no CIN (trusts aren't allotted one) |
| **funder_type** | `corporate_csr` | |
| **section_135_bound** | **No** | The Trust itself isn't Section-135-bound; that obligation sits with parent Axis Bank Limited |
| **website** | **https://www.axisbankfoundation.org** | |
| **profile** (JSON) | *see breakdown below* | |
| **source_url** | **https://www.axisbankfoundation.org/about-us/overview.html** | Single link per instruction — the page the core facts (founding year, mission, pivot history) are drawn from |
| **source_name** | "Axis Bank Foundation — Overview page" | |
| **fetched_at** | 2026-09-29 | |
| **content_hash** | *(auto — leave for pipeline)* | |
| **extractor_version** | `manual-research-v1` | |
| **as_of** | **FY2025-26** | Updated after deep-read of ABF AR2025-26 |
| **archive_url** | **https://web.archive.org/web/20260929093946/https://www.axisbankfoundation.org/about-us/overview.html** | Succeeded on retry via browser tool (fetch_url's own attempts at "Save Page Now" and the availability API both failed — see note below); archived 2026-09-29. |
| **registry_status** | `in_vetting` | |
| **parent_id** | *(left empty)* | Per gap-list guidance: only populate once an Axis Bank Limited funder row exists in your system |

---

## `profile` JSON — key-by-key detail

### `flagship_program`
> **Sustainable Livelihood Programme (SLP)**, launched 2011, delivered across two core pillars — **Rural Livelihoods** and **Skill Development** — plus **Ecosystem Action** (capacity-building/enabler) and, in some years, **Special Projects** and **Research and Knowledge** categories. Sequential mission commitments:
> - **Mission 1 Million** (2011–2018): foundational phase — water access, agricultural productivity, horticulture, livestock, agroforestry, for 1 million individuals.
> - **Mission 2 Million**: committed to 2 million households; **achieved as of 2025-03-31** — 2,046,247 cumulative households across 23,686 villages, 32 states/UTs. ⚠️ **Launch-year inconsistency across ABF's own primary sources, presented honestly rather than resolved by picking one:** AR2022-23 (Munish Sharda's message) says "launched Mission 2 Million in **2017**"; AR2023-24 and AR2024-25 Outreach chapters both say "**2018**" (stated as "2018–2024" and "2018–2025" impact windows); Axis Bank's own official press release dated 2025-03-03 announcing Mission 4 Million says Mission 2 Million was "**a commitment taken in 2019**." All three are genuine ABF/Axis-Bank-sourced claims — none has been silently overridden.
> - **Mission 4 Million** (launched 2025-03-03 at "Abhisaran 2025"/"One Axis CSR Vision" event): next phase, additional 2 million rural households (4 million cumulative). **Progress as of 2026-03-31: 27,59,126 cumulative households, 33,517 villages, 1,394 blocks, 306 districts, 32 states/UTs** (ABF AR2025-26, pp.18 & 76). ⚠️ The target year is stated two ways in AR2025-26: "by 2031" (p.9) and "by 2030" (p.14, CEO bio). FY2025-26 is described as "the first full year of Mission 4 Million" and ABF's "twentieth year" (Chairperson's letter, p.2).
> - ABF pivoted to this livelihoods-first strategy in **2011-12**, having originally founded in **2006** with a focus on education and highway trauma care, expanding **2007–2010** into skilling/training for Persons with Disabilities.

### `funding_trend`
> See `funder_csr_years` and `funder_csr_spend` tables below for full year-by-year figures (FY2020-21 through FY2025-26). Trend in ₹ crore: 74.85 → 84.89 → 113.53 → 154.01 → 231.96 → **352.92\*** (FY2025-26; \*includes funds disbursed by Axis Bank Limited, and the ABF-only share is not disclosed).

### `grant_terms`
> - Implements via NGO/civil-society partners at the grassroots (see `funder_partners` — 46 named SLP partners in FY2024-25 alone).
> - **Co-funded by multiple Axis Group entities** — composition changes year to year: FY2023-24's funding-partner list was Axis Bank Limited, Axis Asset Management Company Limited, Axis Capital Limited, Axis Finance Limited, Axis Securities Limited, Axis Trustee Services Limited, and Freecharge Payment Technologies Private Limited (**Invoicemart/A.TReDS was not listed this year** — it only appears in the FY2024-25 list, so treat "co-funder since" claims as year-specific, not a fixed roster).
> - **FY2025-26 co-funders (AR2025-26 p.16):** Axis Asset Management Company Limited, Axis Bank Limited, Axis Capital Limited, **Axis Direct**, Axis Finance Limited, Axis Trustee Services Limited, Freecharge Payment Technologies Private Limited, Invoicemart (A.TReDS). All 8 have a CEO quote in the report.
> - Chairperson's letter (AR2025-26 p.3) signals interest in **impact bonds and outcome-linked financing**. This is a stated direction, not a disclosed instrument.
> - Historically (FY2015-16 Annual Report), Axis Bank contributed "up to 1% of net profit after tax" annually to ABF — pre-dating the Section 135 2% mandate; current-year % not independently re-confirmed.
> - Multi-year, programmatic structure organised around "Mission" targets, not one-off disbursements or annual open calls.

### `governance_note`
> - Registered as a Public Trust in 2006 (Axis Bank Corporate Profile page; ABF AR2015-16). Exact trust registration number: **not found** (see Changelog §c).
> - **FCRA registered** since **2015-09-11**, registration number **083781476** (ABF AR2015-16) — renewal/current-validity status **not found** (fcraonline.nic.in did not load in this pass).
> - Governed by a Board of Trustees (see `leadership_note`); CSR Committee-equivalent oversight sits with the Trustees themselves (ABF, being a Trust, has no separate statutory "CSR Committee" of the kind Section-135 companies must form — that requirement and body belong to Axis Bank Limited, out of scope here).
> - No CIN — ABF is a Trust, not a company.

### `leadership_note`
> **Board of Trustees (per AR2024-25; all 8 re-confirmed unchanged in AR2025-26 "Governing Board", pp.10–14):**
> | Name | Role | Trustee Since | Notes |
> |---|---|---|---|
> | **S. Ramadorai** | Chairperson | 2010 | Padma Bhushan; former CEO & MD, TCS (1996–2009); former Chairman, NSDC/NSDA |
> | **Dhruvi Shah** | Executive Trustee & CEO (AR2025-26 adds: **Group Head – Corporate Social Responsibility, Axis Bank**) | 2021 (Head of Programs at ABF since 2016; CEO since **2020-11**, per ABF's own Board of Trustees page — more precise than the previously-used "since 2020") | 18 years at ABN AMRO/RBS Bank N.V. prior, heading their "Sustainable Development and Not-for-Profit Management" vertical from 2008 |
> | **Sheela Patel** | Trustee | 2006 | Founder-Director, SPARC; Padma Shri (2011) |
> | **Som Mittal** | Trustee | 2015 | Former Chairman/President, NASSCOM |
> | **Rajesh Dahiya** | Trustee | 2015 | Founder-CEO, GoodGovern; former ED, Axis Bank Ltd. |
> | **Sushma Iyengar** | Trustee | 2019 | Founder, Kutch Mahila Vikas Sangathan |
> | **Munish Sharda** | Trustee | 2023 | Also Executive Director, Axis Bank Limited |
> | **Vijay Mulbagal** | Trustee | 2024 | AR2025-26 title: Group Head – Wholesale Bank Coverage, Corporate Salary, Sustainability & CSR, Axis Bank (author of "Way Forward", p.78) |
>
> **Named ABF staff (non-Trustee):** Abhinav Sen (Vice President, ABF — named in AR2024-25); Shubhanjali Roye (Program Manager, CSR, ABF — LinkedIn); Isha Ayyer (Senior Manager, CSR, ABF — LinkedIn).

### `kabil_grant_status`
> No KABIL-related grant, program, or reference found in any ABF source. Not applicable / not found.

### `general_contact_email`
> **foundation@axisbank.com** (as printed in AR2022-23, AR2023-24 footers; ABF's live website contact page shows the same address). Note: my prior version of this file listed `foundation@axis.bank.in` as primary based on the live site render at that time — the two most-recently-downloaded Annual Reports (FY2022-23, FY2023-24) both print `foundation@axisbank.com`, so that is now treated as at least equally current; both forms are recorded.
> Source: ABF Annual Report 2023-24, p.64; ABF Annual Report 2022-23, p.52.
> **AR2025-26 back cover prints no email.** It gives only the postal address: *Axis Bank Foundation, 2nd Floor, Axis House, Pandurang Budhkar Marg, Worli, Mumbai, Maharashtra 400025*, plus LinkedIn, Instagram, Facebook and www.axisbankfoundation.org.

---
---

**Official IDs (`funder_identifiers`)**

*One row per identifier. `id_value` is required, so rows with nothing found are **not loaded here** — they are recorded instead in `credential_events` below as `not_found`/`check_blocked`, per instruction.*

| id_type | id_value | verified | source_url | is_current | source_name | fetched_at | archive_url |
|---|---|---|---|---|---|---|---|
| `domain` | `axisbankfoundation.org` | Yes | https://www.axisbankfoundation.org | Yes | ABF website | 2026-09-29 | Not found (see Changelog) |
| `name` | `ABF` (common short-form, not a legal former name) | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | Yes | ABF Annual Report 2024-25 | 2026-09-29 | Not found |

**Removed:** `cin` row (belonged to Axis Bank Limited — deleted per scope rules; the parent's CIN `L65110GJ1993PLC020769` should live only on the Axis Bank Limited funder row, if/when created).
**Not loaded as rows (id_value would be empty — recorded in `credential_events` instead):** `pan`, `csr1`, `darpan`, `reg_no`.
**Not an allowed `id_type` in this schema:** FCRA registration `083781476` — recorded only in `credential_events` and in `profile.governance_note` above.

---
---

**Registration history (`credential_events`)**

*One row per check performed. All rows are for Axis Bank Foundation; `org_id`/`funder_id` link columns omitted (file is ABF-only).*

| credential | event | event_date | valid_until | verified | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|
| `reg_no` | `registered` | 2006-01-01 *(year confirmed; exact day/month not disclosed anywhere — using Jan 1 as a placeholder per instruction to use a full date with a note)* | — | No *(fact of registration confirmed; number itself not_available)* | Registered as Public Trust in 2006. Trust registration number itself not published in any source checked. | https://www.axis.bank.in/about-us/corporate-profile | Axis Bank Corporate Profile page | 2026-09-29 | Current |
| `fcra` | `registered` | 2015-09-11 | not_found | Yes (number + date explicitly published) | Registration No. 083781476. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/Axis-Bank-Foundation-Annual-Report-2015-16.pdf | ABF Annual Report 2015-16 | 2026-09-29 | FY2015-16 |
| `fcra` | `check_blocked` | 2026-09-29 | — | No | Attempted to verify current FCRA renewal/validity status directly on the FCRA portal; page failed to load (ReadTimeout) after 60s. Portal requires further attempts outside this session. | https://fcraonline.nic.in/home/index.aspx | FCRA Online (Ministry of Home Affairs) | 2026-09-29 | — |
| `12a` | `not_found` | 2026-09-29 | — | No | Not disclosed for ABF itself in the 5 ABF Annual Reports read in full (FY2015-16, FY2022-23, FY2023-24, FY2024-25, FY2025-26); the other 5 were not read page by page. (TISS-ABF CSR Process Manual lists 12A as a requirement for ABF's *NGO grant partners*, not proof of ABF's own status.) | https://www.axisbankfoundation.org/download/knowledge-corner/TISS-ABF-CSR-Process-Manual.pdf | TISS-ABF CSR Process Manual (checked; no ABF-own 12A number found) | 2026-09-29 | — |
| `12a` | `check_blocked` | 2026-09-29 | — | No | Income Tax e-Filing "Verify 12A/80G Registration" tool requires the organisation's own PAN as a search input — cannot search by name alone; PAN itself is unknown (see `pan` row). | https://eportal.incometax.gov.in | Income Tax India e-Filing portal | 2026-09-29 | — |
| `80g` | `not_found` | 2026-09-29 | — | No | Same as 12A — no number/date found in the 5 ABF Annual Reports read in full. | (5 ABF Annual Reports read in full — see `documents`) | ABF Annual Reports | 2026-09-29 | — |
| `80g` | `check_blocked` | 2026-09-29 | — | No | Same portal constraint as 12A above. | https://eportal.incometax.gov.in | Income Tax India e-Filing portal | 2026-09-29 | — |
| `csr1` | `not_found` | 2026-09-29 | — | No | Plausible ABF holds a CSR-1 (as an implementing agency for Axis Group CSR spend), but no CSR00xxxxxx number located in the 5 ABF Annual Reports read in full. | (5 ABF Annual Reports read in full — see `documents`) | ABF Annual Reports | 2026-09-29 | — |
| `csr1` | `check_blocked` | 2026-09-29 | — | No | Attempted mca.gov.in CSR-1 registered-entities data page — returned HTTP 403 Access Denied. | https://www.mca.gov.in/content/mca/global/en/data-and-reports/csr-data/csr1-data.html | MCA CSR Data portal | 2026-09-29 | — |
| `darpan` | `not_found` | 2026-09-29 | — | No | No NGO Darpan Unique ID found in the 5 ABF Annual Reports read in full. | (5 ABF Annual Reports read in full — see `documents`) | ABF Annual Reports | 2026-09-29 | — |
| `darpan` | `check_blocked` | 2026-09-29 | — | No | NGO Darpan NPO Directory search (ngodarpan.gov.in/#/search-ngo) requires solving an image CAPTCHA before the Search button activates — not solvable via this automated session. | https://ngodarpan.gov.in/#/search-ngo | NGO Darpan (NITI Aayog) | 2026-09-29 | — |
| `pan` | `not_found` | 2026-09-29 | — | No | PAN not disclosed in the 5 ABF Annual Reports read in full (none publish a Form 10B audit report or a standalone income-and-expenditure statement with PAN printed on it). | (5 ABF Annual Reports read in full — see `documents`) | ABF Annual Reports | 2026-09-29 | — |
| `reg_no` | `registered` | 2006-01-01 *(year only)* | — | No | AR2025-26 p.8: "Registered as a charitable trust in 2006". Corroborates the row above; no registration number printed. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.8) | 2026-09-29 | FY2025-26 |
| `pan` | `not_found` | 2026-09-29 | — | No | AR2025-26 (88 pp.) read in full: no PAN number or status printed. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 |
| `12a` | `not_found` | 2026-09-29 | — | No | AR2025-26 (88 pp.) read in full: no 12A number or status printed. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 |
| `80g` | `not_found` | 2026-09-29 | — | No | AR2025-26 (88 pp.) read in full: no 80G number or status printed. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 |
| `csr1` | `not_found` | 2026-09-29 | — | No | AR2025-26 (88 pp.) read in full: no CSR1 number or status printed. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 |
| `darpan` | `not_found` | 2026-09-29 | — | No | AR2025-26 (88 pp.) read in full: no DARPAN number or status printed. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 |
| `fcra` | `not_found` | 2026-09-29 | — | No | AR2025-26 (88 pp.) read in full: no FCRA number or status printed (the FCRA number 083781476 from AR2015-16 is not restated). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 |

**Removed:** the `cin`/`not_available` row (kept in prior version for cross-reference; deleted here per scope rules since it's Axis Bank Ltd's identifier type, not ABF's, and its inclusion risked confusion — the fact "ABF has no CIN" is stated once in `profile.governance_note` instead).

---
---

---
---

**Focus sectors (`funder_tags`)**

*`tag_id` shown as tag names — map to your `tags.id`. All rows for Axis Bank Foundation.*

| tag (→ tags.id) | role | is_inferred | tagged_by | note |
|---|---|---|---|---|
| Rural Livelihoods | primary | No | agent-research | Core SLP pillar; largest spend category every year on record (e.g. ₹198.29 Cr of ₹231.96 Cr total, FY24-25). |
| Skill Development / Vocational Training | primary | No | agent-research | Second SLP pillar; explicit focus on youth and Persons with Disabilities. |
| Women Empowerment | primary | No | agent-research | Stated in Vision & Mission; recurring dedicated chapters across multiple Annual Reports. |
| Environmental Sustainability / Natural Resource Management | secondary | No | agent-research | Watershed management, water security, climate-resilient agriculture; FICCI Sustainable Agriculture Award 2024 (Gold) for work via WOTR in Jharkhand/Telangana/Maharashtra. |
| Disability Inclusion (PwD livelihoods/skilling) | secondary | No | agent-research | Explicit since 2007–2010 expansion; continues today (e.g. TRRAIN partnership, ~2,400 PwDs trained across Kerala per 2024 press coverage). |
| Health & Nutrition (linked to livelihoods) | secondary | No | agent-research | Integrated into SLP from 2022/2023 onward per AR2022-23 and AR2024-25 chapters; delivered via CINI, Harsha Trust, Rajarhat Prasari, PRADAN in Jharkhand/Odisha/West Bengal. |
| Education | secondary | No | agent-research | ABF's original 2006 focus. **Historical — ended ~2011-12** when ABF pivoted to livelihoods (`valid_to = 2012-01-01`, approximate). |
| Disaster Relief (highway trauma care) | secondary | No | agent-research | Part of the original 2006 mandate. **Historical — no evidence of current activity** (`valid_to = not_found`, treat as ended alongside the Education pivot). |
| Community Institution Building / System Strengthening | secondary | No | agent-research | SHGs, gram panchayats, village organisations, farmer producer collectives — a named current theme across multiple Annual Reports. |

| Artisan / Creative & Traditional Livelihoods | secondary | No | agent-research | AR2025-26: Creative Dignity/Industree (Karnataka ceramics), Contact Base (Odisha & Jharkhand folk artists; 5,500+ artists mapped). The Outreach page (p.76) counts 5,165 households in artisan enterprises. |
| Climate Resilience / Climate Adaptation | secondary | No | agent-research | AR2025-26 Chairperson's letter ("Resilience… must become embedded"), climate-readiness assessment of 35 partners (p.83), Chhattisgarh community-based climate action model (p.26). |
| Youth Employability | secondary | No | agent-research | AR2025-26: Generation India, Medha, Youth4Jobs and Udyogini in 20+ state chapters; 81,203 youth trained (2018–2026). |
| Local Governance / Public-System Convergence | secondary | No | agent-research | AR2025-26: TRIF Public Policy in Action Fellows (Aspirational Districts), MGNREGA/VB-G RAM G convergence (₹1,200 cr leveraged in Chhattisgarh), 7,95,876 households linked to schemes. |
| Rural Livelihoods *(update)* | primary | No | agent-research | FY2025-26 has no category split. The ₹198.29 cr figure in the row above is FY2024-25. |

**Removed:** the inferred "Financial Inclusion" tag (was based on parent Axis Bank Ltd.'s CSR policy language, not ABF's own stated focus — out of scope).

---
---

**Geography (`funder_locations`)**

*One row per state (no aggregate "All-India" row). `valid_from`/`valid_to` are real dates or `not_found` — no "~" or year-only approximations left un-flagged. All sources are ABF's own documents.*

| location (→ locations.id) | role | valid_from | valid_to | note | source_url | source_name | fetched_at | as_of | archive_url |
|---|---|---|---|---|---|---|---|---|---|
| Maharashtra — Mumbai (Worli) | `registered` | 2006-01-01 | — | Head Office: Axis House, C2, Wadia International Centre, Worli, Mumbai. (Registered-office row now linked at city/district level per instruction, not state-level.) | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2023-24.pdf | ABF Annual Report 2023-24 (p.64, address block) | 2026-09-29 | Current | Not found |
| Rajasthan | `funds` | 2012-01-01 | — | SRIJAN partnership, "Partner Since: 2012" per ABF's own Programme Partners list; 4 districts (unnamed individually). **AR2025-26 (p.63):** 8 partners, 28 blocks; districts: Ajmer, Alwar, Anupgarh, Balotra, Banswara, Baran, Barmer, Beawar, Bharatpur, Bhilwara, Bikaner, Bundi, Chittorgarh, Churu, Dausa, Deeg, Dholpur, Didwana-Kuchaman, Dudu, Ganganagar, Gangapur City, Hanumangarh, Jaipur, Jaipur Rural, Jaisalmer, Jalore, Jhalawar, Jhunjhunu, Jodhpur, Jodhpur Rural, Karauli, Kekri, Khairthal-Tijara, Kota, Kotputli-Behror, Nagaur, Neem Ka Thana, Pali, Phalodi, Pratapgarh, Rajsamand, Salumbar, Sanchore, Sawai Madhopur, Shahpura, Sikar, Sirohi, Tonk, Udaipur. Earliest partner start year printed: 2014. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf | ABF Annual Report 2022-23 (p.47) | 2026-09-29 | FY2022-23 | Not found |
| Gujarat | `funds` *(upgraded from `operates`: AR2025-26 shows 7 partners and 18 blocks)* | 2023-01-01 *(site visit reported in AR2022-23, referring to Jan 2023)* | — | **Changed from `funds` to `operates` per instruction** — original evidence was a homepage gallery photo caption, which is weak; upgraded now with stronger evidence: ABF Trustees' January 2023 site visit to NM Sadguru Foundation projects in **Dahod and Panchmahal districts**, incl. a named lift-irrigation project in Punsri, Dahod. **AR2025-26 (p.31):** 7 partners, 18 blocks; districts: Ahmedabad, Amreli, Anand, Aravalli, Banaskantha, Bharuch, Bhavnagar, Botad, Chhota Udaipur, Dahod, Dang, Devbhoomi Dwarka, Gandhinagar, Gir Somnath, Jamnagar, Junagadh, Kheda, Kutch, Mahisagar, Mehsana, Morbi, Narmada, Navsari, Panchmahal, Patan, Porbandar, Rajkot, Sabarkantha, Surat, Surendranagar, Tapi, Vadodara, Valsad. Earliest partner start year printed: 2013. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf | ABF Annual Report 2022-23 (p.45) | 2026-09-29 | FY2022-23 | Not found |
| Madhya Pradesh | `funds` | 2011-01-01 *(year only — earliest partner 'since' year printed in AR2025-26)* | — | Named beneficiary case study ("Sita Devi, Farmer, Madhya Pradesh") in AR2024-25; also a named "adaptive/climate-resilient livelihoods" state in AR2023-24 ("Andhra Pradesh, Madhya Pradesh, Odisha and Rajasthan, reaching 1,50,000 households"). **AR2025-26 (p.51):** 14 partners, 103 blocks; districts: Alirajpur, Anuppur, Barwani, Betul, Bhopal, Chhatarpur, Damoh, Dewas, Dhar, Dindori, Guna, Gwalior, Jhabua, Katni, Khargone, Maihar, Mandla, Niwari, Panna, Rajgarh, Ratlam, Rewa, Sagar, Satna, Sehore, Shahdol, Shivpuri, Singrauli, Tikamgarh, Umaria. Earliest partner start year printed: 2011. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 | Not found |
| Odisha | `funds` | 2012-01-01 *(year only — earliest partner 'since' year printed in AR2025-26)* | — | Siangbali GP, Daringbadi block, MGNREGS case study (AR2024-25); also named in AR2023-24's health-and-nutrition rollout ("Odisha, Jharkhand and West Bengal") and FICCI-award-winning Harsha Trust partnership (FICCI Sustainable Agriculture Awards 2023). **AR2025-26 (p.59):** 9 partners, 58 blocks; districts: Angul, Balangir, Bhubaneswar, Ganjam, Kalahandi, Kandhamal, Keonjhar, Koraput, Mayurbhanj, Nabarangpur, Rayagada, Subarnapur. Earliest partner start year printed: 2012. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf ; https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2023-24.pdf | ABF Annual Reports 2024-25 & 2023-24 | 2026-09-29 | FY2023-24 / FY2024-25 | Not found |
| Jharkhand | `funds` | 2019-01-01 *(year only — earliest partner 'since' year printed in AR2025-26)* | — | FICCI 2024 Gold Award project via WOTR — Khunti district specifically named; also named in the FY2023-24 health-and-nutrition rollout and in the FY2023-24 chairman's letter (12 districts, 26 blocks, High Impact Watershed Project). **AR2025-26 (p.39):** 5 partners, 69 blocks; districts: Bokaro, Chatra, Dhanbad, Dumka, East Singhbhum, Garhwa, Giridih, Godda, Gumla, Hazaribagh, Khunti, Latehar, Lohardaga, Palamu, Ramgarh, Ranchi, Sahibganj, Saraikela-Kharsawan, Simdega, West Singhbhum. Earliest partner start year printed: 2019. | https://www.axis.bank.in/about-us/press-releases/axis-bank-foundations-sustainable-livelihood-programme-strikes-gold-at-ficci-s-sustainable-agriculture-summit-and-awards-2024 | Axis Bank press release re: ABF's FICCI award (2024-12) | 2026-09-29 | FY2024 (award year) | Not found |
| Telangana | `funds` | 2014-01-01 *(year only — earliest partner 'since' year printed in AR2025-26)* | — | FICCI 2024 Gold Award — Narayanpet district specifically named (WOTR watershed project); also named in AR2023-24 ("our collaboration with Watershed Organisation Trust (WOTR) is promoting water conservation and sustainable agriculture" in Telangana). **AR2025-26 (p.67):** 3 partners, 19 blocks; districts: Hyderabad, Khammam, Mahabubnagar, Medchal, Narayanpet, Vikarabad. Earliest partner start year printed: 2014. | https://www.axis.bank.in/about-us/press-releases/axis-bank-foundations-sustainable-livelihood-programme-strikes-gold-at-ficci-s-sustainable-agriculture-summit-and-awards-2024 | Axis Bank press release re: ABF's FICCI award (2024-12) | 2026-09-29 | FY2024 | Not found |
| Chhattisgarh | `funds` | 2011-01-01 *(year only — earliest partner 'since' year printed in AR2025-26)* | — | Earth Care Award 2024 (with BRLF) — "High Impact Mega Watershed Project," 12 districts, 26 blocks, 1 lakh+ families; also a state-level convening venue (Raipur, Oct 2024). **AR2025-26 (p.26):** 5 partners, 124 blocks; districts: Balod, Balrampur, Bastar, Bijapur, Bilaspur, Dantewada, Dhamtari, Gaurela-Pendra-Marwahi, Gariyabandh, Jashpur, Kabirdham, Kanker, Kondagaon, Korba, Koriya, Mahasamund, Mungeli, Narayanpur, Raigarh, Rajnandgaon, Sukma, Surajpur, Surguja. Earliest partner start year printed: 2011. | https://www.axisbank.com/about-us/press-releases/axis-bank-foundation-wins-earth-care-award-2024-for-its-community-based-climate-action-work | Axis Bank press release re: ABF's Earth Care Award 2024 | 2026-09-29 | FY2024 | Not found |
| Andhra Pradesh | `funds` | 2014-01-01 *(year only — earliest partner 'since' year printed in AR2025-26)* | — | Named "adaptive/climate-resilient livelihoods" state in AR2023-24. **AR2025-26 (p.22):** 5 partners, 27 blocks; districts: Anantapuramu, Chittoor, East Godavari, Guntur, Krishna, Sri Sathya Sai, Visakhapatnam, Vizianagaram. Earliest partner start year printed: 2014. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2023-24.pdf | ABF Annual Report 2023-24 (p.05) | 2026-09-29 | FY2023-24 | Not found |
| West Bengal | `funds` | 2023-01-01 *(health-nutrition integration began 2023 per AR narrative)* | not_found | Named in the FY2023-24 health-and-nutrition rollout across "Odisha, Jharkhand and West Bengal." **Role corrected from the invalid `funds (historical)` to plain `funds`; this is actually recent (2023–24), not historical — the earlier "historical, ~2015" framing was based on a different, older reference (TISS manual) that is superseded by this newer evidence.** **AR2025-26 (p.74):** 5 partners, 28 blocks; districts: Bankura, Birbhum, Cooch Behar, Darjeeling, Jalpaiguri, Jhargram, Kalimpong, Kolkata, North 24 Parganas, Purulia, South 24 Parganas. Earliest partner start year printed: 2014. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2023-24.pdf | ABF Annual Report 2023-24 (p.05) | 2026-09-29 | FY2023-24 | Not found |
| Assam | `funds` | not_found | — | "Bina Bora, Nursery-Owner and Entrepreneur, Assam" community-voice case study (AR2024-25); flood-resilient farming named as a Northeast model example. **AR2025-26 North East chapter (p.56; 9 partners/93 blocks for the whole region):** districts in the footprint list for this state: Barpeta, Cachar, Dhemaji, Goalpara, Guwahati, Jorhat, Kamrup, Kamrup Metropolitan, Kokrajhar, Majuli, Nalbari, Tinsukia. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 (p.61-62) | 2026-09-29 | FY2024-25 | Not found |
| Meghalaya | `funds` | not_found | — | Jaksongram village case study (community conservation area / CCA management, AR2024-25). **AR2025-26 North East chapter (p.56; 9 partners/93 blocks for the whole region):** districts in the footprint list for this state: East Garo Hills, East Jaintia Hills, East Khasi Hills, Eastern West Khasi Hills, North Garo Hills, Ri Bhoi, South Garo Hills, South West Garo Hills, South West Khasi Hills, West Garo Hills, West Jaintia Hills, West Khasi Hills. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 (p.63) | 2026-09-29 | FY2024-25 | Not found |
| Nagaland | `funds` *(upgraded 2026-09-29: AR2025-26 names North East Initiative Development Agency (since 2023) for Nagaland & Mizoram, and Eleutheros Christian Society (since 2024) for Eastern Nagaland)* | 2025-03-03 *(Northeast expansion framing dates to the FY24-25 "Towards the Northeast" chapter and the Mission4Million launch)* | — | Named as an agroforestry model example ("agroforestry in Nagaland") — a stated example, not yet evidenced by a specific spend figure, hence `operates` not `funds`. **AR2025-26 North East chapter (p.56; 9 partners/93 blocks for the whole region):** districts in the footprint list for this state: Chumukedima, Kiphire, Longleng, Mokokchung, Mon, Noklak, Nuiland, Peren, Phek, Shamator, Tseminyu, Tuensang. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 (p.61) | 2026-09-29 | FY2024-25 | Not found |
| Mizoram | `funds` *(upgraded 2026-09-29: NEIDA named partner, AR2025-26 p.56)* | 2025-03-03 | — | Named as a bamboo-cooperative model example ("bamboo cooperatives in Mizoram") — stated example, not yet evidenced by spend figure. **AR2025-26 North East chapter (p.56; 9 partners/93 blocks for the whole region):** districts in the footprint list for this state: Aizawl, Champhai, Lunglei, Mamit, Serchhip. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 (p.61) | 2026-09-29 | FY2024-25 | Not found |
| Kerala | `funds` | 2019-01-01 *(year only — earliest partner 'since' year printed in AR2025-26)* | — | TRRAIN partnership — ~2,400 Persons with Disabilities trained across Kerala (2024 press coverage). **AR2025-26 (p.45):** 4 partners, 6 blocks; districts: Ernakulam, Kasaragod, Malappuram, Thiruvananthapuram, Wayanad. Earliest partner start year printed: 2019. | https://thecsruniverse.com/articles/axis-bank-foundation-and-trrain-collaborate-to-create-inclusive-work-opportunities-for-persons-with-disabilities | The CSR Universe (press coverage of ABF–TRRAIN partnership) | 2026-09-29 | Undated in source — flagged, but retained since it is the only figure found *(exception: this is press coverage, not an ABF document, so treated as lower-confidence; kept because it is the only named-state PwD evidence found)* | Not found |
| Bihar | `funds` | 2018-01-01 *(year only — earliest partner 'since' year in the chapter)* | — | **AR2025-26 (p.24):** 6 partners, 35 blocks; districts: Banka, Bhagalpur, Gaya, Hajipur, Jamui, Katihar, Khagaria, Lakhisarai, Munger, Muzaffarpur, Nalanda, Nawada, Patna, Vaishali. Earliest partner start year printed: 2018. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.24) | 2026-09-29 | FY2025-26 | Not found |
| Delhi | `funds` | 2023-01-01 *(year only — earliest partner 'since' year in the chapter)* | — | **AR2025-26 (p.29):** 2 partners, no block count printed; districts: Central Delhi, South West Delhi. Earliest partner start year printed: 2023. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.29) | 2026-09-29 | FY2025-26 | Not found |
| Haryana | `funds` | 2022-01-01 *(year only — earliest partner 'since' year in the chapter)* | — | **AR2025-26 (p.33):** 1 partner, no block count printed; districts: Ambala, Karnal, Kurukshetra, Panchkula, Panipat, Sonipat, Yamuna Nagar. Earliest partner start year printed: 2022. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.33) | 2026-09-29 | FY2025-26 | Not found |
| Himachal Pradesh | `funds` | 2024-01-01 *(year only — earliest partner 'since' year in the chapter)* | — | **AR2025-26 (p.35):** 2 partners, 2 blocks; districts: Hamirpur, Kangra. Earliest partner start year printed: 2024. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.35) | 2026-09-29 | FY2025-26 | Not found |
| Jammu and Kashmir | `funds` | 2024-01-01 *(year only — earliest partner 'since' year in the chapter)* | — | **AR2025-26 (p.37):** 2 partners, 6 blocks; districts: Anantnag, Badgam, Baramulla, Kulgam. Earliest partner start year printed: 2024. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.37) | 2026-09-29 | FY2025-26 | Not found |
| Karnataka | `funds` | 2023-01-01 *(year only — earliest partner 'since' year in the chapter)* | — | **AR2025-26 (p.42):** 5 partners, 38 blocks; districts: Bagalkot, Bengaluru, Bengaluru Rural, Davanagere, Gadag, Hassan, Kalaburagi, Koppal, Mandya, Mysuru, Ramanagara. Earliest partner start year printed: 2023. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.42) | 2026-09-29 | FY2025-26 | Not found |
| Ladakh | `funds` | 2024-01-01 *(year only — earliest partner 'since' year in the chapter)* | — | **AR2025-26 (p.48):** 1 partner, 12 blocks; districts: Kargil, Leh. Earliest partner start year printed: 2024. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.48) | 2026-09-29 | FY2025-26 | Not found |
| Maharashtra | `funds` | 2014-01-01 *(year only — earliest partner 'since' year in the chapter)* | — | **AR2025-26 (p.54):** 13 partners, 140 blocks; districts: Ahilyanagar, Akola, Amravati, Beed, Chandrapur, Dhule, Gadchiroli, Gondia, Hingoli, Jalgaon, Jalna, Kolhapur, Latur, Mumbai, Nagpur, Nanded, Nandurbar, Nashik, Parbhani, Pune, Ratnagiri, Satara, Thane, Wardha, Washim, Yavatmal. Earliest partner start year printed: 2014. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.54) | 2026-09-29 | FY2025-26 | Not found |
| Puducherry | `funds` | 2024-01-01 *(year only — earliest partner 'since' year in the chapter)* | — | **AR2025-26 (p.61):** 2 partners, 2 blocks; districts: Puducherry. Earliest partner start year printed: 2024. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.61) | 2026-09-29 | FY2025-26 | Not found |
| Tamil Nadu | `funds` | 2011-01-01 *(year only — earliest partner 'since' year in the chapter)* | — | **AR2025-26 (p.65):** 5 partners, 81 blocks; districts: Ariyalur, Chennai, Coimbatore, Dharmapuri, Dindigul, Erode, Kanchipuram, Madurai, Namakkal, Pudukkottai, Ramanathapuram, Salem, Sivagangai, Tiruchirappalli, Tiruvallur, Vellore, Virudhunagar. Earliest partner start year printed: 2011. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.65) | 2026-09-29 | FY2025-26 | Not found |
| Uttar Pradesh | `funds` | 2022-01-01 *(year only — earliest partner 'since' year in the chapter)* | — | **AR2025-26 (p.69):** 7 partners, 57 blocks; districts: Agra, Aligarh, Azamgarh, Bahraich, Banda, Barabanki, Basti, Bhadohi, Bulandshahr, Chitrakoot, Etawah, Gautam Buddha Nagar, Ghaziabad, Gonda, Gorakhpur, Hamirpur, Jhansi, Kanpur, Kanpur Dehat, Lucknow, Maharajganj, Meerut, Mirzapur, Prayagraj, Raebareli, Samali, Shahjahanpur, Sitapur, Sonbhadra, Sultanpur, Unnao, Varanasi. Earliest partner start year printed: 2022. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.69) | 2026-09-29 | FY2025-26 | Not found |
| Uttarakhand | `funds` | 2024-01-01 *(year only — earliest partner 'since' year in the chapter)* | — | **AR2025-26 (p.72):** 2 partners, 16 blocks; districts: Bageshwar, Chamoli, Dehradun, Nainital, Pauri Garhwal, Pithoragarh, Tehri Garhwal, Uttarkashi. Earliest partner start year printed: 2024. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.72) | 2026-09-29 | FY2025-26 | Not found |
| Manipur | `funds` | 2023-01-01 *(year only)* | — | **AR2025-26 North East chapter (p.56; 9 partners/93 blocks for the whole region):** districts in the footprint list for this state: Bishnupur, Churachandpur, Jiribam, Tamenglong. SELCO Foundation (since 2023) works in Manipur; also in NoDE. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.56) | 2026-09-29 | FY2025-26 | Not found |
| Tripura | `funds` | not_found | — | **AR2025-26 North East chapter (p.56; 9 partners/93 blocks for the whole region):** districts in the footprint list for this state: Dhalai, Gomati, West Tripura. No Tripura-specific partner is named. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.56) | 2026-09-29 | FY2025-26 | Not found |
| Arunachal Pradesh | `funds` | 2024-01-01 *(year only)* | — | **AR2025-26 North East chapter (p.56; 9 partners/93 blocks for the whole region):** districts in the footprint list for this state: Changlang. NoDE (with SeSTA, since 2024) covers Arunachal Pradesh. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.56) | 2026-09-29 | FY2025-26 | Not found |
| **Remaining states/UTs** | — | — | — | AR2025-26 names **29** states/UTs (22 state chapters + 7 NE states; p.20 and pp.22–75) against the 32 claimed. The other 3 are not named anywhere in the report. The chapter badges add up to 962 blocks, not the 1,394 cumulative (p.76); Delhi and Haryana print no block count. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |

---
---

---
---

**Yearly CSR filing (`funder_csr_years`)**

*Four ABF-only rows (FY2022-23 to FY2025-26), `section_135_applicable = No` throughout, `average_net_profit`/`prescribed_csr` intentionally left empty (ABF is a Trust, not a Section-135 company). Figures are ABF's own Sustainable Livelihood Programme spend, cross-checked across two independent ABF Annual Reports each where possible.*

| fiscal_year | section_135_applicable | average_net_profit | prescribed_csr | total_spent (₹) | admin_overheads | impact_assessment_done | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2022-23 | No | *(empty — n/a)* | *(empty — n/a)* | **1,135,300,000** (₹113.53 cr = ₹99.83 cr Rural Livelihoods + ₹9.93 cr Skill Development + ₹3.77 cr Ecosystem Action) | **Not found.** ABF's "Financial Highlights" tables give category spend only, never a separate admin-overhead line. | **Not found** — no impact-assessment disclosure located in ABF's own AR2022-23 or the retrospective 3-yr tables in AR2023-24/AR2024-25. | ⚠️ Project-count discrepancy: AR2022-23's own Financial Highlights table (p.48) states 33 Rural Livelihoods + 7 Skill Dev + 5 Ecosystem Action + 2 Special = **47–48 total** projects for this year; but the *later* AR2023-24 (p.61) and AR2024-25 (p.17) 3-year retrospective tables both independently state **26 + 6 + 5 + 1 = 38 total** for the same FY2022-23. Two of ABF's own three reports agree on 38 — presented as the more likely figure, but the FY22-23 report's own contemporaneous count (47–48) is not discarded, just flagged. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf ; https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2023-24.pdf | ABF Annual Reports 2022-23 & 2023-24 (cross-checked) | 2026-09-29 | FY2022-23 |
| FY2023-24 | No | *(empty)* | *(empty)* | **1,540,100,000** (₹154.01 cr = ₹129.54 cr + ₹18.39 cr + ₹6.08 cr) | Not found | Not found | Project count: 29 + 7 + 6 + 1 = 43, consistent across AR2023-24 (p.61) and AR2024-25 (p.17). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2023-24.pdf | ABF Annual Report 2023-24 | 2026-09-29 | FY2023-24 |
| FY2024-25 | No | *(empty)* | *(empty)* | **2,319,600,000** (₹231.96 cr = ₹198.29 cr + ₹23.63 cr + ₹10.04 cr) | Not found | Not found | Project count: 46 + 6 + 7 + 0 = 59, per AR2024-25 (p.17). **Now cross-checked:** AR2025-26 p.18 restates ₹231.96 cr, 59 projects, 3,87,467 households. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 |

| FY2025-26 | No | *(empty)* | *(empty)* | **3,529,200,000** (₹352.92 cr) ⚠️ **includes funds disbursed by Axis Bank Limited** (report footnote). The ABF-only portion is not disclosed. | Not found | Not found | 58 projects; 7,12,879 households reached this year. **No category split** (Rural Livelihoods / Skill Dev / Ecosystem Action) is published for FY2025-26. The ~52% jump over FY2024-25 is partly a change in reporting basis (the Bank's disbursements are now included), so it is not a like-for-like increase. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.18) | 2026-09-29 | FY2025-26 |

**Schema columns not shown in the table above, checked in every ABF report including AR2025-26:** `spent_on_projects` (6a), `impact_assessment_cost` (6c), `unspent_transferred` (6e) and `excess_spent` (6f). ABF is a Trust and publishes no CSR annexure, so these are **not published** for any year. Leave them empty; don't enter 0. For FY2025-26, `impact_assessment_done` is also **not found**. AR2025-26 reports a climate-readiness assessment of 35 partners and a migration study (p.83), but neither is an impact assessment of ABF's CSR spend.

**Removed:** all 4 Axis Bank Ltd rows (FY2022-23 through FY2025-26 statutory Annexure-4 figures) and the Bank's CSR Committee table — both out of scope, belong on the Axis Bank Limited funder row.

---
---

---
---

**Spend breakdown (`funder_csr_spend`)**

*Category-level totals only — the only figures ABF itself publishes with real ₹ amounts. `csr_sector_id` mapped to the nearest Schedule VII language. Amounts in ₹ (crore × 10,000,000). All bank-direct rows and the Aspirational-District BRSR table removed per scope.*

| fiscal_year | csr_sector_id (Schedule VII mapping) | project_count | amount (₹) | via_agency | is_ongoing | notes | source_url | source_name | fetched_at | as_of | archive_url |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2020-21 | Rural Livelihoods → *Livelihood Enhancement Projects (Sch. VII item (ii)/(x))* | not_found *(project count not given for this year in the source table)* | 707,500,000 | Yes | Yes | Newly found (ABF AR2022-23, 3-yr trend table). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf | ABF Annual Report 2022-23 (p.48) | 2026-09-29 | FY2020-21 | Not found |
| FY2020-21 | Skill Development → *Vocational Skills (Sch. VII item (ii))* | not_found | 41,000,000 | Yes | Yes | Same source. | (same) | (same) | 2026-09-29 | FY2020-21 | Not found |
| FY2020-21 | *(Total)* | not_found | 748,500,000 | — | — | 25 states, 10,982 villages that year. | (same) | (same) | 2026-09-29 | FY2020-21 | Not found |
| FY2021-22 | Rural Livelihoods | 23 | 791,100,000 | Yes | Yes | (same) | (same) | (same) | 2026-09-29 | FY2021-22 | Not found |
| FY2021-22 | Skill Development | 3 | 56,700,000 | Yes | Yes | (same) | (same) | (same) | 2026-09-29 | FY2021-22 | Not found |
| FY2021-22 | Ecosystem Action → *Capacity Building (Sch. VII item (ix)/general)* | 1 | 1,100,000 | Yes | Yes | (same) | (same) | (same) | 2026-09-29 | FY2021-22 | Not found |
| FY2021-22 | *(Total)* | 27 | 848,900,000 | — | — | 26 states, 12,436 villages. | (same) | (same) | 2026-09-29 | FY2021-22 | Not found |
| FY2022-23 | Rural Livelihoods | 26 *(or 33 — see funder_csr_years note)* | 998,300,000 | Yes | Yes | Cross-checked figure (38-total version); see `funder_csr_years` for the discrepancy flag. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 (3-yr trend table) | 2026-09-29 | FY2022-23 | Not found |
| FY2022-23 | Skill Development | 6 *(or 7)* | 99,300,000 | Yes | Yes | Same. | (same) | (same) | 2026-09-29 | FY2022-23 | Not found |
| FY2022-23 | Ecosystem Action | 5 | 37,700,000 | Yes | Yes | Same. | (same) | (same) | 2026-09-29 | FY2022-23 | Not found |
| FY2023-24 | Rural Livelihoods | 29 | 1,295,400,000 | Yes | Yes | — | (same) | (same) | 2026-09-29 | FY2023-24 | Not found |
| FY2023-24 | Skill Development | 7 | 183,900,000 | Yes | Yes | — | (same) | (same) | 2026-09-29 | FY2023-24 | Not found |
| FY2023-24 | Ecosystem Action | 6 | 60,800,000 | Yes | Yes | — | (same) | (same) | 2026-09-29 | FY2023-24 | Not found |
| FY2024-25 | Rural Livelihoods | 46 | 1,982,900,000 | Yes | Yes | — | (same) | (same) | 2026-09-29 | FY2024-25 | Not found |
| FY2024-25 | Skill Development | 6 | 236,300,000 | Yes | Yes | — | (same) | (same) | 2026-09-29 | FY2024-25 | Not found |
| FY2024-25 | Ecosystem Action | 7 | 100,400,000 | Yes | Yes | — | (same) | (same) | 2026-09-29 | FY2024-25 | Not found |

**FY2025-26:** AR2025-26 gives **no sector, state or project split**. The only row the report supports is the year total, in the same style as the FY2020-21/FY2021-22 *(Total)* rows above:

| fiscal_year | csr_sector_id | state_location_id | project_count | amount (₹) | via_agency | is_ongoing | notes | source_url | source_name | fetched_at | as_of | archive_url |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2025-26 | *(Total — leave empty)* | *(empty)* | 58 | 3,529,200,000 | Yes | Yes | ₹352.92 cr, footnoted "*Includes funds disbursed by Axis Bank Limited" (p.18). Not ABF-only, and not comparable with FY2024-25. `implementing_agency` / `project_name` aren't printed. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.18) | 2026-09-29 | FY2025-26 | Not found |

**Deleted per instruction:** all "Special Projects" rows (`amount` unavailable, required field would be empty — dropped rather than force-loaded).
**Removed per scope:** the Aspirational-District BRSR table (bank data) and all 5 bank-direct project rows (Financial Literacy Training, Mobile Vans, Child Heart Surgeries, Mid-Day Meal Program, Axis DilSe).
**`project_name` + `implementing_agency` + real per-project `amount`:** still **not found** for any individual project among the ~59/yr — ABF publishes category totals and a separate partner-name list (see `funder_partners`), never a project-by-project ₹ figure. `agency_csr1`: not found for any partner (see `funder_partners`).

---
---

**Programmes (`programs`) — hierarchy**

*`kind` corrected (Rural Livelihoods, Skill Development → `programme`; Ecosystem Action added as `programme`, `is_enabler=Yes`). All dates in YYYY-MM-DD or `not_found`. Bank-direct themes removed.*

| name | kind | parent | status | start_date | end_date | is_enabler | description | source_url | fetched_at | as_of | archive_url |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Livelihoods | `theme` | — | active | 2011-01-01 *(approximate — "2011-12" pivot year, day/month not disclosed)* | — | No | ABF's core strategic theme since its 2011-12 pivot from an original education/trauma-care mandate. All current ABF grant-making sits under this theme. | https://www.axisbankfoundation.org/about-us/overview.html | 2026-09-29 | FY2024-25 | Not found |
| Sustainable Livelihood Programme (SLP) | `programme` | → Livelihoods | active | 2011-01-01 | — | No | ABF's flagship and only current grant-making vehicle, delivered through NGO/CSO/government partnerships across rural India. It combines income diversification (farm and non-farm), natural resource management, skilling, and — since 2022-23 — health and nutrition, aiming to build resilient, self-reliant rural households rather than deliver one-off relief. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | 2026-09-29 | FY2024-25 | Not found |
| Rural Livelihoods | `programme` *(changed from `project` per instruction)* | → Sustainable Livelihood Programme | active | 2011-01-01 | — | No | The largest SLP pillar by spend, covering farm and non-farm income diversification: agriculture, horticulture, livestock, agroforestry, watershed/water-resource management, and market/credit linkages for rural households. Reached ₹198.29 crore in spend across 46 projects in FY2024-25 alone. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | 2026-09-29 | FY2024-25 | Not found |
| Skill Development | `programme` *(changed from `project`)* | → Sustainable Livelihood Programme | active | 2007-01-01 *(approximate — "2007-2010" origin window for PwD skilling, exact date not disclosed)* | — | No | Vocational and employability skilling for rural youth, with an explicit sub-focus on Persons with Disabilities (e.g. via TRRAIN, Enable India). Spent ₹23.63 crore across 6 projects in FY2024-25. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | 2026-09-29 | FY2024-25 | Not found |
| Ecosystem Action | `programme` *(newly added per instruction)* | → Sustainable Livelihood Programme | active | not_found | — | **Yes** | A capacity-building/enabling pillar rather than direct service delivery — strengthens community institutions (SHGs, federations, Village Level Institutions), builds partner-NGO organisational capacity (finance, governance, MEL, digital MIS per the "Towards the Northeast" chapter), and supports cross-learning platforms (Abhisaran, Samagam, Samanvay). Spent ₹10.04 crore across 7 projects in FY2024-25. **FY2025-26 activities (AR2025-26 pp.80–83):** Abhisaran convenings in Odisha (Sep 2025, 7 partners; Dec 2025 digital-tools workshop, 6 partners); Chhattisgarh follow-on (4 partners, 6 workshops, 9 trainings); NorthEast Edit with North East Together (21 NGOs, 38 funders/CSR, 12 knowledge partners; NE non-profit directory launched); a leadership-coaching pilot for 5 partner CEOs; governance workshops with 30+ partners, producing the *Good Governance Toolkit*; a communications programme with India Development Review for 23 partners (*Communications is Capacity*, 7 playbooks); the *Vikaasvaani* quarterly newsletter; 20 thematic playbooks (English and Hindi); a migration study with Development Intelligence Unit (~2,000 households); and a climate-readiness assessment of 35 SLP partners. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | 2026-09-29 | FY2024-25 | Not found |
| Mission 1 Million | `phase` | → Sustainable Livelihood Programme | concluded | 2011-01-01 | 2018-01-01 | No | Foundational SLP phase targeting 1 million individuals, focused on water access, agricultural productivity, and diversification into horticulture, livestock, and agroforestry. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | 2026-09-29 | FY2024-25 | Not found |
| Mission 2 Million | `phase` | → Sustainable Livelihood Programme | concluded | not_found *(2017, 2018, or 2019 depending on source — see the flagged inconsistency in `profile.flagship_program` above; using not_found here rather than silently picking one)* | 2025-03-31 | No | Committed to reaching 2 million rural households; achieved and formally marked complete at the "Abhisaran 2025" event (2025-03-03), reaching 2,046,247 cumulative households. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | 2026-09-29 | FY2024-25 | Not found |
| Mission 4 Million | `phase` | → Sustainable Livelihood Programme | active | 2025-03-03 | 2031-01-01 *(target year, exact date not disclosed)* | No | Successor to Mission 2 Million, launched at "Abhisaran 2025"/"One Axis CSR Vision," targeting an additional 2 million rural households (4 million cumulative) by 2031, with added focus on climate resilience, capacity building, and community leadership. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | 2026-09-29 | FY2024-25 | Not found |
| Towards the Northeast (expansion) | `phase` | → Sustainable Livelihood Programme | active | 2024-04-01 *(approximate — FY2024-25 start, exact date not disclosed)* | — | No | Strategic geographic expansion into North-East India (named examples: Assam, Meghalaya, Nagaland, Mizoram), combining integrated farming, forest/non-farm livelihoods, decentralised renewable energy, skilling, and public-scheme convergence, delivered through capacity-building of local CSOs. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | 2026-09-29 | FY2024-25 | Not found |
| SRIJAN Partnership | `project` | → Rural Livelihoods | active | 2012-01-01 | — | No | Livelihoods partnership with SRIJAN (Self Reliant Initiatives through Joint Action, founded by Ved Arya) covering 4 districts of Rajasthan since 2012. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf | 2026-09-29 | FY2022-23 | Not found |
| Health & Nutrition Integration | `project` *(cross-cutting, sits partly under Rural Livelihoods)* | → Sustainable Livelihood Programme | active | 2022-01-01 | — | Yes *(an overlay/enabler on existing livelihood projects, not standalone service delivery)* | Began integrating health and nutrition into SLP in 2022-23, delivered via CINI, Harsha Trust, Rajarhat Prasari, and PRADAN across Jharkhand, Odisha and West Bengal. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | 2026-09-29 | FY2024-25 | Not found |
| Education | `theme` | — | concluded | 2006-01-01 | 2012-01-01 *(approximate)* | No | ABF's original founding focus (2006), superseded by the livelihoods pivot. No current activity. | https://www.axisbankfoundation.org/about-us/overview.html | 2026-09-29 | — | Not found |
| Highway Trauma Care | `theme` | — | concluded | 2006-01-01 | not_found | No | Part of ABF's original 2006 founding mandate alongside Education; no evidence of current activity in any Annual Report reviewed. | https://www.axisbankfoundation.org/about-us/overview.html | 2026-09-29 | — | Not found |

**New / updated programme rows from AR2025-26** *(full schema columns; `details` JSON included)*

| name | kind | parent | status | start_date | end_date | is_enabler | description | details (JSON) | source_url | source_name | fetched_at | as_of | archive_url |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mission 4 Million *(update)* | `phase` | → Sustainable Livelihood Programme | active | 2025-03-03 | 2031-03-31 *("by 2031", p.9. ⚠️ p.14 says "by 2030")* | No | FY2025-26 was the first full year. 27,59,126 households reached cumulatively (2018–2026), with 7,12,879 added in FY2025-26, across 33,517 villages, 1,394 blocks, 306 districts and 32 states/UTs. | `{"target_households": 4000000, "achieved_cumulative": 2759126, "achieved_fy2025_26": 712879, "projects_fy2025_26": 58}` | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.9, 18, 76) | 2026-09-29 | FY2025-26 | Not found |
| Northeast Organisational Development for Empowerment (NoDE) | `project` | → Ecosystem Action | active | 2024-01-01 *(year only)* | — | **Yes** | Developed by SeSTA with ABF. Each North East grassroots organisation gets an institutional assessment, then long-term accompaniment on leadership, governance, compliance, MEL, finance, HR, communications, fundraising and digital systems. Covers Assam, Nagaland, Meghalaya, Manipur and Arunachal Pradesh. | `{"implementer": "Seven Sisters Development Assistance (SeSTA)", "states": ["Assam","Nagaland","Meghalaya","Manipur","Arunachal Pradesh"]}` | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.56–58) | 2026-09-29 | FY2025-26 | Not found |
| Abhisaran (convening platform) | `project` | → Ecosystem Action | active | not_found | — | **Yes** | ABF's multi-stakeholder convening platform. In FY2025-26 it held an Odisha state convening (September 2025, 7 partners) and a digital-tools workshop (December 2025, 6 partners). A Chhattisgarh follow-on from FY2024-25 led 4 partners to run 6 workshops and 9 trainings. | `{"events_fy2025_26": ["Odisha convening Sep 2025 (7 partners)", "Odisha tech workshop Dec 2025 (6 partners)"]}` | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.80–81) | 2026-09-29 | FY2025-26 | Not found |
| The NorthEast Edit | `project` | → Ecosystem Action | concluded *(one-off event)* | not_found | not_found | **Yes** | Convening with North East Together: 24 representatives from 21 NGOs, 38 from funding/CSR/philanthropy and 12 from knowledge partners. Launched a directory of North East non-profits. | `{"ngo_reps": 24, "ngos": 21, "funder_reps": 38, "knowledge_partner_reps": 12}` | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.81) | 2026-09-29 | FY2025-26 | Not found |
| Unlocking Potential — leadership coaching pilot | `project` | → Ecosystem Action | active *(pilot)* | not_found | — | **Yes** | One-to-one professional coaching for 5 emerging CEOs of partner organisations. | `{"participants": 5}` | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.81–82) | 2026-09-29 | FY2025-26 | Not found |
| Good Governance workshops & Toolkit | `project` | → Ecosystem Action | active | not_found | — | **Yes** | Workshops in Bhubaneswar, Delhi and Ahmedabad with 30+ partner organisations, producing *The Good Governance Toolkit* for nonprofit boards. | `{"partner_orgs": "30+", "cities": ["Bhubaneswar","Delhi","Ahmedabad"]}` | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.82) | 2026-09-29 | FY2025-26 | Not found |
| Communications is Capacity | `project` | → Ecosystem Action | active | not_found | — | **Yes** | Communications capacity-building for 23 partner organisations with India Development Review, producing 7 playbooks. | `{"partner_orgs": 23, "playbooks": 7, "with": "India Development Review"}` | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.82) | 2026-09-29 | FY2025-26 | Not found |
| Vikaasvaani newsletter & thematic playbooks | `project` | → Ecosystem Action | active | not_found | — | **Yes** | A quarterly partner newsletter, plus 20 thematic playbooks in English and Hindi on water, agriculture, livestock, nutrition and entrepreneurship. | `{"playbooks": 20, "languages": ["English","Hindi"]}` | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.83) | 2026-09-29 | FY2025-26 | Not found |
| Migration study | `project` | → Ecosystem Action | concluded | not_found | not_found | **Yes** | Multi-state study of ~2,000 migrant households across major migration corridors, with Development Intelligence Unit. | `{"households": 2000, "with": "Development Intelligence Unit"}` | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.83) | 2026-09-29 | FY2025-26 | Not found |
| Climate-readiness assessment | `project` | → Ecosystem Action | concluded | not_found | not_found | **Yes** | Assessment of 35 SLP implementing organisations: how they integrate climate into programme design, their capacity, data systems and measurement. | `{"orgs_assessed": 35}` | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.83) | 2026-09-29 | FY2025-26 | Not found |
| Health & Nutrition Integration *(update)* | `project` | → Sustainable Livelihood Programme | active | 2023-01-01 *(CINI "since 2023")* | — | Yes | Life-cycle health and nutrition work with Child In Need Institute in Khunti and Dumka (Jharkhand), reaching 40,080 households. CINI is also a partner in Odisha and West Bengal. | `{"households_jharkhand": 40080, "partner": "Child In Need Institute"}` | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.39) | 2026-09-29 | FY2025-26 | Not found |
| Public Policy in Action Fellows (district governance) | `project` | → Rural Livelihoods | active | 2022-01-01 *(TRIF "since 2022")* | — | **Yes** | Transform Rural India Foundation fellows placed in district administrations to improve planning and cross-department convergence, notably in Aspirational Districts (Chhattisgarh, Jharkhand). | `{"implementer": "Transform Rural India Foundation", "designation": "aspirational district"}` | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.26, 39) | 2026-09-29 | FY2025-26 | Not found |
| Development Practitioners' Training (Uttarakhand) | `project` | → Rural Livelihoods | active | 2025-01-01 *(PSI "since 2025")* | — | **Yes** | Part of a five-year initiative with People's Science Institute in Chamoli. Aims to train 50 rural youth as development professionals. | `{"target_youth": 50, "households": 2000}` | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.72) | 2026-09-29 | FY2025-26 | Not found |
| Axis Cares | `programme` | — *(Axis employee giving; listed under ABF "Programme Partners")* | active | not_found | — | No | "Axis Cares inspires Axisians towards making a difference in society…" Employee contributions channelled to 8 NGO partners. Kept separate from the SLP. | `{"partners_fy2025_26": 8}` | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.84) | 2026-09-29 | FY2025-26 | Not found |

*Existing rows above: the Ecosystem Action spend ("₹10.04 crore across 7 projects") is FY2024-25. AR2025-26 publishes no FY2025-26 spend or project count per pillar. The existing table has no `source_name` or `details` columns, so fill `source_name` from the URL (all ABF Annual Reports or the ABF website) and set `details` = `{}`.*

**Removed per scope:** Financial Inclusion & Literacy (theme) + its 2 projects, and Healthcare & Humanitarian Relief (theme) + its 3 projects — all Axis Bank Limited direct programmes, out of scope for this ABF-only file.

---
---

---
---

**Where programmes ran (`funder_footprints`)**

*One row per state (no aggregate rows); `fiscal_year` in required `FYyyyy-yy` format or the row is dropped per instruction. All sources ABF-only.*

| program | fiscal_year | location (name_as_printed) | notes | source_url | source_name | fetched_at | as_of | archive_url |
|---|---|---|---|---|---|---|---|---|
| Sustainable Livelihood Programme | FY2022-23 | *(aggregate: 26 states — individual names not published by ABF)* | Aggregate only — see `funder_locations` for the individually-named subset. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf | ABF Annual Report 2022-23 | 2026-09-29 | FY2022-23 | Not found |
| Sustainable Livelihood Programme | FY2023-24 | *(aggregate: 28 states)* | Same. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2023-24.pdf | ABF Annual Report 2023-24 | 2026-09-29 | FY2023-24 | Not found |
| Sustainable Livelihood Programme | FY2024-25 | *(aggregate: 32 states, 23,686 villages, 775 blocks, 300 districts)* | Same. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 | Not found |
| Rural Livelihoods (pillar) — SRIJAN partnership | FY2012-13 *(partner-since year; not necessarily first-project year)* | Rajasthan | 4 districts, unnamed individually. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf | ABF Annual Report 2022-23 (Programme Partners) | 2026-09-29 | FY2022-23 | Not found |
| Rural Livelihoods (pillar) | FY2024-25 | Odisha | Siangbali GP, Daringbadi block case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 | Not found |
| Rural Livelihoods (pillar) | FY2024-25 | Madhya Pradesh | "Sita Devi, Farmer" case study; district not specified. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 | Not found |
| Rural Livelihoods (pillar) | FY2022-23 | Gujarat | Trustee site visit, Dahod & Panchmahal districts, NM Sadguru Foundation. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf | ABF Annual Report 2022-23 | 2026-09-29 | FY2022-23 | Not found |
| Environmental Sustainability / NRM | FY2024-25 | Jharkhand | FICCI 2024 Gold Award, WOTR-implemented, Khunti district. | https://www.axis.bank.in/about-us/press-releases/axis-bank-foundations-sustainable-livelihood-programme-strikes-gold-at-ficci-s-sustainable-agriculture-summit-and-awards-2024 | Axis Bank press release | 2026-09-29 | FY2024-25 | Not found |
| Environmental Sustainability / NRM | FY2024-25 | Telangana | FICCI 2024 Gold Award, Narayanpet district. | (same) | Axis Bank press release | 2026-09-29 | FY2024-25 | Not found |
| Environmental Sustainability / NRM | FY2024-25 | Maharashtra | FICCI 2024 Gold Award, Ahmednagar & Beed districts. | (same) | Axis Bank press release | 2026-09-29 | FY2024-25 | Not found |
| Environmental Sustainability / NRM | FY2023-24 | Chhattisgarh | Earth Care Award 2024 (with BRLF), 12 districts, 26 blocks. | https://www.axisbank.com/about-us/press-releases/axis-bank-foundation-wins-earth-care-award-2024-for-its-community-based-climate-action-work | Axis Bank press release | 2026-09-29 | FY2023-24 | Not found |
| Towards the Northeast (phase) | FY2024-25 | Assam | Bina Bora case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 | Not found |
| Towards the Northeast (phase) | FY2024-25 | Meghalaya | Jaksongram village case study. | (same) | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 | Not found |
| Towards the Northeast (phase) | FY2024-25 | Nagaland | Named agroforestry model example (`operates`, not yet spend-evidenced). | (same) | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 | Not found |
| Towards the Northeast (phase) | FY2024-25 | Mizoram | Named bamboo-cooperative model example (`operates`, not yet spend-evidenced). | (same) | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 | Not found |
| Skill Development (pillar) | FY2024-25 *(press date; project itself undated in ABF's own materials)* | Kerala | TRRAIN partnership, ~2,400 PwDs trained. | https://thecsruniverse.com/articles/axis-bank-foundation-and-trrain-collaborate-to-create-inclusive-work-opportunities-for-persons-with-disabilities | The CSR Universe (press) | 2026-09-29 | FY2024-25 (approx.) | Not found |

### FY2025-26 — `funder_footprints` rows (ABF AR2025-26, pp.20–75)

*Schema columns: program → programs.id · fiscal_year · location → locations.id · name_as_printed · notes · source columns. The source columns are the same on every row: `source_url` = https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf · `source_name` = ABF Annual Report 2025-26 · `fetched_at` = 2026-09-29 · `as_of` = FY2025-26 · `archive_url` = Not found. Each chapter's footprint map carries the caption "Highlighted areas in the map depict our programme footprint". The district lists are taken from the "project locations … are spread across" sentence in each chapter.*

#### (a) State level — one row per state/UT (29)

| program | fiscal_year | location (state) | name_as_printed | notes |
|---|---|---|---|---|
| Sustainable Livelihood Programme | FY2025-26 | Andhra Pradesh | Andhra Pradesh | Chapter p.22; map badge 5 partners / 27 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Bihar | Bihar | Chapter p.24; map badge 6 partners / 35 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Chhattisgarh | Chhattisgarh | Chapter p.26; map badge 5 partners / 124 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Delhi | Delhi | Chapter p.29; map badge 2 partners / block count not printed. |
| Sustainable Livelihood Programme | FY2025-26 | Gujarat | Gujarat | Chapter p.31; map badge 7 partners / 18 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Haryana | Haryana | Chapter p.33; map badge 1 partners / block count not printed. |
| Sustainable Livelihood Programme | FY2025-26 | Himachal Pradesh | Himachal Pradesh | Chapter p.35; map badge 2 partners / 2 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Jammu and Kashmir | Jammu and Kashmir | Chapter p.37; map badge 2 partners / 6 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Jharkhand | Jharkhand | Chapter p.39; map badge 5 partners / 69 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Karnataka | Karnataka | Chapter p.42; map badge 5 partners / 38 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Kerala | Kerala | Chapter p.45; map badge 4 partners / 6 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Ladakh | Ladakh | Chapter p.48; map badge 1 partners / 12 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Madhya Pradesh | Madhya Pradesh | Chapter p.51; map badge 14 partners / 103 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Maharashtra | Maharashtra | Chapter p.54; map badge 13 partners / 140 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Odisha | Odisha | Chapter p.59; map badge 9 partners / 58 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Puducherry | Puducherry | Chapter p.61; map badge 2 partners / 2 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Rajasthan | Rajasthan | Chapter p.63; map badge 8 partners / 28 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Tamil Nadu | Tamil Nadu | Chapter p.65; map badge 5 partners / 81 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Telangana | Telangana | Chapter p.67; map badge 3 partners / 19 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Uttar Pradesh | Uttar Pradesh | Chapter p.69; map badge 7 partners / 57 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Uttarakhand | Uttarakhand | Chapter p.72; map badge 2 partners / 16 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | West Bengal | West Bengal | Chapter p.74; map badge 5 partners / 28 blocks. |
| Sustainable Livelihood Programme | FY2025-26 | Assam | Assam *(within "North East India" chapter)* | p.56; the regional badge (9 partners / 93 blocks) covers all NE states together. |
| Sustainable Livelihood Programme | FY2025-26 | Meghalaya | Meghalaya *(within "North East India" chapter)* | p.56; the regional badge (9 partners / 93 blocks) covers all NE states together. |
| Sustainable Livelihood Programme | FY2025-26 | Nagaland | Nagaland *(within "North East India" chapter)* | p.56; the regional badge (9 partners / 93 blocks) covers all NE states together. |
| Sustainable Livelihood Programme | FY2025-26 | Mizoram | Mizoram *(within "North East India" chapter)* | p.56; the regional badge (9 partners / 93 blocks) covers all NE states together. |
| Sustainable Livelihood Programme | FY2025-26 | Manipur | Manipur *(within "North East India" chapter)* | p.56; the regional badge (9 partners / 93 blocks) covers all NE states together. |
| Sustainable Livelihood Programme | FY2025-26 | Tripura | Tripura *(within "North East India" chapter)* | p.56; the regional badge (9 partners / 93 blocks) covers all NE states together. |
| Sustainable Livelihood Programme | FY2025-26 | Arunachal Pradesh | Arunachal Pradesh *(within "North East India" chapter)* | p.56; the regional badge (9 partners / 93 blocks) covers all NE states together. |

#### (b) District level — one row per district as printed

| program | fiscal_year | location (district → state) | name_as_printed | notes |
|---|---|---|---|---|
| SLP | FY2025-26 | Anantapuramu → Andhra Pradesh | Anantapuramu | p.22.  |
| SLP | FY2025-26 | Chittoor → Andhra Pradesh | Chittoor | p.22.  |
| SLP | FY2025-26 | East Godavari → Andhra Pradesh | East Godavari | p.22.  |
| SLP | FY2025-26 | Guntur → Andhra Pradesh | Guntur | p.22.  |
| SLP | FY2025-26 | Krishna → Andhra Pradesh | Krishna | p.22.  |
| SLP | FY2025-26 | Sri Sathya Sai → Andhra Pradesh | Sri Sathya Sai | p.22.  |
| SLP | FY2025-26 | Visakhapatnam → Andhra Pradesh | Visakhapatnam | p.22.  |
| SLP | FY2025-26 | Vizianagaram → Andhra Pradesh | Vizianagaram | p.22.  |
| SLP | FY2025-26 | Banka → Bihar | Banka | p.24.  |
| SLP | FY2025-26 | Bhagalpur → Bihar | Bhagalpur | p.24.  |
| SLP | FY2025-26 | Gaya → Bihar | Gaya | p.24.  |
| SLP | FY2025-26 | Hajipur → Bihar | Hajipur | p.24. Hajipur is the HQ town of Vaishali district, which is also listed. Map to Vaishali or drop as a duplicate. |
| SLP | FY2025-26 | Jamui → Bihar | Jamui | p.24.  |
| SLP | FY2025-26 | Katihar → Bihar | Katihar | p.24.  |
| SLP | FY2025-26 | Khagaria → Bihar | Khagaria | p.24.  |
| SLP | FY2025-26 | Lakhisarai → Bihar | Lakhisarai | p.24.  |
| SLP | FY2025-26 | Munger → Bihar | Munger | p.24.  |
| SLP | FY2025-26 | Muzaffarpur → Bihar | Muzaffarpur | p.24.  |
| SLP | FY2025-26 | Nalanda → Bihar | Nalanda | p.24.  |
| SLP | FY2025-26 | Nawada → Bihar | Nawada | p.24.  |
| SLP | FY2025-26 | Patna → Bihar | Patna | p.24.  |
| SLP | FY2025-26 | Vaishali → Bihar | Vaishali | p.24.  |
| SLP | FY2025-26 | Balod → Chhattisgarh | Balod | p.26.  |
| SLP | FY2025-26 | Balrampur → Chhattisgarh | Balrampur | p.26.  |
| SLP | FY2025-26 | Bastar → Chhattisgarh | Bastar | p.26.  |
| SLP | FY2025-26 | Bijapur → Chhattisgarh | Bijapur | p.26.  |
| SLP | FY2025-26 | Bilaspur → Chhattisgarh | Bilaspur | p.26.  |
| SLP | FY2025-26 | Dantewada → Chhattisgarh | Dantewada | p.26.  |
| SLP | FY2025-26 | Dhamtari → Chhattisgarh | Dhamtari | p.26.  |
| SLP | FY2025-26 | Gaurela-Pendra-Marwahi → Chhattisgarh | Gaurela-Pendra-Marwahi | p.26.  |
| SLP | FY2025-26 | Gariyabandh → Chhattisgarh | Gariyabandh | p.26. LGD spelling: Gariaband. |
| SLP | FY2025-26 | Jashpur → Chhattisgarh | Jashpur | p.26.  |
| SLP | FY2025-26 | Kabirdham → Chhattisgarh | Kabirdham | p.26.  |
| SLP | FY2025-26 | Kanker → Chhattisgarh | Kanker | p.26.  |
| SLP | FY2025-26 | Kondagaon → Chhattisgarh | Kondagaon | p.26.  |
| SLP | FY2025-26 | Korba → Chhattisgarh | Korba | p.26.  |
| SLP | FY2025-26 | Koriya → Chhattisgarh | Koriya | p.26.  |
| SLP | FY2025-26 | Mahasamund → Chhattisgarh | Mahasamund | p.26.  |
| SLP | FY2025-26 | Mungeli → Chhattisgarh | Mungeli | p.26.  |
| SLP | FY2025-26 | Narayanpur → Chhattisgarh | Narayanpur | p.26.  |
| SLP | FY2025-26 | Raigarh → Chhattisgarh | Raigarh | p.26.  |
| SLP | FY2025-26 | Rajnandgaon → Chhattisgarh | Rajnandgaon | p.26.  |
| SLP | FY2025-26 | Sukma → Chhattisgarh | Sukma | p.26.  |
| SLP | FY2025-26 | Surajpur → Chhattisgarh | Surajpur | p.26.  |
| SLP | FY2025-26 | Surguja → Chhattisgarh | Surguja | p.26.  |
| SLP | FY2025-26 | Central Delhi → Delhi | Central Delhi | p.29. Printed only as "Central and South West Delhi". |
| SLP | FY2025-26 | South West Delhi → Delhi | South West Delhi | p.29. Printed only as "Central and South West Delhi". |
| SLP | FY2025-26 | Ahmedabad → Gujarat | Ahmedabad | p.31.  |
| SLP | FY2025-26 | Amreli → Gujarat | Amreli | p.31.  |
| SLP | FY2025-26 | Anand → Gujarat | Anand | p.31.  |
| SLP | FY2025-26 | Aravalli → Gujarat | Aravalli | p.31.  |
| SLP | FY2025-26 | Banaskantha → Gujarat | Banaskantha | p.31.  |
| SLP | FY2025-26 | Bharuch → Gujarat | Bharuch | p.31.  |
| SLP | FY2025-26 | Bhavnagar → Gujarat | Bhavnagar | p.31.  |
| SLP | FY2025-26 | Botad → Gujarat | Botad | p.31.  |
| SLP | FY2025-26 | Chhota Udaipur → Gujarat | Chhota Udaipur | p.31.  |
| SLP | FY2025-26 | Dahod → Gujarat | Dahod | p.31.  |
| SLP | FY2025-26 | Dang → Gujarat | Dang | p.31.  |
| SLP | FY2025-26 | Devbhoomi Dwarka → Gujarat | Devbhoomi Dwarka | p.31.  |
| SLP | FY2025-26 | Gandhinagar → Gujarat | Gandhinagar | p.31.  |
| SLP | FY2025-26 | Gir Somnath → Gujarat | Gir Somnath | p.31.  |
| SLP | FY2025-26 | Jamnagar → Gujarat | Jamnagar | p.31.  |
| SLP | FY2025-26 | Junagadh → Gujarat | Junagadh | p.31.  |
| SLP | FY2025-26 | Kheda → Gujarat | Kheda | p.31.  |
| SLP | FY2025-26 | Kutch → Gujarat | Kutch | p.31.  |
| SLP | FY2025-26 | Mahisagar → Gujarat | Mahisagar | p.31.  |
| SLP | FY2025-26 | Mehsana → Gujarat | Mehsana | p.31.  |
| SLP | FY2025-26 | Morbi → Gujarat | Morbi | p.31.  |
| SLP | FY2025-26 | Narmada → Gujarat | Narmada | p.31.  |
| SLP | FY2025-26 | Navsari → Gujarat | Navsari | p.31.  |
| SLP | FY2025-26 | Panchmahal → Gujarat | Panchmahal | p.31.  |
| SLP | FY2025-26 | Patan → Gujarat | Patan | p.31.  |
| SLP | FY2025-26 | Porbandar → Gujarat | Porbandar | p.31.  |
| SLP | FY2025-26 | Rajkot → Gujarat | Rajkot | p.31.  |
| SLP | FY2025-26 | Sabarkantha → Gujarat | Sabarkantha | p.31.  |
| SLP | FY2025-26 | Surat → Gujarat | Surat | p.31.  |
| SLP | FY2025-26 | Surendranagar → Gujarat | Surendranagar | p.31.  |
| SLP | FY2025-26 | Tapi → Gujarat | Tapi | p.31.  |
| SLP | FY2025-26 | Vadodara → Gujarat | Vadodara | p.31.  |
| SLP | FY2025-26 | Valsad → Gujarat | Valsad | p.31.  |
| SLP | FY2025-26 | Ambala → Haryana | Ambala | p.33.  |
| SLP | FY2025-26 | Karnal → Haryana | Karnal | p.33.  |
| SLP | FY2025-26 | Kurukshetra → Haryana | Kurukshetra | p.33.  |
| SLP | FY2025-26 | Panchkula → Haryana | Panchkula | p.33.  |
| SLP | FY2025-26 | Panipat → Haryana | Panipat | p.33.  |
| SLP | FY2025-26 | Sonipat → Haryana | Sonipat | p.33.  |
| SLP | FY2025-26 | Yamuna Nagar → Haryana | Yamuna Nagar | p.33.  |
| SLP | FY2025-26 | Hamirpur → Himachal Pradesh | Hamirpur | p.35.  |
| SLP | FY2025-26 | Kangra → Himachal Pradesh | Kangra | p.35.  |
| SLP | FY2025-26 | Anantnag → Jammu and Kashmir | Anantnag | p.37.  |
| SLP | FY2025-26 | Badgam → Jammu and Kashmir | Badgam | p.37. LGD spelling: Budgam. |
| SLP | FY2025-26 | Baramulla → Jammu and Kashmir | Baramulla | p.37.  |
| SLP | FY2025-26 | Kulgam → Jammu and Kashmir | Kulgam | p.37.  |
| SLP | FY2025-26 | Bokaro → Jharkhand | Bokaro | p.39.  |
| SLP | FY2025-26 | Chatra → Jharkhand | Chatra | p.39.  |
| SLP | FY2025-26 | Dhanbad → Jharkhand | Dhanbad | p.39.  |
| SLP | FY2025-26 | Dumka → Jharkhand | Dumka | p.39.  |
| SLP | FY2025-26 | East Singhbhum → Jharkhand | East Singhbhum | p.39.  |
| SLP | FY2025-26 | Garhwa → Jharkhand | Garhwa | p.39.  |
| SLP | FY2025-26 | Giridih → Jharkhand | Giridih | p.39.  |
| SLP | FY2025-26 | Godda → Jharkhand | Godda | p.39.  |
| SLP | FY2025-26 | Gumla → Jharkhand | Gumla | p.39.  |
| SLP | FY2025-26 | Hazaribagh → Jharkhand | Hazaribagh | p.39.  |
| SLP | FY2025-26 | Khunti → Jharkhand | Khunti | p.39.  |
| SLP | FY2025-26 | Latehar → Jharkhand | Latehar | p.39.  |
| SLP | FY2025-26 | Lohardaga → Jharkhand | Lohardaga | p.39.  |
| SLP | FY2025-26 | Palamu → Jharkhand | Palamu | p.39.  |
| SLP | FY2025-26 | Ramgarh → Jharkhand | Ramgarh | p.39.  |
| SLP | FY2025-26 | Ranchi → Jharkhand | Ranchi | p.39.  |
| SLP | FY2025-26 | Sahibganj → Jharkhand | Sahibganj | p.39.  |
| SLP | FY2025-26 | Saraikela-Kharsawan → Jharkhand | Saraikela-Kharsawan | p.39.  |
| SLP | FY2025-26 | Simdega → Jharkhand | Simdega | p.39.  |
| SLP | FY2025-26 | West Singhbhum → Jharkhand | West Singhbhum | p.39.  |
| SLP | FY2025-26 | Bagalkot → Karnataka | Bagalkot | p.42.  |
| SLP | FY2025-26 | Bengaluru → Karnataka | Bengaluru | p.42.  |
| SLP | FY2025-26 | Bengaluru Rural → Karnataka | Bengaluru Rural | p.42.  |
| SLP | FY2025-26 | Davanagere → Karnataka | Davanagere | p.42.  |
| SLP | FY2025-26 | Gadag → Karnataka | Gadag | p.42.  |
| SLP | FY2025-26 | Hassan → Karnataka | Hassan | p.42.  |
| SLP | FY2025-26 | Kalaburagi → Karnataka | Kalaburagi | p.42.  |
| SLP | FY2025-26 | Koppal → Karnataka | Koppal | p.42.  |
| SLP | FY2025-26 | Mandya → Karnataka | Mandya | p.42.  |
| SLP | FY2025-26 | Mysuru → Karnataka | Mysuru | p.42.  |
| SLP | FY2025-26 | Ramanagara → Karnataka | Ramanagara | p.42.  |
| SLP | FY2025-26 | Kolar → Karnataka | Kolar | p.42. Case-study district; not in the chapter's district list. |
| SLP | FY2025-26 | Ernakulam → Kerala | Ernakulam | p.45.  |
| SLP | FY2025-26 | Kasaragod → Kerala | Kasaragod | p.45.  |
| SLP | FY2025-26 | Malappuram → Kerala | Malappuram | p.45.  |
| SLP | FY2025-26 | Thiruvananthapuram → Kerala | Thiruvananthapuram | p.45.  |
| SLP | FY2025-26 | Wayanad → Kerala | Wayanad | p.45.  |
| SLP | FY2025-26 | Kargil → Ladakh | Kargil | p.48.  |
| SLP | FY2025-26 | Leh → Ladakh | Leh | p.48.  |
| SLP | FY2025-26 | Alirajpur → Madhya Pradesh | Alirajpur | p.51.  |
| SLP | FY2025-26 | Anuppur → Madhya Pradesh | Anuppur | p.51.  |
| SLP | FY2025-26 | Barwani → Madhya Pradesh | Barwani | p.51.  |
| SLP | FY2025-26 | Betul → Madhya Pradesh | Betul | p.51.  |
| SLP | FY2025-26 | Bhopal → Madhya Pradesh | Bhopal | p.51.  |
| SLP | FY2025-26 | Chhatarpur → Madhya Pradesh | Chhatarpur | p.51.  |
| SLP | FY2025-26 | Damoh → Madhya Pradesh | Damoh | p.51.  |
| SLP | FY2025-26 | Dewas → Madhya Pradesh | Dewas | p.51.  |
| SLP | FY2025-26 | Dhar → Madhya Pradesh | Dhar | p.51.  |
| SLP | FY2025-26 | Dindori → Madhya Pradesh | Dindori | p.51.  |
| SLP | FY2025-26 | Guna → Madhya Pradesh | Guna | p.51.  |
| SLP | FY2025-26 | Gwalior → Madhya Pradesh | Gwalior | p.51.  |
| SLP | FY2025-26 | Jhabua → Madhya Pradesh | Jhabua | p.51.  |
| SLP | FY2025-26 | Katni → Madhya Pradesh | Katni | p.51.  |
| SLP | FY2025-26 | Khargone → Madhya Pradesh | Khargone | p.51.  |
| SLP | FY2025-26 | Maihar → Madhya Pradesh | Maihar | p.51.  |
| SLP | FY2025-26 | Mandla → Madhya Pradesh | Mandla | p.51.  |
| SLP | FY2025-26 | Niwari → Madhya Pradesh | Niwari | p.51.  |
| SLP | FY2025-26 | Panna → Madhya Pradesh | Panna | p.51.  |
| SLP | FY2025-26 | Rajgarh → Madhya Pradesh | Rajgarh | p.51.  |
| SLP | FY2025-26 | Ratlam → Madhya Pradesh | Ratlam | p.51.  |
| SLP | FY2025-26 | Rewa → Madhya Pradesh | Rewa | p.51.  |
| SLP | FY2025-26 | Sagar → Madhya Pradesh | Sagar | p.51.  |
| SLP | FY2025-26 | Satna → Madhya Pradesh | Satna | p.51.  |
| SLP | FY2025-26 | Sehore → Madhya Pradesh | Sehore | p.51.  |
| SLP | FY2025-26 | Shahdol → Madhya Pradesh | Shahdol | p.51.  |
| SLP | FY2025-26 | Shivpuri → Madhya Pradesh | Shivpuri | p.51.  |
| SLP | FY2025-26 | Singrauli → Madhya Pradesh | Singrauli | p.51.  |
| SLP | FY2025-26 | Tikamgarh → Madhya Pradesh | Tikamgarh | p.51.  |
| SLP | FY2025-26 | Umaria → Madhya Pradesh | Umaria | p.51.  |
| SLP | FY2025-26 | Ahilyanagar → Maharashtra | Ahilyanagar | p.54. Renamed from Ahmednagar (2024). |
| SLP | FY2025-26 | Akola → Maharashtra | Akola | p.54.  |
| SLP | FY2025-26 | Amravati → Maharashtra | Amravati | p.54.  |
| SLP | FY2025-26 | Beed → Maharashtra | Beed | p.54.  |
| SLP | FY2025-26 | Chandrapur → Maharashtra | Chandrapur | p.54.  |
| SLP | FY2025-26 | Dhule → Maharashtra | Dhule | p.54.  |
| SLP | FY2025-26 | Gadchiroli → Maharashtra | Gadchiroli | p.54.  |
| SLP | FY2025-26 | Gondia → Maharashtra | Gondia | p.54.  |
| SLP | FY2025-26 | Hingoli → Maharashtra | Hingoli | p.54.  |
| SLP | FY2025-26 | Jalgaon → Maharashtra | Jalgaon | p.54.  |
| SLP | FY2025-26 | Jalna → Maharashtra | Jalna | p.54.  |
| SLP | FY2025-26 | Kolhapur → Maharashtra | Kolhapur | p.54.  |
| SLP | FY2025-26 | Latur → Maharashtra | Latur | p.54.  |
| SLP | FY2025-26 | Mumbai → Maharashtra | Mumbai | p.54. Mumbai also houses ABF's registered office. |
| SLP | FY2025-26 | Nagpur → Maharashtra | Nagpur | p.54.  |
| SLP | FY2025-26 | Nanded → Maharashtra | Nanded | p.54.  |
| SLP | FY2025-26 | Nandurbar → Maharashtra | Nandurbar | p.54.  |
| SLP | FY2025-26 | Nashik → Maharashtra | Nashik | p.54.  |
| SLP | FY2025-26 | Parbhani → Maharashtra | Parbhani | p.54.  |
| SLP | FY2025-26 | Pune → Maharashtra | Pune | p.54.  |
| SLP | FY2025-26 | Ratnagiri → Maharashtra | Ratnagiri | p.54.  |
| SLP | FY2025-26 | Satara → Maharashtra | Satara | p.54.  |
| SLP | FY2025-26 | Thane → Maharashtra | Thane | p.54.  |
| SLP | FY2025-26 | Wardha → Maharashtra | Wardha | p.54.  |
| SLP | FY2025-26 | Washim → Maharashtra | Washim | p.54.  |
| SLP | FY2025-26 | Yavatmal → Maharashtra | Yavatmal | p.54.  |
| SLP | FY2025-26 | Angul → Odisha | Angul | p.59.  |
| SLP | FY2025-26 | Balangir → Odisha | Balangir | p.59.  |
| SLP | FY2025-26 | Bhubaneswar → Odisha | Bhubaneswar | p.59. A city, not a district. It is in Khordha district. |
| SLP | FY2025-26 | Ganjam → Odisha | Ganjam | p.59.  |
| SLP | FY2025-26 | Kalahandi → Odisha | Kalahandi | p.59.  |
| SLP | FY2025-26 | Kandhamal → Odisha | Kandhamal | p.59.  |
| SLP | FY2025-26 | Keonjhar → Odisha | Keonjhar | p.59.  |
| SLP | FY2025-26 | Koraput → Odisha | Koraput | p.59.  |
| SLP | FY2025-26 | Mayurbhanj → Odisha | Mayurbhanj | p.59.  |
| SLP | FY2025-26 | Nabarangpur → Odisha | Nabarangpur | p.59.  |
| SLP | FY2025-26 | Rayagada → Odisha | Rayagada | p.59.  |
| SLP | FY2025-26 | Subarnapur → Odisha | Subarnapur | p.59.  |
| SLP | FY2025-26 | Puducherry → Puducherry | Puducherry | p.61. UT district. |
| SLP | FY2025-26 | Ajmer → Rajasthan | Ajmer | p.63.  |
| SLP | FY2025-26 | Alwar → Rajasthan | Alwar | p.63.  |
| SLP | FY2025-26 | Anupgarh → Rajasthan | Anupgarh | p.63.  |
| SLP | FY2025-26 | Balotra → Rajasthan | Balotra | p.63.  |
| SLP | FY2025-26 | Banswara → Rajasthan | Banswara | p.63.  |
| SLP | FY2025-26 | Baran → Rajasthan | Baran | p.63.  |
| SLP | FY2025-26 | Barmer → Rajasthan | Barmer | p.63.  |
| SLP | FY2025-26 | Beawar → Rajasthan | Beawar | p.63.  |
| SLP | FY2025-26 | Bharatpur → Rajasthan | Bharatpur | p.63.  |
| SLP | FY2025-26 | Bhilwara → Rajasthan | Bhilwara | p.63.  |
| SLP | FY2025-26 | Bikaner → Rajasthan | Bikaner | p.63.  |
| SLP | FY2025-26 | Bundi → Rajasthan | Bundi | p.63.  |
| SLP | FY2025-26 | Chittorgarh → Rajasthan | Chittorgarh | p.63.  |
| SLP | FY2025-26 | Churu → Rajasthan | Churu | p.63.  |
| SLP | FY2025-26 | Dausa → Rajasthan | Dausa | p.63.  |
| SLP | FY2025-26 | Deeg → Rajasthan | Deeg | p.63.  |
| SLP | FY2025-26 | Dholpur → Rajasthan | Dholpur | p.63.  |
| SLP | FY2025-26 | Didwana-Kuchaman → Rajasthan | Didwana-Kuchaman | p.63.  |
| SLP | FY2025-26 | Dudu → Rajasthan | Dudu | p.63.  |
| SLP | FY2025-26 | Ganganagar → Rajasthan | Ganganagar | p.63.  |
| SLP | FY2025-26 | Gangapur City → Rajasthan | Gangapur City | p.63.  |
| SLP | FY2025-26 | Hanumangarh → Rajasthan | Hanumangarh | p.63.  |
| SLP | FY2025-26 | Jaipur → Rajasthan | Jaipur | p.63.  |
| SLP | FY2025-26 | Jaipur Rural → Rajasthan | Jaipur Rural | p.63.  |
| SLP | FY2025-26 | Jaisalmer → Rajasthan | Jaisalmer | p.63.  |
| SLP | FY2025-26 | Jalore → Rajasthan | Jalore | p.63.  |
| SLP | FY2025-26 | Jhalawar → Rajasthan | Jhalawar | p.63.  |
| SLP | FY2025-26 | Jhunjhunu → Rajasthan | Jhunjhunu | p.63.  |
| SLP | FY2025-26 | Jodhpur → Rajasthan | Jodhpur | p.63.  |
| SLP | FY2025-26 | Jodhpur Rural → Rajasthan | Jodhpur Rural | p.63.  |
| SLP | FY2025-26 | Karauli → Rajasthan | Karauli | p.63.  |
| SLP | FY2025-26 | Kekri → Rajasthan | Kekri | p.63.  |
| SLP | FY2025-26 | Khairthal-Tijara → Rajasthan | Khairthal-Tijara | p.63.  |
| SLP | FY2025-26 | Kota → Rajasthan | Kota | p.63.  |
| SLP | FY2025-26 | Kotputli-Behror → Rajasthan | Kotputli-Behror | p.63.  |
| SLP | FY2025-26 | Nagaur → Rajasthan | Nagaur | p.63.  |
| SLP | FY2025-26 | Neem Ka Thana → Rajasthan | Neem Ka Thana | p.63.  |
| SLP | FY2025-26 | Pali → Rajasthan | Pali | p.63.  |
| SLP | FY2025-26 | Phalodi → Rajasthan | Phalodi | p.63.  |
| SLP | FY2025-26 | Pratapgarh → Rajasthan | Pratapgarh | p.63.  |
| SLP | FY2025-26 | Rajsamand → Rajasthan | Rajsamand | p.63.  |
| SLP | FY2025-26 | Salumbar → Rajasthan | Salumbar | p.63.  |
| SLP | FY2025-26 | Sanchore → Rajasthan | Sanchore | p.63.  |
| SLP | FY2025-26 | Sawai Madhopur → Rajasthan | Sawai Madhopur | p.63.  |
| SLP | FY2025-26 | Shahpura → Rajasthan | Shahpura | p.63.  |
| SLP | FY2025-26 | Sikar → Rajasthan | Sikar | p.63.  |
| SLP | FY2025-26 | Sirohi → Rajasthan | Sirohi | p.63.  |
| SLP | FY2025-26 | Tonk → Rajasthan | Tonk | p.63.  |
| SLP | FY2025-26 | Udaipur → Rajasthan | Udaipur | p.63.  |
| SLP | FY2025-26 | Ariyalur → Tamil Nadu | Ariyalur | p.65.  |
| SLP | FY2025-26 | Chennai → Tamil Nadu | Chennai | p.65. Urban district. |
| SLP | FY2025-26 | Coimbatore → Tamil Nadu | Coimbatore | p.65.  |
| SLP | FY2025-26 | Dharmapuri → Tamil Nadu | Dharmapuri | p.65.  |
| SLP | FY2025-26 | Dindigul → Tamil Nadu | Dindigul | p.65.  |
| SLP | FY2025-26 | Erode → Tamil Nadu | Erode | p.65.  |
| SLP | FY2025-26 | Kanchipuram → Tamil Nadu | Kanchipuram | p.65.  |
| SLP | FY2025-26 | Madurai → Tamil Nadu | Madurai | p.65.  |
| SLP | FY2025-26 | Namakkal → Tamil Nadu | Namakkal | p.65.  |
| SLP | FY2025-26 | Pudukkottai → Tamil Nadu | Pudukkottai | p.65.  |
| SLP | FY2025-26 | Ramanathapuram → Tamil Nadu | Ramanathapuram | p.65.  |
| SLP | FY2025-26 | Salem → Tamil Nadu | Salem | p.65.  |
| SLP | FY2025-26 | Sivagangai → Tamil Nadu | Sivagangai | p.65.  |
| SLP | FY2025-26 | Tiruchirappalli → Tamil Nadu | Tiruchirappalli | p.65.  |
| SLP | FY2025-26 | Tiruvallur → Tamil Nadu | Tiruvallur | p.65.  |
| SLP | FY2025-26 | Vellore → Tamil Nadu | Vellore | p.65.  |
| SLP | FY2025-26 | Virudhunagar → Tamil Nadu | Virudhunagar | p.65.  |
| SLP | FY2025-26 | Hyderabad → Telangana | Hyderabad | p.67. Urban district. |
| SLP | FY2025-26 | Khammam → Telangana | Khammam | p.67.  |
| SLP | FY2025-26 | Mahabubnagar → Telangana | Mahabubnagar | p.67.  |
| SLP | FY2025-26 | Medchal → Telangana | Medchal | p.67.  |
| SLP | FY2025-26 | Narayanpet → Telangana | Narayanpet | p.67.  |
| SLP | FY2025-26 | Vikarabad → Telangana | Vikarabad | p.67.  |
| SLP | FY2025-26 | Agra → Uttar Pradesh | Agra | p.69.  |
| SLP | FY2025-26 | Aligarh → Uttar Pradesh | Aligarh | p.69.  |
| SLP | FY2025-26 | Azamgarh → Uttar Pradesh | Azamgarh | p.69.  |
| SLP | FY2025-26 | Bahraich → Uttar Pradesh | Bahraich | p.69.  |
| SLP | FY2025-26 | Banda → Uttar Pradesh | Banda | p.69.  |
| SLP | FY2025-26 | Barabanki → Uttar Pradesh | Barabanki | p.69.  |
| SLP | FY2025-26 | Basti → Uttar Pradesh | Basti | p.69.  |
| SLP | FY2025-26 | Bhadohi → Uttar Pradesh | Bhadohi | p.69.  |
| SLP | FY2025-26 | Bulandshahr → Uttar Pradesh | Bulandshahr | p.69.  |
| SLP | FY2025-26 | Chitrakoot → Uttar Pradesh | Chitrakoot | p.69.  |
| SLP | FY2025-26 | Etawah → Uttar Pradesh | Etawah | p.69.  |
| SLP | FY2025-26 | Gautam Buddha Nagar → Uttar Pradesh | Gautam Buddha Nagar | p.69.  |
| SLP | FY2025-26 | Ghaziabad → Uttar Pradesh | Ghaziabad | p.69.  |
| SLP | FY2025-26 | Gonda → Uttar Pradesh | Gonda | p.69.  |
| SLP | FY2025-26 | Gorakhpur → Uttar Pradesh | Gorakhpur | p.69.  |
| SLP | FY2025-26 | Hamirpur → Uttar Pradesh | Hamirpur | p.69.  |
| SLP | FY2025-26 | Jhansi → Uttar Pradesh | Jhansi | p.69.  |
| SLP | FY2025-26 | Kanpur → Uttar Pradesh | Kanpur | p.69.  |
| SLP | FY2025-26 | Kanpur Dehat → Uttar Pradesh | Kanpur Dehat | p.69.  |
| SLP | FY2025-26 | Lucknow → Uttar Pradesh | Lucknow | p.69.  |
| SLP | FY2025-26 | Maharajganj → Uttar Pradesh | Maharajganj | p.69.  |
| SLP | FY2025-26 | Meerut → Uttar Pradesh | Meerut | p.69.  |
| SLP | FY2025-26 | Mirzapur → Uttar Pradesh | Mirzapur | p.69.  |
| SLP | FY2025-26 | Prayagraj → Uttar Pradesh | Prayagraj | p.69.  |
| SLP | FY2025-26 | Raebareli → Uttar Pradesh | Raebareli | p.69.  |
| SLP | FY2025-26 | Samali → Uttar Pradesh | Samali | p.69. Printed "Samali", most likely Shamli district (sic). |
| SLP | FY2025-26 | Shahjahanpur → Uttar Pradesh | Shahjahanpur | p.69.  |
| SLP | FY2025-26 | Sitapur → Uttar Pradesh | Sitapur | p.69.  |
| SLP | FY2025-26 | Sonbhadra → Uttar Pradesh | Sonbhadra | p.69.  |
| SLP | FY2025-26 | Sultanpur → Uttar Pradesh | Sultanpur | p.69.  |
| SLP | FY2025-26 | Unnao → Uttar Pradesh | Unnao | p.69.  |
| SLP | FY2025-26 | Varanasi → Uttar Pradesh | Varanasi | p.69.  |
| SLP | FY2025-26 | Bageshwar → Uttarakhand | Bageshwar | p.72.  |
| SLP | FY2025-26 | Chamoli → Uttarakhand | Chamoli | p.72.  |
| SLP | FY2025-26 | Dehradun → Uttarakhand | Dehradun | p.72.  |
| SLP | FY2025-26 | Nainital → Uttarakhand | Nainital | p.72.  |
| SLP | FY2025-26 | Pauri Garhwal → Uttarakhand | Pauri Garhwal | p.72.  |
| SLP | FY2025-26 | Pithoragarh → Uttarakhand | Pithoragarh | p.72.  |
| SLP | FY2025-26 | Tehri Garhwal → Uttarakhand | Tehri Garhwal | p.72.  |
| SLP | FY2025-26 | Uttarkashi → Uttarakhand | Uttarkashi | p.72.  |
| SLP | FY2025-26 | Bankura → West Bengal | Bankura | p.74.  |
| SLP | FY2025-26 | Birbhum → West Bengal | Birbhum | p.74.  |
| SLP | FY2025-26 | Cooch Behar → West Bengal | Cooch Behar | p.74.  |
| SLP | FY2025-26 | Darjeeling → West Bengal | Darjeeling | p.74.  |
| SLP | FY2025-26 | Jalpaiguri → West Bengal | Jalpaiguri | p.74.  |
| SLP | FY2025-26 | Jhargram → West Bengal | Jhargram | p.74.  |
| SLP | FY2025-26 | Kalimpong → West Bengal | Kalimpong | p.74.  |
| SLP | FY2025-26 | Kolkata → West Bengal | Kolkata | p.74. Urban district. |
| SLP | FY2025-26 | North 24 Parganas → West Bengal | North 24 Parganas | p.74.  |
| SLP | FY2025-26 | Purulia → West Bengal | Purulia | p.74.  |
| SLP | FY2025-26 | South 24 Parganas → West Bengal | South 24 Parganas | p.74.  |
| SLP | FY2025-26 | Barpeta → Assam | Barpeta | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Cachar → Assam | Cachar | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Dhemaji → Assam | Dhemaji | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Goalpara → Assam | Goalpara | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Guwahati → Assam | Guwahati | p.56. The report prints one NE-wide list; we assigned the state. A city. It is in Kamrup Metropolitan, which is also listed. |
| SLP | FY2025-26 | Jorhat → Assam | Jorhat | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Kamrup → Assam | Kamrup | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Kamrup Metropolitan → Assam | Kamrup Metropolitan | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Kokrajhar → Assam | Kokrajhar | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Majuli → Assam | Majuli | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Nalbari → Assam | Nalbari | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Tinsukia → Assam | Tinsukia | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | East Garo Hills → Meghalaya | East Garo Hills | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | East Jaintia Hills → Meghalaya | East Jaintia Hills | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | East Khasi Hills → Meghalaya | East Khasi Hills | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Eastern West Khasi Hills → Meghalaya | Eastern West Khasi Hills | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | North Garo Hills → Meghalaya | North Garo Hills | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Ri Bhoi → Meghalaya | Ri Bhoi | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | South Garo Hills → Meghalaya | South Garo Hills | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | South West Garo Hills → Meghalaya | South West Garo Hills | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | South West Khasi Hills → Meghalaya | South West Khasi Hills | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | West Garo Hills → Meghalaya | West Garo Hills | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | West Jaintia Hills → Meghalaya | West Jaintia Hills | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | West Khasi Hills → Meghalaya | West Khasi Hills | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Chumukedima → Nagaland | Chumukedima | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Kiphire → Nagaland | Kiphire | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Longleng → Nagaland | Longleng | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Mokokchung → Nagaland | Mokokchung | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Mon → Nagaland | Mon | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Noklak → Nagaland | Noklak | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Nuiland → Nagaland | Nuiland | p.56. The report prints one NE-wide list; we assigned the state. Printed "Nuiland". LGD: Niuland. |
| SLP | FY2025-26 | Peren → Nagaland | Peren | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Phek → Nagaland | Phek | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Shamator → Nagaland | Shamator | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Tseminyu → Nagaland | Tseminyu | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Tuensang → Nagaland | Tuensang | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Aizawl → Mizoram | Aizawl | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Champhai → Mizoram | Champhai | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Lunglei → Mizoram | Lunglei | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Mamit → Mizoram | Mamit | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Serchhip → Mizoram | Serchhip | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Bishnupur → Manipur | Bishnupur | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Churachandpur → Manipur | Churachandpur | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Jiribam → Manipur | Jiribam | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Tamenglong → Manipur | Tamenglong | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Dhalai → Tripura | Dhalai | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Gomati → Tripura | Gomati | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | West Tripura → Tripura | West Tripura | p.56. The report prints one NE-wide list; we assigned the state.  |
| SLP | FY2025-26 | Changlang → Arunachal Pradesh | Changlang | p.56. The report prints one NE-wide list; we assigned the state.  |

*373 district rows.*

#### (c) Block level — from named case studies

| program | fiscal_year | location (block → district → state) | name_as_printed | notes |
|---|---|---|---|---|
| SLP | FY2025-26 | Gandlapenta → Sri Sathya Sai → Andhra Pradesh | Gandlapenta | p.22, case study "Strengthening Stewardship of Commons for Resilient & Diversified Livelihoods in Andhra Pradesh"; partner: not named in case study. |
| SLP | FY2025-26 | Talupula → Sri Sathya Sai → Andhra Pradesh | Talupula | p.22, case study "Strengthening Stewardship of Commons for Resilient & Diversified Livelihoods in Andhra Pradesh"; partner: not named in case study. |
| SLP | FY2025-26 | Bankey Bazar → Gaya → Bihar | Bankey Bazar | p.24, case study "When the most disadvantaged households started buying together"; partner: not named in case study. |
| SLP | FY2025-26 | Imamganj → Gaya → Bihar | Imamganj | p.24, case study "When the most disadvantaged households started buying together"; partner: not named in case study. |
| SLP | FY2025-26 | Godhra → Panchmahal → Gujarat | Godhra | p.31, case study "From Seasonal Water Availability to Year-Round Livelihoods"; partner: N. M. Sadguru Water and Development Foundation. |
| SLP | FY2025-26 | Ghoghamba → Panchmahal → Gujarat | Ghoghamba | p.31, case study "From Seasonal Water Availability to Year-Round Livelihoods"; partner: N. M. Sadguru Water and Development Foundation. |
| SLP | FY2025-26 | Morwa Hadaf → Panchmahal → Gujarat | Morwa Hadaf | p.31, case study "From Seasonal Water Availability to Year-Round Livelihoods"; partner: N. M. Sadguru Water and Development Foundation. |
| SLP | FY2025-26 | Baijnath → Kangra → Himachal Pradesh | Baijnath | p.35, case study "Making Small Mountain Farms Economically Viable"; partner: Himmotthan Society. |
| SLP | FY2025-26 | Nadaun → Hamirpur → Himachal Pradesh | Nadaun | p.35, case study "Making Small Mountain Farms Economically Viable"; partner: Himmotthan Society. |
| SLP | FY2025-26 | Khunti Sadar → Khunti → Jharkhand | Khunti Sadar | p.39, case study "Building Healthy Futures Through Community-Led Action"; partner: Child In Need Institute. |
| SLP | FY2025-26 | Murhu → Khunti → Jharkhand | Murhu | p.39, case study "Building Healthy Futures Through Community-Led Action"; partner: Child In Need Institute. |
| SLP | FY2025-26 | Erki (Tamar II) → Ranchi *(printed under 'Khunti and Dumka districts'; Erki/Tamar II is a Ranchi-district block — check)* → Jharkhand | Erki (Tamar II) | p.39, case study "Building Healthy Futures Through Community-Led Action"; partner: Child In Need Institute. |
| SLP | FY2025-26 | Gopikandar → Dumka → Jharkhand | Gopikandar | p.39, case study "Building Healthy Futures Through Community-Led Action"; partner: Child In Need Institute. |
| SLP | FY2025-26 | Shikaripara → Dumka → Jharkhand | Shikaripara | p.39, case study "Building Healthy Futures Through Community-Led Action"; partner: Child In Need Institute. |
| SLP | FY2025-26 | Nilambur → Malappuram → Kerala | Nilambur | p.45, case study "From Ecological Restoration to Community-Owned Collectives"; partner: Keystone Foundation. |
| SLP | FY2025-26 | Mananthawadi → Wayanad → Kerala | Mananthawadi | p.45, case study "From Ecological Restoration to Community-Owned Collectives"; partner: Keystone Foundation. |
| SLP | FY2025-26 | Chiktan → Leh/Kargil (district per block not printed) → Ladakh | Chiktan | p.48, case study "Building a Resilient Apricot Value Chain in Ladakh"; partner: Himmotthan Society. |
| SLP | FY2025-26 | Chuchot → Leh/Kargil (district per block not printed) → Ladakh | Chuchot | p.48, case study "Building a Resilient Apricot Value Chain in Ladakh"; partner: Himmotthan Society. |
| SLP | FY2025-26 | Durbuk → Leh/Kargil (district per block not printed) → Ladakh | Durbuk | p.48, case study "Building a Resilient Apricot Value Chain in Ladakh"; partner: Himmotthan Society. |
| SLP | FY2025-26 | Khaltsi → Leh/Kargil (district per block not printed) → Ladakh | Khaltsi | p.48, case study "Building a Resilient Apricot Value Chain in Ladakh"; partner: Himmotthan Society. |
| SLP | FY2025-26 | Kharu → Leh/Kargil (district per block not printed) → Ladakh | Kharu | p.48, case study "Building a Resilient Apricot Value Chain in Ladakh"; partner: Himmotthan Society. |
| SLP | FY2025-26 | Leh → Leh/Kargil (district per block not printed) → Ladakh | Leh | p.48, case study "Building a Resilient Apricot Value Chain in Ladakh"; partner: Himmotthan Society. |
| SLP | FY2025-26 | Nyoma → Leh/Kargil (district per block not printed) → Ladakh | Nyoma | p.48, case study "Building a Resilient Apricot Value Chain in Ladakh"; partner: Himmotthan Society. |
| SLP | FY2025-26 | Rong Chugut → Leh/Kargil (district per block not printed) → Ladakh | Rong Chugut | p.48, case study "Building a Resilient Apricot Value Chain in Ladakh"; partner: Himmotthan Society. |
| SLP | FY2025-26 | Saspol → Leh/Kargil (district per block not printed) → Ladakh | Saspol | p.48, case study "Building a Resilient Apricot Value Chain in Ladakh"; partner: Himmotthan Society. |
| SLP | FY2025-26 | Skurbuchan → Leh/Kargil (district per block not printed) → Ladakh | Skurbuchan | p.48, case study "Building a Resilient Apricot Value Chain in Ladakh"; partner: Himmotthan Society. |
| SLP | FY2025-26 | Sodh → Leh/Kargil (district per block not printed) → Ladakh | Sodh | p.48, case study "Building a Resilient Apricot Value Chain in Ladakh"; partner: Himmotthan Society. |
| SLP | FY2025-26 | Thiksay → Leh/Kargil (district per block not printed) → Ladakh | Thiksay | p.48, case study "Building a Resilient Apricot Value Chain in Ladakh"; partner: Himmotthan Society. |
| SLP | FY2025-26 | Amarpur → Betul/Dindori/Mandla/Shahdol/Singrauli (per-block district not printed) → Madhya Pradesh | Amarpur | p.51, case study "Women's Collectives at the Centre of a Rural Poultry Economy"; partner: Professional Assistance for Development Action. |
| SLP | FY2025-26 | Deosar → Betul/Dindori/Mandla/Shahdol/Singrauli (per-block district not printed) → Madhya Pradesh | Deosar | p.51, case study "Women's Collectives at the Centre of a Rural Poultry Economy"; partner: Professional Assistance for Development Action. |
| SLP | FY2025-26 | Ghoda Dongari → Betul/Dindori/Mandla/Shahdol/Singrauli (per-block district not printed) → Madhya Pradesh | Ghoda Dongari | p.51, case study "Women's Collectives at the Centre of a Rural Poultry Economy"; partner: Professional Assistance for Development Action. |
| SLP | FY2025-26 | Jaisinghnagar → Betul/Dindori/Mandla/Shahdol/Singrauli (per-block district not printed) → Madhya Pradesh | Jaisinghnagar | p.51, case study "Women's Collectives at the Centre of a Rural Poultry Economy"; partner: Professional Assistance for Development Action. |
| SLP | FY2025-26 | Mohgaon → Betul/Dindori/Mandla/Shahdol/Singrauli (per-block district not printed) → Madhya Pradesh | Mohgaon | p.51, case study "Women's Collectives at the Centre of a Rural Poultry Economy"; partner: Professional Assistance for Development Action. |
| SLP | FY2025-26 | Narayanganj → Betul/Dindori/Mandla/Shahdol/Singrauli (per-block district not printed) → Madhya Pradesh | Narayanganj | p.51, case study "Women's Collectives at the Centre of a Rural Poultry Economy"; partner: Professional Assistance for Development Action. |
| SLP | FY2025-26 | Samnapur → Betul/Dindori/Mandla/Shahdol/Singrauli (per-block district not printed) → Madhya Pradesh | Samnapur | p.51, case study "Women's Collectives at the Centre of a Rural Poultry Economy"; partner: Professional Assistance for Development Action. |
| SLP | FY2025-26 | Shahpur → Betul/Dindori/Mandla/Shahdol/Singrauli (per-block district not printed) → Madhya Pradesh | Shahpur | p.51, case study "Women's Collectives at the Centre of a Rural Poultry Economy"; partner: Professional Assistance for Development Action. |
| SLP | FY2025-26 | Akkalkuwa → Nandurbar/Dhule → Maharashtra | Akkalkuwa | p.54, case study "Stabilising Livelihoods in a Water-Stressed Landscape"; partner: Development Support Centre (DSC). |
| SLP | FY2025-26 | Dhadgaon → Nandurbar/Dhule → Maharashtra | Dhadgaon | p.54, case study "Stabilising Livelihoods in a Water-Stressed Landscape"; partner: Development Support Centre (DSC). |
| SLP | FY2025-26 | Dhule → Nandurbar/Dhule → Maharashtra | Dhule | p.54, case study "Stabilising Livelihoods in a Water-Stressed Landscape"; partner: Development Support Centre (DSC). |
| SLP | FY2025-26 | Nandurbar → Nandurbar/Dhule → Maharashtra | Nandurbar | p.54, case study "Stabilising Livelihoods in a Water-Stressed Landscape"; partner: Development Support Centre (DSC). |
| SLP | FY2025-26 | Navapur → Nandurbar/Dhule → Maharashtra | Navapur | p.54, case study "Stabilising Livelihoods in a Water-Stressed Landscape"; partner: Development Support Centre (DSC). |
| SLP | FY2025-26 | Sakri → Nandurbar/Dhule → Maharashtra | Sakri | p.54, case study "Stabilising Livelihoods in a Water-Stressed Landscape"; partner: Development Support Centre (DSC). |
| SLP | FY2025-26 | Shahada → Nandurbar/Dhule → Maharashtra | Shahada | p.54, case study "Stabilising Livelihoods in a Water-Stressed Landscape"; partner: Development Support Centre (DSC). |
| SLP | FY2025-26 | Sindkheda → Nandurbar/Dhule → Maharashtra | Sindkheda | p.54, case study "Stabilising Livelihoods in a Water-Stressed Landscape"; partner: Development Support Centre (DSC). |
| SLP | FY2025-26 | Nettapakkam → Puducherry → Puducherry | Nettapakkam | p.61, case study "(PwD livelihoods)"; partner: Enable India. |
| SLP | FY2025-26 | Puducherry commune → Puducherry → Puducherry | Puducherry commune | p.61, case study "(PwD livelihoods)"; partner: Enable India. |
| SLP | FY2025-26 | Bari → Dholpur/Baran → Rajasthan | Bari | p.63, case study "From Producers to Market Leaders"; partner: Manjari Foundation. |
| SLP | FY2025-26 | Baseri → Dholpur/Baran → Rajasthan | Baseri | p.63, case study "From Producers to Market Leaders"; partner: Manjari Foundation. |
| SLP | FY2025-26 | Dholpur → Dholpur/Baran → Rajasthan | Dholpur | p.63, case study "From Producers to Market Leaders"; partner: Manjari Foundation. |
| SLP | FY2025-26 | Kishanganj → Dholpur/Baran → Rajasthan | Kishanganj | p.63, case study "From Producers to Market Leaders"; partner: Manjari Foundation. |
| SLP | FY2025-26 | Saipau → Dholpur/Baran → Rajasthan | Saipau | p.63, case study "From Producers to Market Leaders"; partner: Manjari Foundation. |
| SLP | FY2025-26 | Damargidda → Narayanpet → Telangana | Damargidda | p.67, case study "Keeping livelihoods rooted in Drylands"; partner: Watershed Organisation Trust. |
| SLP | FY2025-26 | Maddur → Narayanpet → Telangana | Maddur | p.67, case study "Keeping livelihoods rooted in Drylands"; partner: Watershed Organisation Trust. |
| SLP | FY2025-26 | Fatehpur → Barabanki → Uttar Pradesh | Fatehpur | p.69, case study "Building Institutions that Represent Landless and Most Disadvantaged Families"; partner: Trust Community Livelihoods (TCL). |
| SLP | FY2025-26 | Suratganj → Barabanki → Uttar Pradesh | Suratganj | p.69, case study "Building Institutions that Represent Landless and Most Disadvantaged Families"; partner: Trust Community Livelihoods (TCL). |
| SLP | FY2025-26 | Nichlaul → Maharajganj → Uttar Pradesh | Nichlaul | p.69, case study "Building Institutions that Represent Landless and Most Disadvantaged Families"; partner: Trust Community Livelihoods (TCL). |
| SLP | FY2025-26 | Narayanbagar → Chamoli → Uttarakhand | Narayanbagar | p.72, case study "Building the Next Generation of Development Leaders"; partner: People's Science Institute. |
| SLP | FY2025-26 | Tharali → Chamoli → Uttarakhand | Tharali | p.72, case study "Building the Next Generation of Development Leaders"; partner: People's Science Institute. |
| SLP | FY2025-26 | Banarhat → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Banarhat | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Basanti → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Basanti | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Garubathan → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Garubathan | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Gosaba → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Gosaba | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Hingalganj → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Hingalganj | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | JB Sukhiyapokhri → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | JB Sukhiyapokhri | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Kalimpong I → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Kalimpong I | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Khoyrasole → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Khoyrasole | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Kranti → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Kranti | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Lava → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Lava | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Mal → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Mal | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Matiali → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Matiali | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Nagrakata → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Nagrakata | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Patharpratima → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Patharpratima | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Pedong → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Pedong | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Rajnagar → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Rajnagar | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Rangli Rangliot → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Rangli Rangliot | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Sandeshkhali II → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Sandeshkhali II | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |
| SLP | FY2025-26 | Suri I → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Suri I | p.74, case study "Looking Beyond the Spring"; partner: Rajarhat Prasari. |

*77 block rows.* Blocks mentioned only as counts (Odisha 14, Tamil Nadu 12, Chhattisgarh 34) cannot be loaded because they aren't named.

**Removed:** all 6 bank-CSR-theme district-list sections (Education/Environmental Sustainability-as-bank-theme/Financial Inclusion/Health & Nutrition/Sports/Humanitarian & Relief) sourced from the Bank's CSR Impact Report — out of scope. The Heart Surgeries, Mid-Day Meal, and Axis DilSe rows are removed (bank-direct, not ABF).
**Removed:** the (Historical, ~2015) row and the Gujarat/Dahod `funds` row in their old form — both superseded by the corrected, better-evidenced rows above.

---
---

**Partners named (`funder_partners`)**

*Full lists from ABF's own "Programme Partners" pages. `partner_canonical` added; `partner_csr1` — not found for any partner. Company co-funders kept separate from NGO implementing partners.*

### FY2025-26 — `funder_partners` rows (ABF AR2025-26)

*`fiscal_year` = FY2025-26 on every row. Source columns: `source_url` = https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf · `source_name` = ABF Annual Report 2025-26 · `fetched_at` = 2026-09-29 · `as_of` = FY2025-26 · `archive_url` = Not found. `partner_csr1` is not printed for any partner. `org_id` / `partner_funder_id` are Links, to be set when the registry has these rows. "States (since)" comes from the state chapters, pp.22–75; the "since" year is **per state**, so one partner can have different years in different states.*

#### (a) Sustainable Livelihood Programme partners — 47, as printed on p.84

| # | partner_name (as printed) | partner_canonical | partner_kind | program | notes: states (since) |
|---|---|---|---|---|---|
| 1 | Action for Social Advancement | Action for Social Advancement | ngo | Sustainable Livelihood Programme | Madhya Pradesh (since 2017). |
| 2 | Aga Khan Rural Support Programme (India) | AKRSP (India) | ngo | Sustainable Livelihood Programme | Bihar (since 2018); Gujarat (since 2013); Maharashtra (since 2023). |
| 3 | Agri Entrepreneur Growth Foundation | Agri Entrepreneur Growth Foundation (AEGF) | ngo | Sustainable Livelihood Programme | Maharashtra (since 2022); Madhya Pradesh (since 2025). |
| 4 | Ambuja Foundation | Ambuja Foundation | foundation | Sustainable Livelihood Programme | Gujarat (since 2025). **New vs FY2024-25.** |
| 5 | BAIF Institute for Sustainable Livelihoods and Development | BAIF | ngo | Sustainable Livelihood Programme | Maharashtra (since 2025). |
| 6 | Bharat Rural Livelihoods Foundation | BRLF | ngo | Sustainable Livelihood Programme | Chhattisgarh (since 2018); Maharashtra (since 2023). |
| 7 | Bright Future India | Bright Future India | ngo | Skill Development | Maharashtra (since 2023). **New vs FY2024-25.** |
| 8 | Center for Advanced Research and Development | Centre for Advanced Research and Development (CARD) | ngo | Sustainable Livelihood Programme | Madhya Pradesh (since 2024). |
| 9 | Centre for Youth and Social Development | CYSD | ngo | Sustainable Livelihood Programme | Odisha (since 2024). |
| 10 | Child In Need Institute | CINI | ngo | Sustainable Livelihood Programme | Jharkhand (since 2023); Odisha (since 2023); West Bengal (since 2023). |
| 11 | Collectives for Integrated Livelihood Initiatives | CInI | ngo | Sustainable Livelihood Programme | Odisha (since 2023). |
| 12 | Contact Base | Contact Base | ngo | Sustainable Livelihood Programme | Jharkhand (since 2025); Odisha (since 2025). |
| 13 | Development of Humane Action Foundation | DHAN Foundation | ngo | Sustainable Livelihood Programme | Andhra Pradesh (since 2024); Bihar (since 2024); Tamil Nadu (since 2024). |
| 14 | Development Support Centre | Development Support Centre (DSC) | ngo | Sustainable Livelihood Programme | Gujarat (since 2022); Maharashtra (since 2018). |
| 15 | DHAN Vayalagam Tank Foundation | Dhan Vayalagam Tank Foundation (DVTF) | ngo | Sustainable Livelihood Programme | Tamil Nadu (since 2011). |
| 16 | Eleutheros Christian Society | Eleutheros Christian Society | ngo | Sustainable Livelihood Programme | NE — Eastern Nagaland (Jhum transition) (since 2024). |
| 17 | Enable India | Enable India | ngo | Skill Development | Andhra Pradesh (since 2024); Jammu and Kashmir (since 2024); Karnataka (since 2024); Kerala (since 2024); Madhya Pradesh (since 2024); Maharashtra (since 2024); Puducherry (since 2024); Tamil Nadu (since 2024); Telangana (since 2024); Uttar Pradesh (since 2024); NE — NE, state not specified (PwD) (since 2024). |
| 18 | Foundation for Ecological Security | FES | ngo | Sustainable Livelihood Programme | Andhra Pradesh (since 2024); Chhattisgarh (since 2022); Madhya Pradesh (since 2024); Maharashtra (since 2022); Odisha (since 2022); Rajasthan (since 2014); NE — Meghalaya (community forest conservation / PES) (since 2023). |
| 19 | Generation India Foundation | Generation India Foundation | ngo | Skill Development | Andhra Pradesh (since 2023); Bihar (since 2023); Delhi (since 2023); Gujarat (since-year not printed); Himachal Pradesh (since 2025); Jammu and Kashmir (since 2025); Jharkhand (since 2025); Karnataka (since 2023); Kerala (since 2023); Madhya Pradesh (since 2023); Maharashtra (since 2025); Rajasthan (since 2025); Tamil Nadu (since 2025); Uttar Pradesh (since 2023); West Bengal (since 2023); NE — NE, state not specified (skilling) (since 2025). |
| 20 | Gram Vikas | Gram Vikas | ngo | Sustainable Livelihood Programme | Odisha (since 2022). |
| 21 | Harsha Trust | Harsha Trust | ngo | Sustainable Livelihood Programme | Odisha (since 2012). |
| 22 | Himmotthan Society | Himmotthan Society | ngo | Sustainable Livelihood Programme | Himachal Pradesh (since 2024); Ladakh (since 2024); Uttarakhand (since 2024). |
| 23 | Ibtada | Ibtada | ngo | Sustainable Livelihood Programme | Rajasthan (since 2019); Uttar Pradesh (since 2024). |
| 24 | Industree Foundation | Industree Foundation | ngo | Sustainable Livelihood Programme | Karnataka: supports Creative Dignity (since 2024), p.42. **New vs FY2024-25.** |
| 25 | Keystone Foundation | Keystone Foundation | ngo | Sustainable Livelihood Programme | Kerala (since 2019). |
| 26 | Manjari Foundation | Manjari Foundation | ngo | Sustainable Livelihood Programme | Rajasthan (since 2025). |
| 27 | Medha Learning Foundation | Medha Learning Foundation | ngo | Skill Development | Bihar (since 2022); Haryana (since 2022); Uttar Pradesh (since 2022). |
| 28 | Navinchandra Mafatlal Sadguru Water and Development Foundation | N M Sadguru Water and Development Foundation | ngo | Sustainable Livelihood Programme | Gujarat (since 2014); Rajasthan (since 2014). |
| 29 | North East Initiative Development Agency | NEIDA | ngo | Sustainable Livelihood Programme | NE — Nagaland & Mizoram (since 2023). |
| 30 | People's Science Institute | People's Science Institute | ngo | Sustainable Livelihood Programme | Madhya Pradesh (since 2025); Uttarakhand (since 2025). **New vs FY2024-25.** |
| 31 | Professional Assistance for Development Action | PRADAN | ngo | Sustainable Livelihood Programme | Bihar (since 2022); Chhattisgarh (since 2011); Jharkhand (since 2019); Madhya Pradesh (since 2011); Odisha (since 2022); West Bengal (since 2022). |
| 32 | Rajarhat Prasari | Rajarhat Prasari | ngo | Sustainable Livelihood Programme | West Bengal (since 2022); NE — Meghalaya (springshed & watershed) (since-year not printed). |
| 33 | Samaj Pragati Sahayog | Samaj Pragati Sahayog (SPS) | ngo | Sustainable Livelihood Programme | Madhya Pradesh (since 2011); Maharashtra (since 2017). |
| 34 | Sarv Seva Samity Sanstha | Sarva Seva Samity Sanstha (4S) | ngo | Sustainable Livelihood Programme | Bihar (since 2022). |
| 35 | SELCO Foundation | SELCO Foundation | ngo | Sustainable Livelihood Programme | NE — Assam, Meghalaya & Manipur (decentralised renewable energy) (since 2023). |
| 36 | Self Reliant Initiatives through Joint Action | SRIJAN | ngo | Sustainable Livelihood Programme | Madhya Pradesh (since 2015); Rajasthan (since 2015). |
| 37 | Seva Mandir | Seva Mandir | ngo | Sustainable Livelihood Programme | Rajasthan (since 2019). |
| 38 | Seven Sisters Development Assistance | SeSTA | ngo | Ecosystem Action + Rural Livelihoods | NE — Assam (household livelihood planning); also runs NoDE (since 2024) with ABF (since 2023). |
| 39 | Shroffs Foundation Trust | Shroffs Foundation Trust | ngo | Sustainable Livelihood Programme | Gujarat (since 2024). |
| 40 | Swayam Shikshan Prayog | Swayam Shikshan Prayog (SSP) | ngo | Sustainable Livelihood Programme | Maharashtra (since 2024). |
| 41 | Transform Rural India Foundation | Transform Rural India Foundation (TRIF) | ngo | Sustainable Livelihood Programme | Chhattisgarh (since 2022); Jharkhand (since 2022); Madhya Pradesh (since 2024); Uttar Pradesh (since 2024). |
| 42 | Trust Community Livelihoods | Trust Community Livelihoods (TCL) | ngo | Sustainable Livelihood Programme | Uttar Pradesh (since 2023). |
| 43 | Trust for Retailers and Retail Associates of India | TRRAIN | ngo | Skill Development | Karnataka (since 2023); Kerala (since 2023); Uttar Pradesh (since 2023). |
| 44 | Udyogini | Udyogini | ngo | Sustainable Livelihood Programme | Chhattisgarh (since 2025); Madhya Pradesh (since 2025); NE — NE, state not specified (vocational/self-employment) (since 2025). **New vs FY2024-25.** |
| 45 | Voluntary Association for Agricultural General Development, Health and Reconstruction Alliance | VAAGDHARA | ngo | Sustainable Livelihood Programme | Madhya Pradesh (since 2024). |
| 46 | Watershed Organisation Trust | WOTR | ngo | Sustainable Livelihood Programme | Maharashtra (since 2022); Telangana (since 2022). |
| 47 | Youth4Jobs Foundation | Youth4Jobs Foundation | ngo | Skill Development | Andhra Pradesh (since 2014); Delhi (since 2023); Gujarat (since-year not printed); Karnataka (since 2023); Maharashtra (since 2014); Odisha (since 2014); Puducherry (since-year not printed); Rajasthan (since 2024); Tamil Nadu (since 2014); Telangana (since 2014); West Bengal (since 2014); NE — NE, state not specified (PwD) (since 2023). |

*Dropped vs FY2024-25 (not on p.84): Anudip Foundation, Creative Dignity, New Resolution India, WELL Labs. Creative Dignity is still described on p.42 as an ABF partner since 2024 "supported by Bangalore-based Industree Foundation". If you want it loaded, use `partner_name` = Creative Dignity, `notes` = "named in chapter, not in p.84 list".*
*Counting differences between the badges and the named partners: Madhya Pradesh has a 14-partner badge but 13 are named; North East has a 9-partner badge but 10 organisations are named.*

#### (b) Axis Cares partners — 8 (p.84)

| partner_name | partner_canonical | partner_kind | program | notes |
|---|---|---|---|---|
| Association of Parents of Mentally Retarded Children | Association of Parents of Mentally Retarded Children | ngo | Axis Cares | Employee giving ("inspires Axisians…"), not SLP. |
| Dakshin Foundation | Dakshin Foundation | ngo | Axis Cares | Employee giving ("inspires Axisians…"), not SLP. |
| Kalanjiyam Trust | Kalanjiyam Trust | ngo | Axis Cares | Employee giving ("inspires Axisians…"), not SLP. New vs FY2024-25. |
| Nav Bharat Jagriti Kendra | Nav Bharat Jagriti Kendra | ngo | Axis Cares | Employee giving ("inspires Axisians…"), not SLP. New vs FY2024-25. |
| Pratham Education Foundation | Pratham Education Foundation | ngo | Axis Cares | Employee giving ("inspires Axisians…"), not SLP. New vs FY2024-25. |
| Salaam Bombay Foundation | Salaam Bombay Foundation | ngo | Axis Cares | Employee giving ("inspires Axisians…"), not SLP. |
| Society for Women's Action and Training Initiatives | Society for Women's Action and Training Initiatives | ngo | Axis Cares | Employee giving ("inspires Axisians…"), not SLP. |
| World Wide Fund for Nature - India | WWF-India | ngo | Axis Cares | Employee giving ("inspires Axisians…"), not SLP. New vs FY2024-25. |

*Dropped vs FY2024-25: Committed Communities Development Trust, Pararth Samiti, Project Partner, Ratna Nidhi Charitable Trust, Signing Hands Foundation.*

#### (c) Co-funders — 8 companies (p.16)

| partner_name | partner_canonical | partner_kind | program | notes |
|---|---|---|---|---|
| Axis Asset Management Company Limited | Axis Asset Management Company Limited | company | Sustainable Livelihood Programme | Co-funder; quote by B. Gopkumar, MD & CEO. `partner_funder_id` → set if this entity is a funder row. |
| Axis Bank Limited | Axis Bank Limited | company | Sustainable Livelihood Programme | Co-funder; quote by parent; the ₹352.92 cr FY25-26 spend includes funds it disbursed. `partner_funder_id` → set if this entity is a funder row. |
| Axis Capital Limited | Axis Capital Limited | company | Sustainable Livelihood Programme | Co-funder; quote by Atul Mehra, MD & CEO. `partner_funder_id` → set if this entity is a funder row. |
| Axis Direct | Axis Direct | company | Sustainable Livelihood Programme | Co-funder; quote by Pranav Haridasan, MD & CEO; not "Axis Securities Limited" as in earlier years. `partner_funder_id` → set if this entity is a funder row. |
| Axis Finance Limited | Axis Finance Limited | company | Sustainable Livelihood Programme | Co-funder; quote by Sai Giridhar, MD & CEO. `partner_funder_id` → set if this entity is a funder row. |
| Axis Trustee Services Limited | Axis Trustee Services Limited | company | Sustainable Livelihood Programme | Co-funder; quote by Rahul Choudhary, MD & CEO (printed "Axis Trustees Services Limited" in the quote). `partner_funder_id` → set if this entity is a funder row. |
| Freecharge Payment Technologies Private Limited | Freecharge Payment Technologies Private Limited | company | Sustainable Livelihood Programme | Co-funder; quote by Sumit Bhatnagar, CEO. `partner_funder_id` → set if this entity is a funder row. |
| Invoicemart (A.TReDS) | Invoicemart (A.TReDS) | company | Sustainable Livelihood Programme | Co-funder; quote by Prakash Sankaran, MD & CEO. `partner_funder_id` → set if this entity is a funder row. |

#### (d) Knowledge, convening and government partners named in the text

| partner_name | partner_canonical | partner_kind | program | notes |
|---|---|---|---|---|
| India Development Review | India Development Review (IDR) | other | Ecosystem Action | Communications capacity-building for 23 partner organisations, producing the *Communications is Capacity* series (p.82). |
| Development Intelligence Unit | Development Intelligence Unit | research | Ecosystem Action | Multi-state migration study, ~2,000 migrant households (p.83). |
| North East Together | North East Together | network | Ecosystem Action | Co-convened *The NorthEast Edit* (p.81). |
| Jharkhand State Livelihood Promotion Society | JSLPS | government | Rural Livelihoods | SRLM partnership (Jharkhand chapter, p.39). |
| Uttar Pradesh State Rural Livelihood Mission | UPSRLM | government | Rural Livelihoods | With TRIF (UP chapter, p.69). |
| Rajasthan Grameen Aajeevika Vikas Parishad | RGAVP | government | Rural Livelihoods | Convergence (Rajasthan chapter, p.63). |
| Chhattisgarh State Minor Forest Produce Federation | CGMFPFED | government | Rural Livelihoods | NTFP / Van Dhan Kendras (Chhattisgarh chapter, p.26). |
| Kudumbashree | Kudumbashree (Kerala State Poverty Eradication Mission) | government | Rural Livelihoods | Named in the Kerala chapter (p.45). |

### FY2025-26 — 47 Sustainable Livelihood Programme partners (ABF Annual Report 2025-26, p.84 — the current, most recent list; newly added this pass)

Action for Social Advancement · Aga Khan Rural Support Programme (India) · Agri Entrepreneur Growth Foundation · **Ambuja Foundation** *(new)* · BAIF Institute for Sustainable Livelihoods and Development · Bharat Rural Livelihoods Foundation · **Bright Future India** *(new)* · Center for Advanced Research and Development · Centre for Youth and Social Development · Child In Need Institute · Collectives for Integrated Livelihood Initiatives · Contact Base · Development of Humane Action Foundation · Development Support Centre · DHAN Vayalagam Tank Foundation · Eleutheros Christian Society · Enable India · Foundation for Ecological Security · Generation India Foundation · Gram Vikas · Harsha Trust · Himmotthan Society · Ibtada · **Industree Foundation** *(new)* · Keystone Foundation · Manjari Foundation · Medha Learning Foundation · Navinchandra Mafatlal Sadguru Water and Development Foundation · North East Initiative Development Agency · **People's Science Institute** *(new)* · Professional Assistance for Development Action · Rajarhat Prasari · Samaj Pragati Sahayog · Sarv Seva Samity Sanstha · SELCO Foundation · **Self Reliant Initiatives through Joint Action (SRIJAN)** · Seva Mandir · Seven Sisters Development Assistance · Shroffs Foundation Trust · Swayam Shikshan Prayog · Transform Rural India Foundation · Trust Community Livelihoods · Trust for Retailers and Retail Associates of India · **Udyogini** *(new)* · Voluntary Association for Agricultural General Development, Health and Reconstruction Alliance · Watershed Organisation Trust · Youth4Jobs Foundation

*(all rows: `fiscal_year = FY2025-26`; `source_url = https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf`; `source_name = ABF Annual Report 2025-26`; `fetched_at = 2026-09-29`; `as_of = FY2025-26`)*

**Dropped from FY2024-25's 46-name list (not present in FY2025-26's 47):** Anudip Foundation, Creative Dignity, New Resolution India, WELL Labs — genuinely absent from the newer list (not an extraction error; checked p.84 in full), flagged as likely-ended or paused partnerships rather than assumed continuing.

**FY2025-26 — 8 "Axis Cares" (employee-volunteering) partners (AR2025-26 p.84):** Association of Parents of Mentally Retarded Children · Dakshin Foundation · Kalanjiyam Trust · Nav Bharat Jagriti Kendra · Pratham Education Foundation · Salaam Bombay Foundation · Society for Women's Action and Training Initiatives · World Wide Fund for Nature - India *(4 new vs FY2024-25's list: Kalanjiyam Trust, Nav Bharat Jagriti Kendra, Pratham Education Foundation, WWF-India; 5 dropped: Committed Communities Development Trust, Pararth Samiti, Project Partner, Ratna Nidhi Charitable Trust, Signing Hands Foundation)*

**Also confirmed from AR2025-26 (pp.1-16):** Dhruvi Shah's title expanded to **"Group Head – Corporate Social Responsibility, Axis Bank AND Executive Trustee & CEO, Axis Bank Foundation"** (previously CEO of ABF only) — she now holds a Bank-side CSR leadership role too, per this newest report. As of 2026-03-31: **2.75 million families reached across 33,517 villages in 32 states/UTs** (cumulative Mission 4 Million progress figure, newer than the 2,046,247/23,686-villages figure used elsewhere in this file for FY2024-25/Mission 2 Million completion — both are genuine, sequential milestones, not a contradiction). ABF states it is entering **"its twentieth year"** in this FY2025-26 report (2006 + 20 = 2026, consistent with the founding year already recorded).

### FY2024-25 — 46 Sustainable Livelihood Programme partners (ABF Annual Report 2024-25, p.66)

Action for Social Advancement · Aga Khan Rural Support Programme (India) · Agri Entrepreneur Growth Foundation · Anudip Foundation · BAIF Institute for Sustainable Livelihoods and Development · Bharat Rural Livelihoods Foundation · Center for Advanced Research and Development · Centre for Youth and Social Development · Child in Need Institute (CINI) · Collectives For Integrated Livelihood Initiatives (CInI) · Contact Base · Creative Dignity · Development of Humane Action Foundation (DHAN) · Development Support Centre (DSC) · Dhan Vayalagam Tank Foundation (DVTF) · Eleutheros Christian Society · Enable India · Foundation for Ecological Security (FES) · Generation India Foundation · Gram Vikas · Harsha Trust · Himmotthan Society · Ibtada · Keystone Foundation · Manjari Foundation · Medha Learning Foundation · Navinchandra Mafatlal Sadguru Water & Development Foundation (NMSWDF) · New Resolution India · Northeast Initiative Development Agency · Professional Assistance for Development Action (PRADAN) · Rajarhat Prasari · Samaj Pragati Sahayog (SPS) · Sarv Seva Samity Sanstha (4S) · SELCO Foundation · Self Reliant Initiatives through Joint Action (SRIJAN) · Seva Mandir · Seven Sisters Development Assistance · Shroffs Foundation Trust · Swayam Shikshan Prayog · Transforming Rural India (TRI) · Trust Community Livelihoods · Trust for Retailers and Retail Associates of India (TRRAIN) · VAAGDHARA · WELL Labs · Watershed Organisation Trust (WOTR) · Youth 4 Jobs Foundation

*(all rows: `partner_kind` = ngo/foundation/research per name; `fiscal_year = FY2024-25`; `source_url = https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf`; `source_name = ABF Annual Report 2024-25`; `fetched_at = 2026-09-29`; `as_of = FY2024-25`)*

**FY2024-25 — 9 "Axis Cares" (employee-volunteering) partners — kept distinct from SLP grant partners:**
Association of Parents of Mentally Retarded Children · Committed Communities Development Trust · Dakshin Foundation · Pararth Samiti · Project Partner · Ratna Nidhi Charitable Trust · Salaam Bombay Foundation · Signing Hands Foundation · Society for Women's Action and Training Initiative

### FY2023-24 — 34 SLP partners + "Partner Since" years newly found for repeat partners (ABF AR2023-24 p.60, cross-ref. with AR2022-23)

| partner_name | partner_since (from AR2022-23) | fiscal_year |
|---|---|---|
| Aga Khan Rural Support Programme (India) | 2013 | FY2023-24 |
| Agri Entrepreneur Growth Foundation | 2022 | FY2023-24 |
| Bharat Rural Livelihoods Foundation | 2018 | FY2023-24 |
| Collective for Integrated Livelihood Initiatives (CInI) | 2018 | FY2023-24 |
| Development Support Center (DSC) | 2018 | FY2023-24 |
| Dhan Vayalagam Tank Foundation | 2011 | FY2023-24 |
| Foundation for Ecological Security | 2014 | FY2023-24 |
| Gram Vikas | 2022 | FY2023-24 |
| Generation India Foundation | 2022 | FY2023-24 |
| Harsha Trust | 2012 | FY2023-24 |
| IBTADA | 2019 | FY2023-24 |
| Keystone Foundation | 2019 | FY2023-24 |
| Medha Learning Foundation | 2022 | FY2023-24 |
| Navinchandra Mafatlal Sadguru Water & Development Foundation | 2014 | FY2023-24 |
| Professional Assistance for Development Action (PRADAN) | 2011 | FY2023-24 |
| Rajarhat Prasari | 2022 | FY2023-24 |
| Sahjeevan | 2019 | FY2023-24 |
| Samaj Pragati Sahayog | 2011 | FY2023-24 |
| Sarv Seva Samity Sanstha (4S) | 2022 | FY2023-24 |
| Self Reliant Initiatives through Joint Action (SRIJAN) | **2012** | FY2023-24 |
| Seva Mandir | 2019 | FY2023-24 |
| Shahani Academic & Global Empowerment (SAGE) Foundation | 2022 | FY2023-24 |
| Transforming Rural India Foundation (TRIF) | 2022 | FY2023-24 |
| Watershed Organisation Trust | 2018 | FY2023-24 |
| Youth 4 Jobs Foundation | 2014 | FY2023-24 |
| Anudip Foundation, Child In Need Institute, New Resolution India, SELCO Foundation, Seven Sisters Development Assistance, Swayam Shikshan Prayog, Trust Community Livelihood, TRRAIN, WELL Labs | not_found | FY2023-24 |

*All rows: `source_url = https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2023-24.pdf`.*
**FY2023-24 "Axis Cares" partners (9):** Association of Parents Mentally Retarded Children · Committed Communities Development Trust · Contact Base · Goonj · Project Mumbai · Ratna Nidhi Charitable Trust · Shaishav · The Society for the Rehabilitation of Crippled Children · Society for Women's Action and Training Initiative

### FY2022-23 — ~27 partners with real founder names and "Partner Since" years (ABF AR2022-23 p.47)

| partner_name | founder | partner_since |
|---|---|---|
| Aga Khan Rural Support Programme (India) | HH The Aga Khan | 2013 |
| Agri Entrepreneur Growth Foundation | Tata Trusts, Syngenta Foundation India, IDH Sustainable Trade Initiative | 2022 |
| Anudip Foundation | Dipak Basu | 2022 |
| Bharat Rural Livelihoods Foundation | Ministry of Rural Development, Govt. of India | 2018 |
| Collective for Integrated Livelihood Initiatives | Chairperson: Arun Pandhi | 2018 |
| Centre for Social and Economic Progress | Chairman: Vikram Singh Mehta | 2021 |
| Development Support Center | Late Anil C. Shah | 2018 |
| Dhan Vayalagam Tank Foundation | M. P. Vasimalai | 2011 |
| Foundation for Ecological Security | Dr. Amrita Patel et al. | 2014 |
| Generation India Foundation | Arunesh Singh | 2022 |
| Gram Vikas | Joe Madiath | 2022 |
| Harsha Trust | Bismaya Mahapatra et al. | 2012 |
| IBTADA | Rajesh Singhi | 2019 |
| Kalanjiam Foundation | M. P. Vasimalai (DHAN Foundation) | 2019 |
| Keystone Foundation | Snehlata Nath, Pratim Roy, Mathew John | 2019 |
| Medha Learning Foundation | Byomkesh Mishra | 2022 |
| Navinchandra Mafatlal Sadguru Water & Development Foundation | Late Harnath Jagawat, Sharmishtha H Jagawat | 2014 |
| Professional Assistance for Development Action (PRADAN) | Deep Joshi, Vijay Mahajan | 2011 |
| Rajarhat Prasari | Gouranga Banerjee | 2022 |
| Sahjeevan | Sandeep Virmani et al. | 2019 |
| Samaj Pragati Sahayog | Rangu Rao, Dr. Mihir Shah et al. | 2011 |
| Sarva Seva Samity Sanstha (4S) | Vijay Mahajan | 2022 |
| Self Reliant Initiatives through Joint Action (SRIJAN) | **Ved Arya** | **2012** |
| Seva Mandir | Dr. Mohan Singh Mehta | 2019 |
| Shahani Academic And Global Empowerment (SAGE) Foundation | Maya Shahani | 2022 |
| The Organic and Fairtrade Cotton Secretariat | Ashish Mondal, Prashant Pastore, Murli Dhar | 2022 |
| Transforming Rural India Foundation | Anish Kumar, Anirban Ghose | 2022 |
| Watershed Organisation Trust | Late Fr. Hermann Bacher, Crispino Lobo | 2018 |
| Youth 4 Jobs Foundation | Meera Shenoy | 2014 |

*All rows: `fiscal_year = FY2022-23`; `source_url = https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf`.*

### Company co-funders (kept separate — not implementing NGOs)

**FY2025-26 (AR2025-26 p.16): Axis Asset Management Company Limited · Axis Bank Limited · Axis Capital Limited · Axis Direct · Axis Finance Limited · Axis Trustee Services Limited · Freecharge Payment Technologies Private Limited · Invoicemart (A.TReDS).** "Axis Securities Limited" is not named in FY2025-26. "Axis Direct" (MD & CEO Pranav Haridasan) appears instead, which is presumably its brand name.

Earlier years: Axis Capital Limited · Axis Asset Management Company Limited · Axis Securities Limited · Axis Trustee Services Limited · Axis Finance Limited · Freecharge Payment Technologies Private Limited — all `partner_kind=company`, present FY2023-24 & FY2024-25.
**Invoicemart (A.TReDS)** — `partner_kind=company`, FY2024-25 **and FY2025-26** *(corrected: it is not "FY2024-25 only"; it is listed again in AR2025-26 p.16)* (absent from the FY2023-24 co-funder list — treat "co-funder since" claims as year-specific, not a fixed roster).

**Removed per scope:** CSC Academy, Sri Sathya Sai Health & Education Trust, Akshaya Patra Foundation, Sunbird Trust (all Axis Bank Ltd. direct partners, not ABF's).
**Discrepancy noted, not resolved:** **Dilasa Sanstha** (Maharashtra tribal livelihoods, previously listed in this file from an older legacy micro-site) **does not appear in any of the 3 most recent official "Programme Partners" lists** (FY2022-23/23-24/24-25) — flagged as possibly a legacy/discontinued partnership, not corroborated by current ABF reporting.

---
---

**Grants to NGOs (`grants`)**

⚠️ Still blocked — no visibility into your `orgs` registry, and `org_id` is required. With the fuller partner list now available, the candidate pool has grown substantially (46+ names). Rather than re-list all 46, here are the ones with the strongest evidence (real founder names, "Partner Since" years, multi-year continuity):

| Candidate title | Likely org | amount | currency | status | outcomes (JSON) | notes | source_url |
|---|---|---|---|---|---|---|---|
| SRIJAN — Rajasthan (and Madhya Pradesh) livelihoods | Self Reliant Initiatives through Joint Action (SRIJAN) | **not_found — re-verified 2026-09-29 across all 4 downloaded ABF Annual Reports (2022-23, 2023-24, 2024-25, 2025-26); no per-partner/per-project ₹ amount exists in any of them.** ABF's financial disclosure is limited to aggregate category totals (Rural Livelihoods/Skill Development/Ecosystem Action) per fiscal year — confirmed again on a full re-read of AR2025-26's Rajasthan chapter (pp.65-66), which is ABF's most narratively detailed report yet and still gives no partner-level budget figure anywhere in the document. | INR | **active** *(confirmed current via AR2025-26, its most recently published report, which explicitly describes this as an ongoing partnership — upgraded from "unconfirmed" now that continuity runs across all 4 Annual Reports checked, 2022-23 through 2025-26)* | `{"districts_rajasthan": 4, "state_rajasthan": "Rajasthan", "state_mp": "Madhya Pradesh", "partner_since_AR2022-23_and_AR2023-24": 2012, "partner_since_AR2025-26": 2015, "rajasthan_state_total_partners_FY2025-26": 8, "rajasthan_state_total_blocks_FY2025-26": 28, "focus": ["watershed restoration", "climate-resilient agriculture", "water governance", "dairy", "goat rearing", "poultry", "women's producer organisations (Ajeevika Sakhis)", "financial inclusion", "self-employment", "WASH/nutrition linkages"]}` | Founder: Ved Arya. **⚠️ New discrepancy found on this re-check:** AR2022-23 and AR2023-24 both say "Partner Since: 2012," but AR2025-26 (p.65) says SRIJAN has been a Rajasthan partner "since 2015" — a 3-year inconsistency across ABF's own reports, presented as-found rather than resolved. AR2025-26 also newly reveals SRIJAN is grouped alongside Foundation for Ecological Security (since 2014), N.M. Sadguru WDF (since 2014), Seva Mandir (since 2019), Ibtada (since 2019), Manjari Foundation (since 2025), and Generation India Foundation (since 2025) as part of Rajasthan's 8-partner, 28-block SLP portfolio for FY2025-26. Full narrative describes SRIJAN's role as combining watershed restoration/climate-resilient agriculture with dairy, goat-rearing, poultry and other allied livelihoods, plus women's producer-institution and financial-inclusion work — richer qualitative detail than any prior report gave, but still **zero ₹ figures** tied to SRIJAN specifically. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf ; https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Watershed Organisation Trust (WOTR) — Maharashtra & Telangana NRM | Watershed Organisation Trust | **not_found — re-verified 2026-09-29 across all 4 Annual Reports + both award press releases; no ₹ grant figure exists anywhere for WOTR specifically.** | INR | **active** *(confirmed current in both Maharashtra and Telangana state chapters of AR2025-26, ABF's newest report)* | `{"states_confirmed_active": ["Maharashtra","Telangana"], "state_award_mention_only": "Jharkhand (FICCI 2024, not re-confirmed as an ongoing state partnership in AR2025-26's Jharkhand chapter)", "telangana_reach_FY2025-26": 10500, "telangana_reach_unit": "rural families", "telangana_blocks": ["Damargidda","Maddur"], "telangana_district": "Narayanpet", "telangana_state_total_partners_FY2025-26": 3, "telangana_state_total_blocks_FY2025-26": 19, "award": "FICCI Sustainable Agriculture Gold 2024 (Jharkhand+Telangana+Maharashtra watershed work)"}` | Founders: Late Fr. Hermann Bacher, Crispino Lobo. **⚠️ Discrepancy found:** AR2022-23/AR2023-24 both print "Partner Since: 2018," but AR2025-26's own Maharashtra and Telangana state chapters both say WOTR has been active "since 2022" in each — a 4-year inconsistency across ABF's own reports, presented as-found. Case study title: "Keeping Livelihoods Rooted in Drylands" (Telangana, AR2025-26 p.67). | https://www.axis.bank.in/about-us/press-releases/axis-bank-foundations-sustainable-livelihood-programme-strikes-gold-at-ficci-s-sustainable-agriculture-summit-and-awards-2024 ; https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Harsha Trust — Odisha livelihoods | Harsha Trust | **not_found — re-verified 2026-09-29 across all 4 Annual Reports + the FICCI award press release; no ₹ grant figure exists anywhere for Harsha Trust specifically.** | INR | **active** *(confirmed current in AR2025-26's Odisha chapter, ABF's newest report)* | `{"state": "Odisha", "partner_since": 2012, "note": "2012 is the earliest 'partner since' year printed anywhere in AR2025-26's Odisha chapter (9 partners total), suggesting Harsha Trust may be Odisha's longest-standing SLP partner", "odisha_state_total_partners_FY2025-26": 9, "odisha_state_total_blocks_FY2025-26": 58, "award": "FICCI Sustainable Agriculture Awards 2023 winner"}` | Founders: Bismaya Mahapatra, Chivukula Venkat, Mahadev Rao, Nihar Ranjan Tripathy. No discrepancy found on this re-check — "since 2012" is consistent across AR2022-23, AR2023-24 partner-list, and AR2025-26's Odisha chapter. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf ; https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Bharat Rural Livelihoods Foundation (BRLF) — Chhattisgarh (& Maharashtra) | Bharat Rural Livelihoods Foundation | **not_found — re-verified 2026-09-29 across all 4 Annual Reports + the Earth Care Award press release; no ₹ *grant* figure from ABF to BRLF exists anywhere.** ⚠️ **Important distinction found and flagged, not to be confused with a grant amount:** BRLF's own Chhattisgarh case study in AR2025-26 (p.26) states the project has leveraged **"nearly ₹1,200 crore" (₹12,000,000,000) of MGNREGA funds** across its two completed phases — this is **government scheme money unlocked through the project's convergence work, not ABF's CSR spend**. Recording this as `amount` would misrepresent it as ABF's own grant; it is deliberately excluded from that field. | INR | **active** *(confirmed current in Chhattisgarh; a third phase began in 2024 per AR2025-26)* | `{"state_primary": "Chhattisgarh", "state_secondary": "Maharashtra (since 2023, per FY2024-25/25-26 partner-since data)", "partner_since_chhattisgarh": 2018, "chhattisgarh_reach_cumulative": 150000, "chhattisgarh_reach_unit": "rural families", "chhattisgarh_structures_built_phases_1_2": 48000, "chhattisgarh_area_treated_hectares_phases_1_2": 700000, "chhattisgarh_household_income_growth_pct": 60, "mgnrega_funds_leveraged_inr_NOT_ABF_grant": 12000000000, "award": "Earth Care Award 2024 (co-recipient with ABF)"}` | BRLF is a Section 8 (not-for-profit) company established in 2015 by the Ministry of Rural Development, Government of India — "founder" is the Ministry itself, not an individual. Co-convenes the "Samanvay" cross-learning platform annually with ABF (separate from its role as an implementing partner). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf ; https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |


**FY2025-26 grant candidates (AR2025-26 case studies)** *(still blocked on `org_id`; `status=unconfirmed`, `currency=INR`; no amounts printed)*

| title | likely org | amount | start_date | status | outcomes (JSON) | notes | source_url |
|---|---|---|---|---|---|---|---|
| Bharat Rural Livelihoods Foundation — Chhattisgarh (From Watersheds to Resilient Livelihoods: Scaling a Community-Based Climate Action Model) | Bharat Rural Livelihoods Foundation | not_found | 2018-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 150000, "unit": "rural families"}` | Case study, p.26. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Youth4Jobs — Delhi ((PwD employment)) | Youth4Jobs | not_found | 2023-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 1375, "unit": "young people with disabilities"}` | Case study, p.29. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| N. M. Sadguru Water and Development Foundation — Gujarat (From Seasonal Water Availability to Year-Round Livelihoods) | N. M. Sadguru Water and Development Foundation | not_found | 2014-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 12186, "unit": "households"}` | Case study, p.31. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Medha Learning Foundation — Haryana (From First Jobs to First Career Decisions) | Medha Learning Foundation | not_found | 2022-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 4800, "unit": "youth"}` | Case study, p.33. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Himmotthan Society — Himachal Pradesh (Making Small Mountain Farms Economically Viable) | Himmotthan Society | not_found | 2024-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 4500, "unit": "rural families"}` | Case study, p.35. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Enable India — Jammu and Kashmir (When Opportunity Learns to Travel) | Enable India | not_found | 2024-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 144, "unit": "people with disabilities"}` | Case study, p.37. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Child In Need Institute — Jharkhand (Building Healthy Futures Through Community-Led Action) | Child In Need Institute | not_found | 2023-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 40080, "unit": "rural households"}` | Case study, p.39. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Creative Dignity (supported by Industree Foundation) — Karnataka (Building an artisan-focused livelihood ecosystem from scratch) | Creative Dignity (supported by Industree Foundation) | not_found | 2024-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 23, "unit": "women trained in ceramic production"}` | Case study, p.42. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Keystone Foundation — Kerala (From Ecological Restoration to Community-Owned Collectives) | Keystone Foundation | not_found | 2019-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 6200, "unit": "rural families"}` | Case study, p.45. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Himmotthan Society — Ladakh (Building a Resilient Apricot Value Chain in Ladakh) | Himmotthan Society | not_found | 2024-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 7500, "unit": "rural families"}` | Case study, p.48. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Professional Assistance for Development Action — Madhya Pradesh (Women's Collectives at the Centre of a Rural Poultry Economy) | Professional Assistance for Development Action | not_found | 2011-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 33993, "unit": "rural households"}` | Case study, p.51. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Development Support Centre (DSC) — Maharashtra (Stabilising Livelihoods in a Water-Stressed Landscape) | Development Support Centre (DSC) | not_found | 2018-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 102011, "unit": "rural families"}` | Case study, p.54. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Contact Base — Odisha (Preserving Heritage, Creating Livelihoods) | Contact Base | not_found | 2025-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 3000, "unit": "rural families across 14 blocks"}` | Case study, p.59. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Enable India — Puducherry ((PwD livelihoods)) | Enable India | not_found | 2024-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 380, "unit": "PwDs"}` | Case study, p.61. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Manjari Foundation — Rajasthan (From Producers to Market Leaders) | Manjari Foundation | not_found | 2025-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 21000, "unit": "rural families"}` | Case study, p.63. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| DHAN Foundation / Dhan Vayalagam Tank Foundation — Tamil Nadu (Tanks that are reviving lands, livelihoods and lives) | DHAN Foundation / Dhan Vayalagam Tank Foundation | not_found | 2024-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 60000, "unit": "rural families across 12 blocks"}` | Case study, p.65. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Watershed Organisation Trust — Telangana (Keeping livelihoods rooted in Drylands) | Watershed Organisation Trust | not_found | 2022-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 10500, "unit": "rural families"}` | Case study, p.67. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Trust Community Livelihoods (TCL) — Uttar Pradesh (Building Institutions that Represent Landless and Most Disadvantaged Families) | Trust Community Livelihoods (TCL) | not_found | 2023-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 10000, "unit": "rural [noun missing in source]"}` | Case study, p.69. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| People's Science Institute — Uttarakhand (Building the Next Generation of Development Leaders) | People's Science Institute | not_found | 2025-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 2000, "unit": "rural families"}` | Case study, p.72. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Rajarhat Prasari | not_found | 2022-01-01 *(year only; state-level 'since')* | unconfirmed | `{"reach": 61000, "unit": "rural families"}` | Case study, p.74. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf |

*AP (6,630 households, Gandlapenta/Talupula) and Bihar (12,405 families, Bankey Bazar/Imamganj) case studies name **no** implementing partner, so they aren't listed as grant candidates. Their blocks are in `funder_footprints` (c).*
*Correction to the candidate rows above: AR2025-26 gives **state-level** start years that differ from the earlier ones. WOTR is "since 2022" in Maharashtra and Telangana (earlier: 2018). SRIJAN is "since 2015" in MP and Rajasthan (earlier: 2012 in Rajasthan). BRLF is "since 2018" in Chhattisgarh and "since 2023" in Maharashtra. Keep both: they are different partnerships.*

**Removed:** Akshaya Patra Foundation, Sri Sathya Sai Health & Education Trust, Sunbird Trust (bank-direct, out of scope). Dilasa Sanstha candidate removed given the discrepancy noted above.

---
---

**Calls for proposals (`rfps`)**

⚠️ None found — confirmed via: no "apply now"/open-call page anywhere on axisbankfoundation.org; the TISS-ABF CSR Process Manual describes an internal, relationship-led partner-identification process, not a public window.

| title | status | deadline | amount_min | amount_max | eligibility (JSON) | notes | source_url |
|---|---|---|---|---|---|---|---|
| *(no rows)* | — | — | — | — | `{}` | No public RFP mechanism exists; partner selection is relationship-led. *(Corrected: the earlier note's references to a nonexistent "official CSR Policy PDF" and "earlier Part D" have been removed.)* | https://www.axisbankfoundation.org/download/knowledge-corner/TISS-ABF-CSR-Process-Manual.pdf |

---
---

**Application forms (`proposal_templates`)**

⚠️ None found — no downloadable blank form on axisbankfoundation.org. Table intentionally empty (confirmed absence, not a gap).

---
---

**Contacts (`contacts`)**

*All rows for Axis Bank Foundation. `email`/`phone` empty where not published (fine, not a gap). Bank CSR Committee members and `csr@axisbank.com` removed per scope.*

| name | role | kind | is_public | verified | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|
| S. Ramadorai | Chairperson (Trustee since 2010) | office_bearer | Yes | Yes | Padma Bhushan; former CEO & MD, TCS. | https://www.axisbankfoundation.org/about-us/board-of-trustees.html | ABF Board of Trustees page | 2026-09-29 | FY2024-25 |
| Dhruvi Shah | Executive Trustee & CEO, ABF; Group Head – Corporate Social Responsibility, Axis Bank (AR2025-26 p.14) (Trustee since 2021; joined ABF 2016; CEO since 2020) | office_bearer | Yes | Yes | "Establish and manage NGO partnerships; Develop and manage Grant Portfolio" per her own LinkedIn profile. | https://www.axisbankfoundation.org/about-us/board-of-trustees.html | ABF Board of Trustees page | 2026-09-29 | FY2024-25 |
| Sheela Patel | Trustee (since 2006) | office_bearer | Yes | Yes | Founder-Director, SPARC. | (same) | (same) | 2026-09-29 | FY2024-25 |
| Som Mittal | Trustee (since 2015) | office_bearer | Yes | Yes | Former Chairman/President, NASSCOM. | (same) | (same) | 2026-09-29 | FY2024-25 |
| Rajesh Dahiya | Trustee (since 2015) | office_bearer | Yes | Yes | Founder-CEO, GoodGovern. | (same) | (same) | 2026-09-29 | FY2024-25 |
| Sushma Iyengar | Trustee (since 2019) | office_bearer | Yes | Yes | Founder, Kutch Mahila Vikas Sangathan. | (same) | (same) | 2026-09-29 | FY2024-25 |
| Munish Sharda | Trustee (since 2023) | office_bearer | Yes | Yes | Also Executive Director, Axis Bank Ltd. | (same) | (same) | 2026-09-29 | FY2024-25 |
| Vijay Mulbagal | Trustee (since 2024) | office_bearer | Yes | Yes | AR2025-26 (p.13, p.78): Group Head – Wholesale Bank Coverage, Corporate Salary, Sustainability & CSR, Axis Bank. Wrote the "Way Forward" section. | (same) | (same) | 2026-09-29 | FY2024-25 |
| Abhinav Sen | Vice President, Axis Bank Foundation | programme | **Yes** *(named in ABF's own published Annual Report, not a third-party source)* | Yes | Named as a fireside-chat participant in ABF's own AR2024-25, p.77. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 |
| Shubhanjali Roye | Program Manager, CSR, Axis Bank Foundation | programme | No | Unverified *(LinkedIn only, not cross-confirmed)* | — | https://in.linkedin.com/in/shubhanjali-roye-27a2819b | LinkedIn (self-reported profile) | 2026-09-29 | Sept 2026 |
| Isha Ayyer | Senior Manager, CSR, Axis Bank Foundation | programme | No | Unverified *(LinkedIn only)* | At ABF since Mar 2022. | https://in.linkedin.com/in/isha-ayyer-3b292418 | LinkedIn (self-reported profile) | 2026-09-29 | Sept 2026 |

*AR2025-26 ("Governing Board", pp.10–14) re-confirms all 8 trustees and their "Trustee since" years unchanged. For each trustee row, add `source_url` = https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf, `source_name` = ABF Annual Report 2025-26, `as_of` = FY2025-26. Its bios add Ramadorai as Chairperson of Mission Karmayogi Bharat and Munish Sharda as ED at Axis Bank and Chairman of A.TReDS. **No ABF staff below trustee level are named** in AR2025-26: Abhinav Sen (from AR2024-25) is not mentioned. No email or phone is printed, only the postal address. The co-funder CEOs on pp.16–17 work for the co-funding companies, not ABF, so they aren't added as contacts.*

**Removed:** the 4 Bank CSR Committee members and `csr@axisbank.com` — Axis Bank Limited's, not ABF's.
**General mailbox** (`foundation@axisbank.com`) moved to `profile.general_contact_email` in Part A (not force-fit into a fake named row here).
**archive_url for the Board of Trustees source page:** https://web.archive.org/web/20260929081953/https://www.axisbankfoundation.org/about-us/board-of-trustees.html (archived 2026-09-29 via browser tool, applies to all 8 Trustee rows above).

---
---

**Impact numbers (`metrics`)**

*`method`, `is_self_reported`, `target`, source columns added to every row. `stage=output` corrected for households/villages/blocks/districts (were `outcome`).*

| name | value | target | period | stage | unit | method | is_self_reported | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Households impacted (cumulative, Mission 2 Million) | 2,046,247 | **2,000,000** | as of 2025-03-31 | output | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 |
| Households impacted (Mission 4 Million target) | *(superseded; see the FY2025-26 row: 2,759,126)* | **4,000,000** *(cumulative)* | 2025–2031 | output | households | monitoring_data | Yes | (same) | (same) | 2026-09-29 | FY2024-25 |
| Households impacted (FY24-25 only) | 387,467 | — | FY2024-25 | output | households | monitoring_data | Yes | (same) | (same) | 2026-09-29 | FY2024-25 |
| Villages covered (cumulative) | 23,686 | — | as of FY2024-25 | output | villages | monitoring_data | Yes | (same) | (same) | 2026-09-29 | FY2024-25 |
| Blocks covered (cumulative) | 775 | — | as of FY2024-25 | output | blocks | monitoring_data | Yes | (same) | (same) | 2026-09-29 | FY2024-25 |
| Districts covered (cumulative) | 300 | — | as of FY2024-25 | output | districts | monitoring_data | Yes | (same) | (same) | 2026-09-29 | FY2024-25 |
| States/UTs covered (cumulative) | 32 | — | as of FY2024-25 | output | states/UTs | monitoring_data | Yes | (same) | (same) | 2026-09-29 | FY2024-25 |
| Water harvesting potential created (cumulative) | 166,000,000 *("16.60 Crore")* | — | 2018–2025 | outcome | **cubic metres** *(corrected from "litres")* | monitoring_data | Yes | (same) | (same) | 2026-09-29 | FY2024-25 |
| Trees planted (horticulture & agroforestry, cumulative) | 6,210,000 | — | since Mission 2 Million | outcome | trees | monitoring_data | Yes | (same) | (same) | 2026-09-29 | FY2024-25 |
| Youth trained (cumulative) | 67,749 | — | as of FY2024-25 | output | individuals | monitoring_data | Yes | (same) | (same) | 2026-09-29 | FY2024-25 |
| Youth with disabilities trained (cumulative) | 25,045 | — | as of FY2024-25 | output | individuals | monitoring_data | Yes | (same) | (same) | 2026-09-29 | FY2024-25 |
| Skill Centres (cumulative) | 136 | — | as of FY2024-25 | output | centres | monitoring_data | Yes | (same) | (same) | 2026-09-29 | FY2024-25 |
| Self-Help Groups (SHGs), cumulative | 115,000 | — | as of FY2024-25 | output | groups | monitoring_data | Yes | (same) | (same) | 2026-09-29 | FY2024-25 |
| Members in SHGs (cumulative) | 1,242,000 | — | as of FY2024-25 | output | individuals | monitoring_data | Yes | (same) | (same) | 2026-09-29 | FY2024-25 |
| Young rural entrepreneurs supported (cumulative) | 30,000 | — | since Mission 2 Million | outcome | individuals | monitoring_data | Yes | (same) | (same) | 2026-09-29 | FY2024-25 |
| Young rural entrepreneurs supported (FY24-25 only) | 10,000 | — | FY2024-25 | outcome | individuals | monitoring_data | Yes | (same) | (same) | 2026-09-29 | FY2024-25 |
| Total CSR spend (FY24-25) | 2,319,600,000 | — | FY2024-25 | input | ₹ | monitoring_data | Yes | (same) | (same) | 2026-09-29 | FY2024-25 |
| Households impacted (cumulative, Mission 4 Million) | 2,759,126 | 4,000,000 | 2018 – 2026-03-31 | output | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households impacted (FY25-26 only) | 712,879 | — | FY2025-26 | output | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Projects (FY25-26) | 58 | — | FY2025-26 | output | projects | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Villages covered (cumulative) | 33,517 | — | as of 2026-03-31 | output | villages | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Blocks covered (cumulative) | 1,394 | — | as of 2026-03-31 | output | blocks | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Districts covered (cumulative) | 306 | — | as of 2026-03-31 | output | districts | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| States/UTs covered (cumulative) | 32 | — | as of 2026-03-31 | output | states/UTs | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Youth trained (cumulative) | 81,203 | — | 2018–2026 | output | individuals | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Youth with disabilities trained (cumulative) | 31,394 | — | 2018–2026 | output | individuals | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Skill Centres (cumulative) | 185 | — | 2018–2026 | output | centres | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households linked to schemes & entitlements | 795,876 | — | 2018–2026 | outcome | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| SHGs engaged and strengthened | 146,858 | — | 2018–2026 | output | groups | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Members in SHGs capacitated | 1,610,645 | — | 2018–2026 | output | individuals | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Federations engaged and strengthened | 1,406 | — | 2018–2026 | output | federations | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Village Level Institutions engaged | 17,017 | — | 2018–2026 | output | VLIs | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Members in VLIs | 653,814 | — | 2018–2026 | output | individuals | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Water harvesting potential created | 192,615,656 | — | 2018–2026 | outcome | cubic metres | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households with micro-irrigation | 42,415 | — | 2018–2026 | outcome | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households with major/minor lift irrigation | 19,754 | — | 2018–2026 | outcome | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Area brought under irrigation | 125,916 | — | 2018–2026 | outcome | hectares | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households with agroforestry | 245,091 | — | 2018–2026 | outcome | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Trees planted (horticulture & agroforestry) | 7,434,045 | — | 2018–2026 | outcome | trees | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households supported — Rabi crops | 1,429,204 | — | 2018–2026 | output | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households supported — Kharif crops | 1,899,464 | — | 2018–2026 | output | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households supported — Summer crops | 284,723 | — | 2018–2026 | output | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households supported — Integrated cultivation | 401,513 | — | 2018–2026 | output | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households supported — Kitchen gardens | 807,674 | — | 2018–2026 | output | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households supported — Sericulture | 5,158 | — | 2018–2026 | output | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households supported — Apiculture | 34,829 | — | 2018–2026 | output | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households optimising agrochemicals / bio-inputs | 718,966 | — | 2018–2026 | outcome | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households supported for livestock | 825,607 | — | 2018–2026 | output | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Livestock CRPs (Pashu Sakhis) | 15,489 | — | 2018–2026 | output | individuals | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Livestock health camps | 18,837 | — | 2018–2026 | output | camps | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households with access to drinking water | 65,258 | — | 2018–2026 | outcome | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households using alternate/improved cooking fuel | 32,815 | — | 2018–2026 | outcome | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Individuals worked with to address anaemia | 84,924 | — | 2018–2026 | output | individuals | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Women & girls trained on health and nutrition | 391,469 | — | 2018–2026 | output | individuals | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Health camps | 8,926 | — | 2018–2026 | output | camps | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households with improved access to health schemes | 191,639 | — | 2018–2026 | outcome | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Adolescent girls using sanitary napkins | 74,732 | — | 2018–2026 | outcome | individuals | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households — agri enterprises | 7,712 | — | 2018–2026 | outcome | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households — livestock enterprises | 2,212 | — | 2018–2026 | outcome | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households — skill-based enterprises | 8,210 | — | 2018–2026 | outcome | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| PwDs supported through enterprises | 3,209 | — | 2018–2026 | outcome | individuals | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Households — artisan enterprises | 5,165 | — | 2018–2026 | outcome | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |
| Total spend (FY25-26) ⚠️ incl. Axis Bank Ltd disbursements | 3,529,200,000 | — | FY2025-26 | input | ₹ | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (pp.18, 76) | 2026-09-29 | FY2025-26 |

**FY2025-26 state-level and ecosystem metrics** *(set `location_id` to the state named in `name`; `program_id` = SLP, or Ecosystem Action for the last 7 rows)*

| name | value | target | period | stage | unit | method | is_self_reported | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|---|---|
| households — Andhra Pradesh case study | 6,630 | — | FY2025-26 ("currently supporting") | output | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.22) | 2026-09-29 | FY2025-26 |
| rural families — Bihar case study | 12,405 | — | FY2025-26 ("currently supporting") | output | rural families | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.24) | 2026-09-29 | FY2025-26 |
| rural families — Chhattisgarh case study | 150,000 | — | FY2025-26 ("currently supporting") | output | rural families (12 districts, 34 blocks; third phase from 2024) | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.26) | 2026-09-29 | FY2025-26 |
| young people with disabilities — Delhi case study | 1,375 | — | FY2025-26 ("currently supporting") | output | young people with disabilities | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.29) | 2026-09-29 | FY2025-26 |
| households — Gujarat case study | 12,186 | — | FY2025-26 ("currently supporting") | output | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.31) | 2026-09-29 | FY2025-26 |
| youth — Haryana case study | 4,800 | — | FY2025-26 ("currently supporting") | output | youth | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.33) | 2026-09-29 | FY2025-26 |
| rural families — Himachal Pradesh case study | 4,500 | — | FY2025-26 ("currently supporting") | output | rural families | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.35) | 2026-09-29 | FY2025-26 |
| people with disabilities — Jammu and Kashmir case study | 144 | — | FY2025-26 ("currently supporting") | output | people with disabilities (Baramulla & Kulgam) | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.37) | 2026-09-29 | FY2025-26 |
| rural households — Jharkhand case study | 40,080 | — | FY2025-26 ("currently supporting") | output | rural households (13,160 Khunti Sadar+Murhu; 26,920 Erki, Gopikandar, Shikaripara) — health & nutrition | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.39) | 2026-09-29 | FY2025-26 |
| women trained in ceramic production — Karnataka case study | 23 | — | FY2025-26 ("currently supporting") | output | women trained in ceramic production (Kolar district) | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.42) | 2026-09-29 | FY2025-26 |
| rural families — Kerala case study | 6,200 | — | FY2025-26 ("currently supporting") | output | rural families | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.45) | 2026-09-29 | FY2025-26 |
| rural families — Ladakh case study | 7,500 | — | FY2025-26 ("currently supporting") | output | rural families | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.48) | 2026-09-29 | FY2025-26 |
| rural households — Madhya Pradesh case study | 33,993 | — | FY2025-26 ("currently supporting") | output | rural households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.51) | 2026-09-29 | FY2025-26 |
| rural families — Maharashtra case study | 102,011 | — | FY2025-26 ("currently supporting") | output | rural families | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.54) | 2026-09-29 | FY2025-26 |
| rural families across 14 blocks — Odisha case study | 3,000 | — | FY2025-26 ("currently supporting") | output | rural families across 14 blocks (Koraput & Subarnapur); 5,500+ artists/artisans identified | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.59) | 2026-09-29 | FY2025-26 |
| PwDs — Puducherry case study | 380 | — | FY2025-26 ("currently supporting") | output | PwDs | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.61) | 2026-09-29 | FY2025-26 |
| rural families — Rajasthan case study | 21,000 | — | FY2025-26 ("currently supporting") | output | rural families | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.63) | 2026-09-29 | FY2025-26 |
| rural families across 12 blocks — Tamil Nadu case study | 60,000 | — | FY2025-26 ("currently supporting") | output | rural families across 12 blocks (Madurai, Ramanathapuram, Sivagangai, Virudhunagar) | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.65) | 2026-09-29 | FY2025-26 |
| rural families — Telangana case study | 10,500 | — | FY2025-26 ("currently supporting") | output | rural families | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.67) | 2026-09-29 | FY2025-26 |
| rural [noun missing in source] — Uttar Pradesh case study | 10,000 | — | FY2025-26 ("currently supporting") | output | rural [noun missing in source] (Musahar Manch) | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.69) | 2026-09-29 | FY2025-26 |
| rural families — Uttarakhand case study | 2,000 | — | FY2025-26 ("currently supporting") | output | rural families; Development Practitioners' Training aims to train 50 rural youth | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.72) | 2026-09-29 | FY2025-26 |
| rural families — West Bengal case study | 61,000 | — | FY2025-26 ("currently supporting") | output | rural families | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Water bodies restored since 2011 — Pambar–Kottakaraiyar basin (Tamil Nadu) | 1,776 | — | 2011–2026 | output | water bodies | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.65) | 2026-09-29 | FY2025-26 |
| Land & water conservation structures — Chhattisgarh (phases 1–2) | 48,000 | — | phases 1–2 | output | structures ("over") | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.26) | 2026-09-29 | FY2025-26 |
| Area treated — Chhattisgarh (phases 1–2) | 700,000 | — | phases 1–2 | output | hectares ("more than 7 lakh") | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.26) | 2026-09-29 | FY2025-26 |
| MGNREGA funds leveraged — Chhattisgarh (phases 1–2) | 12,000,000,000 | — | phases 1–2 | input | ₹ ("nearly Rs 1,200 crore") | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.26) | 2026-09-29 | FY2025-26 |
| Household income growth — Chhattisgarh supported families | 60 | — | phases 1–2 | outcome | % ("at least") | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.26) | 2026-09-29 | FY2025-26 |
| HP households supported this year | 1,288 | — | FY2025-26 | output | households | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.35) | 2026-09-29 | FY2025-26 |
| HP area under springshed management | 145.5 | — | FY2025-26 | output | acres | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.35) | 2026-09-29 | FY2025-26 |
| HP water harvesting & storage structures | 162 | — | FY2025-26 | output | structures | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.35) | 2026-09-29 | FY2025-26 |
| Kerala collectives: finance leveraged | 916,000 | — | FY2025-26 | outcome | ₹ ("approximately Rs 9.16 lakh") | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.45) | 2026-09-29 | FY2025-26 |
| Ladakh apricot cooperative members | 560 | — | since 2020 | output | farmers (11 villages) | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.48) | 2026-09-29 | FY2025-26 |
| Odisha artists/artisans identified | 5,500 | — | FY2025-26 | output | individuals ("over") | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.59) | 2026-09-29 | FY2025-26 |
| Northeast Edit participants | 74 | — | FY2025-26 | output | individuals (24 NGO + 38 funder + 12 knowledge-partner reps) | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.81) | 2026-09-29 | FY2025-26 |
| Partner orgs in governance workshops | 30 | — | FY2025-26 | output | organisations ("more than 30") | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.82) | 2026-09-29 | FY2025-26 |
| Partner orgs in communications programme | 23 | — | FY2025-26 | output | organisations | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.82) | 2026-09-29 | FY2025-26 |
| Thematic playbooks developed | 20 | — | FY2025-26 | output | playbooks | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.83) | 2026-09-29 | FY2025-26 |
| Organisations in climate-readiness assessment | 35 | — | FY2025-26 | output | organisations | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.83) | 2026-09-29 | FY2025-26 |
| Migrant households in migration study | 2,000 | — | FY2025-26 | output | households (approx.) | monitoring_data | Yes | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.83) | 2026-09-29 | FY2025-26 |

*FY2025-26 rows are cumulative for Mission 4 Million, 2018–2026 ("Outreach", p.76), unless marked FY25-26. They were checked against the rendered page image. The Mission 4 Million target row above (value 0) is superseded by the 2,759,126 cumulative row.*

**Removed:** the entire "Axis Bank Limited — company-wide CSR beneficiaries by theme (BRSR)" table — bank data, out of scope.

---
---

**Documents (`documents`)**

*All 10 ABF Annual Reports listed with real URLs. `is_ai_generated=No`; `is_public=Yes`. `status=read` where downloaded and read this session; `status=received` where only the URL was confirmed.*

| title | doc_type | source_url | source_name | fetched_at | as_of | status | archive_url |
|---|---|---|---|---|---|---|---|
| Axis Bank Foundation Annual Report 2025-26 | annual report | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF website | 2026-09-29 | FY2025-26 | read *(88 pp., read in full 2026-09-29; no audited accounts, PAN, 12A/80G, CSR-1 or Darpan ID printed)* | Not found |
| Axis Bank Foundation Annual Report 2024-25 | annual report | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF website | 2026-09-29 | FY2024-25 | read | Not found |
| Axis Bank Foundation Annual Report 2023-24 | annual report | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2023-24.pdf | ABF website | 2026-09-29 | FY2023-24 | read | Not found |
| Axis Bank Foundation Annual Report 2022-23 | annual report | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf | ABF website | 2026-09-29 | FY2022-23 | read | Not found |
| Axis Bank Foundation Annual Report 2021-22 | annual report | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABFAR_2021-22_digital_v8.pdf | ABF website | 2026-09-29 | FY2021-22 | received | Not found |
| Axis Bank Foundation Annual Report 2020-21 | annual report | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2020-21.pdf | ABF website | 2026-09-29 | FY2020-21 | received | Not found |
| Axis Bank Foundation Annual Report 2019-20 | annual report | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2019_20_Final.pdf | ABF website | 2026-09-29 | FY2019-20 | received | Not found |
| Axis Bank Foundation Annual Report 2018-19 | annual report | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2018_19_Final.pdf | ABF website | 2026-09-29 | FY2018-19 | received | Not found |
| Axis Bank Foundation Annual Report 2017-18 | annual report | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2017_18_Final.pdf | ABF website | 2026-09-29 | FY2017-18 | received | Not found |
| Axis Bank Foundation Annual Report 2016-17 | annual report | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/Axis-Bank-Foundation-Annual-Report-2016-17.pdf | ABF website | 2026-09-29 | FY2016-17 | received | Not found |
| Axis Bank Foundation Annual Report 2015-16 | annual report | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/Axis-Bank-Foundation-Annual-Report-2015-16.pdf | ABF website | 2026-09-29 | FY2015-16 | read | Not found |
| TISS-ABF CSR Process Manual | brochure | https://www.axisbankfoundation.org/download/knowledge-corner/TISS-ABF-CSR-Process-Manual.pdf | ABF Knowledge Corner | 2026-09-29 | ~2015 | read | Not found |

**Removed:** 5 Axis Bank Ltd documents + the "Axis Bank Limited CSR Policy" placeholder row — out of scope.
**Still not found:** any standalone "audited accounts"/"income and expenditure statement" document distinct from the narrative Annual Reports above (checked all 10; none contain one).

---
---

---
---

**Where programmes ran — state list (`program_locations`)**

*State-level only; district detail is in `funder_footprints` above. All bank-CSR-theme lists removed.*

| program_id | location_id | role | valid_from | valid_to | note | source_url | source_name | fetched_at | as_of | archive_url |
|---|---|---|---|---|---|---|---|---|---|---|
| SRIJAN Partnership | Rajasthan | `funds` | 2012-01-01 | — | 4 districts, unnamed individually. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf | ABF Annual Report 2022-23 | 2026-09-29 | FY2022-23 | Not found |
| Rural Livelihoods | Odisha | `operates` | 2024-04-01 | — | Siangbali GP, Daringbadi block case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 | Not found |
| Rural Livelihoods | Madhya Pradesh | `operates` | 2024-04-01 | — | "Sita Devi, Farmer" case study; district not specified. | (same) | (same) | 2026-09-29 | FY2024-25 | Not found |
| Rural Livelihoods | Gujarat | `operates` | 2023-01-01 | — | Trustee site visit, Dahod & Panchmahal districts. **Replaces the earlier weak "Dahod, funds" gallery-caption row.** | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf | ABF Annual Report 2022-23 | 2026-09-29 | FY2022-23 | Not found |
| Environmental Sustainability / NRM | Jharkhand | `funds` | 2024-01-01 | — | FICCI 2024 Gold Award, WOTR-implemented, Khunti district. | https://www.axis.bank.in/about-us/press-releases/axis-bank-foundations-sustainable-livelihood-programme-strikes-gold-at-ficci-s-sustainable-agriculture-summit-and-awards-2024 | Axis Bank press release | 2026-09-29 | FY2024-25 | Not found |
| Environmental Sustainability / NRM | Telangana | `funds` | 2024-01-01 | — | Same FICCI award evidence, Narayanpet district. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024 | Not found |
| Environmental Sustainability / NRM | Maharashtra | `funds` | 2024-01-01 | — | Same FICCI award evidence, Ahmednagar & Beed districts. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024 | Not found |
| Environmental Sustainability / NRM | Chhattisgarh | `funds` | 2023-01-01 | — | Earth Care Award 2024 with BRLF, 12 districts, 26 blocks. | https://www.axisbank.com/about-us/press-releases/axis-bank-foundation-wins-earth-care-award-2024-for-its-community-based-climate-action-work | Axis Bank press release | 2026-09-29 | FY2023-24 | Not found |
| Towards the Northeast | Assam | `operates` | 2024-04-01 | — | Bina Bora case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 | Not found |
| Towards the Northeast | Meghalaya | `operates` | 2024-04-01 | — | Jaksongram village case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 | Not found |
| Towards the Northeast | Nagaland | `operates` | 2024-04-01 | — | **Role changed from `priority` to `operates`** per instruction; named model example. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 | Not found |
| Towards the Northeast | Mizoram | `operates` | 2024-04-01 | — | Same correction; named model example. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 | Not found |
| Skill Development | Kerala | `funds` | not_found | — | TRRAIN partnership, ~2,400 PwDs. | https://thecsruniverse.com/articles/axis-bank-foundation-and-trrain-collaborate-to-create-inclusive-work-opportunities-for-persons-with-disabilities | The CSR Universe (press) | 2026-09-29 | FY2024-25 (approx.) | Not found |
| Sustainable Livelihood Programme | Andhra Pradesh | `funds` | — | — | FY2025-26 state chapter, p.22. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Bihar | `funds` | — | — | FY2025-26 state chapter, p.24. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Chhattisgarh | `funds` | — | — | FY2025-26 state chapter, p.26. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Delhi | `funds` | — | — | FY2025-26 state chapter, p.29. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Gujarat | `funds` | — | — | FY2025-26 state chapter, p.31. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Haryana | `funds` | — | — | FY2025-26 state chapter, p.33. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Himachal Pradesh | `funds` | — | — | FY2025-26 state chapter, p.35. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Jammu and Kashmir | `funds` | — | — | FY2025-26 state chapter, p.37. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Jharkhand | `funds` | — | — | FY2025-26 state chapter, p.39. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Karnataka | `funds` | — | — | FY2025-26 state chapter, p.42. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Kerala | `funds` | — | — | FY2025-26 state chapter, p.45. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Ladakh | `funds` | — | — | FY2025-26 state chapter, p.48. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Madhya Pradesh | `funds` | — | — | FY2025-26 state chapter, p.51. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Maharashtra | `funds` | — | — | FY2025-26 state chapter, p.54. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Odisha | `funds` | — | — | FY2025-26 state chapter, p.59. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Puducherry | `funds` | — | — | FY2025-26 state chapter, p.61. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Rajasthan | `funds` | — | — | FY2025-26 state chapter, p.63. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Tamil Nadu | `funds` | — | — | FY2025-26 state chapter, p.65. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Telangana | `funds` | — | — | FY2025-26 state chapter, p.67. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Uttar Pradesh | `funds` | — | — | FY2025-26 state chapter, p.69. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Uttarakhand | `funds` | — | — | FY2025-26 state chapter, p.72. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | West Bengal | `funds` | — | — | FY2025-26 state chapter, p.74. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Assam | `funds` | — | — | FY2025-26 state chapter, p.56. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Meghalaya | `funds` | — | — | FY2025-26 state chapter, p.56. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Nagaland | `funds` | — | — | FY2025-26 state chapter, p.56. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Mizoram | `funds` | — | — | FY2025-26 state chapter, p.56. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Manipur | `funds` | — | — | FY2025-26 state chapter, p.56. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Tripura | `funds` | — | — | FY2025-26 state chapter, p.56. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Sustainable Livelihood Programme | Arunachal Pradesh | `funds` | — | — | FY2025-26 state chapter, p.56. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Andhra Pradesh | `funds` | — | — | Skilling/PwD partners: Generation India Foundation, Enable India, Youth4Jobs (p.22). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Bihar | `funds` | — | — | Skilling/PwD partners: Medha Learning Foundation, Generation India Foundation (p.24). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Delhi | `funds` | — | — | Skilling/PwD partners: Generation India Foundation, Youth4Jobs (p.29). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Gujarat | `funds` | — | — | Skilling/PwD partners: Generation India Foundation, Youth4Jobs (p.31). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Haryana | `funds` | — | — | Skilling/PwD partners: Medha Learning Foundation (p.33). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Himachal Pradesh | `funds` | — | — | Skilling/PwD partners: Generation India Foundation (p.35). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Jammu and Kashmir | `funds` | — | — | Skilling/PwD partners: Enable India, Generation India Foundation (p.37). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Jharkhand | `funds` | — | — | Skilling/PwD partners: Generation India Foundation (p.39). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Karnataka | `funds` | — | — | Skilling/PwD partners: Generation India Foundation, Enable India, Trust for Retailers and Retail Associates of India, Youth4Jobs (p.42). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Kerala | `funds` | — | — | Skilling/PwD partners: Generation India Foundation, Enable India, Trust for Retailers and Retail Associates of India (p.45). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Madhya Pradesh | `funds` | — | — | Skilling/PwD partners: Generation India Foundation, Enable India (p.51). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Maharashtra | `funds` | — | — | Skilling/PwD partners: Generation India Foundation, Bright Future India, Enable India, Youth4Jobs (p.54). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Odisha | `funds` | — | — | Skilling/PwD partners: Youth4Jobs (p.59). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Puducherry | `funds` | — | — | Skilling/PwD partners: Enable India, Youth4Jobs (p.61). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Rajasthan | `funds` | — | — | Skilling/PwD partners: Generation India Foundation, Youth4Jobs (p.63). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Tamil Nadu | `funds` | — | — | Skilling/PwD partners: Generation India Foundation, Enable India, Youth4Jobs (p.65). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Telangana | `funds` | — | — | Skilling/PwD partners: Enable India, Youth4Jobs (p.67). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | Uttar Pradesh | `funds` | — | — | Skilling/PwD partners: Medha Learning Foundation, Generation India Foundation, Enable India, Trust for Retailers and Retail Associates of India (p.69). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Skill Development | West Bengal | `funds` | — | — | Skilling/PwD partners: Generation India Foundation, Youth4Jobs (p.74). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Health & Nutrition Integration | Jharkhand | `funds` | 2023-01-01 | — | Child In Need Institute (since 2023) (p.39). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Health & Nutrition Integration | Odisha | `funds` | 2023-01-01 | — | Child In Need Institute (since 2023) (p.59). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Health & Nutrition Integration | West Bengal | `funds` | 2023-01-01 | — | Child In Need Institute (since 2023) (p.74). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| NoDE | Assam | `funds` | 2024-01-01 | — | NoDE coverage per p.56–58. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| NoDE | Nagaland | `funds` | 2024-01-01 | — | NoDE coverage per p.56–58. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| NoDE | Meghalaya | `funds` | 2024-01-01 | — | NoDE coverage per p.56–58. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| NoDE | Manipur | `funds` | 2024-01-01 | — | NoDE coverage per p.56–58. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| NoDE | Arunachal Pradesh | `funds` | 2024-01-01 | — | NoDE coverage per p.56–58. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Towards the Northeast | Assam | `funds` | — | — | Named in the North East chapter (p.56). Upgrades the FY2024-25 `operates` rows. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Towards the Northeast | Meghalaya | `funds` | — | — | Named in the North East chapter (p.56). Upgrades the FY2024-25 `operates` rows. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Towards the Northeast | Nagaland | `funds` | — | — | Named in the North East chapter (p.56). Upgrades the FY2024-25 `operates` rows. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Towards the Northeast | Mizoram | `funds` | — | — | Named in the North East chapter (p.56). Upgrades the FY2024-25 `operates` rows. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Towards the Northeast | Manipur | `funds` | — | — | Named in the North East chapter (p.56). Upgrades the FY2024-25 `operates` rows. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Towards the Northeast | Tripura | `funds` | — | — | Named in the North East chapter (p.56). Upgrades the FY2024-25 `operates` rows. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Towards the Northeast | Arunachal Pradesh | `funds` | — | — | Named in the North East chapter (p.56). Upgrades the FY2024-25 `operates` rows. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |
| Development Practitioners' Training | Uttarakhand | `funds` | 2025-01-01 | — | Chamoli (p.72). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 | Not found |

*FY2025-26 rows added above. The existing `program_id` value "Environmental Sustainability / NRM" is **not a row in `programs`**, so it can't be linked; remap those rows to Rural Livelihoods. Same for the "SRIJAN Partnership" row: it maps to the `project` row of that name.*

**Removed per scope:** the (Historical, ABF pre-pivot) row, Gujarat/Dahod gallery-caption row, and Child Heart Surgeries/Mid-Day Meal Program/Axis DilSe rows — superseded or out of scope (bank-direct).

*Registered-office row (`role=registered`) already captured in the `funder_locations` section earlier in this file — not duplicated here.*

---
---

## Grant places (`grant_locations`)

⚠️ Same structural blocker as `grants` — `grant_id` is required and no real `grants` rows could be produced. Location evidence retained for the 3 strongest candidates (SRIJAN, WOTR, Harsha Trust — see `grants` above), ready to attach once `grant_id`s exist:

| candidate grant | location_id | note | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|
| SRIJAN — Rajasthan livelihoods | Rajasthan (state level; 4 districts, not individually named) | "Reached out to farmers in four districts of Rajasthan... since 2012." | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf | ABF Annual Report 2022-23 | 2026-09-29 | FY2022-23 |
| WOTR — multi-state NRM | Jharkhand (Khunti district), Telangana (Narayanpet district), Maharashtra (Ahmednagar & Beed districts) | FICCI 2024 Gold Award project detail — most granular district-level evidence in this file. | https://www.axis.bank.in/about-us/press-releases/axis-bank-foundations-sustainable-livelihood-programme-strikes-gold-at-ficci-s-sustainable-agriculture-summit-and-awards-2024 | Axis Bank press release | 2026-09-29 | FY2024-25 |
| BRLF/ABF — Chhattisgarh watershed | Chhattisgarh (12 districts, 26 blocks, unnamed individually) | Earth Care Award 2024. | https://www.axisbank.com/about-us/press-releases/axis-bank-foundation-wins-earth-care-award-2024-for-its-community-based-climate-action-work | Axis Bank press release | 2026-09-29 | FY2023-24 |


**FY2025-26 candidate `grant_locations` (named blocks from case studies)**

| candidate grant | location_id (block → district → state) | note | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|
| N. M. Sadguru Water and Development Foundation — Gujarat (From Seasonal Water Availability to Year-Round Livelihoods) | Godhra → Panchmahal → Gujarat | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.31) | 2026-09-29 | FY2025-26 |
| N. M. Sadguru Water and Development Foundation — Gujarat (From Seasonal Water Availability to Year-Round Livelihoods) | Ghoghamba → Panchmahal → Gujarat | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.31) | 2026-09-29 | FY2025-26 |
| N. M. Sadguru Water and Development Foundation — Gujarat (From Seasonal Water Availability to Year-Round Livelihoods) | Morwa Hadaf → Panchmahal → Gujarat | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.31) | 2026-09-29 | FY2025-26 |
| Himmotthan Society — Himachal Pradesh (Making Small Mountain Farms Economically Viable) | Baijnath → Kangra → Himachal Pradesh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.35) | 2026-09-29 | FY2025-26 |
| Himmotthan Society — Himachal Pradesh (Making Small Mountain Farms Economically Viable) | Nadaun → Hamirpur → Himachal Pradesh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.35) | 2026-09-29 | FY2025-26 |
| Child In Need Institute — Jharkhand (Building Healthy Futures Through Community-Led Action) | Khunti Sadar → Khunti → Jharkhand | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.39) | 2026-09-29 | FY2025-26 |
| Child In Need Institute — Jharkhand (Building Healthy Futures Through Community-Led Action) | Murhu → Khunti → Jharkhand | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.39) | 2026-09-29 | FY2025-26 |
| Child In Need Institute — Jharkhand (Building Healthy Futures Through Community-Led Action) | Erki (Tamar II) → Ranchi *(printed under 'Khunti and Dumka districts'; Erki/Tamar II is a Ranchi-district block — check)* → Jharkhand | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.39) | 2026-09-29 | FY2025-26 |
| Child In Need Institute — Jharkhand (Building Healthy Futures Through Community-Led Action) | Gopikandar → Dumka → Jharkhand | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.39) | 2026-09-29 | FY2025-26 |
| Child In Need Institute — Jharkhand (Building Healthy Futures Through Community-Led Action) | Shikaripara → Dumka → Jharkhand | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.39) | 2026-09-29 | FY2025-26 |
| Keystone Foundation — Kerala (From Ecological Restoration to Community-Owned Collectives) | Nilambur → Malappuram → Kerala | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.45) | 2026-09-29 | FY2025-26 |
| Keystone Foundation — Kerala (From Ecological Restoration to Community-Owned Collectives) | Mananthawadi → Wayanad → Kerala | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.45) | 2026-09-29 | FY2025-26 |
| Himmotthan Society — Ladakh (Building a Resilient Apricot Value Chain in Ladakh) | Chiktan → Leh/Kargil (district per block not printed) → Ladakh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.48) | 2026-09-29 | FY2025-26 |
| Himmotthan Society — Ladakh (Building a Resilient Apricot Value Chain in Ladakh) | Chuchot → Leh/Kargil (district per block not printed) → Ladakh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.48) | 2026-09-29 | FY2025-26 |
| Himmotthan Society — Ladakh (Building a Resilient Apricot Value Chain in Ladakh) | Durbuk → Leh/Kargil (district per block not printed) → Ladakh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.48) | 2026-09-29 | FY2025-26 |
| Himmotthan Society — Ladakh (Building a Resilient Apricot Value Chain in Ladakh) | Khaltsi → Leh/Kargil (district per block not printed) → Ladakh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.48) | 2026-09-29 | FY2025-26 |
| Himmotthan Society — Ladakh (Building a Resilient Apricot Value Chain in Ladakh) | Kharu → Leh/Kargil (district per block not printed) → Ladakh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.48) | 2026-09-29 | FY2025-26 |
| Himmotthan Society — Ladakh (Building a Resilient Apricot Value Chain in Ladakh) | Leh → Leh/Kargil (district per block not printed) → Ladakh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.48) | 2026-09-29 | FY2025-26 |
| Himmotthan Society — Ladakh (Building a Resilient Apricot Value Chain in Ladakh) | Nyoma → Leh/Kargil (district per block not printed) → Ladakh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.48) | 2026-09-29 | FY2025-26 |
| Himmotthan Society — Ladakh (Building a Resilient Apricot Value Chain in Ladakh) | Rong Chugut → Leh/Kargil (district per block not printed) → Ladakh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.48) | 2026-09-29 | FY2025-26 |
| Himmotthan Society — Ladakh (Building a Resilient Apricot Value Chain in Ladakh) | Saspol → Leh/Kargil (district per block not printed) → Ladakh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.48) | 2026-09-29 | FY2025-26 |
| Himmotthan Society — Ladakh (Building a Resilient Apricot Value Chain in Ladakh) | Skurbuchan → Leh/Kargil (district per block not printed) → Ladakh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.48) | 2026-09-29 | FY2025-26 |
| Himmotthan Society — Ladakh (Building a Resilient Apricot Value Chain in Ladakh) | Sodh → Leh/Kargil (district per block not printed) → Ladakh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.48) | 2026-09-29 | FY2025-26 |
| Himmotthan Society — Ladakh (Building a Resilient Apricot Value Chain in Ladakh) | Thiksay → Leh/Kargil (district per block not printed) → Ladakh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.48) | 2026-09-29 | FY2025-26 |
| Professional Assistance for Development Action — Madhya Pradesh (Women's Collectives at the Centre of a Rural Poultry Economy) | Amarpur → Betul/Dindori/Mandla/Shahdol/Singrauli (per-block district not printed) → Madhya Pradesh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.51) | 2026-09-29 | FY2025-26 |
| Professional Assistance for Development Action — Madhya Pradesh (Women's Collectives at the Centre of a Rural Poultry Economy) | Deosar → Betul/Dindori/Mandla/Shahdol/Singrauli (per-block district not printed) → Madhya Pradesh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.51) | 2026-09-29 | FY2025-26 |
| Professional Assistance for Development Action — Madhya Pradesh (Women's Collectives at the Centre of a Rural Poultry Economy) | Ghoda Dongari → Betul/Dindori/Mandla/Shahdol/Singrauli (per-block district not printed) → Madhya Pradesh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.51) | 2026-09-29 | FY2025-26 |
| Professional Assistance for Development Action — Madhya Pradesh (Women's Collectives at the Centre of a Rural Poultry Economy) | Jaisinghnagar → Betul/Dindori/Mandla/Shahdol/Singrauli (per-block district not printed) → Madhya Pradesh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.51) | 2026-09-29 | FY2025-26 |
| Professional Assistance for Development Action — Madhya Pradesh (Women's Collectives at the Centre of a Rural Poultry Economy) | Mohgaon → Betul/Dindori/Mandla/Shahdol/Singrauli (per-block district not printed) → Madhya Pradesh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.51) | 2026-09-29 | FY2025-26 |
| Professional Assistance for Development Action — Madhya Pradesh (Women's Collectives at the Centre of a Rural Poultry Economy) | Narayanganj → Betul/Dindori/Mandla/Shahdol/Singrauli (per-block district not printed) → Madhya Pradesh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.51) | 2026-09-29 | FY2025-26 |
| Professional Assistance for Development Action — Madhya Pradesh (Women's Collectives at the Centre of a Rural Poultry Economy) | Samnapur → Betul/Dindori/Mandla/Shahdol/Singrauli (per-block district not printed) → Madhya Pradesh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.51) | 2026-09-29 | FY2025-26 |
| Professional Assistance for Development Action — Madhya Pradesh (Women's Collectives at the Centre of a Rural Poultry Economy) | Shahpur → Betul/Dindori/Mandla/Shahdol/Singrauli (per-block district not printed) → Madhya Pradesh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.51) | 2026-09-29 | FY2025-26 |
| Development Support Centre (DSC) — Maharashtra (Stabilising Livelihoods in a Water-Stressed Landscape) | Akkalkuwa → Nandurbar/Dhule → Maharashtra | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.54) | 2026-09-29 | FY2025-26 |
| Development Support Centre (DSC) — Maharashtra (Stabilising Livelihoods in a Water-Stressed Landscape) | Dhadgaon → Nandurbar/Dhule → Maharashtra | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.54) | 2026-09-29 | FY2025-26 |
| Development Support Centre (DSC) — Maharashtra (Stabilising Livelihoods in a Water-Stressed Landscape) | Dhule → Nandurbar/Dhule → Maharashtra | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.54) | 2026-09-29 | FY2025-26 |
| Development Support Centre (DSC) — Maharashtra (Stabilising Livelihoods in a Water-Stressed Landscape) | Nandurbar → Nandurbar/Dhule → Maharashtra | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.54) | 2026-09-29 | FY2025-26 |
| Development Support Centre (DSC) — Maharashtra (Stabilising Livelihoods in a Water-Stressed Landscape) | Navapur → Nandurbar/Dhule → Maharashtra | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.54) | 2026-09-29 | FY2025-26 |
| Development Support Centre (DSC) — Maharashtra (Stabilising Livelihoods in a Water-Stressed Landscape) | Sakri → Nandurbar/Dhule → Maharashtra | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.54) | 2026-09-29 | FY2025-26 |
| Development Support Centre (DSC) — Maharashtra (Stabilising Livelihoods in a Water-Stressed Landscape) | Shahada → Nandurbar/Dhule → Maharashtra | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.54) | 2026-09-29 | FY2025-26 |
| Development Support Centre (DSC) — Maharashtra (Stabilising Livelihoods in a Water-Stressed Landscape) | Sindkheda → Nandurbar/Dhule → Maharashtra | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.54) | 2026-09-29 | FY2025-26 |
| Enable India — Puducherry ((PwD livelihoods)) | Nettapakkam → Puducherry → Puducherry | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.61) | 2026-09-29 | FY2025-26 |
| Enable India — Puducherry ((PwD livelihoods)) | Puducherry commune → Puducherry → Puducherry | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.61) | 2026-09-29 | FY2025-26 |
| Manjari Foundation — Rajasthan (From Producers to Market Leaders) | Bari → Dholpur/Baran → Rajasthan | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.63) | 2026-09-29 | FY2025-26 |
| Manjari Foundation — Rajasthan (From Producers to Market Leaders) | Baseri → Dholpur/Baran → Rajasthan | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.63) | 2026-09-29 | FY2025-26 |
| Manjari Foundation — Rajasthan (From Producers to Market Leaders) | Dholpur → Dholpur/Baran → Rajasthan | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.63) | 2026-09-29 | FY2025-26 |
| Manjari Foundation — Rajasthan (From Producers to Market Leaders) | Kishanganj → Dholpur/Baran → Rajasthan | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.63) | 2026-09-29 | FY2025-26 |
| Manjari Foundation — Rajasthan (From Producers to Market Leaders) | Saipau → Dholpur/Baran → Rajasthan | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.63) | 2026-09-29 | FY2025-26 |
| Watershed Organisation Trust — Telangana (Keeping livelihoods rooted in Drylands) | Damargidda → Narayanpet → Telangana | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.67) | 2026-09-29 | FY2025-26 |
| Watershed Organisation Trust — Telangana (Keeping livelihoods rooted in Drylands) | Maddur → Narayanpet → Telangana | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.67) | 2026-09-29 | FY2025-26 |
| Trust Community Livelihoods (TCL) — Uttar Pradesh (Building Institutions that Represent Landless and Most Disadvantaged Families) | Fatehpur → Barabanki → Uttar Pradesh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.69) | 2026-09-29 | FY2025-26 |
| Trust Community Livelihoods (TCL) — Uttar Pradesh (Building Institutions that Represent Landless and Most Disadvantaged Families) | Suratganj → Barabanki → Uttar Pradesh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.69) | 2026-09-29 | FY2025-26 |
| Trust Community Livelihoods (TCL) — Uttar Pradesh (Building Institutions that Represent Landless and Most Disadvantaged Families) | Nichlaul → Maharajganj → Uttar Pradesh | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.69) | 2026-09-29 | FY2025-26 |
| People's Science Institute — Uttarakhand (Building the Next Generation of Development Leaders) | Narayanbagar → Chamoli → Uttarakhand | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.72) | 2026-09-29 | FY2025-26 |
| People's Science Institute — Uttarakhand (Building the Next Generation of Development Leaders) | Tharali → Chamoli → Uttarakhand | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.72) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Banarhat → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Basanti → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Garubathan → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Gosaba → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Hingalganj → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | JB Sukhiyapokhri → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Kalimpong I → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Khoyrasole → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Kranti → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Lava → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Mal → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Matiali → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Nagrakata → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Patharpratima → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Pedong → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Rajnagar → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Rangli Rangliot → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Sandeshkhali II → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |
| Rajarhat Prasari — West Bengal (Looking Beyond the Spring) | Suri I → Birbhum/Darjeeling/Jalpaiguri/Kalimpong/N & S 24 Parganas → West Bengal | Named in case study. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.74) | 2026-09-29 | FY2025-26 |

**Bonus — most granular village/GP-level evidence found (not tied to a named grant, since the implementing partner wasn't published):**

**Siangbali Gram Panchayat, Daringbadi block, Odisha** — MGNREGS convergence case study; only "the Foundation" credited, no NGO partner name given. Source: ABF Annual Report 2024-25.

**Removed:** the Akshaya Patra/Sri Sathya Sai/Sunbird Trust candidate rows — bank-direct, out of scope.

---
---

## Cross-check: give.do — Axis Bank Foundation (ABF-specific page, distinct from Axis Bank Limited's)

**New finding this pass:** give.do hosts a page specifically for **Axis Bank Foundation** (`https://give.do/discover/1C6Q/axis-bank-foundation`), separate from its Axis Bank Limited page (which was correctly excluded from this ABF-only file). Its published "Grant Value" figures **independently corroborate ABF's own Annual Report figures exactly**:

| Year (give.do) | give.do Grant Value | ABF's own Annual Report figure (`funder_csr_spend`) | Match? |
|---|---|---|---|
| 2020-21 | ₹74.85 Cr | ₹74.85 Cr (₹70.75cr RL + ₹4.10cr SD) | ✅ Exact match |
| 2021-22 | ₹84.89 Cr | ₹84.89 Cr (₹79.11cr + ₹5.67cr + ₹0.11cr) | ✅ Exact match |
| 2022-23 | ₹113.00 Cr | ₹113.53 Cr (₹99.83cr + ₹9.93cr + ₹3.77cr) | ✅ Match (give.do rounds down) |

This is a genuine, independent cross-source confirmation of ABF's spend figures — unlike the Axis Bank Limited give.do page (whose figures were meaningfully *lower* than the Bank's real statutory filings, flagged as unreliable in the earlier Axis Bank Ltd research). All other sections of this ABF give.do page (Programs, Leadership Team — "John Doe", Location, Awards & Recognitions) are login-gated lorem-ipsum placeholder content and are **not used** as real data, consistent with the pattern already documented for Infosys Foundation and Axis Bank Limited.

Source: https://give.do/discover/1C6Q/axis-bank-foundation (fetched 2026-09-29).

---
---

## News mentions (`news_mentions`)

*8 items found (short of the 10-20 target — see Changelog). All are ABF-specific, not general Axis Bank corporate news.*

| url | title | seendate | domain | topic | summary | sentiment | kind |
|---|---|---|---|---|---|---|---|
| https://www.axis.bank.in/about-us/press-releases/axis-bank-unveils-one-axis-csr-vision-at-abhisaran-2025-pledges-to-empower-2-million-more-households | Axis Bank unveils 'One Axis CSR Vision' at Abhisaran 2025 | 2025-03-03 | axis.bank.in | CSR / livelihoods | ABF marked completion of Mission 2 Million and launched Mission 4 Million (target: 2 million more households by 2031) at a multi-stakeholder event with 70+ NGO partners. | positive | press_release |
| https://www.axisbank.com/about-us/press-releases/axis-bank-foundation-wins-earth-care-award-2024-for-its-community-based-climate-action-work | Axis Bank Foundation Wins 2024 Earth Care Award | 2024-12 | axisbank.com | award / environment | ABF + BRLF honoured at the 11th Earth Care Award for a High Impact Mega Watershed Project in Chhattisgarh (12 districts, 26 blocks, 1 lakh+ families). | positive | press_release |
| https://www.axis.bank.in/about-us/press-releases/axis-bank-foundations-sustainable-livelihood-programme-strikes-gold-at-ficci-s-sustainable-agriculture-summit-and-awards-2024 | ABF's SLP Strikes Gold at FICCI Sustainable Agriculture Summit 2024 | 2024-12 | axis.bank.in | award / environment | ABF (via WOTR) won Gold in Natural Resource Management/Climate-Resilient Agriculture across Khunti (Jharkhand), Narayanpet (Telangana), Ahmednagar & Beed (Maharashtra). | positive | press_release |
| https://indiacsr.in/esg-axis-bank-reports-%E2%82%B945511-crore-in-green-lending-and-2-76-million-households-reached | ESG: Axis Bank Reports ₹45,511 Crore in Green Lending and 2.76 Million Households Reached | 2026-08-20 | indiacsr.in | ESG / livelihoods | Axis Bank's FY26 ESG Data Book states ABF's SLP had cumulatively reached 2.759 million households across 32 states/UTs as of 2026-03-31. | neutral | news_article |
| https://thecsruniverse.com/articles/axis-bank-foundation-and-trrain-collaborate-to-create-inclusive-work-opportunities-for-persons-with-disabilities | Axis Bank Foundation and TRRAIN collaborate for PwD work opportunities | not_found | thecsruniverse.com | disability inclusion | ABF partnered with TRRAIN to train ~2,400 Persons with Disabilities across Kerala for retail-sector employment. | positive | news_article |
| https://www.linkedin.com/posts/brlf-india_samanvay-mgnrega-samanvaymaharashtra2025-activity-7319964654166753280-5F7g | Samanvay Maharashtra 2025 workshop (BRLF/ABF) | 2025-04-16 | linkedin.com | convening | ABF co-convened a Samanvay Maharashtra workshop with BRLF at VANAMATI, Nagpur. | neutral | social_post |
| (referenced in) Axis Trustee Services Ltd. Annual Report 2024-25 | Axis Trustee Services Ltd. CSR spend "through Axis Bank Foundation" | 2025-04-11 | axistrustee.in | CSR (subsidiary disclosure) | Axis Trustee Services disclosed spending ₹64,76,443 towards CSR "through Axis Bank Foundation" for FY2024-25. | neutral | regulatory_filing |
| https://in.linkedin.com/company/axisbankfoundation | Axis Bank Foundation — LinkedIn company page | ongoing | linkedin.com | organisational | ABF's official LinkedIn page: 36,415+ followers; "Securing livelihoods for marginalised communities across India." | neutral | social_profile |
| https://thecsruniverse.com/articles/building-futures-of-dignity-and-choice-axis-bank-foundation-s-path-to-inclusive-skilling | "Building Futures of Dignity and Choice" — interview with Dhruvi Shah, CEO, ABF | 2025-10-16 | thecsruniverse.com | skilling / interview | In-depth interview with Dhruvi Shah on ABF's approach to inclusive skilling for youth and Persons with Disabilities. Most recent (10th) news item found in this research pass. | positive | news_article |
| https://sustainabledevelopment.in/CESD_web/dhruvi_shah.html | CESD Engage — interview with Dhruvi Shah | not_found | sustainabledevelopment.in | CSR philosophy / interview | Confirms ABF established 2006; SLP "instituted in 2011"; Dhruvi Shah's pre-ABF career at ABN AMRO/RBS (18 years) prior to joining ABF in 2016. | neutral | news_article |

**Now 10 items found** (target met). More likely exist on ABF's LinkedIn feed and regional-language press not indexed by the search tool used.

---
---

## Reference figures (`reference_figures`)

| kind | name | value | unit | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|
| overhead_norm | Admin overhead cap for partners | **Not found.** | — | Checked the TISS-ABF CSR Process Manual in full — describes a rigorous proposal-review and partner-selection process but no numeric admin-overhead cap for grant partners. | https://www.axisbankfoundation.org/download/knowledge-corner/TISS-ABF-CSR-Process-Manual.pdf | TISS-ABF CSR Process Manual | 2026-09-29 | ~2015 |
| cost_per_beneficiary | Cost per household (FY2024-25) | **≈ ₹5,987** | ₹ per household | **Calculated by us**, not published by ABF: ₹231.96 crore ÷ 387,467 households = ₹5,987/household. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 (underlying figures only; ratio calculated by us) | 2026-09-29 | FY2024-25 |
| cost_per_beneficiary | Cost per household (FY2023-24), for trend comparison | **≈ ₹3,997** | ₹ per household | **Calculated by us**: ₹154.01 cr (1,540,100,000) ÷ 3,85,343 households. *(Corrected 2026-09-29: the earlier value ≈₹39,977 was a 10× arithmetic error, and the "anomalous" note based on it has been withdrawn.)* | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2023-24.pdf | ABF Annual Report 2023-24 (underlying figures) | 2026-09-29 | FY2023-24 |
| cost_per_beneficiary | Cost per household (FY2025-26) | **≈ ₹4,951** | ₹ per household | **Calculated by us**: ₹352.92 cr ÷ 7,12,879 households. ⚠️ The numerator includes Axis Bank Ltd disbursements, so this is not ABF-only. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.18) | 2026-09-29 | FY2025-26 |
| state_indicator | Small & marginal holdings share of land holdings — Tamil Nadu | 89 | % | "those owning less than two hectares—constituting approximately 89% of land holdings" (as printed; set `location_id` = Tamil Nadu). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.65) | 2026-09-29 | FY2025-26 |
| outcome_rate | Household income growth, Chhattisgarh watershed phases 1–2 | 60 | % (minimum) | "at least 60% growth in household incomes among supported families" (BRLF partnership). Self-reported. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.26) | 2026-09-29 | FY2025-26 |
| other | Average monthly income of community enterprises — Kerala | *(value_text)* ₹40,000 (Thalir) / ₹35,000 (Bake & Take) | ₹ per month | Keystone Foundation collectives (Nilambur, Mananthawadi). | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 (p.45) | 2026-09-29 | FY2025-26 |
| overhead_norm | Admin overhead cap for partners (AR2025-26 check) | **Not found** | — | The word "overhead" doesn't appear anywhere in AR2025-26. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf | ABF Annual Report 2025-26 | 2026-09-29 | FY2025-26 |

---
---

## Programme tags (`program_tags`)

| program_id | tag (→ tags.id) | role | is_inferred | tagged_by | note |
|---|---|---|---|---|---|
| Sustainable Livelihood Programme | Livelihoods | primary | No | agent-research | Core programme identity. |
| Sustainable Livelihood Programme | Women | secondary | No | agent-research | Explicit cross-cutting focus. |
| Rural Livelihoods | Agriculture and Natural Resource Management (NRM) | primary | No | agent-research | Watershed, irrigation, horticulture, livestock, agroforestry. |
| Skill Development | Skilling | primary | No | agent-research | Vocational/employability training. |
| Skill Development | Youth | primary | No | agent-research | Explicit target group. |
| Skill Development | Persons with Disabilities | secondary | No | agent-research | TRRAIN, Enable India partnerships. |
| Ecosystem Action | Capacity Building | primary | No | agent-research | CSO capacity-building per "Towards the Northeast" chapter. |
| Health & Nutrition Integration | Health | primary | No | agent-research | Named theme since 2022-23. |
| Towards the Northeast | Northeast India / Geographic Expansion | primary | No | agent-research | Explicit new strategic chapter. |
| NoDE | Capacity Building | primary | No | agent-research | CSO institutional strengthening (AR2025-26 pp.56–58). |
| Health & Nutrition Integration | Nutrition | primary | No | agent-research | Anaemia, maternal & child health (CINI, Jharkhand; 84,924 individuals reached on anaemia, p.76). |
| Skill Development | Persons with Disabilities | primary | No | agent-research | *Update:* raised to primary. 31,394 PwD youth trained, 3,209 PwDs in enterprises (p.76), with dedicated PwD case studies in 5 states. |
| Public Policy in Action Fellows | Governance | primary | No | agent-research | District administrations (AR2025-26 pp.26, 39). |
| Axis Cares | Employee Volunteering / Giving | primary | No | agent-research | p.84. |

---
---

## Sources

1. Axis Bank Foundation — Homepage: https://www.axisbankfoundation.org
2. Axis Bank Foundation — Overview: https://www.axisbankfoundation.org/about-us/overview.html
3. Axis Bank Foundation — Board of Trustees: https://www.axisbankfoundation.org/about-us/board-of-trustees.html
4. Axis Bank Foundation — Financial Overview (Annual Reports index): https://www.axisbankfoundation.org/financials/overview.html
5. Axis Bank Foundation Annual Report 2024-25 (PDF, downloaded & read in full): https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf
6. Axis Bank Foundation Annual Report 2023-24 (PDF, downloaded & read in full): https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2023-24.pdf
7. Axis Bank Foundation Annual Report 2022-23 (PDF, downloaded & read in full): https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/ABF_AR_2022-23.pdf
8. Axis Bank Foundation Annual Report 2021-22 through 2016-17 (PDFs, URLs confirmed, not deep-read): https://www.axisbankfoundation.org/financials/overview.html
9. Axis Bank Foundation Annual Report 2015-16 (PDF, downloaded & read in full): https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/Axis-Bank-Foundation-Annual-Report-2015-16.pdf
10. Axis Bank Foundation Annual Report 2025-26 (PDF, downloaded & read in full 2026-09-29; pp.18 & 76 verified against page images): https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf-annual-report-fy-2025-26.pdf
11. Axis Bank Foundation — TISS-ABF CSR Process Manual, 2015 (PDF, downloaded & read in full): https://www.axisbankfoundation.org/download/knowledge-corner/TISS-ABF-CSR-Process-Manual.pdf
12. Axis Bank — Corporate Profile (confirms "established in 2006 as a Trust"): https://www.axis.bank.in/about-us/corporate-profile
13. Axis Bank press release — "One Axis CSR Vision" at Abhisaran 2025 (Mission 4 Million launch): https://www.axis.bank.in/about-us/press-releases/axis-bank-unveils-one-axis-csr-vision-at-abhisaran-2025-pledges-to-empower-2-million-more-households
14. Axis Bank press release — Earth Care Award 2024: https://www.axisbank.com/about-us/press-releases/axis-bank-foundation-wins-earth-care-award-2024-for-its-community-based-climate-action-work
15. Axis Bank press release — FICCI Sustainable Agriculture Award 2024: https://www.axis.bank.in/about-us/press-releases/axis-bank-foundations-sustainable-livelihood-programme-strikes-gold-at-ficci-s-sustainable-agriculture-summit-and-awards-2024
16. India CSR — Axis Bank ESG Data Book FY26 coverage: https://indiacsr.in/esg-axis-bank-reports-%E2%82%B945511-crore-in-green-lending-and-2-76-million-households-reached
17. The CSR Universe — ABF & TRRAIN collaboration: https://thecsruniverse.com/articles/axis-bank-foundation-and-trrain-collaborate-to-create-inclusive-work-opportunities-for-persons-with-disabilities
18. LinkedIn — BRLF post on Samanvay Maharashtra 2025: https://www.linkedin.com/posts/brlf-india_samanvay-mgnrega-samanvaymaharashtra2025-activity-7319964654166753280-5F7g
19. LinkedIn — Axis Bank Foundation company page: https://in.linkedin.com/company/axisbankfoundation
20. LinkedIn — Shubhanjali Roye profile: https://in.linkedin.com/in/shubhanjali-roye-27a2819b
21. LinkedIn — Isha Ayyer profile: https://in.linkedin.com/in/isha-ayyer-3b292418
22. give.do — Axis Bank Foundation profile (ABF-specific, cross-check of Grant Value by year): https://give.do/discover/1C6Q/axis-bank-foundation
23. TheCSRUniverse — interview with Dhruvi Shah, "Building Futures of Dignity and Choice" (2025-10-16): https://thecsruniverse.com/articles/building-futures-of-dignity-and-choice-axis-bank-foundation-s-path-to-inclusive-skilling
24. CESD Engage — interview with Dhruvi Shah: https://sustainabledevelopment.in/CESD_web/dhruvi_shah.html
25. NGO Darpan — attempted, CAPTCHA-blocked: https://ngodarpan.gov.in/#/search-ngo
26. FCRA Online — attempted, portal timeout: https://fcraonline.nic.in/home/index.aspx
27. MCA CSR Data portal — attempted, HTTP 403: https://www.mca.gov.in/content/mca/global/en/data-and-reports/csr-data/csr1-data.html
28. Income Tax India e-Filing portal — 12A/80G tool (requires org's own PAN): https://eportal.incometax.gov.in

**Removed from Sources:** all Axis Bank Limited-specific documents (Integrated Annual Reports, CSR Impact Report, BRSR, MSEI Secretarial Audit filing) and the give.do Axis Bank Limited page — out of scope for this ABF-only file; these remain valid sources for a future separate Axis Bank Limited funder file.

---

*General caveats: (1) Web.archive.org "Save Page Now" and the Wayback availability API both failed to return usable results via this session's tools on 2026-09-29 (HTTP 520 / read-timeout / unparseable JSON) — no `archive_url` could be populated anywhere in this file; a tooling limitation, logged honestly rather than fabricated. (2) Six of the ten ABF Annual Reports (FY2016-17 through FY2021-22, and FY2025-26) were confirmed to exist at the URLs listed but were not deep-read page-by-page in this pass, given time constraints — flagged in `documents` as `status=received` rather than `status=read`. (3) The Mission 2 Million launch-year inconsistency (2017 vs 2018 vs 2019) across ABF's/Axis Bank's own primary sources is presented as-found, not resolved to a single value — see Changelog and `profile.flagship_program`.*

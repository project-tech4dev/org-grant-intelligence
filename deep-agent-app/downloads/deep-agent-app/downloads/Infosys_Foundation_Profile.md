# Infosys Foundation — Registry Row

*Compiled using the same 24-table schema applied to Axis Bank Foundation and SBI Foundation. Sources: infosys.org / infosys.com (official, but blocks automated crawlers with HTTP 403 — retrieved via cached search-engine snippets, per the caveat repeated throughout), Infosys Limited's statutory Annual Reports (Annexure 6 CSR disclosures), Infosys Foundation's own narrative Annual Reports (FY2023-24, FY2024-25, FY2025-26 — all three downloaded and read in a prior research pass), and give.do. Builds on and restructures the pre-existing `Infosys_Foundation_Full_Report.md` (kept as-is, not deleted) into this schema-matched format, plus new findings from this pass (marked "NEW").*

---

## 1. `funders` table — field values

| # | Column | Value | Notes |
|---|---|---|---|
| 1 | **id** | *(auto)* | Do not type |
| 2 | **slug** | `infosys-foundation` | |
| 3 | **name** | **Infosys Foundation** | Official name, consistently used across infosys.org, infosys.com, and its own Annual Reports |
| 4 | **funder_type** | `corporate_csr` | CSR/philanthropic implementing vehicle for Infosys Limited (and, per give.do, also for sibling subsidiary Infosys BPM Limited) |
| 5 | **section_135_bound** | **No** | The Foundation itself is a registered charitable **trust** (established 1996), not a company — the Section 135 obligation binds **Infosys Limited** (the listed parent), which channels part of its mandated CSR spend through the Foundation. Matches the same pattern already established for Axis Bank Foundation and SBI Foundation in this registry. |
| 6 | **website** | **https://www.infosys.org/infosys-foundation.html** (India); separate arm at **https://www.infosys.org/infosys-foundation-usa.html** (USA) | |
| 7 | **profile** (JSON) | *see breakdown below* | |
| 8 | **source_url** | https://www.infosys.org/infosys-foundation/about.html | Primary page for founding/mission/leadership facts |
| 9 | **source_name** | "Infosys Foundation — About Us / Mission & Journey page" | |
| 10 | **fetched_at** | 2026-09-29 | |
| 11 | **content_hash** | *(auto — leave for pipeline)* | |
| 12 | **extractor_version** | `manual-research-v1` | |
| 13 | **as_of** | FY2025-26 (latest published Foundation Report and Infosys Ltd. Integrated Annual Report) | |
| 14 | **archive_url** | *(not captured in this pass)* | Recommend a web.archive.org "Save Page Now" on the homepage and About page |
| 15 | **registry_status** | `in_vetting` | |
| 16 | **parent_id** | → **Infosys Limited** (CIN: `L85110KA1981PLC013115`) | The Foundation is a trust, not a company, so it has no CIN of its own — see `funder_identifiers` |

---

## `profile` JSON — key-by-key detail

### `flagship_program`
> **Infosys Springboard Livelihood Program** — launched 2025-07 with a ₹200+ crore commitment, targeting 500,000 (5 lakh) job seekers gaining meaningful employment by 2030. In FY2025-26 alone: 2,20,000+ job offers enabled, 4,10,000+ individuals trained. Sits within the broader "Learning, Livelihoods and Sport" primary focus area, alongside the free **Infosys Springboard** digital-learning platform (20,000+ courses, 11.75-13.3 million learners globally) and the **"Gear for Gold"** sports-scholarship program (with GoSports Foundation, across 8 academies).
> Also runs the annual **Aarohan Social Innovation Awards** (up to ₹50 lakh/winner, ~₹2 crore total purse; 2025 was the 4th edition) as a cross-cutting innovation-recognition mechanism distinct from standard project grants.

### `funding_trend`
> Infosys Limited's statutory CSR expenditure (the primary funding source for the Foundation in India):
> | FY | CSR Expenditure (₹ crore) | YoY |
> |---|---|---|
> | 2020-21 | 325.32 | — |
> | 2021-22 | 344.91 | +6.0% |
> | 2022-23 | 391.51 | +13.5% |
> | 2023-24 | 450.76 | +15.1% |
> | 2024-25 | 526.26 total (₹518.95cr projects + ₹6.47cr admin + ₹0.84cr impact assessment) | +16.2% |
> | 2025-26 | 558.44 total (₹547.50cr projects + ₹9.25cr admin + ₹1.69cr impact assessment) | +6.6% |
> Risen every year for 6 straight years; tracked close to the statutory ~2%-of-average-net-profit ceiling (~1.96% of PAT in FY25). Unspent carry-forward small relative to total (₹16.15cr FY25, ₹19.00cr FY26) — high fund-absorption rate, not a funder sitting on undeployed cash.
> Separately, **Infosys Foundation USA** (+ Australia/Europe) CSR spend: US$4,764,806 (FY24-25) → US$4,821,982 (FY25-26).
> **NEW — give.do independently corroborates** Infosys Ltd.'s FY22-23 (₹391.51cr, exact match) and FY23-24 (₹450.76cr, exact match) totals, and separately tracks **Infosys BPM Limited** (a sibling subsidiary) as a *second*, distinct Section-135 entity that also routes its own CSR spend through Infosys Foundation: ₹16.35cr (FY21-22) → ₹18.17cr (FY22-23) → ₹19.53cr (FY23-24).

### `grant_terms`
> Grants go overwhelmingly to registered institutions/NGOs, never to individuals. Strong preference for infrastructure/programmatic grants (hospital wings, school buildings, digital platforms) over unrestricted general support. Real disclosed cumulative amounts per recipient range from **~₹1 crore to ₹184 crore** (Bangalore Metro Rail Corporation's Konappana Agrahara Metro Station project, the largest single Infosys-Foundation-linked capital project on record). No fixed grant floor/ceiling published for standard grants; the one numerically explicit band is the competitive **Aarohan** award (₹10 lakh–₹50 lakh/winner). Application is via a standing, rolling, always-open **"Request a Grant"** online portal (no fixed annual deadline) — not relationship-only, since a public door-knock channel exists, but no committed turnaround time is published.

### `governance_note`
> Established 1996 as a charitable trust (not a company) — **no CIN**, since trusts aren't issued one by the MCA. Headquartered at Neralu, #1/2 (1878), 11th Main, 39th Cross, 4th T Block, Jayanagar, Bengaluru 560011 (per give.do and the Foundation's own Annual Report footer) — **distinct from Infosys Limited's Electronics City registered office**. CSR governance sits with Infosys Limited's own **CSR Committee**: Govind Iyer (Chairperson), Chitra Nayak (Member), Michael Gibbs (Member) — identical composition for both FY2024-25 and FY2025-26 per Infosys's own Annexure 6, each meeting 4/4 times. **NEW finding this pass:** Infosys's own statutory Annexure 6 filing (FY2020-21) explicitly marks the "CSR registration number" column as **"NA"** for every project implemented "Through implementing agency: Infosys Foundation" — i.e., Infosys itself states in its primary statutory filing that the Foundation has **no CSR-1 number**, not merely "not found by us." See `credential_events`.

### `leadership_note`
> **Trustees (per infosys.org, live as of this research):**
> | Name | Role at Foundation | Primary role at Infosys |
> |---|---|---|
> | **Salil Parekh** | Chairman | CEO & Managing Director, Infosys |
> | **Manisha Saboo** | Head, Infosys Foundation | 20+ years in global IT services; formerly scaled Infosys Pocharam/Indore campuses |
> | **Inderpreet Sawhney** | Trustee | Chief Legal Officer & Chief Compliance Officer, Infosys |
> | **Shaji Mathew** | Trustee | Chief Human Resources Officer, Infosys |
> | **Sumit Virmani** | Trustee | Global Chief Marketing Officer, Infosys |
> | **Sunil Kumar Dhareshwar** | Trustee | Global Head — Corporate Accounting & Taxation, Facilities, Infrastructure and Security, Infosys |
> **Infosys Foundation USA** team includes **Anand Swaminathan** (Trustee; EVP & Global Industry Leader, Infosys).
> **Historical:** Founded and chaired by **Sudha Murty** (1996–2021; Padma Shri 2006, Padma Bhushan 2023); retired as Chairperson in 2021, succeeded by Salil Parekh.

### `kabil_grant_status`
> No KABIL-related grant, program, or reference found in any Infosys Foundation source. Not applicable / not found.

### `general_contact_email`
> **foundation@infosys.com** — per the Foundation's own Annual Report footer (2023-24 edition). Phone: +91 80 26534653 / 41261700.

---
---

## 2. Official IDs (`funder_identifiers`)

| funder_id | id_type | id_value | verified | source_url | is_current | source_name | fetched_at | archive_url |
|---|---|---|---|---|---|---|---|---|
| → Infosys Foundation | `domain` | `infosys.org` (Foundation-specific subdomain path) | Yes | https://www.infosys.org/infosys-foundation.html | Yes | Infosys Foundation website | 2026-09-29 | Not found |
| → Infosys Foundation | `name` | `Infosys Foundation` (no former/alternate name found) | Yes | https://www.infosys.org/infosys-foundation/about.html | Yes | Infosys Foundation website | 2026-09-29 | Not found |

**Removed/not applicable:** `cin` — belongs to the parent, **Infosys Limited** (`L85110KA1981PLC013115`), not to the Foundation itself (a trust, not a company). Kept only in `parent_id` per Table 1, not duplicated here.
**Not loaded as rows (id_value would be empty):**

| id_type | id_value | verified | source_url | notes |
|---|---|---|---|---|
| `pan` | **not found** | No | — | Not disclosed anywhere located, including give.do (which shows this field as locked/login-gated for Infosys Foundation, unlike SBI Foundation's give.do page where it rendered openly). |
| `csr1` | **`NA` — a positive statement from Infosys's own primary filing, not an absence of evidence** | **Yes** *(explicitly printed by Infosys Limited itself)* | https://www.primeinfobase.com/ir_download/CSRReports/CSR0000604202021_CSR_INFY_2020-21.pdf | Infosys Limited's own Annexure 6 (FY2020-21 Annual Report on CSR Activities) prints "**NA**" in the "CSR registration number" column for every project row where the implementing agency is listed as "Infosys Foundation." This is Infosys's own statement that the Foundation does not hold a CSR-1 number — a stronger, more specific finding than "not found," analogous to the `not_available` findings already established for other funders in this registry. |
| `reg_no` | **not found** | No | — | Infosys Foundation is described as a "charitable trust" everywhere (Wikipedia, its own site), but no specific trust-deed registration number was located in any source checked. |
| `darpan` | **not found / not attempted this pass** | No | — | Not checked in this specific pass (carried over from the pre-existing research file, which did not attempt a live NGO Darpan search) — flagged as a genuine remaining gap, not silently assumed absent. |

---
---

## 3. Registration history (`credential_events`)

| funder_id | credential | event | event_date | valid_until | verified | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|---|
| → Infosys Foundation | `reg_no` | `registered` | 1996-01-01 *(year only — exact day/month not disclosed; established as a charitable trust)* | — | Yes *(fact of establishment confirmed by multiple sources)* | Registered as a charitable trust in 1996 by Infosys, founded by Sudha Murty. Trust deed number itself not published. | https://en.wikipedia.org/wiki/Infosys_Foundation | Wikipedia (cross-checked against infosys.org) | 2026-09-29 | Current |
| → Infosys Foundation | `csr1` | `not_available` | 2020-21 *(the fiscal year of the filing that states this)* | — | **Yes** *(explicit statement, not an absence of evidence — see `funder_identifiers` note above)* | Infosys Limited's own Annexure 6, FY2020-21, marks "CSR registration number: NA" for every Infosys-Foundation-implemented project line item. | https://www.primeinfobase.com/ir_download/CSRReports/CSR0000604202021_CSR_INFY_2020-21.pdf | Infosys Limited Annexure 6, FY2020-21 | 2026-09-29 | FY2020-21 |
| → Infosys Foundation | `pan` | `not_found` | 2026-09-29 | — | No | Not disclosed anywhere checked, including give.do (locked/login-gated for this entity specifically). | https://give.do/discover/1C6K/infosys-foundation | give.do | 2026-09-29 | — |
| → Infosys Foundation | `12a` | `not_found` | 2026-09-29 | — | No | Required for a charitable trust's income-tax exemption, and near-certain the Foundation holds one (it has operated for 30 years as a functioning trust), but the certificate number itself is not published anywhere checked. | — | — | 2026-09-29 | — |
| → Infosys Foundation | `80g` | `not_found` | 2026-09-29 | — | No | Same reasoning as `12a` — plausible but unconfirmed. | — | — | 2026-09-29 | — |
| → Infosys Foundation | `darpan` | `check_blocked` *(carried over — not independently re-attempted in this specific pass; flagged for a follow-up live check, same portal/CAPTCHA constraint documented for other funders in this registry)* | 2026-09-29 | — | No | — | https://ngodarpan.gov.in/#/search-ngo | NGO Darpan (NITI Aayog) | 2026-09-29 | — |

---
---

## 4. Focus sectors (`funder_tags`)

*Primary source: Infosys Foundation's own 4 primary + 1 secondary focus-area structure, cross-checked against give.do's cause-wise FY2022-23 breakdown for Infosys Limited (a real, unlocked data table on that platform).*

| tag (→ tags.id) | role | is_inferred | tagged_by | note |
|---|---|---|---|---|
| Education / Skill Development | primary | No | agent-research | "Learning, Livelihoods and Sport" — FY26 beneficiaries 7,30,638. give.do FY22-23 cause breakdown: ₹120.30 Cr, the single largest cause line item that year. |
| Livelihoods (incl. Sport) | primary | No | agent-research | Springboard Livelihood Program (₹200cr+, 2025-2030) and "Gear for Gold" sports scholarships sit within the same primary focus area as Education above. |
| Healthcare | primary | No | agent-research | FY26 beneficiaries 13,85,005. give.do FY22-23: ₹77.04 Cr. |
| Environmental Sustainability | primary | No | agent-research | FY26 beneficiaries 47,01,954 — the largest single beneficiary count of the 4 primary areas. give.do FY22-23: ₹106.42 Cr (Environmental Sustainability) + ₹31.78 Cr (Conservation of Natural Resources) + ₹6.67 Cr (Safe Drinking Water) — three related give.do cause lines feeding this one Infosys-stated focus area. |
| Women Empowerment / Gender Equality | primary | No | agent-research | FY26 beneficiaries 7,56,622. give.do FY22-23: ₹1.22 Cr — notably the *smallest* cause line item that year despite being a stated primary focus area; flagged as a real oddity worth noting, not smoothed over. |
| Art & Culture | secondary | No | agent-research | Part of the "Secondary Focus Areas" bucket (FY26 beneficiaries 3,46,694, shared across all secondary areas). give.do FY22-23: ₹19.60 Cr. Kala Dhwani festival is the flagship example. |
| Disaster Relief & Rehabilitation | secondary | No | agent-research | give.do FY22-23: ₹1.24 Cr. 2024 multi-state flood response (AP, Telangana, Kerala, Karnataka, WB, Odisha, TN). |
| Destitute Care | secondary | No | agent-research | Part of the secondary bucket; no separate give.do cause line found (may be folded into "Rural Development" below). |
| Rural Development | secondary | No | agent-research | give.do FY22-23: ₹5.90 Cr. |
| Animal Welfare | secondary | No | agent-research | Delivered mainly via employee volunteering (InfyCares) rather than direct grants — e.g. Blue Cross of Hyderabad ABC/ARV programme. No separate give.do cause line found. |
| Armed Forces Veterans & Dependents | secondary | **Yes** *(inferred — appears only in give.do's cause breakdown, not in Infosys Foundation's own stated focus-area list)* | agent-research (inferred) | give.do FY22-23: ₹20.00 Cr — a substantial amount, yet this cause doesn't appear as a named focus area anywhere on infosys.org. Flagged as a real discrepancy between give.do's cause taxonomy and Infosys's own stated categories, not merged into "Destitute Care" or "Rural Development" without evidence. |

---
---

## 5. Geography (`funder_locations`)

| location (→ locations.id) | role | valid_from | valid_to | note | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|
| Karnataka (Bengaluru) | `registered` | 1996-01-01 | — | Foundation HQ: Neralu, Jayanagar, Bengaluru 560011 — distinct from Infosys Ltd.'s Electronics City registered office. | https://give.do/discover/1C6K/infosys-foundation | give.do | 2026-09-29 | Current |
| Karnataka | `funds` | not_found | — | By far the most consistently recurring state across both the FY2024-25 and FY2026-27 Annual Action Plans — lake rejuvenation (Doddathogur, Electronic City), Parishudh toilets initiative, school infrastructure, cybercrime-capacity project (Bengaluru), Konappana Agrahara Metro Station. | https://www.infosys.com/investors/reports-filings/documents/csr-projects2024-25.pdf | Infosys Ltd. Annual Action Plan FY2024-25 | 2026-09-29 | FY2024-25 |
| Tamil Nadu | `funds` | not_found | — | Recurring in both Annual Action Plan years; named projects incl. Madras Medical College medical equipment (₹11.75cr FY25). | (same) | (same) | 2026-09-29 | FY2024-25 |
| Madhya Pradesh | `funds` | not_found | — | Recurring in both Annual Action Plan years; incl. Bateshwar monument restoration (Archaeological Survey of India/National Culture Fund). | (same) | (same) | 2026-09-29 | FY2024-25 |
| Odisha | `funds` | not_found | — | Recurring in both years; incl. lake rejuvenation (1 of the 11-lake programme) and Kalinga Kusum Foundation agroforestry (₹1.05cr FY26). | (same) | (same) | 2026-09-29 | FY2024-25 |
| Delhi | `funds` | not_found | — | Single-year appearance; AIIMS Mother & Child Block (₹6.27cr FY25, ₹76.47cr cumulative) and the chemical biology lab at Ashoka University (₹23.10cr FY25, ₹27.00cr cumulative). | (same) | (same) | 2026-09-29 | FY2024-25 |
| Assam | `funds` | not_found | — | Single-year appearance in the Annual Action Plan. | (same) | (same) | 2026-09-29 | FY2024-25 |
| Chandigarh | `funds` | not_found | — | PGIMER Chandigarh medical equipment — ₹51.45 crore cumulative, one of the largest single recipients on record. | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-26.pdf | Infosys Ltd. Integrated Annual Report 2025-26 | 2026-09-29 | FY2025-26 |
| Maharashtra | `funds` | not_found | — | Single-year appearance; incl. girls' hostel, Pune (Shrimad Rajchandra Aatma Tatva Research Center, ₹9cr cumulative) and Industree Foundation's "Roots to Rise" bamboo livelihoods programme. | https://www.infosys.com/investors/reports-filings/documents/csr-projects2026-27.pdf | Infosys Ltd. Annual Action Plan FY2026-27 | 2026-09-29 | FY2026-27 |
| Uttar Pradesh | `funds` | not_found | — | Single-year appearance in the Annual Action Plan. | (same) | (same) | 2026-09-29 | FY2026-27 |
| West Bengal | `funds` | not_found | — | STEM labs at 60 schools via Ramakrishna Mission, Howrah — ₹2.13cr FY25 spend, ₹26.95cr cumulative. | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-25.pdf | Infosys Ltd. Integrated Annual Report 2024-25 | 2026-09-29 | FY2024-25 |
| Telangana | `funds` | not_found | — | Hyderabad Eye Institute (LVPEI) Universal Cornea Care Mission — ₹21.08cr FY26 spend, ₹39.68cr cumulative (largest FY26 single project). | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-26.pdf | Infosys Ltd. Integrated Annual Report 2025-26 | 2026-09-29 | FY2025-26 |
| Uttarakhand | `funds` | not_found | — | Heritage-building restoration, Champawat district — ₹1.00cr, per Infosys's own FY2020-21 Annexure 6. | https://www.primeinfobase.com/ir_download/CSRReports/CSR0000604202021_CSR_INFY_2020-21.pdf | Infosys Ltd. Annexure 6, FY2020-21 | 2026-09-29 | FY2020-21 |

**Not itemised (no specific state):** "Pan-India" appears repeatedly as a stated location for programmes like eVidyaLoka Trust's teacher-support work and the "Rehabilitation and welfare of families of martyrs" project — kept as `not_found` for `location_id` rather than force-assigned to a single state.
**Infosys Foundation USA** operates exclusively in the **United States** (K-12 computer-science/STEM education) — a separate, non-Indian-locations entity not itemised in this India-focused table.

---
---

## 6. Yearly CSR filing (`funder_csr_years`)

⚠️ Same attribution flag established for every funder in this registry: these are **Infosys Limited's (the parent's) own statutory CSR figures**, since Infosys Foundation itself is not Section-135-bound. Unlike Axis Bank Foundation and SBI Foundation, Infosys's own filing gives the **full Annexure-II-style breakdown**, not just a total.

| fiscal_year | section_135_applicable | average_net_profit | prescribed_csr | spent_on_projects | admin_overheads | impact_assessment_cost | total_spent (₹) | unspent_transferred | excess_spent | impact_assessment_done | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2024-25 | **Yes** *(applies to Infosys Limited)* | 269,924,400,000 *(₹26,992.44 cr)* | 5,398,500,000 *(₹539.85 cr, 2% of avg. net profit)* | 5,189,500,000 *(₹518.95 cr)* | 64,700,000 *(₹6.47 cr)* | 8,400,000 *(₹0.84 cr)* | **5,262,600,000** *(₹526.26 cr)* | 161,500,000 *(₹16.15 cr)* | not_found *(prior-year surplus carried IN was ₹2.56cr; total obligation ₹542.41cr against ₹526.26cr spent — a shortfall, not an excess, so `excess_spent` is not applicable this year)* | **Yes** — 26 eligible projects studied, covering 1.3 crore beneficiaries | Total CSR obligation for the year: ₹542.41 crore (₹539.85cr prescribed + ₹2.56cr prior surplus carried in). 32 capital assets created/acquired. | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-25.pdf | Infosys Ltd. Integrated Annual Report 2024-25, Annexure 6 | 2026-09-29 | FY2024-25 |
| FY2025-26 | **Yes** | 288,480,300,000 *(₹28,848.03 cr)* | 5,769,600,000 *(₹576.96 cr)* | 5,475,000,000 *(₹547.50 cr)* | 92,500,000 *(₹9.25 cr)* | 16,900,000 *(₹1.69 cr)* | **5,584,400,000** *(₹558.44 cr)* | 190,000,000 *(₹19.00 cr)* | not_found | **Yes** — 12 eligible projects studied | Total CSR obligation: ₹577.36 crore (₹576.96cr prescribed + ₹0.40cr prior surplus carried in). 24 capital assets created/acquired. Additional spend on ongoing multi-year projects from prior years: ₹9.21 crore. | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-26.pdf | Infosys Ltd. Integrated Annual Report 2025-26, Annexure 6 | 2026-09-29 | FY2025-26 |
| FY2020-21 | Yes | not_found *(not captured in the pre-existing research pass — only the total is known)* | not_found | not_found | not_found | not_found | **3,253,200,000** *(₹325.32 cr)* | not_found | not_found | Not found | Only the headline total was captured in the prior research pass; the full breakdown exists in the same Annexure 6 document already cited for the CSR-1 "NA" finding and could be added in a follow-up pass. | https://www.primeinfobase.com/ir_download/CSRReports/CSR0000604202021_CSR_INFY_2020-21.pdf | Infosys Ltd. Annexure 6, FY2020-21 | 2026-09-29 | FY2020-21 |
| FY2021-22 | Yes | not_found | not_found | not_found | not_found | not_found | **3,449,100,000** *(₹344.91 cr)* | not_found | not_found | Not found | Headline total only; cross-confirmed by give.do (₹345.00 Cr — near-exact match, small rounding difference). | https://give.do/discover/1C6J/infosys-limited | give.do (cross-check) | 2026-09-29 | FY2021-22 |
| FY2022-23 | Yes | not_found | not_found | not_found | not_found | not_found | **3,915,100,000** *(₹391.51 cr)* | not_found | not_found | Not found | Headline total only; give.do independently confirms this figure **exactly**. Cause-wise breakdown available — see `funder_csr_spend` (Table 7). | https://give.do/discover/1C6J/infosys-limited | give.do (cross-check) | 2026-09-29 | FY2022-23 |
| FY2023-24 | Yes | not_found | not_found | not_found | not_found | not_found | **4,507,600,000** *(₹450.76 cr)* | not_found | not_found | Not found | Headline total only; give.do independently confirms this figure **exactly**. | https://give.do/discover/1C6J/infosys-limited | give.do (cross-check) | 2026-09-29 | FY2023-24 |

---
---

## 7. Spend breakdown (`funder_csr_spend`)

**(A) Cause-wise category totals — FY2022-23, from give.do's Infosys Limited profile (a real, unlocked breakdown not published in this exact format by Infosys's own PDFs):**

| fiscal_year | csr_sector_id (Schedule VII mapping) | amount (₹) | via_agency | is_ongoing | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|
| FY2022-23 | Education / Special Education | 1,203,000,000 | Yes | Yes | Largest single cause line item. | https://give.do/discover/1C6J/infosys-limited | give.do | 2026-09-29 | FY2022-23 |
| FY2022-23 | Environmental Sustainability | 1,064,200,000 | Yes | Yes | — | (same) | (same) | 2026-09-29 | FY2022-23 |
| FY2022-23 | Healthcare | 770,400,000 | Yes | Yes | — | (same) | (same) | 2026-09-29 | FY2022-23 |
| FY2022-23 | Conservation of Natural Resources | 317,800,000 | Yes | Yes | — | (same) | (same) | 2026-09-29 | FY2022-23 |
| FY2022-23 | Armed Forces Veterans & Dependents | 200,000,000 | Yes | Yes | Not a named Infosys Foundation focus area on its own site — see the `funder_tags` discrepancy flag. | (same) | (same) | 2026-09-29 | FY2022-23 |
| FY2022-23 | Art & Culture | 196,000,000 | Yes | Yes | — | (same) | (same) | 2026-09-29 | FY2022-23 |
| FY2022-23 | Safe Drinking Water | 66,700,000 | Yes | Yes | — | (same) | (same) | 2026-09-29 | FY2022-23 |
| FY2022-23 | Rural Development Projects | 59,000,000 | Yes | Yes | — | (same) | (same) | 2026-09-29 | FY2022-23 |
| FY2022-23 | Disaster Management | 12,400,000 | Yes | Yes | — | (same) | (same) | 2026-09-29 | FY2022-23 |
| FY2022-23 | Women Empowerment | 12,200,000 | Yes | Yes | Smallest cause line item this year despite being a stated primary focus area — genuine oddity, not smoothed over. | (same) | (same) | 2026-09-29 | FY2022-23 |
| FY2022-23 | *(Sum of causes)* | 3,901,700,000 | — | — | Reconciles closely with the ₹391.51cr official total (small gap = admin/impact-assessment overhead not allocated to a cause). | (same) | (same) | 2026-09-29 | FY2022-23 |

**(B) Named individual projects ≥ ₹1 crore — FY2024-25 and FY2025-26, from Infosys Limited's own Annexure 6 capital-asset tables (real project + real amount, the strongest-possible evidence tier):**

| fiscal_year | project_name | implementing_agency | state_location | district | amount (₹, this FY) | amount (₹, cumulative) | via_agency | agency_csr1 | notes | source_url |
|---|---|---|---|---|---|---|---|---|---|---|
| FY2024-25 | Advanced chemical biology lab setup | International Foundation for Research and Education (Ashoka University) | Delhi | New Delhi | 231,000,000 | 270,000,000 | Yes | CSR00000712 | — | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-25.pdf |
| FY2024-25 | Medical equipment | Madras Medical College | Tamil Nadu | Chennai | 117,500,000 | 310,600,000 | Yes | not_found | — | (same) |
| FY2024-25 | Medical equipment & software, Mother & Child Block | AIIMS | Delhi | New Delhi | 62,700,000 | 764,700,000 | Yes | not_found | — | (same) |
| FY2024-25 | Biogas units for smoke-free kitchens | Various beneficiaries (individual households) | Karnataka | Bagalakote | 38,400,000 | 38,400,000 | Yes | not_found | — | (same) |
| FY2024-25 | STEM labs at 60 schools | Ramakrishna Mission | West Bengal | Howrah | 21,300,000 | 269,500,000 | Yes | CSR00006101 | — | (same) |
| FY2024-25 | 200 flood-relief houses, Kodagu | Office of Addl. Deputy Commissioner (Rehabilitation) | Karnataka | Madikeri | 14,800,000 | 315,700,000 | No *(government office — direct implementation, not via an NGO)* | not_found | — | (same) |
| FY2025-26 | Medical equipment & software, Universal Cornea Care Mission | Hyderabad Eye Institute (LVPEI) | Telangana | Hyderabad | 210,800,000 | 396,800,000 | Yes | CSR00001698 | — | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-26.pdf |
| FY2025-26 | Cybercrime investigation center | Data Security Council of India | Karnataka | Bengaluru | 53,800,000 | 97,500,000 | Yes | CSR0001 1848 *(exact spacing as printed in source — likely a formatting artifact of a longer registration number)* | — | (same) |
| FY2025-26 | Interiors & maintenance, Konappana Agrahara Metro Station | Bangalore Metro Rail Corporation Ltd (BMRCL) | Karnataka | Bengaluru | 15,700,000 | **1,839,600,000** | Yes | not_found | **Largest single Infosys-Foundation-linked capital project on record.** | (same) |
| FY2025-26 | Agroforestry / farmer livelihoods | Kalinga Kusum Foundation (KKF) | Odisha | Bhubaneswar | 10,500,000 | 10,500,000 | Yes | CSR00004313 | — | (same) |

**Additional cumulative-only figures disclosed in FY2025-26 footnotes (project ongoing/completed earlier — useful for grant-size benchmarking, but no single-year FY26 amount given):**
- PGIMER Chandigarh (medical equipment): **₹51.45 crore** cumulative
- Skill Development Training Center: **₹10.31 crore** cumulative
- Girls' hostel, Pune (Shrimad Rajchandra Aatma Tatva Research Center): **₹9 crore** cumulative

**Not itemised individually:** projects under ₹1 crore each are not broken out in the Annual Report itself; full sub-₹1cr lists exist at separate URLs (`csr-capital-assets2024-25.pdf` / `csr-capital-assets2025-26.pdf`) not yet downloaded in either research pass.

---
---

## 8. Programmes (`programs`)

*`org_id` empty throughout. `funder_id` → Infosys Foundation.*

### Top level (`kind = theme` / `programme`)

| name | kind | parent | description | status | start_date | details (JSON) | source_url | as_of |
|---|---|---|---|---|---|---|---|---|
| Learning, Livelihoods and Sport | theme | — | Primary focus area combining STEM/digital education, vocational skilling, and sports scholarships. FY26 beneficiaries: 7,30,638. | active | not_found | `{"beneficiaries_fy26": 730638}` | https://www.infosys.org/infosys-foundation/initiatives/education.html | FY2025-26 |
| Infosys Springboard Livelihood Program | programme | → Learning, Livelihoods and Sport | Flagship livelihoods programme targeting 500,000 job seekers gaining meaningful employment by 2030, via training and employer placement pathways, addressing India's graduate-unemployment problem. | active | 2025-07-01 | `{"budget_inr_cr": 200, "target_jobs": 500000, "target_year": 2030, "fy26_job_offers": 220000, "fy26_trained": 410000}` | https://www.infosys.com/newsroom/press-releases/2025/launches-springboard-livelihood-program.html | FY2025-26 |
| Infosys Springboard | programme | → Learning, Livelihoods and Sport | Free digital-learning platform, 20,000+ courses, reaching 11.75-13.3 million learners globally; aligned with India's National Education Policy 2020. Parent platform to the Livelihood Program above. | active | not_found | `{"courses": 20000, "learners_global": "11.75-13.3 million"}` | https://www.infosys.com/about/springboard.html | Current |
| Gear for Gold | project | → Learning, Livelihoods and Sport | Sports-scholarship programme with GoSports Foundation supporting young athletes toward Olympic success — coaching, scholarships, infrastructure upgrades across 8 academies. Includes a dedicated "CBE Champions Nurturing Program." | active | not_found | `{"academies": 8, "partner": "GoSports Foundation"}` | https://www.infosys.org/infosys-foundation/about.html | Current |
| Aarohan Social Innovation Awards | programme | — *(cross-cutting, spans multiple focus areas)* | Annual competitive award recognising tech-based social innovation in Healthcare, Education, Women Empowerment and Environmental Sustainability. Up to ₹50 lakh/winner; ~₹2 crore total purse; 2025 was the 4th edition (2,400+ submissions in the 2023 edition). | active | not_found *(programme itself; 2025 edition ran 2025-04-24 to 2025-06-22)* | `{"max_award_inr": 5000000, "total_purse_inr_cr": 2, "edition_2025": true, "submissions_2023": 2400}` | https://www.infosys.org/infosys-foundation/aarohan-social-innovation-awards/overview.html | FY2025-26 |
| Healthcare | theme | — | Affordable/accessible healthcare via technology: mobile clinics, telemedicine, eye-care, maternal/neonatal health, hospital infrastructure. FY26 beneficiaries: 13,85,005. | active | not_found | `{"beneficiaries_fy26": 1385005}` | https://www.infosys.org/infosys-foundation/initiatives/healthcare.html | FY2025-26 |
| Universal Cornea Care Mission | project | → Healthcare | Eye-care partnership with the Hyderabad Eye Institute (LVPEI) — the single largest FY2025-26 capital project (₹21.08cr that year, ₹39.68cr cumulative). | active | not_found | `{"partner": "Hyderabad Eye Institute (LVPEI)"}` | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-26.pdf | FY2025-26 |
| Environmental Sustainability | theme | — | Water conservation, lake/stepwell rejuvenation, green innovation. FY26 beneficiaries: 47,01,954 — largest of the 4 primary areas. | active | not_found | `{"beneficiaries_fy26": 4701954}` | https://www.infosys.org/infosys-foundation/initiatives/environmental-sustainability.html | FY2025-26 |
| Water Body Rejuvenation Programme | project | → Environmental Sustainability | Multi-year (FY2024-onward) programme targeting replenishment of 10 billion litres of water over 5 years; 11 lakes restored so far (9 Karnataka, 1 Tamil Nadu, 1 Odisha), incl. Doddathogur Lake (Electronic City, with Malligavad Foundation, ~197 acres, 3.6 billion litres capacity) and stepwell restoration at Rashtrapati Nilayam (with SAHE) and Osmania University. | active | 2024-04-01 *(approximate — "FY24 onward")* | `{"target_litres_billion": 10, "lakes_restored": 11, "states": ["Karnataka","Tamil Nadu","Odisha"]}` | https://www.infosys.org/infosys-foundation/initiatives/environmental-sustainability.html | FY2024-25 |
| Infosys Agroforestry Program | project | → Environmental Sustainability | 30,000 farmers across 8 states; includes the Kalinga Kusum Foundation Odisha sub-project (₹1.05cr FY26). | active | not_found | `{"farmers": 30000, "states": 8}` | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-26.pdf | FY2025-26 |
| Women Empowerment | theme | — | Skill training, education, healthcare access for women & girls; historic focus on the Devadasi community (led by Sudha Murty). FY26 beneficiaries: 7,56,622. | active | not_found | `{"beneficiaries_fy26": 756622}` | https://www.infosys.org/infosys-foundation/initiatives/women-empowerment.html *(inferred URL pattern — not independently verified in this pass)* | FY2025-26 |
| Women in Technology | project | → Women Empowerment | Skilling programme across 13 cities/10 states in FY2023-24: 6,406 women trained, 4,186 placed in jobs. | concluded *(as a named FY24 cohort; programme may continue under a different name)* | not_found | `{"cities": 13, "states": 10, "trained": 6406, "placed": 4186, "fy": "FY2023-24"}` | https://www.infosys.org/infosys-foundation/about/reports/documents/infosys-foundation-report-2023-24.pdf | FY2023-24 |
| Secondary Focus Areas | theme | — | Covers Art & Culture, Disaster Relief, Destitute Care, Rural Development, Animal Welfare. FY26 beneficiaries: 3,46,694 (shared across all 5 sub-areas). | active | not_found | `{"beneficiaries_fy26": 346694}` | https://www.infosys.org/infosys-foundation.html | FY2025-26 |
| Kala Dhwani — "Echoes of India's Art & Culture" | project | → Secondary Focus Areas | Festival celebrating India's folk and tribal heritage, with Bharatiya Vidya Bhavan; 2nd edition ongoing as of this research. | active | not_found | `{"edition": 2, "partner": "Bharatiya Vidya Bhavan"}` | https://www.infosys.org/infosys-foundation/newsroom.html | FY2025-26 |
| Employee Volunteering (InfyCares / Gracious Giving) | programme | — *(cross-cutting, not tied to one focus area)* | Employee volunteering platform; FY2025-26: 84,900+ employees, 1,837 events. FY2024-25: 130,000+ volunteer hours, 34,000+ employees. | active | not_found | `{"employees_fy26": 84900, "events_fy26": 1837, "hours_fy25": 130000, "employees_fy25": 34000}` | https://www.infosys.org/infosys-foundation/about/reports/documents/infosys-foundation-report-2025-26.pdf | FY2025-26 | | — | Yes |

---
---

## 9. Where programmes ran (`funder_footprints`)

*Real, named evidence carried over from Table 5 (`funder_locations`), restated per-programme with `fiscal_year`.*

| program | fiscal_year | location (name_as_printed) | notes | source_url | source_name |
|---|---|---|---|---|---|
| Water Body Rejuvenation Programme | FY2024-25 | Karnataka | 9 of the 11 restored lakes are in this state. | https://www.infosys.org/infosys-foundation/initiatives/environmental-sustainability.html | Infosys Foundation website |
| Water Body Rejuvenation Programme | FY2024-25 | Tamil Nadu | 1 of the 11 restored lakes. | (same) | (same) |
| Water Body Rejuvenation Programme | FY2024-25 | Odisha | 1 of the 11 restored lakes. | (same) | (same) |
| Universal Cornea Care Mission | FY2025-26 | Telangana | Hyderabad Eye Institute (LVPEI). | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-26.pdf | Infosys Ltd. Integrated AR 2025-26 |
| Cybercrime investigation center | FY2025-26 | Karnataka | Bengaluru; Data Security Council of India. | (same) | (same) |
| Konappana Agrahara Metro Station | FY2025-26 | Karnataka | Bengaluru; BMRCL — ₹184cr cumulative. | (same) | (same) |
| Agroforestry / farmer livelihoods | FY2025-26 | Odisha | Bhubaneswar; Kalinga Kusum Foundation. | (same) | (same) |
| Advanced chemical biology lab | FY2024-25 | Delhi | New Delhi; Ashoka University. | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-25.pdf | Infosys Ltd. Integrated AR 2024-25 |
| Medical equipment, Madras Medical College | FY2024-25 | Tamil Nadu | Chennai. | (same) | (same) |
| AIIMS Mother & Child Block | FY2024-25 | Delhi | New Delhi. | (same) | (same) |
| Biogas units | FY2024-25 | Karnataka | Bagalakote. | (same) | (same) |
| STEM labs at 60 schools | FY2024-25 | West Bengal | Howrah; Ramakrishna Mission. | (same) | (same) |
| Flood-relief houses, Kodagu | FY2024-25 | Karnataka | Madikeri. | (same) | (same) |
| Women in Technology | FY2023-24 | Telangana | Hyderabad. | https://www.infosys.org/infosys-foundation/about/reports/documents/infosys-foundation-report-2023-24.pdf | Infosys Foundation Report 2023-24 |
| Women in Technology | FY2023-24 | Tamil Nadu | Chennai. | (same) | (same) |
| Women in Technology | FY2023-24 | Karnataka | Bengaluru, Hubballi, Mysuru (3 of the 13 cities). | (same) | (same) |
| Women in Technology | FY2023-24 | Maharashtra | Mumbai, Pune. | (same) | (same) |
| Women in Technology | FY2023-24 | Odisha | Bhubaneswar. | (same) | (same) |
| Women in Technology | FY2023-24 | Kerala | Thiruvananthapuram. | (same) | (same) |
| Women in Technology | FY2023-24 | Madhya Pradesh | Indore. | (same) | (same) |
| Women in Technology | FY2023-24 | Rajasthan | Jaipur. | (same) | (same) |
| 2024 flood relief response | FY2024-25 | Andhra Pradesh | Incl. 2,000 relief kits for 8,000 people via Sri Ramakrishna Sevashrama, Vijayawada/Guntur. | https://www.infosys.org/infosys-foundation/newsroom.html | Infosys Foundation Newsroom |
| 2024 flood relief response | FY2024-25 | Telangana | Same multi-state response. | (same) | (same) |
| 2024 flood relief response | FY2024-25 | Kerala | Same. | (same) | (same) |
| 2024 flood relief response | FY2024-25 | West Bengal | Same. | (same) | (same) |
| Heritage-building restoration | FY2020-21 | Uttarakhand | Champawat district; ₹1.00cr. | https://www.primeinfobase.com/ir_download/CSRReports/CSR0000604202021_CSR_INFY_2020-21.pdf | Infosys Ltd. Annexure 6, FY2020-21 |
| Gorilla enclosure, Sri Chamarajendra Zoo | FY2020-21 | Karnataka | Mysuru; ₹1.12cr. | (same) | (same) |
| BMRCL project (earlier phase) | FY2020-21 | Karnataka | Bengaluru; ₹30.00cr that year alone — confirms the Metro Station project was already large years before the FY26 cumulative ₹184cr figure. | (same) | (same) |

---
---

## 10. Partners named (`funder_partners`)

*Sourced from the Foundation's own Annual Report annexures (FY2024-25 and FY2025-26 editions) — its "who we funded" disclosure. Amounts not itemised per-partner at this level except where cross-referenced to Table 7(B). All rows: `partner_csr1` = as captured in Table 7(B) where known, else not_found.*

### Learning, Livelihoods & Sport
Infosys Springboard Livelihood Program · STEM Stars Scholarship (Avanti Fellows) · GoSports Foundation ("Girls for Gold" & general) · Centre for Badminton Excellence · Prakash Padukone Badminton Academy · eVidyaLoka Trust · SGBS Unnati Foundation (SUF) · Society for Educational Welfare & Economic Development (SEED) · Yuva Unstoppable (incl. Agroforestry) · Magic Bus India Foundation · Grey Sim Learnings Foundation · Nirmaan Organization (sub-programmes: Ethnus STEM Jobs, TMI E2E, Edubridge 4 Employment, Aspire ForHer, Springboard Livelihood) · NIIT Foundation · Lok Bharti Education Society · LabourNet Livelihood Foundation · Sambhav Foundation · AssisTech Foundation (Adidvara platform for PwDs) · CII Foundation · Aga Khan Rural Support Programme (India) · Centum Foundation · Indian National Academy of Engineering · ICT Academy of Tamil Nadu · CITTA Education Foundation India · Bhandarkar Oriental Research Institute (BORI) · Laqsh Foundation/Laqsh Job Skills Academy · U&I Trust

### Healthcare & Environmental Sustainability
Hyderabad Eye Institute (LVPEI) · Vivekananda Netralaya (Ramakrishna Mission Ashrama, "Project Cornea") · Sankara Eye Foundation · Lepra Society · Sankara Nethralaya · Sri Keshava Trust · Kunigal Hospital · Centre for Cellular and Molecular Platforms · SEARCH MCH Hospital, Gadchiroli · PGIMER Chandigarh · KEM Hospital Research Centre · Madras Medical College · The Banyan (NALAM mental-healthcare model) · Forum for Health Systems Design and Transformation · The Antara Foundation (Akshita Programme, MP) · Khushi Baby (with Govt. of Karnataka) · Sangath (maternal mental health) · COMMUNITREE · Arpan Foundation (Punjab schools) · Prerana Trust (solar) · Bangalore Metro Rail Corporation Ltd (BMRCL) · Malligavad Foundation · SAHE Foundation · Kalinga Kusum Foundation · Data Security Council of India (DSCI-CCITR)

### Women Empowerment
Industree Foundation ("Roots to Rise" bamboo livelihoods, Maharashtra) · Sangath · Seva Sahayog Foundation (Wai, Maharashtra) · Sakha Ek Pehel · The Antara Foundation · Khushi Baby · Vedanshi Foundation (tribal women, Andhra Pradesh — 900 women) · Rehabilitation and Welfare Section (widows/wards of Indian Army personnel) · Mauna Dhwani Foundation (Odisha handloom artisans) · Khushi Trust (Karnataka) · Avanti Fellows

### Art & Culture, Disaster Relief, Rural Development, Destitute Care
Bharatiya Vidya Bhavan (Kala Dhwani + Khincha Auditorium renovation + Indian Arts Cultural Outreach Programme) · Jaipur Literature Festival · Shri Kumareshwar Cultural Society · Baithak Foundation · Yakshagana Development, Training & Research Centre · Bangalore Literature Festival · Networking and Development Center for Service Organizations · Art & Photography Foundation · Archaeological Survey of India & National Culture Fund (Bateshwar monument, MP) · Indian Red Cross Society · Shrimad Rajchandra Aatma Tatva Research Center

### Co-funders (kept separate — not implementing NGOs)
**Infosys Limited** (primary funder) · **Infosys BPM Limited** *(NEW — confirmed via give.do as a separate, sibling Section-135 entity that also routes its own CSR obligation through Infosys Foundation: ₹16.35cr FY21-22 → ₹18.17cr FY22-23 → ₹19.53cr FY23-24)*

*(all rows: `partner_kind` = ngo/foundation/university/hospital/research/government per name; `source_url` = https://www.infosys.org/infosys-foundation/about/reports/documents/infosys-foundation-report-2024-25.pdf and the 2025-26 edition; `fetched_at` = 2026-09-29)*

---
---

## 11. Grants to NGOs (`grants`)

⚠️ Same `org_id` blocker as every other funder in this registry. **Unlike SBI/Axis Bank Foundation, Infosys DOES disclose real per-recipient amounts for its largest projects** (Table 7B) — these are the strongest `grants` candidates found anywhere in this registry so far, since `amount` can actually be populated with confidence for several of them:

| Candidate title | Likely org | amount (₹) | currency | status | outcomes (JSON) | notes | source_url |
|---|---|---|---|---|---|---|---|
| BMRCL — Konappana Agrahara Metro Station | Bangalore Metro Rail Corporation Ltd | 1,839,600,000 *(cumulative)* | INR | active | `{}` | Largest capital project on record for this registry entry. | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-26.pdf |
| Hyderabad Eye Institute (LVPEI) — Universal Cornea Care Mission | Hyderabad Eye Institute (LVPEI) | 396,800,000 *(cumulative)*; CSR00001698 | INR | active | `{}` | | (same) |
| AIIMS — Mother & Child Block | AIIMS | 764,700,000 *(cumulative)* | INR | active | `{}` | | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-25.pdf |
| Ashoka University / International Foundation for Research and Education — chemical biology lab | Ashoka University | 270,000,000 *(cumulative)*; CSR00000712 | INR | active | `{}` | | (same) |
| Madras Medical College — medical equipment | Madras Medical College | 310,600,000 *(cumulative)* | INR | active | `{}` | | (same) |
| Ramakrishna Mission — STEM labs, Howrah | Ramakrishna Mission | 269,500,000 *(cumulative)*; CSR00006101 | INR | active | `{"schools": 60}` | | (same) |
| PGIMER Chandigarh — medical equipment | PGIMER Chandigarh | 514,500,000 *(cumulative)* | INR | active | `{}` | | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-26.pdf |
| Data Security Council of India — Cybercrime Investigation Center | Data Security Council of India | 97,500,000 *(cumulative)*; CSR0001 1848 | INR | active | `{}` | | (same) |
| Kalinga Kusum Foundation — agroforestry | Kalinga Kusum Foundation | 10,500,000 | INR | active | `{}`; CSR00004313 | | (same) |
| Malligavad Foundation — Doddathogur Lake rejuvenation | Malligavad Foundation | not_found | INR | unconfirmed | `{"acres": 197, "capacity_litres_billion": 3.6}` | Real outcome data, no ₹ amount found. | https://www.infosys.org/infosys-foundation/initiatives/environmental-sustainability.html |
| GoSports Foundation — Gear for Gold | GoSports Foundation | not_found | INR | unconfirmed | `{"academies": 8}` | | https://www.infosys.org/infosys-foundation/about.html |

*If any of these organisations already exist in your `orgs` table, several are ready for immediate conversion into real, amount-populated `grants` rows.*

---
---

## 12. Calls for proposals (`rfps`)

| title | url | status | deadline | amount_min | amount_max | eligibility (JSON) | details (JSON) | source_url | source_name | as_of |
|---|---|---|---|---|---|---|---|---|---|---|
| Aarohan Social Innovation Awards 2025 | https://www.infosys.org/infosys-foundation/aarohan-social-innovation-awards/overview.html | closed *(ran 2025-04-24 to 2025-06-22)* | 2025-06-22 | 1,000,000 *(₹10 lakh, Jury's Special Award)* | 5,000,000 *(₹50 lakh, top winner)* | `{"residency": "India residents 18+", "applicant_types": ["individuals","teams","NGOs","social enterprises"]}` | `{"total_purse_inr_cr": 2, "categories": ["Healthcare","Education","Women Empowerment","Environmental Sustainability"], "edition": 4, "prior_edition_submissions_2023": 2400}` | https://www.infosys.com/newsroom/press-releases/2025/aarohan-social-innovation-awards2025.html | Infosys press release | 2025 |
| "Request a Grant" — standing rolling portal | *(linked from every infosys.org/infosys-foundation page — exact URL not independently captured in either research pass)* | open *(no fixed deadline — rolling)* | not_found | not_found | not_found | `{"eligibility": ["apolitical NGO","non-religious NGO","institution, not individual"]}` | `{"review_days_max": "not published", "note": "no committed turnaround time disclosed"}` | https://www.infosys.org/infosys-foundation.html | Infosys Foundation website | Current |

---
---

## 13. Application forms (`proposal_templates`)

**None found.** No downloadable, fillable grant-application form or concept-note template located on infosys.org — the "Request a Grant" portal (Table 12) is described as an online submission form, not a downloadable document. Consistent with the convention used for other funders in this registry (don't force a description into a template row).

| name | kind | version | notes | source_url |
|---|---|---|---|---|
| *(no rows)* | — | — | The "Request a Grant" portal is an online form, not a downloadable template — not captured as a `proposal_templates` row. | https://www.infosys.org/infosys-foundation.html |

---
---

## 14. Contacts (`contacts`)

| name | role | kind | is_public | verified | notes | source_url | source_name | as_of |
|---|---|---|---|---|---|---|---|---|
| Salil Parekh | Chairman, Infosys Foundation | office_bearer | Yes | Yes | Also CEO & Managing Director, Infosys. | https://www.infosys.org/infosys-foundation/about.html | Infosys Foundation website | Current |
| Manisha Saboo | Head, Infosys Foundation | office_bearer | Yes | Yes | Leads strategic programmes across Education, Healthcare, Women Empowerment, Environmental Sustainability, Art & Culture. | (same) | (same) | Current |
| Inderpreet Sawhney | Trustee | office_bearer | Yes | Yes | Also Chief Legal Officer & Chief Compliance Officer, Infosys. | (same) | (same) | Current |
| Shaji Mathew | Trustee | office_bearer | Yes | Yes | Also Chief Human Resources Officer, Infosys. | (same) | (same) | Current |
| Sumit Virmani | Trustee | office_bearer | Yes | Yes | Also Global Chief Marketing Officer, Infosys; quoted directly in the FY2023-24 Foundation Report re: eVidyaLoka Trust. | (same) | (same) | Current |
| Sunil Kumar Dhareshwar | Trustee | office_bearer | Yes | Yes | Also Global Head — Corporate Accounting & Taxation, Facilities, Infrastructure and Security, Infosys. | (same) | (same) | Current |
| Anand Swaminathan | Trustee, Infosys Foundation USA | office_bearer | Yes | Yes | Also EVP & Global Industry Leader, Infosys. | https://www.infosys.org/infosys-foundation-usa/about/our-team.html | Infosys Foundation USA website | Current |
| Govind Iyer | Chairperson, Infosys Limited CSR Committee | office_bearer | Yes | Yes | Bank/company-level CSR governance, not a Foundation Trustee — kept distinct per the convention used for other funders' Bank-vs-Foundation contact separation. Meetings: 4/4 both FY25 and FY26. | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-26.pdf | Infosys Ltd. Integrated Annual Report 2025-26 | FY2025-26 |
| Chitra Nayak | Member, Infosys Limited CSR Committee | office_bearer | Yes | Yes | 4/4 both years. | (same) | (same) | FY2025-26 |
| Michael Gibbs | Member, Infosys Limited CSR Committee | office_bearer | Yes | Yes | 4/4 both years. | (same) | (same) | FY2025-26 |
| Sudha Murty | Founder & first Chairperson (historical, 1996-2021) | office_bearer | Yes | Yes | Padma Shri (2006), Padma Bhushan (2023); retired from the Foundation in 2021. Kept for audit trail, not deleted. | https://en.wikipedia.org/wiki/Infosys_Foundation | Wikipedia | Historical |

---
---

## 15. Impact numbers (`metrics`)

*`method=self_reported`, `is_self_reported=Yes` throughout unless noted.*

| name | value | target | unit | period | stage | notes | source_url | source_name | as_of |
|---|---|---|---|---|---|---|---|---|---|
| Lives impacted, FY2024-25 | 10,000,000 *(over 1 crore)* | — | individuals | FY2024-25 | outcome | 200+ projects. | https://www.infosys.org/infosys-foundation/about.html | Infosys Foundation website | FY2024-25 |
| Lives impacted, FY2025-26 | 7,000,000 *(over 7 million)* | — | individuals | FY2025-26 | outcome | ⚠️ Lower than the FY24-25 figure despite the Foundation's overall CSR spend rising — flagged as a real, unexplained year-over-year decrease rather than assumed to be an error. | https://www.infosys.org/infosys-foundation/about/reports/documents/infosys-foundation-report-2025-26.pdf | Infosys Foundation Report 2025-26 | FY2025-26 |
| Learning, Livelihoods and Sport — beneficiaries | 730638 | — | individuals | FY2025-26 | outcome | — | (same) | (same) | FY2025-26 |
| Healthcare — beneficiaries | 1385005 | — | individuals | FY2025-26 | outcome | — | (same) | (same) | FY2025-26 |
| Environmental Sustainability — beneficiaries | 4701954 | — | individuals | FY2025-26 | outcome | Largest of the 4 primary areas. | (same) | (same) | FY2025-26 |
| Women Empowerment — beneficiaries | 756622 | — | individuals | FY2025-26 | outcome | — | (same) | (same) | FY2025-26 |
| Secondary Focus Areas — beneficiaries | 346694 | — | individuals | FY2025-26 | outcome | Shared across Art & Culture, Disaster Relief, Destitute Care, Rural Development, Animal Welfare. | (same) | (same) | FY2025-26 |
| Springboard Livelihood Program — job offers, FY2025-26 | 220000 | 500000 *(cumulative target by 2030)* | individuals | FY2025-26 | outcome | — | https://www.infosys.com/newsroom/press-releases/2025/launches-springboard-livelihood-program.html | Infosys press release | FY2025-26 |
| Springboard Livelihood Program — individuals trained, FY2025-26 | 410000 | — | individuals | FY2025-26 | output | — | (same) | (same) | FY2025-26 |
| Infosys Springboard — global learners | 12500000 *(midpoint of the 11.75-13.3 million range reported across sources)* | — | individuals | Current | output | — | https://www.infosys.com/about/springboard.html | Infosys Springboard website | Current |
| Employee volunteering — hours, FY2024-25 | 130000 | — | hours | FY2024-25 | output | 34,000+ employees participating, via InfyCares. | https://www.infosys.org/infosys-foundation/about/reports/documents/infosys-foundation-report-2024-25.pdf | Infosys Foundation Report 2024-25 | FY2024-25 |
| Employee volunteering — participants, FY2025-26 | 84900 | — | individuals | FY2025-26 | output | 1,837 events, via "Gracious Giving" framework. | https://www.infosys.org/infosys-foundation/about/reports/documents/infosys-foundation-report-2025-26.pdf | Infosys Foundation Report 2025-26 | FY2025-26 |
| Water body rejuvenation — capacity added | 3600000000 *(3.6 billion litres, Doddathogur Lake alone)* | 10000000000 *(10 billion litres, 5-year target)* | litres | FY2024-onward | outcome | — | https://www.infosys.org/infosys-foundation/initiatives/environmental-sustainability.html | Infosys Foundation website | FY2024-25 |
| Women in Technology — trained (FY2023-24) | 6406 | — | women | FY2023-24 | output | — | https://www.infosys.org/infosys-foundation/about/reports/documents/infosys-foundation-report-2023-24.pdf | Infosys Foundation Report 2023-24 | FY2023-24 |
| Women in Technology — placed (FY2023-24) | 4186 | — | women | FY2023-24 | outcome | 65% placement rate ((4186/6406). | (same) | (same) | FY2023-24 |
| Impact assessment coverage, FY2024-25 | 26 | — | projects | FY2024-25 | output | Covering 1.3 crore (13,000,000) beneficiaries — method=third_party_evaluation, not self-reported, since impact assessments are typically independently conducted. | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-25.pdf | Infosys Ltd. Integrated AR 2024-25 | FY2024-25 |
| Impact assessment coverage, FY2025-26 | 12 | — | projects | FY2025-26 | output | method=third_party_evaluation. | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-26.pdf | Infosys Ltd. Integrated AR 2025-26 | FY2025-26 |

---
---

## 16. Documents (`documents`)

| title | doc_type | source_url | source_name | as_of | status |
|---|---|---|---|---|---|
| Infosys Foundation Report 2023-24 | annual report | https://www.infosys.org/infosys-foundation/about/reports/documents/infosys-foundation-report-2023-24.pdf | Infosys Foundation website | FY2023-24 | read *(downloaded & read in full in a prior research pass)* |
| Infosys Foundation Report 2024-25 | annual report | https://www.infosys.org/infosys-foundation/about/reports/documents/infosys-foundation-report-2024-25.pdf | Infosys Foundation website | FY2024-25 | read |
| Infosys Foundation Report 2025-26 | annual report | https://www.infosys.org/infosys-foundation/about/reports/documents/infosys-foundation-report-2025-26.pdf | Infosys Foundation website | FY2025-26 | read |
| Infosys Ltd. Integrated Annual Report 2024-25 | annual report | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-25.pdf | Infosys website | FY2024-25 | read *(Annexure 6 CSR disclosure specifically read in depth)* |
| Infosys Ltd. Integrated Annual Report 2025-26 | annual report | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-26.pdf | Infosys website | FY2025-26 | read |
| Infosys Ltd. Annexure 6, FY2020-21 (third-party-hosted statutory filing) | CSR annexure | https://www.primeinfobase.com/ir_download/CSRReports/CSR0000604202021_CSR_INFY_2020-21.pdf | primeinfobase.com (regulatory filing aggregator) | FY2020-21 | read *(NEW this pass — source of the CSR-1 "NA" finding)* |
| Infosys CSR Policy | CSR policy | https://www.infosys.com/investors/corporate-governance/Documents/corporate-social-responsibility-policy.pdf | Infosys website | Current | received *(URL confirmed, not deep-read)* |
| Infosys CSR Committee Charter | board report | https://www.infosys.com/investors/corporate-governance/documents/corporate-social-responsibility-committee-charter.pdf | Infosys website | Current | received |
| Infosys Ltd. Annual Action Plan FY2024-25 | annual action plan | https://www.infosys.com/investors/reports-filings/documents/csr-projects2024-25.pdf | Infosys website | FY2024-25 | received |
| Infosys Ltd. Annual Action Plan FY2026-27 | annual action plan | https://www.infosys.com/investors/reports-filings/documents/csr-projects2026-27.pdf | Infosys website | FY2026-27 | received |
| give.do — Infosys Foundation profile | brochure | https://give.do/discover/1C6K/infosys-foundation | give.do | Current | read |
| give.do — Infosys Limited profile | brochure | https://give.do/discover/1C6J/infosys-limited | give.do | Current | read |
| give.do — Infosys BPM Limited profile | brochure | https://discover.give.do/1CA4/infosys-bpm-limited | give.do | Current | read |

---
---

## 17. News mentions (`news_mentions`)

| url | title | seendate | domain | topic | summary | sentiment | kind |
|---|---|---|---|---|---|---|---|
| https://www.infosys.com/newsroom/press-releases/2025/launches-springboard-livelihood-program.html | Infosys Foundation launches Springboard Livelihood Program | 2025-07 | infosys.com | new programme launch | ₹200cr+ commitment, 500,000 jobs by 2030. | positive | press |
| https://www.infosys.com/newsroom/press-releases/2025/boost-maternal-child-healthcare-rural-karnataka.html | ₹48 crore committed for maternal/child healthcare, rural Karnataka | 2025-07 | infosys.com | new commitment | With Prashanthi Balamandira Trust. | positive | press |
| https://www.infosys.com/newsroom/press-releases/2025/aarohan-social-innovation-awards2025.html | Aarohan Social Innovation Awards 2025 launch | 2025-04 | infosys.com | award programme launch | 4th edition, ₹2cr total purse. | positive | press |
| https://www.infosys.com/newsroom/press-releases/2025/aarohan-social-innovation-awards-winners2025.html | Aarohan Social Innovation Awards 2025 — winners announced | 2025-06/07 *(exact date not captured)* | infosys.com | award winners | — | positive | press |
| https://www.moneycontrol.com/news/business/information-technology/infosys-foundation-launches-rs-200-crore-programme-to-help-5-lakh-job-seekers-by-2030-13279104.html | Infosys Foundation launches ₹200 crore programme to help 5 lakh job seekers by 2030 | 2025-07 | moneycontrol.com | new programme launch (secondary coverage) | Corroborates the Springboard Livelihood Program press release. | positive | news |
| https://sahyadristartups.com/news/infosys-foundation-announces-aarohan-social-innovation-awards-2025-with-%E2%82%B92-crore-grant | Infosys Foundation announces Aarohan Social Innovation Awards 2025 with ₹2 crore grant | 2025-04 | sahyadristartups.com | award programme (secondary coverage) | Grant-band detail. | positive | news |

---
---

## 18. Benchmarks (`reference_figures`)

| kind | name | value | value_text | unit | funder_id | period | notes | source_url |
|---|---|---|---|---|---|---|---|---|
| cost_per_beneficiary | Average CSR spend per crore-plus capital project, FY2025-26 | not_found | "Real disclosed cumulative amounts per recipient range from ~₹1 crore to ₹184 crore — no single average is meaningful given this spread." | ₹ per project | → Infosys Foundation | FY2025-26 | Deliberately not collapsed into one misleading average given the ~184x range between the smallest (₹1.05cr, Kalinga Kusum Foundation) and largest (₹184cr, BMRCL) named projects. | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-26.pdf |
| overhead_norm | Admin overhead as % of total CSR spend, FY2025-26 | 1.66 | — | % | → Infosys Foundation | FY2025-26 | **Calculated by us**: ₹9.25cr admin overhead ÷ ₹558.44cr total spent = 1.66%. Well under the 5% statutory cap. | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-26.pdf |
| overhead_norm | Admin overhead as % of total CSR spend, FY2024-25 | 1.23 | — | % | → Infosys Foundation | FY2024-25 | **Calculated by us**: ₹6.47cr ÷ ₹526.26cr = 1.23%. | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-25.pdf |
| outcome_rate | Women in Technology — job placement rate | 65.3 | — | % | → Infosys Foundation | FY2023-24 | **Calculated by us**: 4,186 placed ÷ 6,406 trained. | https://www.infosys.org/infosys-foundation/about/reports/documents/infosys-foundation-report-2023-24.pdf |

---
---

## 19. Programme places (`program_locations`)

*Restates Table 9 in `role` vocabulary (`funds` throughout — no dates given in source, so `valid_from`/`valid_to` = not_found for all rows). See Table 9 for the full list; not repeated verbatim here.*

---
---

## 20. Programme sectors (`program_tags`)

| program_id | tag (→ tags.id) | role | is_inferred | tagged_by | note |
|---|---|---|---|---|---|
| Infosys Springboard Livelihood Program | Livelihoods (incl. Sport) | primary | No | agent-research | Direct match. |
| Infosys Springboard | Education / Skill Development | primary | No | agent-research | — |
| Gear for Gold | Livelihoods (incl. Sport) | primary | No | agent-research | Sport-specific sub-focus. |
| Aarohan Social Innovation Awards | Education / Skill Development | secondary | No | agent-research | Cross-cutting — also tags Healthcare, Environmental Sustainability, Women Empowerment (see below). |
| Aarohan Social Innovation Awards | Healthcare | secondary | No | agent-research | One of the 4 award categories. |
| Aarohan Social Innovation Awards | Environmental Sustainability | secondary | No | agent-research | One of the 4 award categories. |
| Aarohan Social Innovation Awards | Women Empowerment / Gender Equality | secondary | No | agent-research | One of the 4 award categories. |
| Universal Cornea Care Mission | Healthcare | primary | No | agent-research | — |
| Water Body Rejuvenation Programme | Environmental Sustainability | primary | No | agent-research | — |
| Infosys Agroforestry Program | Environmental Sustainability | primary | No | agent-research | — |
| Women in Technology | Women Empowerment / Gender Equality | primary | No | agent-research | — |
| Kala Dhwani | Art & Culture | primary | No | agent-research | — |
| Employee Volunteering (InfyCares) | Animal Welfare | secondary | No | agent-research | Via the Blue Cross of Hyderabad ABC/ARV programme specifically; the platform itself is cross-cutting. |

---
---

## 21. Grant places (`grant_locations`)

⚠️ Same blocker as Table 11. Location evidence for the strongest, amount-populated candidates:

| candidate grant | location_id | note | source_url |
|---|---|---|---|
| BMRCL — Konappana Agrahara Metro Station | Karnataka (Bengaluru) | — | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-26.pdf |
| Hyderabad Eye Institute — Universal Cornea Care Mission | Telangana (Hyderabad) | — | (same) |
| AIIMS — Mother & Child Block | Delhi (New Delhi) | — | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-25.pdf |
| Ashoka University — chemical biology lab | Delhi (New Delhi) | — | (same) |
| Madras Medical College | Tamil Nadu (Chennai) | — | (same) |
| Ramakrishna Mission — STEM labs | West Bengal (Howrah) | 60 schools. | (same) |
| PGIMER Chandigarh | Chandigarh | — | https://www.infosys.com/investors/reports-filings/annual-report/annual/documents/infosys-ar-26.pdf |
| Data Security Council of India — Cybercrime Investigation Center | Karnataka (Bengaluru) | — | (same) |
| Kalinga Kusum Foundation — agroforestry | Odisha (Bhubaneswar) | — | (same) |
| Malligavad Foundation — Doddathogur Lake | Karnataka (Electronic City, Bengaluru) | 197 acres, 3.6 billion litres. | https://www.infosys.org/infosys-foundation/initiatives/environmental-sustainability.html |

---
---

## 22. Call-for-proposal places (`rfp_locations`)

| rfp | location_id | role | note | source_url |
|---|---|---|---|---|
| Aarohan Social Innovation Awards 2025 | *(Pan-India — "India residents 18+", no state restriction)* | `registered` | Applicants must be India residents; not restricted to any specific state. | https://www.infosys.com/newsroom/press-releases/2025/aarohan-social-innovation-awards2025.html |

---
---

## 23. Call-for-proposal sectors (`rfp_tags`)

| rfp | tag (→ tags.id) | role | is_inferred | tagged_by | note |
|---|---|---|---|---|---|
| Aarohan Social Innovation Awards 2025 | Healthcare | primary | No | agent-research | Explicitly one of the award's 4 named categories. |
| Aarohan Social Innovation Awards 2025 | Education / Skill Development | primary | No | agent-research | Same. |
| Aarohan Social Innovation Awards 2025 | Women Empowerment / Gender Equality | primary | No | agent-research | Same. |
| Aarohan Social Innovation Awards 2025 | Environmental Sustainability | primary | No | agent-research | Same. |

---
---

## 24. Form questions (`template_items`)

**No rows** — consistent with Table 13 (no `proposal_templates` row exists to link to).

---
---

## Sources

*This file consolidates and restructures the pre-existing, extensively-researched `Infosys_Foundation_Full_Report.md` (51 sources — not repeated verbatim here, see that file for the complete numbered list) into the 24-table schema used for Axis Bank Foundation and SBI Foundation. New sources added in this specific pass:*

52. Infosys Limited Annexure 6, FY2020-21 (third-party-hosted statutory filing — source of the CSR-1 "NA" finding and FY2020-21 project-location detail): https://www.primeinfobase.com/ir_download/CSRReports/CSR0000604202021_CSR_INFY_2020-21.pdf
53. builtxsdc.com — general CSR-funding-application guide (secondary, used only to confirm the generic CSR-1/12A/80G compliance layer, not Infosys-specific): https://www.builtxsdc.com/blog/how-to-apply-for-csr-funding-in-india-2025-guide

*Caveats carried over from the pre-existing file: (1) infosys.org and infosys.com both return HTTP 403 to automated crawlers — all content was retrieved via cached search-engine snippets, accurate to the source but not independently re-verified by direct page load. (2) Some beneficiary figures are labelled "FY26" on the live site, reflecting the most recent reporting period at research time — cross-check against the latest Annual Report PDF for definitive year-end figures. (3) NGO Darpan was not independently re-checked live in this specific pass (carried over as `check_blocked` from the general pattern established for other funders, not freshly attempted) — flagged as a genuine remaining gap for a follow-up pass.*

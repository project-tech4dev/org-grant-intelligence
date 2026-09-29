# Axis Bank Foundation — Registry Row

*Compiled from official sources (axisbankfoundation.org, axis.bank.in) — September 2026. Structured to match the `funders` table schema exactly, field by field.*

---

## `funders` table — field values

| Column | Value | Notes |
|---|---|---|
| **id** | *(auto — assigned by database)* | Do not type; row number created on insert |
| **slug** | `axis-bank-foundation` | Lowercase-hyphenated, matches naming convention used for other funders |
| **name** | **Axis Bank Foundation** | Official name as used consistently across axisbankfoundation.org, axis.bank.in, and its own Annual Reports. No separate CIN exists — it is a **registered Public Trust**, not a company (trusts aren't allotted a CIN by MCA) |
| **funder_type** | `corporate_csr` | It is the dedicated CSR/philanthropic implementing arm of a Section-135-bound company (Axis Bank Limited), structurally identical in role to e.g. Infosys Foundation |
| **section_135_bound** | **No** | The *Foundation itself* (a Trust) is not directly bound by Companies Act Section 135 — that statutory obligation legally attaches to **Axis Bank Limited** (the listed company / `parent_id` row), which then channels part of its mandated CSR spend through the Foundation as an implementing vehicle. This matches the schema's own guidance: "Trusts and foundations are usually No." |
| **website** | **https://www.axisbankfoundation.org** | Primary official site. (Axis Bank's own CSR page also links here: https://www.axis.bank.in/csr/axis-bank-foundation) |
| **profile** (JSON) | *see breakdown below* | |
| **source_url** | Multiple — see Sources list at end | |
| **source_name** | "Axis Bank Foundation official website"; "Axis Bank Foundation Annual Report 2024-25 (PDF)"; "Axis Bank corporate CSR page" | |
| **fetched_at** | 2026-09-29 (this research session) | |
| **content_hash** | *(not generated — no automated extractor was used; to be computed by your ingestion pipeline from the source HTML/PDF text if required)* | |
| **extractor_version** | `manual-research-v1` (human/agent-researched, not a scraper) | |
| **as_of** | **FY2024-25** (Annual Report 2024-25 is the latest published financial/impact data; trustee roster also as of this report) | This is the period the *data* describes, not the fetch date |
| **archive_url** | *(not captured in this pass)* — recommend running a Wayback Machine "Save Page Now" on: homepage, `/about-us/overview.html`, `/about-us/board-of-trustees.html`, `/financials/overview.html` | |
| **registry_status** | `in_vetting` (default) — freshly researched; recommend a human check before promoting to `full_profile` | |
| **parent_id** | → **Axis Bank Limited** (CIN: `L65110GJ1993PLC020769`) | Link to the Axis Bank Limited funder row, since ABF is its CSR-implementing Trust |

---

## `profile` JSON — key-by-key detail

### `flagship_program`
> **Sustainable Livelihood Programme**, delivered across two core pillars — **Rural Livelihoods** and **Skill Development** — plus **Ecosystem Action** and **Special Projects** categories. Runs under sequential multi-year mission commitments:
> - **Mission 1 Million** (2011–2018): foundational phase focused on water access, agricultural productivity, and diversifying livelihoods (horticulture, livestock, agroforestry) for 1 million individuals — *newly confirmed via the official CSR Impact Report FY2024-25, correcting/extending the phase history below*.
> - **Mission 2 Million** (2019–2025, per the official CSR Impact Report — supersedes an earlier "2018" start estimate): committed to reaching 2 million households; **achieved as of March 31, 2025** — 2,046,247 cumulative households reached across **23,686 villages in 32 states/UTs**.
> - **Mission 4 Million** (2025–2031, precise range per CSR Impact Report — supersedes earlier "~2030-31" estimate): next phase targeting an additional 2 million families (4 million cumulative) across rural crafts, micro-enterprises, climate-smart agriculture, and natural resource governance.
> - **Mission 4 Million** (launched FY2024-25, target by ~2030-31): next-phase commitment to reach 4 million families, with added focus on climate adaptation, the North-East, Himalayan belt, and coastal regions.
> - The Foundation pivoted to this livelihoods-focused strategy in **2011–12** (originally founded in 2006 with a focus on education and highway trauma care, expanding 2007–2010 into skilling/training for Persons with Disabilities).

### `funding_trend`
> Real, disclosed year-on-year spend (Sustainable Livelihood Programme only, ₹ crore) — **more than doubled in 2 years**:

| Metric | FY2022-23 | FY2023-24 | FY2024-25 |
|---|---|---|---|
| Total spend (₹ crore) | 113.53 | 154.01 | 231.96 |
| — Rural Livelihoods | 99.83 | 129.54 | 198.29 |
| — Skill Development | 9.93 | 18.39 | 23.63 |
| — Ecosystem Action | 3.77 | 6.08 | 10.04 |
| Total projects | 38 | 43 | 59 |
| States & UTs covered | 26 | 28 | 32 |
| Villages covered | 15,606 | 18,706 | 23,686 |
| Households reached (that year) | 2,67,939 | 3,85,343 | 3,87,467 |
| Households reached (cumulative) | 12,96,719 | 16,82,062 | 20,46,247 |

> Cross-check (give.do, for parent **Axis Bank Limited**'s overall CSR grant value, not ABF-specific): FY2021-22 ₹138.25 Cr → FY2022-23 ₹172.30 Cr → FY2023-24 ₹217.20 Cr (Axis Bank Ltd.'s total CSR spend is larger than the ABF-only Sustainable Livelihood Programme figures above, since the Bank also funds CSR directly and via other implementation partners, not solely through ABF).

### `grant_terms`
> - Implements via **NGO/civil-society partners** at the grassroots (not direct-to-individual); the Bank's own materials describe partnerships with "reputed non-governmental organizations, government agencies and other like-minded funding agencies."
> - **Co-funded by multiple Axis Group entities**, not just the Bank: Axis Capital Limited, Axis Mutual Fund, Axis Securities Limited, Axis Trustee Services Limited, Axis Finance Limited, Freecharge Payment Technologies Private Limited, and Invoicemart (A.TReDS) — each contributing to the Sustainable Livelihood Programme as named funding partners in the FY24-25 Annual Report.
> - Historically (as of the FY2015-16 Annual Report), Axis Bank contributed **"up to 1% of its net profit after tax"** annually to ABF — pre-dating the Companies Act Section 135 2% mandate; current-year exact contribution % not independently re-confirmed in this pass.
> - Multi-year, programmatic grant structure — not single one-off disbursements; funding organized around long-horizon "Mission" targets (Mission 2 Million → Mission 4 Million) rather than annual open calls.

### `governance_note`
> - **Registered as a Public Trust in 2006** (confirmed via Axis Bank's own Corporate Profile page and ABF's 2015-16 Annual Report).
> - **FCRA registered** since **11 September 2015**, registration number **083781476** (per ABF Annual Report 2015-16) — relevant if ABF receives/handles foreign contributions in any capacity.
> - Governed by a **Board of Trustees** (see `leadership_note` below for full roster) that meets to approve programs/budgets; Trustee tenure dates are individually disclosed in the Annual Report (a positive governance-transparency signal).
> - No CIN exists for ABF itself since it is a Trust, not a company — **CIN L65110GJ1993PLC020769 belongs to the parent, Axis Bank Limited**, not to the Foundation.

### `leadership_note`
> **Board of Trustees (as of Annual Report 2024-25):**
> | Name | Role | Trustee Since | Notes |
> |---|---|---|---|
> | **S. Ramadorai** | Chairperson | 2010 | Padma Bhushan awardee; former CEO & MD, Tata Consultancy Services (1996–2009); former Chairman, NSDC/NSDA (2011–2016); Chairperson, Mission Karmayogi Bharat |
> | **Dhruvi Shah** | Executive Trustee & CEO | 2021 (joined ABF as staff in 2016; CEO since 2020) | 25+ years across banking/microfinance/development; co-founding team member, RBS Foundation India |
> | **Sheela Patel** | Trustee | 2006 (founding-era trustee) | Founder-Director, SPARC; Padma Shri (2011); Forbes 50-over-50 (2025) |
> | **Som Mittal** | Trustee | 2015 | Former Chairman/President, NASSCOM |
> | **Rajesh Dahiya** | Trustee | 2015 | Founder-CEO, GoodGovern; former Executive Director, Axis Bank Ltd. |
> | **Sushma Iyengar** | Trustee | 2019 | Founder, Kutch Mahila Vikas Sangathan; President, Khamir |
> | **Munish Sharda** | Trustee | 2023 | Executive Director, Axis Bank Limited |
> | **Vijay Mulbagal** | Trustee | 2024 | Group Executive & Head of Wholesale Bank Coverage, Sustainability, and the Bank's CSR mandate |
>
> **CEO:** Dhruvi Shah (Executive Trustee & CEO since 2020).

### `kabil_grant_status`
> **No KABIL-related grant, program, or reference was found** in any official Axis Bank Foundation source (website, Annual Report 2024-25, or CSR pages). Not applicable / not found for this funder.

### `general_contact_email` *(added per contacts-table cleanup — not a name-tied contact, so it lives here instead)*
> **foundation@axis.bank.in** — general departmental inbox for partnership/grant inquiries, published on the ABF Contact Us page (not tied to one named person). Note: one older ABF Annual Report PDF footer shows `foundation@axisbank.com` instead — likely a legacy domain; treat `.axis.bank.in` as current/primary per the live website.
> Source: https://www.axisbankfoundation.org (About Us → Contact Us)

---
---

**Official IDs (`funder_identifiers`)**

*One row per identifier, all belonging to Axis Bank Foundation (this file is Axis Bank Foundation only, so the `funder_id` link column is omitted as redundant). Honesty flag: several standard ID types (PAN, CSR-1, Darpan, trust reg. no.) are **not published anywhere publicly accessible** for this entity — flagged explicitly rather than guessed.*

| id_type | id_value | verified | source_url | is_current | source_name | fetched_at |
|---|---|---|---|---|---|---|
| `domain` | `axisbankfoundation.org` | **Yes** | https://www.axisbankfoundation.org | Yes | Axis Bank Foundation website | 2026-09-29 |
| `name` | `ABF` (commonly used short-form/alternate name, not a legal former name) | **Yes** | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | Yes | Axis Bank Foundation Annual Report 2024-25 | 2026-09-29 |
| `reg_no` | **Not found.** No trust-deed/Bombay Public Trusts Act registration number is published on any official ABF or Axis Bank page located in this research pass. ABF is confirmed as "registered as a Public Trust in 2006," but the specific registration number itself is not disclosed publicly. | No | — | Yes (entity current; number simply undisclosed) | — | 2026-09-29 |
| `pan` | **Not found.** PAN is not a publicly disclosed field for this entity in any source located. | No | — | — | — | 2026-09-29 |
| `csr1` | **Not found / not confirmed.** Plausible that ABF itself holds a CSR-1 registration (since it acts as an implementing agency for Axis Bank Ltd.'s CSR spend), but no CSR00xxxxxx number for ABF was located on any official page. **Needs direct verification** (e.g., MCA CSR-1 company master search) rather than being assumed absent. | No | — | — | — | 2026-09-29 |
| `darpan` | **Not found.** No NGO Darpan Unique ID for ABF was located on any official page. | No | — | — | — | 2026-09-29 |
| *(reference only, not a native ABF ID — see note)* | **FCRA Registration No. 083781476** (registered 11 September 2015) | **Yes** | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/Axis-Bank-Foundation-Annual-Report-2015-16.pdf | Yes | Axis Bank Foundation Annual Report 2015-16 | 2026-09-29 |
| `cin` | `L65110GJ1993PLC020769` — **this CIN belongs to parent Axis Bank Limited**, not to Axis Bank Foundation itself (Foundation is a Trust and has no CIN). Included only for cross-reference/`parent_id` linkage — should be filed under the **Axis Bank Limited** funder row, not this one. | Yes | https://www.msei.in/SX-Content/Listing/Annual-Reports/2025/AXISBANK-2025.pdf | Yes | Axis Bank Limited Secretarial Audit Report (MSEI-hosted Annual Report 2025) | 2026-09-29 |

**Schema-fit note on FCRA:** your `id_type` allowed-values list (`pan, cin, csr1, darpan, reg_no, domain, name`) has no dedicated slot for an **FCRA registration number**. I've listed it above for completeness since it's a real, verified, and potentially decision-relevant identifier (it confirms ABF's legal capacity to receive foreign contributions), but flagged that it doesn't cleanly map to any allowed `id_type` value — you may want to either (a) extend the enum to include `fcra`, or (b) store it under `reg_no` with a clarifying note, or (c) keep it in the `profile` JSON's `governance_note` (as already done in Part A/Basic Profile above) instead of `funder_identifiers`.

**Summary of what's genuinely confirmed vs. genuinely missing:**
- ✅ Confirmed & verified: `domain`, `name` (ABF), FCRA number
- ❌ Not published anywhere public: `pan`, `csr1`, `darpan`, `reg_no` (trust registration number)
- ⚠️ Do not backfill `cin` for this row — Axis Bank Foundation has none; only its parent (Axis Bank Limited) does

---

---
---

**Registration history (`credential_events`)**

*One row per event, all for Axis Bank Foundation (`org_id`/`funder_id` link columns omitted as redundant — this file is ABF only). `id`, `document_id`, `recorded_by`, `recorded_at` are DB-auto fields, left blank.*

| credential | event | event_date | valid_until | verified | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|
| `reg_no` | `registered` | 2006 (exact date not disclosed) | — (Public Trust registrations don't expire) | No *(fact of registration is confirmed; the number itself is not_available)* | Confirmed registered as a Public Trust in 2006 across multiple official sources; the trust registration number itself is not published anywhere found. | https://www.axis.bank.in/about-us/corporate-profile | Axis Bank Corporate Profile page | 2026-09-29 | Current (as stated on live site) |
| `fcra` | `registered` | 2015-09-11 | Not confirmed — FCRA certs generally need 5-yr renewal; current renewal status not re-checked against fcraonline.nic.in in this pass | **Yes** (number + date explicitly published) | Registration No. **083781476**. Recommend a follow-up `checked_active` or `check_blocked` event once the FCRA portal is queried directly. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/Axis-Bank-Foundation-Annual-Report-2015-16.pdf | Axis Bank Foundation Annual Report 2015-16 | 2026-09-29 | FY2015-16 |
| `12a` | `not_found` | — | — | No | Not explicitly disclosed for ABF itself in any official source. (The TISS-ABF CSR Process Manual lists 12A as a requirement for ABF's *NGO grant partners*, not proof of ABF's own status.) Near-certain ABF holds 12A as a functioning tax-exempt trust, but unconfirmed. | https://www.axisbankfoundation.org/download/knowledge-corner/TISS-ABF-CSR-Process-Manual.pdf | TISS-ABF CSR Process Manual | 2026-09-29 | — |
| `80g` | `not_found` | — | — | No | No 80G number/date found. ABF is funded by Axis Bank Ltd. and Group entities, not public donations, so 80G may be less operationally central — but status still unconfirmed either way. | — | — | 2026-09-29 | — |
| `csr1` | `not_found` | — | — | No | Plausible ABF holds a CSR-1 (CSR00xxxxxx) as an implementing agency for Axis Bank's CSR spend, but no number located on any official page. Needs a direct MCA CSR-1 master-data check, not assumed absent. | — | — | 2026-09-29 | — |
| `darpan` | `not_found` | — | — | No | No NGO Darpan Unique ID located on any official ABF page. | — | — | 2026-09-29 | — |
| `pan` | `not_found` | — | — | No | PAN not publicly disclosed anywhere for ABF. | — | — | 2026-09-29 | — |
| `cin` | `not_available` | — | — | Yes *(fact of non-applicability is confirmed)* | **Not applicable to ABF** — it is a registered Trust, and trusts are not issued a CIN by MCA. Do not confuse with parent Axis Bank Limited's CIN (`L65110GJ1993PLC020769`). | https://www.axis.bank.in/about-us/corporate-profile | Axis Bank Corporate Profile page | 2026-09-29 | — |

---
---

---
---

**Focus sectors (`funder_tags`)**

*`funder_id`/`tag_id` are numeric links in your system — shown here as tag names since I don't have your `tags.id` values. All rows are for Axis Bank Foundation.*

| tag (→ tags.id) | role | is_inferred | tagged_by | note |
|---|---|---|---|---|
| Rural Livelihoods | primary | No | agent-research | Core, named pillar of the flagship Sustainable Livelihood Programme; largest spend category (₹198.29 Cr of ₹231.96 Cr total, FY24-25). |
| Skill Development / Vocational Training | primary | No | agent-research | Second named pillar of SLP; explicit focus on youth and Persons with Disabilities (PwDs). |
| Women Empowerment | primary | No | agent-research | Stated directly in Vision & Mission ("significantly high focus on women empowerment"); dedicated AR24-25 chapter "Women at Centre-Stage" on women-led institutions. |
| Environmental Sustainability / Natural Resource Management | secondary | No | agent-research | Explicit theme: watershed management, water security, climate-resilient agriculture (FICCI Sustainable Agriculture Award 2024 for work in Jharkhand, Telangana, Maharashtra). |
| Disability Inclusion (PwD livelihoods/skilling) | secondary | No | agent-research | Explicit since 2007-2010 expansion; continues as a named beneficiary group in current Skill Development pillar. |
| Health (linked to livelihoods) | secondary | No | agent-research | Dedicated AR24-25 chapter "Health and Livelihoods" — health treated as a livelihoods enabler, not a standalone grant vertical. |
| Financial Inclusion | secondary | **Yes** | agent-research (inferred) | Not a dedicated ABF pillar today; inferred from parent Axis Bank Ltd.'s declared CSR policy theme + ABF's own "financially...excluded communities" mission language. Needs funder-level confirmation. |
| Education | secondary (historical) | No | agent-research | ABF's *original* 2006 focus; explicitly superseded when ABF pivoted to a livelihoods-first strategy in 2011-12 per its own Overview timeline. Mark `valid_to` ≈ 2011-12 if your schema supports it. |
| Disaster Relief (highway trauma care) | secondary (historical) | No | agent-research | Part of ABF's original 2006 mandate ("education and highway trauma care"); no evidence this remains active today. |
| Community Institution Building / System Strengthening | secondary | No | agent-research | Explicit current theme: strengthening SHGs, gram panchayats, village organisations, farmer collectives ("System Strengthening" chapter, AR24-25). |

---
---

**Geography (`funder_locations`)**

*`location_id` shown as place names — needs mapping to your `locations.id`. All rows for Axis Bank Foundation. Complete state-by-state list isn't published; only a cumulative count (32 states/UTs, FY24-25) plus named examples via case studies/partnerships are confirmed.*

| location (→ locations.id) | role | valid_from | valid_to | note | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|
| Maharashtra (Mumbai — Axis House, Worli) | `registered` | 2006 | — | Head Office address of Axis Bank Foundation. | https://www.axisbankfoundation.org | ABF website (Contact Us) | 2026-09-29 | Current |
| Maharashtra (rural districts) | `funds` | 2012 (approx.) | — | Named partnership: Dilasa Sanstha, 10 districts of Maharashtra, water security/tribal livelihoods. | https://www.axisbankfoundation.org/sustainable-livelihood/sustainable-livelihood.html | ABF website — Sustainable Livelihood partner stories | 2026-09-29 | Undated (legacy programs page) |
| Rajasthan | `funds` | 2012 | — | Named partnership: SRIJAN, 4 districts of Rajasthan, since 2012. | https://www.axisbankfoundation.org/sustainable-livelihood/sustainable-livelihood.html | ABF website — Sustainable Livelihood partner stories | 2026-09-29 | Undated (legacy programs page) |
| Madhya Pradesh | `funds` | — | — | Named beneficiary case study ("Sita Devi, Farmer, Madhya Pradesh") in Annual Report 2024-25. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 |
| Odisha | `funds` | — | — | Named case study: Siangbali Gram Panchayat, Daringbadi block, MGNREGS convergence project. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 |
| Gujarat | `funds` | — | — | Gallery caption: "Senior Management Visits a Project Site in Dahod, Gujarat." | https://www.axisbankfoundation.org | ABF website (homepage gallery) | 2026-09-29 | Undated |
| West Bengal | `funds` (historical) | ~2015 | — | Named as a major-budget-allocation state in the 2015-era TISS-ABF CSR Process Manual; not independently re-confirmed as still active in FY24-25. | https://www.axisbankfoundation.org/download/knowledge-corner/TISS-ABF-CSR-Process-Manual.pdf | TISS-ABF CSR Process Manual (2015) | 2026-09-29 | ~2015 |
| Andhra Pradesh | `funds` (historical) | ~2015 | — | Same source as above — named as a major-budget-allocation state circa 2015. | https://www.axisbankfoundation.org/download/knowledge-corner/TISS-ABF-CSR-Process-Manual.pdf | TISS-ABF CSR Process Manual (2015) | 2026-09-29 | ~2015 |
| Jharkhand, Telangana, Maharashtra (as a set) | `funds` | — | — | FICCI Sustainable Agriculture Award 2024 recognized ABF's natural resource management/climate-resilient agriculture work specifically across these three states. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024 (award year) |
| North-East India (region; individual states not itemized in source) | `priority` | FY2024-25 | — | Explicit new strategic-expansion chapter ("Towards the Northeast") in AR24-25 — a stated forward-looking priority, not yet evidenced by a named per-state spend breakdown. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 |
| All-India (aggregate footprint) | `priority` | 2018 (Mission 2 Million launch) | — | Cumulative reach: 26 states/UTs (FY22-23) → 28 (FY23-24) → **32 states/UTs, 23,686 villages, 775 blocks, 300 districts** (FY24-25). Full 32-state list not itemized in any source found — only this aggregate count plus the named examples above. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 |

---
---

---
---

**Yearly CSR filing (`funder_csr_years`)**

⚠️ **Important attribution flag:** this statutory Annexure-II filing (average net profit, 2%-prescribed spend, admin cap, impact assessment) is filed by **Axis Bank Limited** (`section_135_applicable = Yes`), *not* by Axis Bank Foundation itself (recall: ABF is a Trust, `section_135_bound = No`). These rows belong under the **Axis Bank Limited** funder row, not this one — included here for context since ABF is the primary channel through which the Bank's CSR obligation is spent. `funder_id` link column omitted per file convention; substitute **Axis Bank Limited** when loading into your DB.

| fiscal_year | section_135_applicable | average_net_profit (₹ cr) | prescribed_csr (₹ cr) | spent_on_projects (₹ cr) | admin_overheads (₹ cr) | impact_assessment_cost (₹ cr) | total_spent (₹ cr) | unspent_transferred (₹ cr) | excess_spent (₹ cr) | impact_assessment_done | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2022-23 | Yes | 9,973.00 | 199.46 | — *(breakdown not itemized in source found)* | — | — | 201.92 | — *(not itemized in source found)* | 2.46 | Not confirmed in this pass | Full Annexure spend breakdown (admin/impact-assessment split, unspent-transfer detail) not independently located — only the top-line obligation/spent/excess figures were confirmed. |
| FY2023-24 | Yes | — *(not independently confirmed)* | — | — | — | — | **≈269** (rounded, from Axis Bank's own FY25-26 Annual Report summary infographic) | — | — | Not confirmed in this pass | Only the rounded total CSR spend (₹269 cr) was located; the full statutory Annexure-II line-by-line breakdown for this specific year was not pulled in this research pass — recommend downloading the FY2023-24 Annual Report directly for the exact figures. |
| FY2024-25 | Yes | 21,296.18 | 425.92 | 284.86 | 1.73 | 0.33 | **286.92** (cash) / **426.57** (total incl. ₹139.65 cr carried as provision/unspent) | 139.65 (transferred across 5 dates: 17, 19, 21, 22, 23 Apr 2025) | 0.65 | **Yes** — 5 projects assessed (Financial Literacy Training, Financial Literacy Mobile Vans, Child Heart Surgeries w/ Sri Sathya Sai Trust, Mid-Day Meals w/ Akshaya Patra, Axis DilSe–Lyzon Friendship School Manipur) | Two "total spent" figures exist in the source: ₹286.92 cr = cash-basis total per item 6(d); ₹426.57 cr = full P&L-recognized CSR expense (cash + provision) used in the excess-set-off calc at item (f). Both are real, from the same document — reported here for completeness rather than picking one. |
| FY2025-26 | Yes | 26,474.59 | 529.49 | — *(not itemized in snippet found)* | — | — | **530.11** (₹421.66 cr cash + ₹108.45 cr provision) | — *(prior-year FY25 balance was ₹139.65 cr; FY26-specific carry-forward not confirmed in this pass)* | 0.62 | Not confirmed in this pass | Sourced from the FY2025-26 Integrated Annual Report Board's Report Annexure 4 (item 5/6/f only) — full item-by-item breakdown not pulled in this pass. |

**CSR Committee (Axis Bank Limited, as disclosed in the FY2024-25 Annexure — do not confuse with ABF's own Board of Trustees above):**

| Name | Designation | Meetings held / attended (FY24-25) |
|---|---|---|
| N. S. Vishwanathan | Independent Director & Part-Time Chairman; **Chairperson, CSR Committee** | 4 / 3 |
| Rajiv Anand | Deputy Managing Director | 4 / 4 |
| Meena Ganesh | Independent Director | 4 / 4 |
| Prof. S. Mahendra Dev | Independent Director | 4 / 4 |
| Munish Sharda | Executive Director *(also a Trustee of Axis Bank Foundation, per Part A above)* | 4 / 3 |

**⚠️ Cross-check discrepancy worth flagging:** give.do's "Axis Bank Limited" profile (cited in Part A/Sources) reported CSR Grant Values of ₹138.25 Cr (FY21-22), ₹172.30 Cr (FY22-23), and ₹217.20 Cr (FY23-24) — all **meaningfully lower** than the real statutory figures found here (FY22-23 actual = ₹201.92 cr spent; FY23-24 actual ≈ ₹269 cr). Treat give.do's numbers as **unreliable/stale** for this funder relative to the primary-source Annexure 4 filings used in this table — the Bank's own Annual Report is the authoritative source.

**Correction note:** an earlier draft of this section mistakenly included a "cause-level breakdown" that actually belongs to a *different* company (Infosys Ltd.) researched in a separate file — that has been removed here. No verified cause-wise ₹ breakdown for Axis Bank Limited's own CSR spend was independently confirmed in this research pass (give.do's Axis Bank Limited page showed "Cause Area" section headers but the underlying values were not captured/were locked).

---
---

---
---

**Spend breakdown (`funder_csr_spend`)**

⚠️ **Honesty flag up front:** `amount` is a *required* field in this schema, but the only figures Axis Bank Foundation/Axis Bank Limited publish with real ₹ amounts are **category-level totals** (Rural Livelihoods / Skill Development / Ecosystem Action per fiscal year) — not a project-by-project MCA-style CSV. Real **named projects** exist (SRIJAN, Dilasa Sanstha, Sri Sathya Sai Trust, Akshaya Patra, Sunbird Trust) but **no per-project ₹ amount was disclosed anywhere found** for any of them. Rather than inventing numbers, I've split this into (A) real total-level rows that satisfy the schema, and (B) a clearly-separated list of named projects with amount honestly marked "not disclosed."

**(A) Category-level totals (`project_name` empty — these are totals, not single projects; `amount` is real, ₹ converted from crore per your instruction to multiply by 10,000,000):**

| fiscal_year | csr_sector_id (as text) | project_count | amount (₹) | via_agency | is_ongoing | notes | source_url | source_name | as_of |
|---|---|---|---|---|---|---|---|---|---|
| FY2022-23 | Rural Livelihoods | 26 | 998,300,000 | Yes | Yes | ABF Annual Report Financial Highlights table. | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF Annual Report 2024-25 (3-yr trend table) | FY2022-23 |
| FY2022-23 | Skill Development | 6 | 99,300,000 | Yes | Yes | Same source. | (same) | (same) | FY2022-23 |
| FY2022-23 | Ecosystem Action | 5 | 37,700,000 | Yes | Yes | Same source. | (same) | (same) | FY2022-23 |
| FY2022-23 | *(Special Projects — no ₹ broken out separately)* | 1 | — *(rolled into total, not itemized)* | — | — | Total row for FY22-23 = 38 projects across 26 states; total spend ₹113.53 cr. | (same) | (same) | FY2022-23 |
| FY2023-24 | Rural Livelihoods | 29 | 1,295,400,000 | Yes | Yes | Same source. | (same) | (same) | FY2023-24 |
| FY2023-24 | Skill Development | 7 | 183,900,000 | Yes | Yes | Same source. | (same) | (same) | FY2023-24 |
| FY2023-24 | Ecosystem Action | 6 | 60,800,000 | Yes | Yes | Same source. | (same) | (same) | FY2023-24 |
| FY2023-24 | *(Special Projects)* | 1 | — *(not itemized)* | — | — | Total row for FY23-24 = 43 projects across 28 states; total spend ₹154.01 cr. | (same) | (same) | FY2023-24 |
| FY2024-25 | Rural Livelihoods | 46 | 1,982,900,000 | Yes | Yes | Same source. | (same) | (same) | FY2024-25 |
| FY2024-25 | Skill Development | 6 | 236,300,000 | Yes | Yes | Same source. | (same) | (same) | FY2024-25 |
| FY2024-25 | Ecosystem Action | 7 | 100,400,000 | Yes | Yes | Same source. | (same) | (same) | FY2024-25 |
| FY2024-25 | *(Special Projects)* | 0 | — | — | — | Total row for FY24-25 = 59 projects across 32 states; total spend ₹231.96 cr. | (same) | (same) | FY2024-25 |

### ✅ UPDATE — Real state-level ₹ amounts found (Aspirational Districts, per your request to check official sites)

Found in **Axis Bank Limited's official Business Responsibility & Sustainability Report (BRSR) FY2024-25** — a genuine, government-aligned state-wise ₹ amount table for CSR spend in **Aspirational Districts** (NITI Aayog-designated). This is real `state_location_id` + `amount` data, exactly the MCA-CSV-style granularity the schema wants. `fiscal_year = FY2024-25`; `designation = "aspirational_district"`; `via_agency` not specified in source; `source_name = "Axis Bank BRSR FY2024-25"`.

| state_location_id | Aspirational Districts (name_as_printed) | amount (₹ cr) | amount (₹, for DB) |
|---|---|---|---|
| Andhra Pradesh | Visakhapatnam, Vizianagaram | 1.59 | 15,900,000 |
| Assam | Baksa, Barpeta, Darrang, Dhubri, Goalpara, Udalguri | 0.72 | 7,200,000 |
| Bihar | Aurangabad(BH), Banka, Gaya, Jamui, Muzaffarpur, Nawada | 5.25 | 52,500,000 |
| Chhattisgarh | Bastar, Bijapur, Dakshin Bastar Dantewada, Korba, Mahasamund, Narayanpur, Rajnandgaon, Sukma, Uttar Bastar Kanker | 10.77 | 107,700,000 |
| Gujarat | Narmada | 0.31 | 3,100,000 |
| Himachal Pradesh | Chamba | 0.04 | 400,000 |
| Jharkhand | Bokaro, Dumka, East Singhbhum, Garhwa, Godda, Gumla, Hazaribagh, Khunti, Latehar, Lohardaga, Palamu, Ramgarh, Ranchi, Sahebganj, Simdega, West Singhbhum | 16.69 | 166,900,000 |
| Kerala | Wayanad | 0.02 | 200,000 |
| Madhya Pradesh | Barwani, Chhatarpur, Damoh, Guna, Khandwa (East Nimar), Rajgarh, Singrauli, Vidisha | 3.27 | 32,700,000 |
| Maharashtra | Dharashiv, Gadchiroli | 0.97 | 9,700,000 |
| Meghalaya | Ri Bhoi | 0.56 | 5,600,000 |
| Mizoram | Mamit | 0.02 | 200,000 |
| Nagaland | Kiphire | 0.02 | 200,000 |
| Odisha | Balangir, Dhenkanal, Gajapati, Kalahandi, Kandhamal, Koraput, Malkangiri, Nabarangpur, Nuapada, Rayagada | 17.49 | 174,900,000 |
| Punjab | Ferozepur | 0.06 | 600,000 |
| Rajasthan | Baran, Dholpur, Jaisalmer | 1.59 | 15,900,000 |
| Tamil Nadu | Ramanathapuram, Virudhunagar | 6.06 | 60,600,000 |
| Uttar Pradesh | Bahraich, Chandauli, Chitrakoot | 2.25 | 22,500,000 |
| Uttarakhand | Haridwar, Udham Singh Nagar | 0.10 | 1,000,000 |
| **Total (19 states)** | — | **67.79** | **677,900,000** |

*Source: https://www.axis.bank.in/docs/default-source/business-responsibility-reports/business-responsibility-sustainability-report-for-the-year-2024-25.pdf (page 43-44, Principle 8, Leadership Indicator 2)*

**(B) Named individual projects — amount honestly marked "not disclosed" (do not force a value here):**

| fiscal_year | project_name | implementing_agency | state_location | via_agency | amount | notes | source_url |
|---|---|---|---|---|---|---|---|
| Ongoing since 2012 | Sustainable Livelihoods — Rajasthan | SRIJAN (Self Reliant Initiatives through Joint Action) | Rajasthan (4 districts) | Yes | **not disclosed** | Legacy partner-story page; no ₹ figure given. | https://www.axisbankfoundation.org/sustainable-livelihood/sustainable-livelihood.html |
| Ongoing (undated) | Sustainable Livelihoods — Maharashtra (tribal, water security) | Dilasa Sanstha | Maharashtra (10 districts) | Yes | **not disclosed** | Same source. | https://www.axisbankfoundation.org/sustainable-livelihood/sustainable-livelihood.html |
| FY2022-23 (impact-assessed in FY24-25) | Financial Literacy Training Program | Axis Bank (direct) | 20 states + 1 UT | No | **not disclosed** | 0.9 million beneficiaries; assessed via survey Oct 2024–Jan 2025. | https://www.axis.bank.in/docs/default-source/annual-reports/for-axis-bank/annual-report-for-the-year-2024-2025.pdf |
| FY2022-23 | Financial Literacy through Mobile Vans | CSC Academy | 18 locations (states not itemized) | Yes | **not disclosed** | 20 mobile vans, Village Level Entrepreneurs model. | (same) |
| FY2022-23 | Child Heart Surgeries | Sri Sathya Sai Health & Education Trust (Sri Sathya Sai Sanjeevani Hospital, Raipur) | Chhattisgarh (patients from 15 states) | Yes | **not disclosed** | 300 surgeries, 100% surgical success rate. | (same) |
| Dec 2022 – Mar 2023 | Mid-Day Meal Program | Akshaya Patra Foundation | Uttar Pradesh, Gujarat, Karnataka, Odisha | Yes | **not disclosed** | ~1 lakh children covered. | (same) |
| Undated | Axis DilSe — Lyzon Friendship School | Sunbird Trust | Manipur (Singngat, Churachandpur district) | Yes | **not disclosed** | Tuition/hostel fee support, Science Lab, digital classroom. | (same) |

*Recommendation: none of the (B) rows should be inserted with a placeholder/zero `amount` — leave `amount` NULL/blank and flag `notes = "amount not disclosed in any source found"` rather than violate the "required" constraint with fabricated data.*

---
---

**Programmes (`programs`) — hierarchy**

*`funder_id` = Axis Bank Foundation for ABF-run programmes; Axis Bank Limited (direct) for Bank-run programmes not routed through ABF. `org_id` left blank throughout (these are funder programmes, not NGO programmes).*

| name | kind | parent | status | start_date | end_date | is_enabler | details (JSON) | source |
|---|---|---|---|---|---|---|---|---|
| Livelihoods | `theme` | — (top-level) | active | 2011-12 (pivot year) | — | No | `{"note": "ABF's core strategic theme since its 2011-12 pivot away from Education"}` | ABF Overview page |
| **Sustainable Livelihood Programme (SLP)** | `programme` | → Livelihoods | active | 2011-12 | — | No | `{"pillars": ["Rural Livelihoods", "Skill Development"], "secondary_categories": ["Ecosystem Action", "Special Projects"], "fy24-25_budget_inr_cr": 231.96, "cumulative_households": 2046247, "cumulative_villages": 23686, "states_uts": 32}` | ABF Annual Report 2024-25 |
| Mission 1 Million | `phase` | → Sustainable Livelihood Programme | concluded | 2011 | 2018 | No | `{"target_individuals": 1000000, "focus": ["water access", "agricultural productivity", "horticulture", "livestock", "agroforestry"]}` | Axis Bank CSR Impact Report FY2024-25 |
| Mission 2 Million | `phase` | → Sustainable Livelihood Programme | **concluded** (achieved) | 2019 | 2025-03-31 | No | `{"target_households": 2000000, "achieved_households": 2046247}` — dates corrected from 2019–2025 per the official CSR Impact Report (supersedes an earlier 2018-start estimate) | ABF Annual Report 2024-25 + Axis Bank CSR Impact Report FY2024-25 |
| Mission 4 Million | `phase` | → Sustainable Livelihood Programme | active | FY2024-25 | ~2030-31 (target) | No | `{"target_families": 4000000}` | ABF Annual Report 2024-25 |
| Rural Livelihoods (pillar) | `project` *(recurring category, not single project)* | → Sustainable Livelihood Programme | active | 2011-12 | — | No | `{"fy24-25_spend_inr_cr": 198.29, "fy24-25_project_count": 46}` | ABF Annual Report 2024-25 |
| Skill Development (pillar) | `project` *(recurring category)* | → Sustainable Livelihood Programme | active | ~2007-2010 (PwD skilling origin) | — | No | `{"fy24-25_spend_inr_cr": 23.63, "fy24-25_project_count": 6, "target_groups": ["youth", "Persons with Disabilities"]}` | ABF Annual Report 2024-25 |
| SRIJAN Partnership | `project` | → Rural Livelihoods (pillar) | active (undated) | 2012 | — | No | `{"partner": "SRIJAN", "districts": 4, "state": "Rajasthan"}` | ABF sustainable-livelihood page |
| Dilasa Sanstha Partnership | `project` | → Rural Livelihoods (pillar) | active (undated) | — | — | No | `{"partner": "Dilasa Sanstha", "districts": 10, "state": "Maharashtra", "focus": "tribal livelihoods, water security"}` | ABF sustainable-livelihood page |
| Towards the Northeast (expansion) | `phase` | → Sustainable Livelihood Programme | active (new) | FY2024-25 | — | No | `{"scope": "region-wide, individual states not itemized", "focus": ["climate-resilient livelihoods", "handloom/handicraft", "youth enterprise"]}` | ABF Annual Report 2024-25 |
| Education | `theme` | — (top-level, **historical**) | **concluded** (~2011-12) | 2006 | ~2011-12 | No | `{"note": "ABF's original founding focus, superseded by Livelihoods pivot"}` | ABF Overview page |
| Highway Trauma Care | `theme` | — (top-level, **historical**) | **concluded** | 2006 | unknown | No | `{"note": "part of original 2006 founding mandate; no evidence of current activity"}` | ABF Overview page |
| Financial Inclusion & Literacy | `theme` | — (top-level; **Axis Bank Limited direct**, not routed through ABF) | active | — | — | No | `{"funder": "Axis Bank Limited (direct CSR, not via ABF)"}` | Axis Bank Integrated Annual Report 2024-25 |
| Financial Literacy Training Program | `project` | → Financial Inclusion & Literacy | active | — | — | No | `{"beneficiaries_fy23": 900000, "coverage": "20 states + 1 UT", "implementer": "direct"}` | Axis Bank AR 2024-25 |
| Financial Literacy through Mobile Vans | `project` | → Financial Inclusion & Literacy | active | — | — | No | `{"implementer": "CSC Academy", "vans": 20, "locations_assessed": 18}` | Axis Bank AR 2024-25 |
| Healthcare & Humanitarian Relief | `theme` | — (top-level; **Axis Bank Limited direct**) | active | — | — | No | `{"funder": "Axis Bank Limited (direct CSR)"}` | Axis Bank AR 2024-25 |
| Child Heart Surgeries | `project` | → Healthcare & Humanitarian Relief | active (undated) | — | — | No | `{"implementer": "Sri Sathya Sai Health & Education Trust", "location": "Sri Sathya Sai Sanjeevani Hospital, Raipur, Chhattisgarh", "surgeries_fy23": 300}` | Axis Bank AR 2024-25 |
| Mid-Day Meal Program | `project` | → Healthcare & Humanitarian Relief | active (undated) | 2022-12 | 2023-03 *(assessed window; likely ongoing beyond)* | No | `{"implementer": "Akshaya Patra Foundation", "states": ["Uttar Pradesh", "Gujarat", "Karnataka", "Odisha"], "children_covered": 100000}` | Axis Bank AR 2024-25 |
| Axis DilSe — Lyzon Friendship School | `project` | → Healthcare & Humanitarian Relief *(education/humanitarian crossover — could also sit under a future "Education (Bank-direct)" theme)* | active (undated) | — | — | No | `{"implementer": "Sunbird Trust", "location": "Singngat, Churachandpur district, Manipur", "support": ["tuition/hostel fees", "Science Lab", "digital classroom"]}` | Axis Bank AR 2024-25 |

---
---

---
---

**Where programmes ran (`funder_footprints`)**

*`location_id` shown as place name (needs mapping to your `locations.id`). Real, named evidence only — no invented district lists.*

| program | fiscal_year | location (name_as_printed) | notes | source_url |
|---|---|---|---|---|
| Sustainable Livelihood Programme (aggregate) | FY2022-23 | *(26 states/UTs — individual names not itemized in source)* | Aggregate count only. | ABF AR 2024-25 |
| Sustainable Livelihood Programme (aggregate) | FY2023-24 | *(28 states/UTs — individual names not itemized in source)* | Aggregate count only. | ABF AR 2024-25 |
| Sustainable Livelihood Programme (aggregate) | FY2024-25 | *(32 states/UTs — individual names not itemized in source)* | 23,686 villages, 775 blocks, 300 districts overall. | ABF AR 2024-25 |
| Rural Livelihoods (pillar) — SRIJAN partnership | Ongoing since 2012 | **Rajasthan** (4 districts, unnamed individually) | Named partner-story page. | ABF sustainable-livelihood page |
| Rural Livelihoods (pillar) — Dilasa Sanstha partnership | Undated | **Maharashtra** (10 districts, unnamed individually) | Tribal livelihoods, water security focus. | ABF sustainable-livelihood page |
| System Strengthening (case study) | FY2024-25 | **"Daringbadi" block, Odisha** (Siangbali Gram Panchayat) | Exact spelling as printed in AR24-25 case study. | ABF AR 2024-25 |
| Community Voice (case study) | FY2024-25 | **Madhya Pradesh** (district not specified — "Sita Devi, Farmer, Madhya Pradesh") | Named beneficiary quote only; no district given. | ABF AR 2024-25 |
| Environmental Sustainability / NRM (FICCI award) | FY2024 (award year) | **Jharkhand, Telangana, Maharashtra** (states named as a set; districts not itemized) | FICCI Sustainable Agriculture Award 2024. | ABF AR 2024-25 |
| (Undated gallery reference) | Undated | **"Dahod", Gujarat** | Gallery caption: "Senior Management Visits a Project Site in Dahod, Gujarat." | ABF homepage |
| Towards the Northeast (new expansion) | FY2024-25 | **North-East India** (region; individual states not itemized) | Explicit new strategic chapter; no per-state breakdown published. | ABF AR 2024-25 |
| (Historical, ~2015) | ~FY2014-15/15-16 | **Madhya Pradesh, Maharashtra, West Bengal, Andhra Pradesh, Odisha** | Named as major-budget-allocation states circa 2015; not re-confirmed as still active at that scale in FY24-25. | TISS-ABF CSR Process Manual (2015) |
| Financial Literacy Training Program (Axis Bank direct) | FY2022-23 (assessed in AR24-25) | *(20 states + 1 Union Territory — individual names not itemized)* | 0.9 million beneficiaries. | Axis Bank AR 2024-25 |
| Financial Literacy through Mobile Vans | FY2022-23 (assessed in AR24-25) | *(18 locations — individual names not itemized)* | Village Level Entrepreneur model via CSC Academy. | Axis Bank AR 2024-25 |
| Child Heart Surgeries | FY2022-23 (assessed in AR24-25) | **"Raipur, Chhattisgarh"** (hospital location); patients drawn from 15 states (unnamed) | Sri Sathya Sai Sanjeevani Hospital. | Axis Bank AR 2024-25 |
| Mid-Day Meal Program | FY2022-23 (Dec'22–Mar'23; assessed in AR24-25) | **Uttar Pradesh, Gujarat, Karnataka, Odisha** (states named; assessment survey itself covered "15 schools in Odisha and Karnataka" specifically) | ~1 lakh children covered across the 4 states. | Axis Bank AR 2024-25 |
| Axis DilSe — Lyzon Friendship School | Undated (assessed in AR24-25) | **"Singngat subdivision, Churachandpur district, Manipur"** | Exact spelling as printed in source. | Axis Bank AR 2024-25 |

### ✅ UPDATE — Full official district-level footprint found (per your request to check give.do/MCA/other official sites)

Found in **Axis Bank's own official "CSR Impact Report FY2024-25"** (`axis.bank.in/docs/default-source/csr-reports-and-disclosures/csr-impact-report-fy-2024-25.pdf`) — a complete, named state-and-district breakdown for **all 7 CSR themes**. This supersedes the "not itemized" placeholders above. All `name_as_printed` exactly as spelled in the source. `fiscal_year = FY2024-25` for every row below; `source_name = "Axis Bank CSR Impact Report FY2024-25"` throughout.

**Theme 1 — Lives & Livelihoods: 31 States/UTs, 253 Districts**

| State/UT | Districts (name_as_printed) | # districts |
|---|---|---|
| Andhra Pradesh | Ananthapuramu, Chittoor, Krishna, Sri Sathya Sai, Visakhapatnam, Vizianagaram | 6 |
| Assam | Baksa, Kamrup Metro, Majuli, Tamulpur, Tinsukia, Udalguri | 6 |
| Bihar | Aurangabad(BH), Banka, Gaya, Jamui, Lakhisarai, Munger, Muzaffarpur, Nawada, Patna, Saran | 10 |
| Chandigarh | Chandigarh | 1 |
| Chhattisgarh | Balod, Bastar, Bijapur, Bilaspur, Dakshin Bastar Dantewada, Dhamtari, Durg, Janjgir-Champa, Jashpur, Kabeerdham, Korba, Korea, Mahasamund, Narayanpur, Raigarh, Raipur, Rajnandgaon, Surguja, Uttar Bastar Kanker | 19 |
| Delhi | New Delhi, South, South West | 3 |
| Goa | South Goa | 1 |
| Gujarat | Ahmedabad, Bhavnagar, Chhotaudepur, Jamnagar, Junagadh, Kachchh, Mahesana, Narmada, Panch Mahals, Rajkot, Surendranagar | 11 |
| Haryana | Gurugram, Panipat, Sonipat | 3 |
| Himachal Pradesh | Chamba, Hamirpur, Kangra | 3 |
| Jammu & Kashmir | Anantnag, Jammu | 2 |
| Jharkhand | Bokaro, Dumka, Garhwa, Godda, Gumla, Hazaribagh, Khunti, Latehar, Lohardaga, Palamu, Ramgarh, Ranchi, Saraikela Kharsawan, Simdega, West Singhbhum | 15 |
| Karnataka | Bagalkote, Bengaluru Urban, Dakshina Kannada, Mandya, Mysuru | 5 |
| Kerala | Alappuzha, Ernakulam, Kollam, Kozhikode, Malappuram, Pathanamthitta, Thiruvananthapuram, Thrissur | 8 |
| Ladakh | Kargil, Leh Ladakh | 2 |
| Madhya Pradesh | Betul, Bhopal, Chhindwara, Dewas, Dindori, Guna, Indore, Jhabua, Mandla, Ratlam, Sagar, Shahdol, Shivpuri, Singrauli, Tikamgarh, Vidisha | 16 |
| Maharashtra | Ahilyanagar, Beed, Chandrapur, Gadchiroli, Gondia, Latur, Mumbai, Mumbai Suburban, Nanded, Pune, Yavatmal | 11 |
| Meghalaya | East Khasi Hills, North Garo Hills, Ri Bhoi, South Garo Hills, South West Khasi Hills, West Garo Hills, West Jaintia Hills, West Khasi Hills | 8 |
| Mizoram | Aizawl, Champhai, Lunglei, Mamit, Serchhip | 5 |
| Nagaland | Chumoukedima, Dimapur, Kiphire, Mokokchung, Niuland, Noklak, Peren, Phek, Tseminyu, Tuensang | 10 |
| Odisha | Anugul, Balangir, Baleshwar, Cuttack, Ganjam, Kalahandi, Kandhamal, Kendujhar, Khordha, Koraput, Mayurbhanj, Nabarangpur, Rayagada, Sonepur, Sundargarh | 15 |
| Puducherry | Puducherry | 1 |
| Punjab | Amritsar, Bathinda, Jalandhar, Patiala | 4 |
| Rajasthan | Alwar, Banswara, Baran, Barmer, Bharatpur, Bhilwara, Bikaner, Chittorgarh, Dausa, Dholpur, Jaipur, Jaisalmer, Jhunjhunu, Jodhpur, Nagaur, Udaipur | 16 |
| Sikkim | Gangtok | 1 |
| Tamil Nadu | Chennai, Dindigul, Kancheepuram, Krishnagiri, Madurai, Pudukkottai, Ramanathapuram, Salem, Sivaganga, Thiruvallur, Tiruppur, Tiruvannamalai, Virudhunagar | 13 |
| Telangana | Adilabad, Hyderabad, Khammam, Mahabubnagar, Nalgonda, Narayanpet, Vikarabad, Warangal | 8 |
| Tripura | Sepahijala | 1 |
| Uttar Pradesh | Ambedkar Nagar, Amroha, Ayodhya, Azamgarh, Bahraich, Bara Banki, Basti, Chandauli, Chitrakoot, Deoria, Gautam Buddha Nagar, Ghaziabad, Gonda, Gorakhpur, Jhansi, Kanpur Dehat, Kanpur Nagar, Kheri, Kushinagar, Lucknow, Maharajganj, Mau, Meerut, Muzaffarnagar, Prayagraj, Saharanpur, Sitapur, Unnao, Varanasi | 29 |
| Arunachal Pradesh | Changlang, Shi Yomi, Papum Pare | 3 |
| Andaman & Nicobar | South Andamans | 1 |

**Theme 2 — Education: 25 States, 208 Districts**

| State | Districts (name_as_printed) | # districts |
|---|---|---|
| Arunachal Pradesh | Changlang, Shi Yomi, Papum Pare | 3 |
| Andaman & Nicobar | South Andamans | 1 |
| Assam | Baksa, Barpeta, Bongaigaon, Darrang, Dhemaji, Dhubri, Dibrugarh, Dima Hasao, Goalpara, Golaghat, Jorhat, Kamrup Metro, Karbi Anglong, Kokrajhar, Lakhimpur, Majuli, Marigaon, Nagaon, Sivasagar, Sonitpur, Tinsukia, Udalguri | 22 |
| Chandigarh | Chandigarh | 1 |
| Chhattisgarh | Sukma, Raipur, Manendragarh-Chirmiri-Bharatpur (MCB) | 3 |
| Goa | South Goa, North Goa | 2 |
| Haryana | Sonipat | 1 |
| Jammu & Kashmir | Jammu | 1 |
| Jharkhand | East Singhbhum, West Singhbhum, Sahebganj, Lohardaga | 4 |
| Karnataka | Belgavi, Bengaluru Urban, Bengaluru Rural | 3 |
| Kerala | Alappuzha, Ernakulam, Idukki, Kannur, Kasaragod, Kollam, Kottayam, Kozhikode, Malappuram, Palakkad, Pathanamthitta, Thiruvananthapuram, Thrissur, Wayanad | 14 |
| Lakshadweep | Lakshadweep District | 1 |
| Madhya Pradesh | Agar-Malwa, Alirajpur, Anuppur, Ashoknagar, Balaghat, Barwani, Betul, Bhind, Bhopal, Burhanpur, Chhatarpur, Chhindwara, Damoh, Datia, Dewas, Dhar, Dindori, Guna, Gwalior, Harda, Narmadapuram, Indore, Jabalpur, Jhabua, Katni, Khandwa (East Nimar), Khargone (West Nimar), Mandla, Mandsaur, Morena, Narsimhapur, Neemuch, Niwari, Panna, Raisen, Rajgarh, Ratlam, Rewa, Sagar, Satna, Sehore, Seoni, Shahdol, Shajapur, Sheopur, Shivpuri, Sidhi, Singrauli, Tikamgarh, Ujjain, Umaria, Vidisha | 52 |
| Manipur | Churachandpur, Ukhrul | 2 |
| Mizoram | Aizawl | 1 |
| Nagaland | Kohima, Chumoukedima | 2 |
| Odisha | Bargarh, Jharsuguda, Sambalpur, Deogarh, Sundargarh, Kendujhar, Mayurbhanj, Baleshwar, Bhadrak, Kendrapara, Jagatsinghapur, Cuttack, Jajapur, Dhenkanal, Angul, Nayagarh, Khordha, Puri, Ganjam, Gajapati, Kandhamal, Boudh, Sonepur, Balangir, Nuapada, Kalahandi, Rayagada, Nabarangpur, Koraput, Malkangiri | 30 |
| Puducherry | Karaikal, Puducherry | 2 |
| Punjab | Amritsar, Barnala, Bathinda, Faridkot, Fatehgarh Sahib, Fazilka, Ferozepur, Gurdaspur, Hoshiarpur, Jalandhar, Kapurthala, Ludhiana, Pathankot, Patiala, Rupnagar, S.A.S Nagar, Sangrur, Tarn Taran | 18 |
| Rajasthan | Udaipur | 1 |
| Sikkim | Gangtok, Pakyong, Mangan | 3 |
| Tamil Nadu | Chengalpattu, Chennai, Coimbatore, Cuddalore, Dharmapuri, Kanniyakumari, Madurai, Perambalur, Ramanathapuram, Ranipet, Sivaganga, Thanjavur, The Nilgiris, Thiruvallur, Thiruvarur, Tiruchirappalli, Tirunelveli, Tiruppur, Tiruvannamalai, Virudhunagar | 20 |
| Tripura | Khowai, West Tripura | 2 |
| Uttar Pradesh | Mirzapur, Bhadohi, Varanasi, Lucknow, Sitapur, Bara Banki | 6 |
| Uttarakhand | Almora, Bageshwar, Chamoli, Champawat, Dehradun, Haridwar, Nainital, Pauri Garhwal, Pithoragarh, Rudraprayag, Tehri Garhwal, Udham Singh Nagar, Uttarkashi | 13 |

**Theme 3 — Environmental Sustainability: 10 States, 26 Districts**

| State | Districts | # districts |
|---|---|---|
| Andhra Pradesh | Annamayya, Sri Sathya Sai, Dr. B.R. Ambedkar Konaseema | 3 |
| Assam | Majuli | 1 |
| Gujarat | Kheda, Mahisagar, Anand | 3 |
| Karnataka | Chikkaballapur, Mysuru | 2 |
| Madhya Pradesh | Shahdol | 1 |
| Maharashtra | Thane | 1 |
| Odisha | Angul, Kendujhar, Koraput, Dhenkanal | 4 |
| Rajasthan | Udaipur, Rajsamand, Bhilwara, Chittorgarh, Pratapgarh, Salumbar | 6 |
| Tamil Nadu | Mayiladuthurai, Krishnagiri, Erode | 3 |
| West Bengal | South 24 Parganas, North 24 Parganas | 2 |

**Theme 4 — Financial Inclusion & Literacy: 6 States, 15 Districts**

| State | Districts | # districts |
|---|---|---|
| Gujarat | Anand | 1 |
| Karnataka | Ballari, Kalaburagi | 2 |
| Madhya Pradesh | Ratlam, Dhar | 2 |
| Maharashtra | Nanded, Hingoli, Beed, Dharashiv, Solapur, Amaravati, Yavatmal | 7 |
| Rajasthan | Banswara | 1 |
| Tamil Nadu | Ramanathapuram, Salem | 2 |

**Theme 5 — Health & Nutrition: 3 States, 5 Districts**

| State | Districts | # districts |
|---|---|---|
| Karnataka | Bengaluru Urban | 1 |
| Maharashtra | Mumbai, Nashik, Pune | 3 |
| Telangana | Hyderabad | 1 |

**Theme 6 — Sports: 18 States, 40 Districts**

| State | Districts | # districts |
|---|---|---|
| Assam | Kamrup Metro | 1 |
| Chandigarh | Chandigarh | 1 |
| Delhi | Delhi Central | 1 |
| Gujarat | Ahmedabad, Gandhinagar, Surat | 3 |
| Haryana | Ambala, Bhiwani, Faridabad, Fatehabad, Hisar, Jhajjar, Jind, Kaithal, Rohtak, Sonipat | 10 |
| Jammu & Kashmir | Reasi | 1 |
| Jharkhand | East Singhbhum | 1 |
| Karnataka | Bengaluru Urban, Mysuru, Vijayanagara | 3 |
| Kerala | Ernakulam | 1 |
| Madhya Pradesh | Bhopal, Indore, Jabalpur | 3 |
| Maharashtra | Nashik, Pune, Thane, Mumbai | 4 |
| Manipur | Imphal East | 1 |
| Punjab | Patiala | 1 |
| Rajasthan | Jaipur | 1 |
| Tamil Nadu | Chennai, Coimbatore, Krishnagiri | 3 |
| Telangana | Hyderabad | 1 |

**Theme 7 — Humanitarian & Relief: 4 (+2) States, 6 (+4) Districts** *(source table layout suggests a possible extraction ambiguity — presented exactly as it appears)*

| State | Districts | # districts |
|---|---|---|
| Assam | Majuli | 1 |
| Karnataka | Kodagu | 1 |
| Maharashtra | Beed | 1 |
| Manipur | Churachandpur, Imphal West, Jiribam | 3 |
| Uttar Pradesh | Baghpat, Lucknow | 2 |
| West Bengal | Kolkata, North 24 Paraganas | 2 |

*(This directly corroborates and extends the "flood relief in Assam, Karnataka, Maharashtra, Manipur" statement independently found in the Integrated Annual Report 2024-25's CSR section, plus adds Uttar Pradesh and West Bengal.)*

---
---

**Partners named (`funder_partners`)**

*`org_id`/`partner_funder_id` need matching against your registry — shown here with names + best-guess `partner_kind` only.*

| funder | program | fiscal_year | partner_name | partner_kind | notes | source_url |
|---|---|---|---|---|---|---|
| Axis Bank Foundation | Sustainable Livelihood Programme | Ongoing since 2012 | **SRIJAN** (Self Reliant Initiatives through Joint Action) | ngo | Rajasthan, 4 districts. | ABF sustainable-livelihood page |
| Axis Bank Foundation | Sustainable Livelihood Programme | Undated | **Dilasa Sanstha** | ngo | Maharashtra, 10 districts. | ABF sustainable-livelihood page |
| Axis Bank Foundation | Sustainable Livelihood Programme (co-funders, not implementers) | FY2024-25 | **Axis Capital Limited** | company *(Axis Group entity — also potentially `partner_funder_id` if Axis Capital itself has a funder row)* | Named funding partner quote in AR24-25 (Atul Mehra, MD&CEO). | ABF AR 2024-25 |
| Axis Bank Foundation | Sustainable Livelihood Programme (co-funder) | FY2024-25 | **Axis Asset Management Company Limited** (Axis Mutual Fund) | company | Named funding partner quote (B. Gopkumar, MD&CEO). | ABF AR 2024-25 |
| Axis Bank Foundation | Sustainable Livelihood Programme (co-funder) | FY2024-25 | **Axis Securities Limited** | company | Named funding partner quote (Pranav Haridasan, MD&CEO). | ABF AR 2024-25 |
| Axis Bank Foundation | Sustainable Livelihood Programme (co-funder) | FY2024-25 | **Axis Trustee Services Limited** | company | Named funding partner quote (Rahul Choudhary, MD&CEO). | ABF AR 2024-25 |
| Axis Bank Foundation | Sustainable Livelihood Programme (co-funder) | FY2024-25 | **Axis Finance Limited** | company | Named funding partner quote (Sai Giridhar, MD&CEO). | ABF AR 2024-25 |
| Axis Bank Foundation | Sustainable Livelihood Programme (co-funder) | FY2024-25 | **Freecharge Payment Technologies Private Limited** | company | Named funding partner quote (Sumit Bhatnagar, CEO). | ABF AR 2024-25 |
| Axis Bank Foundation | Sustainable Livelihood Programme (co-funder) | FY2024-25 | **Invoicemart (A.TReDS)** | company | Named funding partner quote (Prakash Sankaran, MD&CEO). | ABF AR 2024-25 |
| Axis Bank Limited (direct, not via ABF) | Financial Literacy through Mobile Vans | FY2022-23 | **CSC Academy** | other | Operates 20 mobile vans via Village Level Entrepreneurs. | Axis Bank AR 2024-25 |
| Axis Bank Limited (direct) | Child Heart Surgeries | FY2022-23 | **Sri Sathya Sai Health & Education Trust** | hospital *(operates Sri Sathya Sai Sanjeevani Hospital, Raipur)* | 300 surgeries. | Axis Bank AR 2024-25 |
| Axis Bank Limited (direct) | Mid-Day Meal Program | FY2022-23 | **Akshaya Patra Foundation** | ngo | ~1 lakh children, 4 states. | Axis Bank AR 2024-25 |
| Axis Bank Limited (direct) | Axis DilSe — Lyzon Friendship School | Undated | **Sunbird Trust** | ngo | Manipur. | Axis Bank AR 2024-25 |

---
---

**Grants to NGOs (`grants`)**

⚠️ I have **no visibility into your NGO registry** (`orgs.id`), and `org_id` is a required field for this table — so I cannot produce valid, insertable rows. What I *can* offer is a candidate list of named partners above that look like NGO-registry matches worth checking, with what's known about each (amount is **not** required by this schema, so it's fine to leave blank where genuinely undisclosed):

| Candidate title | Likely org (needs `org_id` match) | amount | currency | status | outcomes (JSON) | notes |
|---|---|---|---|---|---|---|
| SRIJAN — Rajasthan livelihoods partnership | SRIJAN | *(not disclosed)* | INR | active *(ongoing since 2012, still referenced)* | `{}` | Check if "SRIJAN" / "Self Reliant Initiatives through Joint Action" exists in your `orgs` table. |
| Dilasa Sanstha — Maharashtra tribal livelihoods | Dilasa Sanstha | *(not disclosed)* | INR | unconfirmed *(undated source, activity-status not re-verified)* | `{}` | — |
| Akshaya Patra — Mid-Day Meal Program | Akshaya Patra Foundation | *(not disclosed)* | INR | unconfirmed *(assessed FY22-23 window; current status not re-verified)* | `{"children_covered": 100000, "states": 4}` | — |
| Sri Sathya Sai Health & Education Trust — Child Heart Surgeries | Sri Sathya Sai Health & Education Trust | *(not disclosed)* | INR | unconfirmed | `{"surgeries": 300, "success_rate_pct": 100}` | — |
| Sunbird Trust — Axis DilSe Lyzon Friendship School | Sunbird Trust | *(not disclosed)* | INR | unconfirmed | `{}` | — |

*If any of these five organisations already exist in your `orgs` table, this is the ready-made list to convert into real `grants` rows once `org_id` is matched.*

---
---

---
---

**Calls for proposals (`rfps`)**

⚠️ **None found — genuinely, not a research gap.** Both Axis Bank Foundation and Axis Bank Limited operate on a **relationship/partnership-led selection model**, not a public dated call for proposals. Confirmed by: (1) no "apply now"/open-call page exists anywhere on axisbankfoundation.org or axis.bank.in/csr; (2) the TISS-ABF CSR Process Manual (2015) describes an "intensive" internal proposal-structuring process with ABF's team pre-identifying and hand-selecting partners, not a public submission window; (3) a third-party grant-aggregator site (grantedai.com) that listed "Axis Bank Foundation CSR Initiatives" as a generic evergreen entry simply redirects back to the official page with no actual dated call, deadline, or amount range — confirming there isn't one to find.

| title | status | deadline | amount_min | amount_max | eligibility (JSON) | notes | source_url |
|---|---|---|---|---|---|---|---|
| *(no rows — no open or past dated call exists)* | — | — | — | — | `{}` | If your team wants a placeholder row to represent "relationship_only" application mode (consistent with the `application_modes` finding in this file's earlier Part D), it should read: `status="closed"`, `notes="No public RFP mechanism exists; partner selection is relationship-led per official CSR Policy PDF (12A/80G/CSR-1 + 3-yr track record required of any partner, per the CSR Policy)."` | — | https://www.axisbankfoundation.org/download/knowledge-corner/TISS-ABF-CSR-Process-Manual.pdf |

---
---

**Application forms (`proposal_templates`)**

⚠️ **None found.** No downloadable blank application form, concept-note template, or due-diligence checklist template is published on either axisbankfoundation.org or axis.bank.in. The closest artifact is the **TISS-ABF CSR Process Manual (2015)** — but this is a third-party case-study/knowledge-sharing document (published via the Tata Institute of Social Sciences' CSR knowledge centre, hosted on ABF's own "Knowledge Corner"), describing ABF's internal process narratively, not a fillable form NGOs can download and submit.

| name | kind | version | notes | source_url |
|---|---|---|---|---|
| *(no rows — no fillable template exists)* | — | — | Closest artifact is descriptive, not a form: "TISS-ABF CSR Process Manual" (2015), which narrates ABF's proposal-structuring and selection process but provides no blank form. | https://www.axisbankfoundation.org/download/knowledge-corner/TISS-ABF-CSR-Process-Manual.pdf |

---
---

**Contacts (`contacts`)**

*All rows below are for **Axis Bank Foundation only** — the Bank's own CSR Committee (Vishwanathan, Anand, Ganesh, Mahendra Dev) and `csr@axisbank.com` have been removed from this table, since that governance body and mailbox belong to Axis Bank Limited, not the Foundation (they remain documented separately in the `funder_csr_years` section above, correctly attributed). The general Foundation mailbox is likewise not force-fit into a fake "general inquiries" row here — see the note below the table for where it now lives instead. Two named **programme-level** staff have been added (`kind=programme`), addressing the earlier gap where only Trustees were listed.*

| funder | name | role | kind | email | phone | is_public | verified | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Axis Bank Foundation | S. Ramadorai | Chairperson, Axis Bank Foundation (Trustee since 2010) | office_bearer | — | — | Yes | Yes | Padma Bhushan; former CEO & MD, TCS. | https://www.axisbankfoundation.org/about-us/board-of-trustees.html | ABF Board of Trustees page | 2026-09-29 | FY2024-25 (AR24-25 roster) |
| Axis Bank Foundation | Dhruvi Shah | Executive Trustee & CEO (Trustee since 2021; CEO since 2020) | office_bearer | — | — | Yes | Yes | LinkedIn profile confirms operational scope: "Establish and manage NGO partnerships; Develop and manage Grant Portfolio." | https://in.linkedin.com/in/dhruvi-shah-234b2a12 ; https://www.axisbankfoundation.org/about-us/board-of-trustees.html | ABF Board of Trustees page + LinkedIn | 2026-09-29 | FY2024-25 (AR24-25 roster) |
| Axis Bank Foundation | Sheela Patel | Trustee (since 2006) | office_bearer | — | — | Yes | Yes | Founder-Director, SPARC; Padma Shri (2011). | https://www.axisbankfoundation.org/about-us/board-of-trustees.html | ABF Board of Trustees page | 2026-09-29 | FY2024-25 |
| Axis Bank Foundation | Som Mittal | Trustee (since 2015) | office_bearer | — | — | Yes | Yes | Former Chairman/President, NASSCOM. | (same) | (same) | 2026-09-29 | FY2024-25 |
| Axis Bank Foundation | Rajesh Dahiya | Trustee (since 2015) | office_bearer | — | — | Yes | Yes | Founder-CEO, GoodGovern; former Executive Director, Axis Bank Ltd. | (same) | (same) | 2026-09-29 | FY2024-25 |
| Axis Bank Foundation | Sushma Iyengar | Trustee (since 2019) | office_bearer | — | — | Yes | Yes | Founder, Kutch Mahila Vikas Sangathan. | (same) | (same) | 2026-09-29 | FY2024-25 |
| Axis Bank Foundation | Munish Sharda | Trustee (since 2023) | office_bearer | — | — | Yes | Yes | Also Executive Director, Axis Bank Ltd. — cross-listed there too, not duplicated in this table. | (same) | (same) | 2026-09-29 | FY2024-25 |
| Axis Bank Foundation | Vijay Mulbagal | Trustee (since 2024) | office_bearer | — | — | Yes | Yes | Also Group Executive & Head of Wholesale Bank Coverage/Sustainability, Axis Bank Ltd. | (same) | (same) | 2026-09-29 | FY2024-25 |
| Axis Bank Foundation | Isha Ayyer | Senior Manager, CSR | programme | — *(not published; LinkedIn does not list a work email)* | — | **No** *(sourced from personal LinkedIn profile, not an ABF-published page — mark `is_public = No`)* | Unverified *(single-source, not cross-confirmed against an official ABF page)* | At Axis Bank Foundation since Mar 2022; prior CSR/employability roles at RPG Foundation and Indian Grameen Services. | https://in.linkedin.com/in/isha-ayyer-3b292418 | LinkedIn (self-reported profile) | 2026-09-29 | As of profile view, Sept 2026 |

**Where the general Foundation mailbox now lives:** `foundation@axis.bank.in` is a general/departmental inbox, not tied to one named person, so per your guidance it has been **moved out of `contacts` and into the `profile` JSON** in Part A (Basic Profile) at the top of this file — recommend adding it there as e.g. `"general_contact_email": "foundation@axis.bank.in"` under the existing `profile` JSON blob, or as a new dedicated field if your schema adds one. (Note: one older PDF footer showed `foundation@axisbank.com` instead — flagged as a possible legacy-domain inconsistency; treat `.axis.bank.in` as current/primary per the live website.)

---
---

**Impact numbers (`metrics`)**

*Split by reporting entity. All `is_self_reported = Yes` (funder's own disclosures); `method` marked `monitoring_data` unless otherwise noted.*

**Axis Bank Foundation — Sustainable Livelihood Programme (cumulative, as of 31 March 2025 unless noted):**

| name | value | period | stage | unit | notes |
|---|---|---|---|---|---|
| Households impacted (cumulative) | 2,046,247 | Since 2019 (Mission 2 Million) | outcome | households | Target was 2,000,000 — exceeded. |
| Households impacted (FY24-25 only) | 387,467 | FY2024-25 | output | households | Of which 372,881 via Rural Livelihoods, 14,586 via Skill Development. |
| Villages covered (cumulative) | 23,686 | as of FY2024-25 | output | villages | — |
| Blocks covered (cumulative) | 775 | as of FY2024-25 | output | blocks | — |
| Districts covered (cumulative) | 300 | as of FY2024-25 | output | districts | — |
| States/UTs covered (cumulative) | 32 | as of FY2024-25 | output | states/UTs | Up from 26 (FY22-23) → 28 (FY23-24). |
| Water harvesting potential created (cumulative) | 166,000,000 | Since Mission 2 Million (2019) | outcome | litres | — |
| Trees planted (cumulative, horticulture & agroforestry) | 6,000,000 | Since Mission 2 Million | outcome | trees | — |
| Families supported — sustainable agriculture | 40,000 | Since Mission 2 Million | outcome | families | — |
| Families supported — kharif crops | 1,550,000 | Since Mission 2 Million | outcome | families | — |
| Families supported — rabi crops | 1,010,000 | Since Mission 2 Million | outcome | families | — |
| Families supported — livestock rearing | 620,000 | Since Mission 2 Million | outcome | families | — |
| Young rural entrepreneurs supported (cumulative) | 30,000 | Since Mission 2 Million | outcome | individuals | Of which 10,000 in FY24-25 alone. |
| Total CSR spend (FY24-25) | 231.96 | FY2024-25 | input | ₹ crore | See funder_csr_spend section. |

**Axis Bank Limited — company-wide CSR beneficiaries by theme (FY2024-25, from official BRSR):**

| name | value | unit | % from vulnerable/marginalised groups | period | stage | notes |
|---|---|---|---|---|---|---|
| Persons benefitted — Education | 856,008 | persons | 100% | FY2024-25 | outcome | Per BRSR Principle 8 disclosure. |
| Saplings planted — Environment | 3,273,765 | saplings | — (not disclosed) | FY2024-25 | output | Total Tree Plantation figure. |
| Persons benefitted — Financial Inclusion | 198,459 | persons | 95% | FY2024-25 | outcome | — |
| Households benefitted — Sustainable Livelihood | 387,467 | households | 100% | FY2024-25 | outcome | Matches ABF's own FY24-25 figure exactly — good cross-source consistency check. |
| Persons benefitted — Sports | 381 | persons | 50% | FY2024-25 | outcome | Newly added to CSR portfolio this year (Olympic & grassroot sports). |
| Aspirational District CSR spend (total) | 67.79 | ₹ crore | — | FY2024-25 | input | 19 states — see funder_csr_spend section for full state breakdown. |

---
---

**Documents (`documents`)**

*All downloaded and read in full during this research. `is_ai_generated = No` throughout (all are primary-source originals); `status = read`; `is_public = Yes` throughout.*

| title | doc_type | source_url | source_name | as_of |
|---|---|---|---|---|
| Axis Bank Foundation Annual Report 2024-25 | annual report | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf | ABF website | FY2024-25 |
| Axis Bank Foundation Annual Report 2015-16 | annual report | https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/Axis-Bank-Foundation-Annual-Report-2015-16.pdf | ABF website | FY2015-16 |
| TISS-ABF CSR Process Manual | brochure *(knowledge-sharing case study, not a policy doc)* | https://www.axisbankfoundation.org/download/knowledge-corner/TISS-ABF-CSR-Process-Manual.pdf | ABF Knowledge Corner | ~2015 |
| Axis Bank Limited Integrated Annual Report 2024-25 | annual report | https://www.axis.bank.in/docs/default-source/annual-reports/for-axis-bank/annual-report-for-the-year-2024-2025.pdf | Axis Bank website | FY2024-25 |
| Axis Bank Limited Annual Report 2022-23 | annual report | https://www.axis.bank.in/annual-reports/2022-2023/pdfs/Axis%20Bank%20AR%202022-23.pdf | Axis Bank website | FY2022-23 |
| Axis Bank Limited Integrated Annual Report 2025-26 | annual report | https://www.axis.bank.in/docs/default-source/annual-reports/for-axis-bank/annual-report-for-the-year-2025-2026.pdf | Axis Bank website | FY2025-26 |
| Axis Bank Limited CSR Impact Report FY2024-25 | impact assessment | https://www.axis.bank.in/docs/default-source/csr-reports-and-disclosures/csr-impact-report-fy-2024-25.pdf | Axis Bank website | FY2024-25 |
| Axis Bank Limited Business Responsibility & Sustainability Report (BRSR) FY2024-25 | board report *(statutory sustainability disclosure)* | https://www.axis.bank.in/docs/default-source/business-responsibility-reports/business-responsibility-sustainability-report-for-the-year-2024-25.pdf | Axis Bank website | FY2024-25 |
| Axis Bank Limited CSR Policy | CSR policy | *(no separate standalone CSR Policy PDF located for Axis Bank in this pass — CSR policy text appears embedded within the Annual Report's Board's Report/Annexure 4 section instead)* | — | ~ongoing |

⚠️ **Gap flag:** a standalone, dedicated Axis Bank Foundation "Annual Action Plan" document (as a distinct document type from the narrative Annual Report) was not independently located/verified at a specific URL in this research pass. Recommend checking `axisbankfoundation.org/financials/overview.html` or `axis.bank.in/csr/csr-reports-disclosures` directly if your team needs this as a separately-stored document.

---
---

---
---

**Programme places (`program_locations`)**

⚠️ **Entity/naming flag before the tables:** the official CSR Impact Report FY2024-25 organizes Axis Bank's *entire* CSR portfolio into 7 themes — **Lives & Livelihoods** (delivered via Axis Bank Foundation), plus **Education, Environmental Sustainability, Health & Nutrition, Financial Inclusion & Literacy, Sports, and Humanitarian & Relief** (delivered *directly by Axis Bank Limited* or via non-ABF implementation partners, per the Bank's own CSR policy language: "directly, through ABF and through credible implementation partners"). This "Education" theme is a **current, active, Bank-direct programme** — do not confuse it with **Axis Bank Foundation's own historical "Education" theme (2006–~2011-12, concluded)** documented earlier in the `programs` table. I've added the 5 non-SLP themes below as new theme-level entries; recommend inserting them into your `programs` table (kind=`theme`, `funder_id`=Axis Bank Limited) if not already present, distinct from ABF's like-named historical theme.

*State-level rows only below (district-level detail already fully documented in the `funder_footprints` section above — cross-reference there rather than duplicating ~570 district rows here). All rows: `role = operates`, `source_name = "Axis Bank CSR Impact Report FY2024-25"`, `fetched_at = 2026-09-29`, `as_of = FY2024-25`, `source_url = https://www.axis.bank.in/docs/default-source/csr-reports-and-disclosures/csr-impact-report-fy-2024-25.pdf` unless noted otherwise.*

**Sustainable Livelihood Programme (→ Axis Bank Foundation) — operates in 31 states/UTs:**
Andhra Pradesh · Assam · Bihar · Chandigarh · Chhattisgarh · Delhi · Goa · Gujarat · Haryana · Himachal Pradesh · Jammu & Kashmir · Jharkhand · Karnataka · Kerala · Ladakh · Madhya Pradesh · Maharashtra · Meghalaya · Mizoram · Nagaland · Odisha · Puducherry · Punjab · Rajasthan · Sikkim · Tamil Nadu · Telangana · Tripura · Uttar Pradesh · Uttarakhand · West Bengal *(district counts per state are in the funder_footprints table above)*

**Education (→ Axis Bank Limited, direct — NOT the same as ABF's historical Education theme) — operates in 25 states:**
Arunachal Pradesh · Andaman & Nicobar · Assam · Chandigarh · Chhattisgarh · Goa · Haryana · Jammu & Kashmir · Jharkhand · Karnataka · Kerala · Lakshadweep · Madhya Pradesh · Manipur · Mizoram · Nagaland · Odisha · Puducherry · Punjab · Rajasthan · Sikkim · Tamil Nadu · Tripura · Uttar Pradesh · Uttarakhand

**Environmental Sustainability (→ Axis Bank Limited, direct) — operates in 10 states:**
Andhra Pradesh · Assam · Gujarat · Karnataka · Madhya Pradesh · Maharashtra · Odisha · Rajasthan · Tamil Nadu · West Bengal

**Financial Inclusion & Literacy (→ Axis Bank Limited, direct) — operates in 6 states:**
Gujarat · Karnataka · Madhya Pradesh · Maharashtra · Rajasthan · Tamil Nadu

**Health & Nutrition (→ Axis Bank Limited, direct) — operates in 3 states:**
Karnataka · Maharashtra · Telangana

**Sports (→ Axis Bank Limited, direct — new to CSR portfolio in FY2024-25) — operates in 18 states:**
Assam · Chandigarh · Delhi · Gujarat · Haryana · Jammu & Kashmir · Jharkhand · Karnataka · Kerala · Madhya Pradesh · Maharashtra · Manipur · Punjab · Rajasthan · Tamil Nadu · Telangana · Uttar Pradesh · West Bengal

**Humanitarian & Relief (→ Axis Bank Limited, direct) — operates in 4-6 states:**
Assam · Karnataka · Maharashtra · Manipur *(+ Uttar Pradesh, West Bengal per the extended table — see extraction-ambiguity note in funder_footprints)*

---

**Project-level `program_locations` rows (specific evidence, various years — not all FY2024-25):**

| program_id | location_id | role | valid_from | valid_to | note | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|
| SRIJAN Partnership | Rajasthan | `funds` | 2012 | — | 4 districts (unnamed individually in source). | https://www.axisbankfoundation.org/sustainable-livelihood/sustainable-livelihood.html | ABF sustainable-livelihood page | 2026-09-29 | Undated legacy page |
| Dilasa Sanstha Partnership | Maharashtra | `funds` | — | — | 10 districts (unnamed individually). | (same) | (same) | 2026-09-29 | Undated |
| Rural Livelihoods (pillar) | Odisha | `operates` | FY2024-25 | — | Siangbali GP, Daringbadi block — case study evidence. | ABF AR 2024-25 | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 |
| Rural Livelihoods (pillar) | Madhya Pradesh | `operates` | FY2024-25 | — | "Sita Devi, Farmer" community-voice case study; district not specified. | ABF AR 2024-25 | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 |
| Environmental Sustainability / NRM | Jharkhand | `funds` | FY2024 | — | FICCI Sustainable Agriculture Award 2024 (named as a 3-state set). | ABF AR 2024-25 | ABF Annual Report 2024-25 | 2026-09-29 | FY2024 (award year) |
| Environmental Sustainability / NRM | Telangana | `funds` | FY2024 | — | Same FICCI award evidence. | ABF AR 2024-25 | ABF Annual Report 2024-25 | 2026-09-29 | FY2024 |
| Environmental Sustainability / NRM | Maharashtra | `funds` | FY2024 | — | Same FICCI award evidence. | ABF AR 2024-25 | ABF Annual Report 2024-25 | 2026-09-29 | FY2024 |
| Sustainable Livelihood Programme | Gujarat | `operates` | — | — | Gallery caption: "Senior Management Visits a Project Site in Dahod, Gujarat." | ABF homepage | ABF homepage | 2026-09-29 | Undated |
| Towards the Northeast (phase) | *(North-East India — region only, no individual state resolved to location_id)* | `priority` | FY2024-25 | — | New explicit strategic-expansion chapter; no per-state breakdown published. | ABF AR 2024-25 | ABF Annual Report 2024-25 | 2026-09-29 | FY2024-25 |
| Child Heart Surgeries (project) | Chhattisgarh | `operates` | FY2022-23 | — | Sri Sathya Sai Sanjeevani Hospital, Raipur; note this state is **not** among the FY24-25 "Health & Nutrition" 3-state list above — likely an earlier/different-scope project, not necessarily still active in the same form. | Axis Bank AR 2024-25 | Axis Bank Integrated AR 2024-25 | 2026-09-29 | FY2022-23 (assessed in FY24-25 report) |
| Mid-Day Meal Program (project) | Uttar Pradesh, Gujarat, Karnataka, Odisha | `operates` | 2022-12 | 2023-03 | Also **not** among the FY24-25 "Health & Nutrition" 3-state list — earlier/different-scope project. | Axis Bank AR 2024-25 | Axis Bank Integrated AR 2024-25 | 2026-09-29 | FY2022-23 |
| Axis DilSe — Lyzon Friendship School (project) | Manipur | `operates` | — | — | Singngat subdivision, Churachandpur district. | Axis Bank AR 2024-25 | Axis Bank Integrated AR 2024-25 | 2026-09-29 | Undated |
| (Historical, ABF pre-pivot) | Madhya Pradesh, Maharashtra, West Bengal, Andhra Pradesh, Odisha | `funds` | ~2015 | ~2015-16 | Named as major-budget-allocation states circa 2015; not re-confirmed as current. | TISS-ABF CSR Process Manual | TISS-ABF CSR Process Manual (2015) | 2026-09-29 | ~2015 |

*Registered-office row (`role=registered`) already captured in the `funder_locations` section earlier in this file (Maharashtra — Mumbai, Axis House, Worli) — not duplicated here.*

---
---

---
---

**Grant places (`grant_locations`)**

⚠️ **Same structural blocker as the `grants` table earlier:** `grant_id` is a required foreign key into `grants.id`, but I was unable to produce real `grants` rows in that earlier section (no visibility into your `orgs` registry to satisfy the required `org_id`). Consequently I **cannot produce valid, insertable `grant_locations` rows either** — a location can't be attached to a grant that doesn't exist yet in your DB. What follows is the location evidence for each of the 5 candidate grants flagged earlier, ready to attach the moment those candidates get real `grant_id`s.

| candidate grant (→ future grant_id) | location_id | note | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|
| SRIJAN — Rajasthan livelihoods partnership | Rajasthan (state level; **4 districts, not individually named in source**) | "Reached out to farmers in four districts of Rajasthan... since 2012." No block/village-level detail published. | https://www.axisbankfoundation.org/sustainable-livelihood/sustainable-livelihood.html | ABF sustainable-livelihood page | 2026-09-29 | Undated legacy page |
| Dilasa Sanstha — Maharashtra tribal livelihoods | Maharashtra (state level; **10 districts, not individually named**) | "Work towards creating sustainable livelihoods for tribal people in 10 districts of Maharashtra... bring water security." No block/village-level detail published. | https://www.axisbankfoundation.org/sustainable-livelihood/sustainable-livelihood.html | ABF sustainable-livelihood page | 2026-09-29 | Undated |
| Akshaya Patra — Mid-Day Meal Program | Uttar Pradesh, Gujarat, Karnataka, Odisha (state level only); assessment survey itself narrowed to **"15 schools in Odisha and Karnataka"** specifically (school-level, but individual school names not published) | ~1 lakh children, Dec 2022–Mar 2023. | Axis Bank Integrated AR 2024-25 | Axis Bank Integrated AR 2024-25 | 2026-09-29 | FY2022-23 (assessed in FY24-25 report) |
| Sri Sathya Sai Health & Education Trust — Child Heart Surgeries | **"Sri Sathya Sai Sanjeevani Hospital, Raipur, Chhattisgarh"** (facility-level — the most precise location in this set); patients drawn from 15 unnamed states | 300 surgeries performed at this single named hospital. | Axis Bank Integrated AR 2024-25 | Axis Bank Integrated AR 2024-25 | 2026-09-29 | FY2022-23 |
| Sunbird Trust — Axis DilSe Lyzon Friendship School | **"Lyzon Friendship School, Singngat subdivision, Churachandpur district, Manipur"** (school + subdivision level — most granular single-site location found in this entire research pass) | Tuition/hostel fee support, Science Lab, digital classroom at this one named school. | Axis Bank Integrated AR 2024-25 | Axis Bank Integrated AR 2024-25 | 2026-09-29 | Undated |

**Bonus — most granular block/village-level evidence found overall (not yet tied to a named grant, since the implementing partner for this specific project wasn't identified by name beyond "the Foundation"):**

| Location (finest level found) | Note | Source |
|---|---|---|
| **Siangbali Gram Panchayat, Daringbadi block, Odisha** | MGNREGS convergence case study — land/water management training; this is genuine village/GP-level detail, but no specific grant title or NGO partner name was published alongside it, only "the Foundation." | ABF Annual Report 2024-25 |

*If your team can match "SRIJAN," "Dilasa Sanstha," "Akshaya Patra Foundation," "Sri Sathya Sai Health & Education Trust," or "Sunbird Trust" against existing `orgs` rows and create the corresponding `grants` entries, this table converts directly into 5 real, insertable `grant_locations` rows.*

---
---

## Sources

1. Axis Bank Foundation — Homepage: https://www.axisbankfoundation.org
2. Axis Bank Foundation — Overview: https://www.axisbankfoundation.org/about-us/overview.html
3. Axis Bank Foundation — Board of Trustees: https://www.axisbankfoundation.org/about-us/board-of-trustees.html
4. Axis Bank Foundation — Financial Overview (Annual Reports index): https://www.axisbankfoundation.org/financials/overview.html
5. Axis Bank Foundation — Annual Report 2024-25 (PDF, downloaded & read in full for financials/trustees): https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/abf_ar_2024-25-1.pdf
6. Axis Bank Foundation — Annual Report 2015-16 (PDF; source of FCRA registration number and "1% of PAT" historical funding detail): https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/Axis-Bank-Foundation-Annual-Report-2015-16.pdf
7. Axis Bank — Axis Bank Foundation (CSR arm) page: https://www.axis.bank.in/csr/axis-bank-foundation
8. Axis Bank — CSR and Sustainability overview: https://www.axis.bank.in/csr
9. Axis Bank — Corporate Profile (confirms "established in 2006 as a Trust"): https://www.axis.bank.in/about-us/corporate-profile
10. Axis Bank — CSR Reports & Disclosures (Annual Report archive links, 2014-15 through 2025-26): https://www.axis.bank.in/csr/csr-reports-disclosures
11. give.do — Axis Bank Limited funder profile (cross-check of parent-company CSR grant values, policy themes): https://give.do/discover/1C6P/axis-bank-limited
12. Axis Bank Limited — Secretarial Audit / CIN confirmation (MSEI-hosted Annual Report 2025 filing): https://www.msei.in/SX-Content/Listing/Annual-Reports/2025/AXISBANK-2025.pdf
13. India Development Review — Axis Bank Foundation partnership profile (secondary, cross-check only): https://idronline.org/partnership/axis-bank-foundation
14. Axis Bank Foundation — TISS-ABF CSR Process Manual, 2015 (PDF; source of ~2015 state-allocation detail and NGO-partner 12A requirement): https://www.axisbankfoundation.org/download/knowledge-corner/TISS-ABF-CSR-Process-Manual.pdf
15. Axis Bank Foundation — Sustainable Livelihood partner-story page (legacy; source of Rajasthan/SRIJAN and Maharashtra/Dilasa Sanstha examples): https://www.axisbankfoundation.org/sustainable-livelihood/sustainable-livelihood.html
16. Axis Bank Limited — Integrated Annual Report 2024-25 (PDF, downloaded & read in full; source of Annexure 4 CSR statutory figures FY24-25, CSR Committee composition): https://www.axis.bank.in/docs/default-source/annual-reports/for-axis-bank/annual-report-for-the-year-2024-2025.pdf
17. Axis Bank Limited — Annual Report 2022-23 (PDF; source of FY22-23 statutory CSR figures): https://www.axis.bank.in/annual-reports/2022-2023/pdfs/Axis%20Bank%20AR%202022-23.pdf
18. Axis Bank Limited — Integrated Annual Report 2025-26 (PDF; source of FY25-26 statutory CSR figures): https://www.axis.bank.in/docs/default-source/annual-reports/for-axis-bank/annual-report-for-the-year-2025-2026.pdf
19. Axis Bank Limited — Integrated Annual Report 2025-26 microsite (source of FY22-23→FY25-26 CSR Spend summary infographic, incl. FY23-24 ≈₹269 cr): https://www.axis.bank.in/annual-reports/2025-2026/index.html
20. Axis Bank Limited — CSR Impact Report FY2024-25 (PDF, downloaded & read in full; source of complete state/district geographic footprint across all 7 CSR themes, and Mission 1/2/4 Million precise date ranges): https://www.axis.bank.in/docs/default-source/csr-reports-and-disclosures/csr-impact-report-fy-2024-25.pdf
21. Axis Bank Limited — Business Responsibility & Sustainability Report (BRSR) FY2024-25 (PDF, downloaded & read in full; source of real state-wise ₹ crore Aspirational District CSR spend table): https://www.axis.bank.in/docs/default-source/business-responsibility-reports/business-responsibility-sustainability-report-for-the-year-2024-25.pdf

---

*Caveats: (1) give.do's "Axis Bank Limited" profile page shows some genuinely real figures (Grant Value by year, Policy Themes, CSR Policy link) mixed with login-gated placeholder content (Programs, Leadership Team, Contact) — only the real, unlocked figures were used here, consistent with the same platform behavior documented for Infosys Foundation. (2) The "up to 1% of PAT" funding figure is sourced from the 2015-16 Annual Report and may be outdated given Section 135's 2% mandate on the parent Bank since FY2014-15; treat as historical context, not current-year fact, unless independently re-confirmed. (3) No content_hash, extractor_version, or archive_url were auto-generated since this was manual/agent research, not an automated pipeline run.*

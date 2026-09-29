# Missing Data Checklist: Axis Bank Foundation, SBI Foundation, Infosys Foundation

**Last checked:** 2026-09-29
**Files checked:** `Axis_Bank_Foundation_Profile.md`, `SBI_Foundation_Profile.md`, `Infosys_Foundation_Profile.md`
**Checked against:** the Sangam database schema (Part A: the 24 funder tables)

---

## Scorecard: how complete is each profile?

### How the score works
Each field is **weighted by how much it matters.** A missing grant amount costs a lot; a missing archive link costs very little.

| Weight | Which fields | Examples |
|---|---|---|
| **3 points** | **Core facts**: the actual data | name, website, PAN, amount, fiscal_year, partner_name, programme description, metric value |
| **1 point** | **Supporting detail** and the `source_url` | start/end dates, email, target, is_ongoing, partner type |
| **0.25 points** | **Bookkeeping** | archive_url, fetched_at, source_name, as_of, notes, verified, tagged_by |
| **Not scored** | Database IDs and links, plus fields that don't apply to a trust | funder_id, org_id, location_id; average_net_profit, prescribed_csr, unspent/excess spent |

- **Scoring:** a field counts fully if it's filled correctly, 75% if it's filled but has a problem, and 0 if it's missing.
- **Parent data:** parent-company data (Axis Bank Ltd, State Bank of India, Infosys Ltd) scores 0, because it will be removed.
- **Tables left out:** tables that don't apply (e.g. Axis runs no calls for proposals) aren't scored.

### Result

| | Axis Bank Foundation | SBI Foundation | Infosys Foundation |
|---|---|---|---|
| **Overall score (weighted)** | **72% 🟡** | **60% 🟡** | **49% 🔴** |
| Core facts only | 81% 🟡 | 67% 🟡 | 58% 🔴 |
| Grants with a ₹ amount | 0 of 23 | 0 of 6 | 0 of 2 (the other 9 rows are Infosys Ltd's) |
| Values ready to copy in (section 2 of each funder) | 14 | 10 | 5 |
| Suggested `registry_status` | `in_vetting` | `in_vetting` | `in_vetting` |

🟢 85% or more · 🟡 60–84% · 🔴 below 60%

**Rule for `registry_status`:** set `full_profile` when the overall score is 85% or more, core facts are 90% or more, no parent data is left and grant amounts are present. Otherwise keep `in_vetting`.

### By area

| Area | Axis | SBI | Infosys |
|---|---|---|---|
| Identity | 91% 🟢 | 82% 🟡 | 83% 🟡 |
| Money | 50% 🔴 | 28% 🔴 | 4% 🔴 |
| Programmes & reach | 77% 🟡 | 71% 🟡 | 59% 🔴 |
| People & partners | 67% 🟡 | 80% 🟡 | 50% 🔴 |
| Focus & places | 67% 🟡 | 79% 🟡 | 69% 🟡 |
| How to apply | n/a | 32% 🔴 | 39% 🔴 |
| Evidence | 79% 🟡 | 82% 🟡 | 68% 🟡 |

**Money is the weakest area for all three** (Axis 50%, SBI 28%, Infosys 4%). The main reason:
- No NGO grant has an amount.

### By table (and which core facts are missing)

| # | Table | Axis | SBI | Infosys | Core facts missing or wrong |
|---|---|---|---|---|---|
| 1 | funders | 96% 🟢 | 81% 🟡 | 91% 🟢 | Axis: profile · SBI: profile · Infosys: website, profile |
| 2 | funder_identifiers | 97% 🟢 | 93% 🟢 | 88% 🟢 | Infosys: id_value |
| 3 | credential_events | 80% 🟡 | 76% 🟡 | 68% 🟡 | Axis: event_date · SBI: event, event_date · Infosys: event, event_date |
| 4 | funder_tags | 98% 🟢 | 100% 🟢 | 98% 🟢 |  |
| 5 | funder_locations | 51% 🔴 | 68% 🟡 | 53% 🔴 | Axis: role · SBI: role · Infosys: role |
| 6 | funder_csr_years | 46% 🔴 | 0% 🔴 | 0% 🔴 | Axis: spent_on_projects, admin_overheads, total_spent · SBI: fiscal_year, spent_on_projects, admin_overheads, total_spent · Infosys: fiscal_year, spent_on_projects, admin_overheads, total_spent |
| 7 | funder_csr_spend | 50% 🔴 | 26% 🔴 | 0% 🔴 | Axis: project_name, implementing_agency · SBI: project_name, implementing_agency, amount · Infosys: fiscal_year, project_name, implementing_agency, amount |
| 8 | programs | 75% 🟡 | 76% 🟡 | 73% 🟡 | Axis: description · Infosys: status |
| 9 | funder_footprints | 83% 🟡 | 84% 🟡 | 56% 🔴 | Axis: fiscal_year · SBI: name_as_printed · Infosys: fiscal_year, name_as_printed |
| 10 | funder_partners | 54% 🔴 | 83% 🟡 | 49% 🔴 | Axis: partner_kind · SBI: partner_kind · Infosys: fiscal_year, partner_kind |
| 11 | grants | 52% 🔴 | 61% 🟡 | 12% 🔴 | Axis: amount, status · SBI: amount · Infosys: title, amount, status |
| 12 | rfps | n/a | 46% 🔴 | 72% 🟡 | SBI: url, status, deadline, eligibility · Infosys: url |
| 13 | proposal_templates | n/a | 0% 🔴 | 0% 🔴 | SBI: name, kind · Infosys: name, kind |
| 14 | contacts | 80% 🟡 | 78% 🟡 | 50% 🔴 | SBI: kind · Infosys: name, role, kind |
| 15 | metrics | 72% 🟡 | 77% 🟡 | 74% 🟡 | Axis: value, unit, period, stage · SBI: value, unit, stage · Infosys: value, period, stage |
| 16 | documents | 95% 🟢 | 88% 🟢 | 35% 🔴 | SBI: source_url · Infosys: title, doc_type, source_url |
| 17 | news_mentions | 68% 🟡 | 71% 🟡 | 86% 🟢 | Axis: url, seendate · SBI: url, seendate · Infosys: seendate |
| 18 | reference_figures | 81% 🟡 | 88% 🟢 | 71% 🟡 | Axis: value · SBI: kind, value · Infosys: kind, value |
| 19 | program_locations | 64% 🟡 | 0% 🔴 | 0% 🔴 | SBI: role · Infosys: role |
| 20 | program_tags | 100% 🟢 | 98% 🟢 | 93% 🟢 |  |
| 21 | grant_locations | 95% 🟢 | 90% 🟢 | 15% 🔴 | Infosys: note |
| 22 | rfp_locations | n/a | 68% 🟡 | 48% 🔴 | Infosys: role |
| 23 | rfp_tags | n/a | 100% 🟢 | 100% 🟢 |  |
| 24 | template_items | n/a | 0% 🔴 | 0% 🔴 | SBI: ord, item_kind, heading · Infosys: ord, item_kind, heading |

"Missing or wrong" means the field is empty, or filled with a problem (see each funder's Fix section). For Infosys, some fields are listed only because most of the rows are Infosys Ltd data, which gets removed: contacts, documents, grants, footprints.

The same numbers are in **`Funder_Completeness_Scores.csv`**, one row per funder per table, ready to load into the database or a sheet. Re-run the scoring after each round of edits to track progress.

---

## What is this file?

We are building one profile per funder, to load into the Sangam database. This file lists **what is still missing or wrong in each profile**, so anyone on the team can pick up a task and fix it.

Each funder has the same 5 sections:

| Section | What it means | What you do |
|---|---|---|
| **1. Remove** | Data about the parent company (Axis Bank Ltd, State Bank of India, Infosys Ltd), not the foundation | Delete it from the profile |
| **2. Ready to fill** | We already found the value and the source | Copy it into the profile |
| **3. Needs research** | Nobody has found this yet | Look in the source listed |
| **4. Fix** | The value is there but wrong, or contradicts another part of the file | Correct it |
| **5. Empty tables** | Tables with no data at all | Fill them, or confirm they don't apply |

**Not covered here:** ID and link columns such as `funder_id`, `org_id`, `location_id` and `tag_id`. Those get matched when the data is loaded.

---

## Table names in plain words

| Table | What it holds |
|---|---|
| `funders` | Basic profile: name, website, type |
| `funder_identifiers` | ID numbers: PAN, CIN, CSR-1, Darpan, trust registration no. |
| `credential_events` | Registrations and their dates: 12A, 80G, FCRA, CSR-1 |
| `funder_tags` | Sectors the funder works in |
| `funder_locations` | States and districts where the funder works |
| `funder_csr_years` | Money spent per year |
| `funder_csr_spend` | Spend split by sector, project and NGO |
| `programs` | The funder's programmes and projects |
| `funder_footprints` | Where each programme ran, by year |
| `funder_partners` | NGOs and co-funders it works with |
| `grants` | Grants to individual NGOs, with amounts |
| `rfps` | Calls for proposals |
| `proposal_templates` / `template_items` | Application forms and their questions |
| `contacts` | People at the funder |
| `metrics` | Impact numbers (households reached etc.) |
| `documents` | Reports we read |
| `news_mentions` | News about the funder |
| `reference_figures` | Benchmarks, e.g. cost per household, overhead % |
| `program_locations` / `program_tags` | Places and sectors of each programme |
| `grant_locations` | Places each grant covers |

---

## At a glance

| | Axis Bank Foundation | SBI Foundation | Infosys Foundation |
|---|---|---|---|
| **Overall** | Most complete of the three | About half done | Weakest; much of the profile is the parent company's data |
| **Biggest gap** | No grant amounts for any NGO | Two RFP PDFs are downloaded but not used | Most spend and grant data is Infosys Ltd's, not the Foundation's |
| **Biggest error** | ID numbers marked "not found" but they exist (AR 2014-15) | Two different leadership lists | CSR-1 marked "not available" (probably wrong) |
| **Values ready to fill now** | 14 | 10 | 5 |
| **Weighted score** | 72% | 60% | 49% |

### Problems in all three profiles
1. **No grant amounts** for any NGO.
   - **Fix:** look in each NGO's own audited accounts, in the "grants received" note that lists donors.
   - **Example that worked:** SRIJAN's accounts show Axis Bank Foundation gave it ₹4.57 cr in FY2022-23.
2. **`archive_url` is empty almost everywhere.** Save each source page on web.archive.org and paste the link.
3. **`source_url` often says "(same)"** or holds text instead of a real link. Every row needs its own full link.
4. **Parent-company data is mixed in.** Each funder should hold only its own data.
5. **"Current" or "Undated"** is written where a period belongs. Use the period the source covers, e.g. `FY2023-24`. FY text like this is fine.

---
---

# 1. Axis Bank Foundation

### 1.1 Remove (Axis Bank Ltd data)
- [ ] Axis Bank Ltd's CIN `L65110GJ1993PLC020769`, still written in a note under `funder_identifiers`
- [ ] FY2025-26 spend of ₹352.92 cr: it includes money Axis Bank Ltd paid out itself. It appears in 5 places: `funder_csr_years`, `funder_csr_spend`, `metrics`, `reference_figures` and `profile.funding_trend`. Drop it, or flag it clearly as "not ABF only".
- [ ] The news item based on the bank's ESG Data Book (indiacsr.in)

### 1.2 Ready to fill (value and source already found)

| Table | Field | Value | Source |
|---|---|---|---|
| `funder_identifiers` | PAN | AAATU2526R | [ABF Annual Report 2014-15](https://www.axisbankfoundation.org/financials/pdf/Annual-Reports/Axis-Bank-Foundation-Annual-Report-2014-15.pdf), pp.76-86 |
| `funder_identifiers` | Trust registration no. | E-23597 (Mumbai, Charity Commissioner) | same |
| `funder_identifiers` | Former name | UTI Bank Foundation | same |
| `credential_events` | 12A | Registered | same |
| `credential_events` | 80G | Certificate no. 80G/2922/2008/2008-09 | same |
| `funder_csr_years` | FY2014-15 admin cost | ₹3,10,90,493 (auditor: M M Nissim & Co) | same |
| `funder_csr_years` | FY2020-21 and FY2021-22 rows | ₹74.85 cr and ₹84.89 cr total spent | ABF AR 2022-23, p.48 |
| `funder_csr_spend` | FY2020-21 project count | 27 (23 Rural Livelihoods + 4 Skill Development) | ABF AR 2022-23, p.48 |
| `grants` | SRIJAN amount, per year | FY21-22 ₹3,90,65,610 · FY22-23 ₹4,57,40,000 · FY23-24 ₹4,42,20,372 · FY24-25 ₹4,40,67,119 | [SRIJAN audited accounts](https://srijanindia.org/fin_report.php), Note 11 |
| `grants` / `funder_locations` / `grant_locations` | SRIJAN districts | Rajasthan: Bundi, Pali, Pratapgarh, Tonk · MP: Raisen, Anuppur, Sagar, Tikamgarh, Chhindwara · Chhattisgarh: Koriya | [ABF partners page](https://www.axisbankfoundation.org/partners/livelihood.html) |
| `metrics` | Mission 1 Million result | 10,01,253 individuals, achieved Sept 2017 | ABF AR 2022-23, p.16 |
| `metrics` | FY2022-23 outreach | 440 blocks · 39,874 youth trained · 17,665 youth with disabilities · 98 skill centres | ABF AR 2022-23, p.18 |
| `funder_partners` | FY2022-23 co-funders | Axis Bank Ltd, Axis AMC, Axis Capital, Axis Finance, Axis Securities, Axis Trustee, Freecharge | ABF AR 2022-23, p.14 |
| `documents` | Missing reports | ABF AR 2014-15 and SRIJAN financial report | links above |

### 1.3 Needs research

| Table | What's missing | Where to look |
|---|---|---|
| `grants` | Amounts for the other 22 NGOs (WOTR, Harsha Trust, PRADAN, BRLF…) | Each NGO's audited accounts ("grants received" note) |
| `funder_identifiers` | CSR-1 number, NGO Darpan ID | MCA CSR-1 list, ngodarpan.gov.in (both blocked for the agent; try by hand) |
| `credential_events` | FCRA and 12A/80G expiry dates | fcraonline.nic.in, Income Tax portal |
| `funder_csr_years` | Admin cost, impact assessment (FY22-23 onwards) | ABF audited accounts (only the AR 2014-15 includes them so far) |
| `programs` | Start dates for 11 programmes | ABF annual reports, press releases |
| `metrics` | Targets (only 3 of 102 rows have one) | ABF annual reports |
| `contacts` | Email and phone | ABF website, or ask the funder |
| `news_mentions` | Language, country, source, review status | Fill in from each article |

### 1.4 Fix

| Table | Problem | Fix |
|---|---|---|
| `programs` | Mission 1 Million end date is 2018 | Change to 2017-09-30 |
| `programs`, `funder_tags` | Education end date is ~2011-12 | Change to 2016-03-31 (phased out in 2015-16) |
| `credential_events` | PAN, 12A, 80G, reg no. marked "not_found" | Replace with the values in 1.2 |
| `news_mentions` | `kind` is invalid on all 10 rows (e.g. "press_release") | Use only news, press or social |
| `programs` | 2 duplicate rows (Mission 4 Million, Health & Nutrition) | Merge; they also give 2 different end dates |
| `funder_csr_spend` | FY2022-23 project count shows "26 (or 33)" | Pick one value and put the other in notes |
| `funder_locations` | A "Remaining states" row is not a real place | Delete it |
| `reference_figures` | Values like "≈ ₹5,987" | Use plain numbers (5987) |
| Closing notes at the end of the file | Say "no archive links found", "PAN not found" | Update them; both are now out of date |

### 1.5 Empty tables
- `rfps`, `proposal_templates`, `template_items`, `rfp_locations`, `rfp_tags`: **OK to leave empty.** ABF has no open calls and publishes no forms (confirmed).

---
---

# 2. SBI Foundation

### 2.1 Remove (State Bank of India data)
- [ ] All 3 rows in `funder_csr_years` (₹502.32 / ₹610.77 / ₹709.01 cr). These are SBI's bank-wide CSR totals. Keep the SBI→Foundation transfer amounts only as context in `profile.funding_trend`.
- [ ] 5 SBI documents: SBI CSR Policy, SBI CSR Initiatives FY25-26, SBI AR 2024, SBI AR 2024-25, SBI Sustainability Report
- [ ] Partner rows "State Bank of India" and "SBI subsidiary companies" (they fund the foundation; they aren't partners). Also "Assistech Foundation" (it gave an award; it isn't a partner).
- [ ] The metric "SBI's allocation to SBI Foundation FY2025-26"
- [ ] The DHAN Academy grant candidate (it's a training venue, not a grant)

### 2.2 Ready to fill (value and source already found)

| Table | Field | Value | Source |
|---|---|---|---|
| `rfps` | Gram Seva deadline and budget | Deadline 2024-12-12 · ₹3–4 cr over 2 years · status closed | `SBI_Foundation_GramSeva_RFP.pdf` (already downloaded) |
| `rfps` | PwD Centre of Excellence call (new row) | Deadline 2024-12-15 · ₹25 lakh–₹5 cr over 12–36 months · status closed | `SBI_Foundation_PWD_CoE_RFP.pdf` (already downloaded) |
| `rfps` | Eligibility rules | "Selection Criteria" section of both PDFs | same PDFs |
| `proposal_templates` | 4–7 forms | NDA, due-diligence checklist, evaluation form, financial format (+ MoU, key-info sheet, guidelines for Gram Seva) | same PDFs (annexures) |
| `template_items` | Form questions | Checklist items, evaluation criteria with points, eligibility rules | same PDFs |
| `rfp_locations` | Gram Seva districts | "Scope of Work" section | Gram Seva PDF |
| `grants` | KABIL grant | CONSERW Jaldhara project, Udalguri (Assam) | `hand-vetting/KABIL_Funder_SBIFoundation.md` |
| `grants` | Dilasa grant | Jaldhara, Jalna (Maharashtra), Dec 2025–Dec 2028 | same file |
| `grants` | Gramya Vikash Mancha grant | Gram Seva, Udalguri (Assam) | same file |
| `contacts` | Emails | md@sbifoundation.co.in, coo@…, gramsevarfp@…, coeforpwd@… | profile text and RFP PDFs |

### 2.3 Needs research

| Table | What's missing | Where to look |
|---|---|---|
| `funder_csr_years` | SBI Foundation's own yearly spend (to replace the SBI rows) | SBI Foundation AR 2024-25 (not read yet). FY24 is already known: ₹217.12 cr in grants. |
| `grants` | Amounts for all grants | Each NGO's audited accounts (KABIL, Dilasa, GVM, Sesame, TISS, Abhinav Bindra Foundation, SUVIDHA) and SBI Foundation's notes to accounts |
| `programs` | Real start dates (current ones are guesses like 2020-01-01) | Annual reports, press releases |
| `programs` | 14 sub-projects plus CONSERW Jaldhara | AR 2023-24 |
| `funder_partners` | Partners shown only as logos | AR pages 19-20, 72, 76 |
| `funder_partners` / `funder_csr_spend` | CSR-1 numbers of partners | MCA CSR-1 list |
| `news_mentions` | Anything from 2023–2026 | Google News: new MD, CONSERW Jaldhara, Asha scholarship |
| `credential_events` | Real 12A/80G dates and expiry | Income Tax portal |

### 2.4 Fix

| Table | Problem | Fix |
|---|---|---|
| `profile` / `contacts` | **Two different leadership lists.** One says MD Swapan Dhar and COO Pratyush Mehrotra; the other says Sanjay Prakash and Jagannath Sahoo. | Re-check sbifoundation.in/Leadership and keep one list |
| `profile.kabil_grant_status` | Says "no KABIL grant found" | Wrong: the CONSERW Jaldhara project exists (see 2.2) |
| `rfps` | Status "unconfirmed" on all 8 rows | Use open, closed or removed (probably closed) |
| `reference_figures` | Overhead shown as 2.87% | Its own working gives 2.81% |
| `funder_csr_spend` | Health spend ₹666.5M | Should be ₹665.5M (30.65% × ₹2,171.17M) |
| `funder_locations` | Note says "13 states" but lists 19 | Change to 19 |
| `metrics` | Sanjeevani (a sub-project, 9.6 lakh) is bigger than its parent programme Jivanam (9.4 lakh) | Re-check both numbers |
| `funder_csr_spend` / `programs` | PwD projects: 12 in one table, 30 in another. YFI batch: 54 vs 55. | Re-check and use one figure |
| `funder_identifiers` | An old row says "CSR-1 not found", but CSR00001456 is listed | Delete the old row |
| `funder_locations` | 13 YFI states marked `funds` using a fellow-placement FAQ | That isn't spend proof; change to `operates` |

### 2.5 Empty tables
- `proposal_templates`, `template_items`: **can be filled now** from the 2 RFP PDFs (see 2.2).
- `program_locations`: the profile only says "see Table 9". Write out the 40 rows.

---
---

# 3. Infosys Foundation

> ⚠️ **The Infosys PDFs are missing from the folder.** The 7 Infosys PDFs in `deep-agent-app/downloads/` at the start of the session are gone: the Foundation reports 2023-24, 2024-25 and 2025-26, the CSR action plans 2024-25 and 2026-27, and the annual reports 2024-25 and 2025-26. Git can't restore them because they were never committed. **Download them again**; until then, none of the Infosys numbers can be checked.

### 3.1 Remove (Infosys Ltd or Infosys Foundation USA data)
- [ ] All 6 rows in `funder_csr_years`. These are Infosys Ltd's legal CSR filing; the Foundation is a trust and doesn't file one.
- [ ] `funder_csr_spend`: the 10 give.do "cause" rows and the sum row (Infosys Ltd data)
- [ ] `funder_csr_spend` / `grants` / `funder_footprints`: the 10 "capital asset" projects (BMRCL, AIIMS, PGIMER, LVPEI, Ashoka, Madras Medical College, RKM, DSCI, KKF…). **Exception:** keep a project if Infosys Ltd's CSR annexure or action plan says it was run through Infosys Foundation.
- [ ] Contacts Govind Iyer, Chitra Nayak and Michael Gibbs (the Infosys Ltd board committee) and Anand Swaminathan (Foundation USA)
- [ ] The USA website link, US$ spend figures and Infosys BPM figures in `profile`
- [ ] 8 of the 13 documents: the Infosys Ltd annual reports, CSR Policy, Committee Charter and give.do pages
- [ ] Both overhead-percentage rows in `reference_figures` (1.66% and 1.23%, both Infosys Ltd)
- [ ] Partner rows "Infosys Ltd" and "Infosys BPM" (they're funders) and "Infosys Springboard Livelihood Program" (it's a programme)

### 3.2 Ready to fill (value and source already found)

| Table | Field | Value | Source |
|---|---|---|---|
| `contacts` | General email and phone | foundation@infosys.com · +91 80 26534653 | profile text |
| `rfp_locations` | Aarohan dates | 2025-04-24 to 2025-06-22; role should be `funds`, place India | profile text |
| `funder_csr_spend` | DSCI CSR-1 | CSR00011848 (currently written with a space) | profile text |
| `news_mentions` | Language / country / review status | en / IN / pending | — |
| `funder_footprints` | 2024 flood-relief states missing | Karnataka, Odisha, Tamil Nadu (named in the text, no row) | profile text |

### 3.3 Needs research

| Table | What's missing | Where to look |
|---|---|---|
| **All spend tables** | **The Foundation's own projects and money.** Which Infosys Ltd CSR projects were run through Infosys Foundation, and how much? | Infosys Ltd CSR annexure (FY21-22 to FY25-26) and action plans. The FY25-26 plan is also missing. |
| `funder_identifiers` | **CSR-1 number.** The profile says "not available", but that's based on a 2020-21 filing, and CSR-1 only became mandatory in April 2021, so it almost certainly exists. | Implementing-agency column of the FY21-22+ CSR annexure or FY24-25 action plan |
| `funder_identifiers` | PAN, trust registration no., NGO Darpan ID | Foundation audited accounts, 80G receipts, ngodarpan.gov.in |
| `credential_events` | 12A, 80G numbers and expiry | Income Tax portal |
| `grants` | Amounts for real Foundation grants (eVidyaLoka, Magic Bus, Antara, The Banyan, Sangath, Khushi Baby, Avanti Fellows, GoSports…) | Each NGO's audited accounts ("grants received" note) |
| `grants` | The ₹48 cr Prashanthi Balamandira Trust commitment | News article already in the profile |
| `rfps` / `proposal_templates` | Request-a-Grant portal link and its form fields | infosys.org |
| `programs` | Start and end dates (only 2 of 15, both guesses) | Press releases, Foundation reports |
| `funder_partners` | Partner type, year and standard name for all 73 names | Foundation reports (once downloaded again) |
| `contacts` | Programme or grants staff | Foundation report credits, LinkedIn |

### 3.4 Fix

| Table | Problem | Fix |
|---|---|---|
| `profile.funding_trend` | Year-on-year growth is wrong | FY25 is +16.7% (not +16.2%); FY26 is +6.1% (not +6.6%) |
| `funder_csr_years` | FY26 spent + unspent = ₹577.44 cr, but obligation says ₹577.36 cr | Re-check the source |
| `reference_figures` | "184x range" | Should be about 175x (184 ÷ 1.05) |
| `metrics` | FY26 Springboard results are sourced to the July 2025 **launch** press release | A launch release can't have full-year results; re-source to the Foundation Report 2025-26 |
| `funder_partners` | 4 duplicate partners (Sangath, Antara, Khushi Baby, Avanti Fellows) | Keep one each |
| `funder_locations` | Maharashtra and UP marked `funds` using a future plan (FY26-27) | Change to `priority` |
| `grants` | CSR-1 numbers typed into the amount cell (4 rows) | Move them to notes |
| `contacts` | "verified = Yes" for all, but the sources were cached search snippets | Re-verify on the live site |
| `programs` | Employee Volunteering row has extra cells, so the table is broken | Fix the row |

### 3.5 Empty tables
- `proposal_templates`, `template_items`: fill them from the Request-a-Grant online form.
- `program_locations`: build it from the `funder_footprints` rows, using Foundation data only.

---

## Suggested order of work
1. **Download the Infosys PDFs again.** Nothing for Infosys can be checked until then.
2. **Do all the "Remove" items** (sections 1.1, 2.1, 3.1). That's quick, and it makes the profiles correct.
3. **Copy in all the "Ready to fill" values** (sections 1.2, 2.2, 3.2). The values and sources are already here.
4. **Fix the contradictions** (sections 1.4, 2.4, 3.4), starting with the SBI leadership list and the SBI KABIL grant.
5. **Research grant amounts from the NGOs' own audited accounts.** This is the biggest gap across all three.
6. **Add archive links** everywhere as a last pass.

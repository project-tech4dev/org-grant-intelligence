# Axis Bank Foundation — Missing Fields by Table

*Gap check of `Axis_Bank_Foundation_Profile.md` against the Sangam schema, Part A (tables 1–24). Scope: **Axis Bank Foundation only**. Checked 2026-09-29 (re-checked after the deep agent update: only `grant_locations` changed).*

**Legend:** ❌ missing / empty · ⚠️ present but invalid or needs fixing · 🗑️ Axis Bank Ltd data, remove from the ABF profile · Auto / Link columns are only listed when they block a row from loading.

---

## Summary

| # | Table | Status |
|---|---|---|
| 1 | `funders` | Mostly done. `archive_url` and a single `source_url` still missing |
| 2 | `funder_identifiers` | 4 of 7 ID types missing, CIN row must be removed |
| 3 | `credential_events` | `event_date` missing on 5 rows; no portal checks done |
| 4 | `funder_tags` | Invalid role values; tags not mapped to IDs |
| 5 | `funder_locations` | Invalid roles; ABF's own 32-state list missing |
| 6 | `funder_csr_years` | No ABF rows at all (all current rows are the bank's) |
| 7 | `funder_csr_spend` | Pillar totals only; no project, state or agency detail |
| 8 | `programs` | `description`, `source_url` and valid dates missing |
| 9 | `funder_footprints` | Invalid years; no ABF district list |
| 10 | `funder_partners` | Only 2 implementing NGOs out of ~59 projects |
| 11 | `grants` | No rows can load (`org_id` not matched) |
| 12 | `rfps` | Done: no open calls exist (documented) |
| 13 | `proposal_templates` | Done: no forms published (documented) |
| 14 | `contacts` | Trustees done; programme and partnership staff thin |
| 15 | `metrics` | Values present; `method` and source columns missing |
| 16 | `documents` | Only 3 ABF documents; `fetched_at` and `archive_url` missing |
| 17 | `news_mentions` | ❌ Nothing collected |
| 18 | `reference_figures` | ❌ Nothing collected |
| 19 | `program_locations` | Started; invalid roles and dates, bank rows mixed in |
| 20 | `program_tags` | ❌ Nothing collected |
| 21 | `grant_locations` | ⚠️ Candidate rows only (blocked until grants exist) |
| 22 | `rfp_locations` | Not needed (no RFPs) |
| 23 | `rfp_tags` | Not needed (no RFPs) |
| 24 | `template_items` | Not needed (no templates) |

---

## 1. `funders`

| Field | Status | What to do |
|---|---|---|
| `source_url` | ⚠️ | Says "Multiple". Put one link, the page the main facts come from (e.g. ABF Overview page) |
| `archive_url` | ❌ | Save the homepage or Overview page on web.archive.org and paste the link |
| `content_hash` | Auto | Leave for the pipeline |
| `profile.general_contact_email` | ⚠️ | New key, not in the "keys in use" list. Fine, but tell the team |
| `parent_id` | ⚠️ | Points to Axis Bank Ltd. Leave it empty unless an Axis Bank Ltd funder row exists |

## 2. `funder_identifiers`

| Field / row | Status | What to do |
|---|---|---|
| `pan` row | ❌ | Find it in ABF's audited accounts, the Form 10B audit report or the FCRA portal |
| `csr1` row | ❌ | Search the MCA CSR-1 registered-entities list for "Axis Bank Foundation" |
| `darpan` row | ❌ | Search the NGO Darpan portal |
| `reg_no` row | ❌ | Trust registration number: Charity Commissioner Maharashtra, or the ABF annual report's audit pages |
| "Not found" rows | ⚠️ | `id_value` is required, so don't load these as rows. Record the lookup in `credential_events` as `not_found` |
| FCRA row | ⚠️ | `fcra` isn't an allowed `id_type` here. Record it in `credential_events` only |
| `cin` row | 🗑️ | The CIN is Axis Bank Ltd's. Remove it |
| `archive_url` | ❌ | Empty on every row |

## 3. `credential_events`

| Field / row | Status | What to do |
|---|---|---|
| `event_date` on the 12a, 80g, csr1, darpan and pan rows | ❌ | Required. Use the date you checked (2026-09-29) |
| `event_date` on the reg_no row | ⚠️ | "2006" isn't a full date. Use the exact date, or 2006-01-01 with a note |
| FCRA `valid_until` | ❌ | Check on fcraonline.nic.in, then add a `checked_active` or `renewed` row |
| 12A and 80G | ❌ | Check the Income Tax portal: e-Filing → Verify 12A/80G registration |
| `cin` row | 🗑️ | Not relevant to a trust. Drop it, or keep a single `not_available` row |
| `source_url` | ⚠️ | "—" on 5 rows. Put the portal link you checked |
| `archive_url`, `document_id` | ❌ | Empty on every row |

## 4. `funder_tags`

| Field / row | Status | What to do |
|---|---|---|
| `tag_id` | ⚠️ | Tag names are used instead of IDs. Map each one to `tags.id` |
| `role` on Education and Disaster Relief | ⚠️ | "secondary (historical)" isn't allowed. Use `secondary` and put "historical, ended 2011-12" in `note` |
| Financial Inclusion tag | 🗑️ | Inferred from the bank's CSR policy. Remove it |

## 5. `funder_locations`

| Field / row | Status | What to do |
|---|---|---|
| `role` on West Bengal and Andhra Pradesh | ⚠️ | "funds (historical)" isn't allowed. Use `funds` and set `valid_to` ≈ 2016 |
| Gujarat (Dahod) as `funds` | ⚠️ | A photo caption isn't spend evidence. Change to `operates`, or remove it |
| Registered office | ⚠️ | Link the Mumbai district, not the Maharashtra state |
| All-India row | ⚠️ | Not a real place. Use one row per state instead. It also still says 2018 (should be 2019) |
| ABF's 32 states | ❌ | Only about 8 are named. Get the full list from the ABF Annual Report 2024-25 |
| `valid_from` | ⚠️ | "2006", "2012 (approx.)" and "~2015" aren't dates |
| `archive_url`, `document_id` | ❌ | Empty on every row |

## 6. `funder_csr_years`

| Field / row | Status | What to do |
|---|---|---|
| All 4 rows (FY22-23 to FY25-26) | 🗑️ | These are Axis Bank Ltd's CSR annexure. Remove them, along with the CSR Committee table |
| ABF rows, one per year | ❌ | Add FY2022-23, FY2023-24 and FY2024-25 from ABF's own accounts |
| `section_135_applicable` | ❌ | `No` for every ABF row |
| `total_spent` | ❌ | ABF's Sustainable Livelihood Programme figures are already in the file: 113.53 / 154.01 / 231.96 cr. Convert to ₹ |
| `admin_overheads` | ❌ | From ABF's income and expenditure statement |
| `impact_assessment_done` | ❌ | Check the ABF annual report |
| `average_net_profit`, `prescribed_csr`, `unspent_transferred`, `excess_spent` | n/a | Leave empty. ABF is a trust, not a company under Section 135 |
| `source_url`, `source_name`, `fetched_at`, `as_of` | ❌ | Missing columns |

## 7. `funder_csr_spend`

| Field / row | Status | What to do |
|---|---|---|
| Aspirational-district (BRSR) table | 🗑️ | This is the bank's spend. Remove it |
| Part (B) bank projects: Financial Literacy, Mobile Vans, Heart Surgeries, Mid-Day Meal, DilSe | 🗑️ | Remove them |
| `csr_sector_id` | ⚠️ | "Rural Livelihoods" is ABF's own category. Map it to a Schedule VII sector (e.g. Livelihood Enhancement Projects, Vocational Skills) |
| `state_location_id` | ❌ | Empty on every row. Find a state-wise split of ABF spend |
| `project_name` + `implementing_agency` + `amount` | ❌ | Per-project rows are missing, for SRIJAN, Dilasa and the rest of the 59 projects |
| `agency_csr1` | ❌ | Empty everywhere |
| "Special Projects" rows | ⚠️ | `amount` is required. Delete them or find the figure |
| `fetched_at`, `archive_url` | ❌ | Missing |

## 8. `programs`

| Field / row | Status | What to do |
|---|---|---|
| `description` | ❌ | Empty on every row. Write 2-4 sentences each |
| `source_url` | ❌ | Only source names are given. Add the links |
| `start_date` / `end_date` | ⚠️ | "2011-12", "FY2024-25", "~2030-31" and "~2007-2010" aren't dates. Use YYYY-MM-DD |
| `kind` on the Rural Livelihoods and Skill Development pillars | ⚠️ | They're marked `project`. Change them to `programme` |
| `fetched_at`, `as_of`, `archive_url` | ❌ | Missing |
| Financial Inclusion and Healthcare themes and their 5 projects | 🗑️ | These are the bank's programmes. Remove them |
| `is_enabler` | ⚠️ | Ecosystem Action is probably `Yes` (capacity building). Add it as a programme |

## 9. `funder_footprints`

| Field / row | Status | What to do |
|---|---|---|
| `fiscal_year` | ⚠️ | "Undated", "Ongoing since 2012" and "~FY2014-15" aren't valid. Use FYyyyy-yy, or drop the row |
| `location_id` on the aggregate rows (26/28/32 states) | ❌ | Required. Replace with one row per state |
| 7-theme district list (CSR Impact Report) | 🗑️ | Bank-wide. Use only the Lives & Livelihoods theme if you confirm it matches ABF, otherwise remove it |
| Lives & Livelihoods district list | ⚠️ | 237 districts are listed but 253 are stated. 16 are missing |
| ABF district list (300 districts) | ❌ | Get it from the ABF Annual Report 2024-25 |
| `source_name`, `fetched_at`, `as_of`, `archive_url` | ❌ | Missing columns |

## 10. `funder_partners`

| Field / row | Status | What to do |
|---|---|---|
| Implementing NGOs | ❌ | Only SRIJAN and Dilasa are named, out of ~59 projects. Get the full partner list from the ABF annual report |
| `fiscal_year` | ⚠️ | "Undated" and "Ongoing since 2012" aren't valid |
| `partner_canonical` | ❌ | Empty on every row |
| `partner_csr1` | ❌ | Empty on every row |
| `program_id` | ⚠️ | Co-funders sit under the Sustainable Livelihood Programme. OK |
| CSC Academy, Sri Sathya Sai Trust, Akshaya Patra, Sunbird Trust | 🗑️ | These are the bank's partners. Remove them |
| `source_url` | ⚠️ | "ABF AR 2024-25" is text, not a link |
| `source_name`, `fetched_at`, `as_of`, `archive_url` | ❌ | Missing |

## 11. `grants`

| Field / row | Status | What to do |
|---|---|---|
| `org_id` | ❌ | Required. Check whether SRIJAN and Dilasa Sanstha are in `orgs` |
| `amount`, `start_date`, `end_date` | ❌ | Not disclosed. Ask the NGOs or check their annual reports |
| `status` | ⚠️ | SRIJAN is marked `active`, but that isn't verified. `unconfirmed` is safer |
| Akshaya Patra, Sri Sathya Sai Trust, Sunbird Trust | 🗑️ | These are the bank's grants. Remove them |
| `source_url`, `source_name`, `fetched_at`, `as_of` | ❌ | Missing |

## 12. `rfps`: ✅ done
- There's no public call. Leaving the table with no rows is correct.
- ⚠️ The note mentions an "official CSR Policy PDF" and an "earlier Part D", and neither exists in the file. Fix or remove that text.

## 13. `proposal_templates`: ✅ done
- No form is published. Leaving the table with no rows is correct.

## 14. `contacts`

| Field / row | Status | What to do |
|---|---|---|
| 8 trustees | ✅ | Done |
| Programme and partnership staff (`kind=programme` / `grants`) | ⚠️ | Only Isha Ayyer, and she's unverified. Add programme heads from the ABF website or annual report |
| `email`, `phone` | ❌ | Empty on every row. Fine if they aren't published |
| `document_id`, `archive_url` | ❌ | Missing |

## 15. `metrics`

| Field / row | Status | What to do |
|---|---|---|
| `method` | ❌ | Only in the intro note. Add it to each row (`monitoring_data`) |
| `is_self_reported` | ❌ | Only in the intro note. Add it to each row (`Yes`) |
| `stage` | ⚠️ | Households, villages, blocks and districts reached are `output`, not `outcome` |
| `target` | ❌ | Mission 2 Million target = 2,000,000 is only in `notes`. Also add the Mission 4 Million target of 4,000,000 |
| Total CSR spend row | ⚠️ | In ₹ crore. Convert to ₹ (2,319,600,000), or remove it (it duplicates the spend table) |
| `chain_key`, `sequence`, `baseline` | ❌ | Optional. Add them if you're building a results chain |
| `source_url`, `source_name`, `fetched_at`, `as_of`, `archive_url` | ❌ | Missing columns |
| BRSR bank-wide metrics table | 🗑️ | Remove it |

## 16. `documents`

| Field / row | Status | What to do |
|---|---|---|
| ABF Annual Reports FY16-17 to FY23-24 | ❌ | Add them from axisbankfoundation.org/financials/overview.html |
| ABF annual action plan | ❌ | Not found yet |
| `fetched_at`, `archive_url` | ❌ | Missing |
| 5 Axis Bank Ltd documents + Axis Bank CSR Policy row | 🗑️ | Remove them |

## 17. `news_mentions`: ❌ nothing collected
- Collect: `url`, `title`, `seendate`, `domain`, `topic`, `summary`, `sentiment`, `kind`.
- Look in: Google News / GDELT, searching "Axis Bank Foundation", and ABF's LinkedIn page.

## 18. `reference_figures`: ❌ nothing collected
- Candidates:
  - ABF's admin overhead cap for partners (`overhead_norm`), from the TISS-ABF manual.
  - Cost per household: FY24-25 ₹231.96 cr ÷ 387,467 households ≈ ₹5,987 per household (`cost_per_beneficiary`). This is calculated by us, so mark it in `notes`.

## 19. `program_locations`

| Field / row | Status | What to do |
|---|---|---|
| Education, Environment, Financial Inclusion, Health, Sports, Humanitarian lists | 🗑️ | These are the bank's themes. Remove them |
| Heart Surgeries, Mid-Day Meal, DilSe rows | 🗑️ | Remove them |
| Sustainable Livelihood Programme (31 states) | ⚠️ | From the bank's report. ABF says 32. Use ABF's list |
| `role` on Towards the Northeast | ⚠️ | "priority" isn't allowed here. Use `operates`, one row per north-east state |
| `location_id` | ⚠️ | Rows with a region, or several states in one row, need one row per state |
| `valid_from` / `valid_to` | ⚠️ | "FY2024-25", "FY2024", "2012" and "~2015" aren't dates |
| Gujarat (Dahod) row | ⚠️ | A photo caption is weak evidence |
| `source_url` | ⚠️ | "ABF AR 2024-25" is text, not a link |
| `document_id`, `archive_url` | ❌ | Missing |

## 20. `program_tags`: ❌ nothing collected
- Collect: `program_id`, `tag_id`, `role`, `is_inferred`, `tagged_by`, `note`.
- Suggested tags:
  - Sustainable Livelihood Programme → livelihoods (primary), women (secondary)
  - Rural Livelihoods → agriculture and natural resource management (NRM)
  - Skill Development → skilling, youth, persons with disabilities
  - Ecosystem Action → capacity building

## 21. `grant_locations`: ⚠️ candidate rows added, but none can be loaded
- `grant_id` is required, and no `grants` rows exist yet, so nothing can be loaded.
- 🗑️ Remove the Akshaya Patra, Sri Sathya Sai and Sunbird rows. They're the bank's grants.
- ⚠️ `as_of` says "Undated legacy page" on the SRIJAN and Dilasa rows, and `source_url` is text, not a link, on the bank rows.
- ❌ The 4 SRIJAN districts and 10 Dilasa districts aren't named. Get them from the NGOs' own websites or reports.
- ✅ Siangbali GP, Daringbadi block (Odisha) is noted as the most detailed place found so far.

## 22–24. `rfp_locations`, `rfp_tags`, `template_items`
- Not needed. There are no RFPs or templates.

---

## Applies to every table
- ❌ `archive_url` is empty everywhere. There isn't a single web.archive.org link.
- ❌ `document_id` isn't linked anywhere. Add document rows first, then link them.
- ⚠️ 16 "Undated" values (up from 13; the new grant_locations section added 3) and several "~" approximate dates need a real date or year.
- ⚠️ Amounts in ₹ crore need converting to ₹ (× 10,000,000).

# SBI Foundation — Registry Row

*Compiled from official sources (sbifoundation.in, sbi.bank.in) and MCA-derived company-database records (Instafinancials) — 2026-09-29.*

---

## `funders` table — field values

| # | Column | Value | Notes |
|---|---|---|---|
| 1 | **id** | *(auto)* | Do not type |
| 2 | **slug** | `sbi-foundation` | |
| 3 | **name** | **SBI Foundation** | Official registered name (matches MCA record exactly — no "Limited"/"Private Limited" suffix used in practice, though it is a company limited by shares) |
| 4 | **funder_type** | `corporate_csr` | CSR-implementing Section 8 company for the State Bank Group |
| 5 | **section_135_bound** | **No** | SBI Foundation itself is the CSR-implementing vehicle, not the Section-135-bound entity. Note a genuine nuance: the parent, **State Bank of India, is a statutory corporation constituted under the State Bank of India Act, 1955 — not a company registered under the Companies Act, 2013 — and therefore has no CIN and is not itself subject to Companies Act Section 135** in the same way a private company is (confirmed "Corporate Identity Number (CIN) of the Listed Entity: Not Applicable" in SBI's own BRSR/Sustainability Report). In practice SBI still follows CSR-equivalent spend obligations as a public sector bank under RBI/DPE/DFS CSR guidelines, and channels this spend through SBI Foundation — but this is not a straightforward "Section 135 → Yes" case like a private company; flagged here for accuracy rather than assumed. |
| 6 | **website** | **https://sbifoundation.in** | |
| 7 | **profile** (JSON) | *see breakdown below* | |
| 8 | **source_url** | https://sbifoundation.in/Leadership | Primary page for governance/leadership facts |
| 9 | **source_name** | "SBI Foundation official website — Leadership page" | |
| 10 | **fetched_at** | 2026-09-29 | |
| 11 | **content_hash** | *(auto — leave for pipeline)* | |
| 12 | **extractor_version** | `manual-research-v1` | |
| 13 | **as_of** | Live site content as of Sept 2026; AGM/filing data as of FY2024-25 (per MCA record) | |
| 14 | **archive_url** | *(not captured in this pass)* | Recommend a web.archive.org "Save Page Now" on the homepage, `/Overview`, and `/Leadership` |
| 15 | **registry_status** | `in_vetting` | Freshly researched; only the `funders` table has been completed so far — no other tables (identifiers, programs, partners, etc.) have been researched yet for this funder |
| 16 | **parent_id** | → **State Bank of India** (no CIN — statutory corporation under the SBI Act, 1955, not the Companies Act) | |

---

## `profile` JSON — key-by-key detail

### `flagship_program`
> SBI Foundation states it runs **9 Flagship Programs** (per its own homepage):
> 1. **Integrated Learning Mission** — "Making quality and inclusive education accessible."
> 2. **Jivanam** — "Making Healthcare accessible and affordable."
> 3. **Gram Seva** — "Building self-reliant and sustainable communities."
> 4. **Sashakti** — "Promoting Gender Equality by Empowering Women."
> 5. **CONSERW** (CONservation through Sustainable Engagement, Restoration & Wildlife protection).
> 6. **Centre of Excellence for PwDs** — "Removing barriers to employment and employability."
> 7. **ACE** — "Providing holistic support to underserved athletes."
> 8. **Livelihood and Entrepreneurship Accelerator Programme (LEAP)** — "Bolstering efforts towards the achievement of sustainable and equitable economic growth."
> 9. **SBI Youth for India (YFI) Fellowship** — a rural fellowship programme (named via its own Programme Head role and URL `/youthforindia`, not detailed on the homepage grid but listed among the 9).
> *(Individual programme pages exist at dedicated URLs — e.g. `/gram-seva`, `/jivanam`, `/conserw`, `/PwDs`, `/youthforindia`, `/women-empowerment`, `/leap`, `/integrated` — none yet deep-read in this pass.)*

### `funding_trend`
> Headline stats, self-reported on the homepage (undated — presented as current "Our Impact" figures, not tied to a specific fiscal year):
> - **Lives Impacted:** 3.15 Cr+ (31.5 million+)
> - **Live Projects:** 350+
> - **Reach:** 28 States & 8 Union Territories
>
> Cross-check from a secondary source (Scribd-hosted copy of the **SBI Foundation Annual Report 2023-24**): as of FY2023-24, the Foundation reported **cumulative funding of over ₹500 crore since 2015**, having "impacted over 31 million lives" through **145 projects** in that year across education, healthcare, rural development and women's empowerment. This is broadly consistent with (and likely the source generation of) the homepage's "3.15 Cr+ lives" / "350+ projects" figures, though the project count differs (145 in FY23-24 vs. 350+ "live" today) — treat as two different snapshots in time, not a contradiction.
> **Not yet obtained:** year-by-year CSR spend broken out by fiscal year (the Annual Reports for FY2024-25, 2023-24, 2022-23, 2020-21, 2019-20, 2018-19, and 2017-18 are all downloadable at https://sbifoundation.in/publication but have not yet been opened/read in this pass).

### `grant_terms`
> **Not yet researched in this pass.** No information was gathered in this session on application process, grant size ranges, or funding modalities (open call vs. relationship-led). Recommend a follow-up pass through the Annual Reports and the "Work with us" section of the website (seen in the site's top navigation but not yet visited).

### `governance_note`
> - **Legal form:** Section 8 company (not-for-profit), registered under the Companies Act, 2013.
> - **CIN:** `U85100MH2015NPL266051` (per Instafinancials, an MCA-data aggregator).
> - **Registration number:** 266051, registered at **ROC Mumbai**.
> - **Incorporated:** 2015-06-26 (per Instafinancials); multiple secondary sources (LinkedIn, SBI's own affiliates page, Facebook) independently confirm "established by State Bank of India in 2015."
> - **Company category/class:** Company limited by shares; Public Company; Indian Non-Government Company.
> - **Authorized share capital:** ₹4,00,00,000 (₹4.00 Cr); **paid-up capital:** ₹4,00,00,000 (₹4.00 Cr) — same figure for both, per Instafinancials.
> - **MCA compliance status:** "ACTIVE compliant." Last AGM: 2025-09-25. Last balance sheet filed: 2025-03-31 (i.e., for FY2024-25).
> - **MCA principal business classification:** "Health And Social Work."
> - **Registered/corporate office:** SBI Foundation, Office No. 35, Ground Floor, The Arcade, World Trade Center, Cuffe Parade, Mumbai, Maharashtra 400005.
> - **General email (per MCA record):** md@sbifoundation.co.in. **Public-facing contact emails (per website):** coo@sbifoundation.co.in (general enquiries); careers@sbifoundation.co.in (recruitment); ashascholarship@sbifoundation.co.in (SBI Asha Scholarship queries).
> - **Phone:** 022-22151689 (general); 080-47285300 (Asha Scholarship queries specifically).
> ⚠️ **CIN not independently cross-verified directly on the MCA portal itself in this pass** (MCA's own site was not queried; the CIN above comes from a third-party aggregator, Instafinancials, which is generally reliable but not a primary government source) — recommend a direct MCA MyOwn CIN search to confirm before treating this as fully verified.

### `leadership_note`
> **Board of Directors (per SBI Foundation's own Leadership page, live as of Sept 2026):**
> | Name | Role |
> |---|---|
> | Mr. Challa Sreenivasulu Setty | Nominee Director & **Chairman**, SBI Foundation (concurrently Chairman, State Bank of India) |
> | Mr. Ashwini Kumar Tewari | Nominee Director (concurrently MD, Corporate Banking & Subsidiaries, SBI) |
> | Mr. Rama Mohan Rao Amara | Nominee Director (concurrently MD, RB & O, SBI) |
> | Mr. Gajendra Singh Rana | Nominee Director (concurrently DMD (HR) & CDO, SBI) |
> | Mr. Amit Jhingran | Nominee Director (concurrently MD & CEO, SBI Life Insurance Company Limited) |
> | Mr. Venkatesh Srinivasan | **Independent Director** |
> | Dr. Tulsi Jayakumar | **Woman Independent Director** |
> | Mr. Swapan Dhar | **Managing Director**, SBI Foundation |
>
> All "Nominee Director" seats are held by serving SBI Group executives, consistent with SBI Foundation's role as the Bank Group's CSR-implementing subsidiary.
>
> **Key Management Team — per SBI Foundation's own live website (sbifoundation.in/Leadership):**
> | Name | Role |
> |---|---|
> | Mr. Swapan Dhar | Managing Director |
> | Mr. Pratyush Mehrotra | President and Chief Operating Officer |
> | Mr. Sushil Kumar Verma | Chief Financial Officer & Chief Admin *(officer — title truncated on source page)* |
>
> ⚠️ **Unresolved discrepancy found — presented as-is, not silently resolved:** SBI Foundation's **give.do page** (`https://give.do/discover/17LP/sbi-foundation`) lists a **different Managing Director & Chief Executive Officer and a different President & COO**:
> | Name (per give.do) | Role (per give.do) |
> |---|---|
> | **Sanjay Prakash** | **Managing Director & Chief Executive Officer** |
> | **Jagannath Sahoo** | **President & Chief Operating Officer** |
> | Sushil Kumar Verma | Chief Financial Officer & Chief Administrator *(matches the website exactly)* |
> | Sashi Bhushan | Vice-President, Disability and Inclusion *(matches the website's "Shashi Bhushan, VP Disability and Inclusion" — spelling variant only)* |
> | Aman Bhaiya | Vice-President & Head (Strategy) *(matches the website exactly)* |
>
> Three of five names match exactly across both sources (CFO, and the two Programme-Head-level VPs), but **the top two seats — MD/CEO and President/COO — differ entirely** between the live website (Swapan Dhar; Pratyush Mehrotra) and give.do (Sanjay Prakash; Jagannath Sahoo). This looks like a genuine leadership transition where one source has not yet been updated, but it is **not possible to tell from the two sources alone which is more current** — neither page carries a visible "last updated" date. Recommend treating this as an open question requiring a fresh, direct check of sbifoundation.in/Leadership (or a news search for "SBI Foundation new MD" / "Sanjay Prakash SBI Foundation") before picking one as authoritative.
>
> **Programme Heads & Team Leads (named individually on the website):**
> Mr. Shashi Bhushan (VP, Disability and Inclusion) · Mr. Aman Bhaiya (VP & Head, Strategy) · Mr. Suresh Panwar (VP, Systems & CISO/DPO) · Mr. Rishi Kumar (Chief Manager, HR & Admin) · Mr. Rajaram Chavan (AVP & Programme Head, Health and Women Empowerment) · Mr. Shiddhalingesh Balloli (Programme Head, SBI Gram Seva) · Mr. Gyan Prakash (Programme Head, SBI YFI Fellowship Program) · Mr. Parveen Kumar (Programme Head, Education) · Mr. Ritesh Sain (Programme Head, Environment and Sports) · Mr. Subhadip Mondal (Programme Head, Livelihood & Skilling) · Mr. Rufus Sunny (Team Lead, Marketing and Communications).

### `kabil_grant_status`
> **No KABIL-related grant, program, or reference was found** in any SBI Foundation source located in this pass. Not applicable / not found for this funder.

---
---

## 2. Official IDs (`funder_identifiers`)

*One row per ID number. All rows belong to SBI Foundation (`funder_id` → the `funders.id` row created for the section above). `id_value` is required, so types with nothing found are not loaded as rows here — see the notes below the table instead.*

| funder_id | id_type | id_value | verified | source_url | is_current | source_name | fetched_at | archive_url |
|---|---|---|---|---|---|---|---|---|
| → SBI Foundation | `cin` | **U85100MH2015NPL266051** | **Yes** *(now cross-confirmed by a second independent source, give.do, in addition to Instafinancials — give.do prints it as "U85100MH2015NPL266051c," with a trailing lowercase "c" that looks like a data-entry artifact rather than a genuine 22nd character, since a CIN is fixed at 21 characters; the 21-character portion matches Instafinancials exactly)* | https://www.instafinancials.com/company/sbi-foundation-U85100MH2015NPL266051 ; https://give.do/discover/17LP/sbi-foundation | Yes | Instafinancials + give.do (cross-checked) | 2026-09-29 | Not found |
| → SBI Foundation | `pan` | **AAVCS9268A** *(newly found — see updated `credential_events` note below)* | **No** *(single-source so far — give.do; not cross-verified against the Income Tax e-Filing PAN verification tool)* | https://give.do/discover/17LP/sbi-foundation | Yes | give.do — SBI Foundation profile | 2026-09-29 | Not found |
| → SBI Foundation | `domain` | `sbifoundation.in` | Yes | https://sbifoundation.in | Yes | SBI Foundation website | 2026-09-29 | Not found |
| → SBI Foundation | `name` | `SBI Foundation` *(current/only name on record — Instafinancials explicitly states "There are no previous names or previous CINs for this company")* | Yes | https://www.instafinancials.com/company/sbi-foundation-U85100MH2015NPL266051 | Yes | Instafinancials | 2026-09-29 | Not found |
| → SBI Foundation | `csr1` | **CSR00001456** *(found in a later research pass — see the resolved `credential_events` row; supersedes the earlier "not found" status)* | **Yes** *(primary source — SBI Foundation's own Directors' Report)* | https://sbifoundation.in/publication (Annual Report 2023-24) | Yes | SBI Foundation Annual Report 2023-24, p.82 | 2026-09-29 | Not found |

**Not loaded as rows (id_value would be empty) — see `credential_events` conventions used for other funders in this registry:**

| id_type | id_value | verified | source_url | is_current | source_name | fetched_at | archive_url | notes |
|---|---|---|---|---|---|---|---|---|
| `csr1` | **not found** (give.do explicitly lists it as "Not Available" too, a second-source corroboration of the same negative result) | No | https://sbi.bank.in/documents/17826/9529227/130721-SBI_CSR_Policy+21+Ver+5+Final.pdf ; https://give.do/discover/17LP/sbi-foundation | — | SBI CSR Policy PDF + give.do | 2026-09-29 | Not found | SBI's own official CSR Policy PDF explains the CSR-1 mechanism in general terms — "Unique CSR Registration Number generated by this process will be mandatory for any CSR donation" — but does **not** print SBI Foundation's own CSR-1 number anywhere located, and give.do's own "CSR Form 1" field for SBI Foundation is blank/"Not Available." Two independent sources now agree there's no publicly visible CSR-1 number, even though it's plausible one exists internally (SBI Foundation receives CSR funds as an implementing agency). |
| `darpan` | **check_blocked** | No | https://ngodarpan.gov.in/#/search-ngo | — | NGO Darpan (NITI Aayog) | 2026-09-29 | Not found | Attempted a live search on the NGO Darpan NPO Directory — the search form requires solving an image CAPTCHA before the Search button activates; not reliably solvable via this automated session. Name "SBI Foundation" was entered into the search field but the search could not be submitted. |
| `reg_no` | **not filled in — schema-fit question** | — | https://www.instafinancials.com/company/sbi-foundation-U85100MH2015NPL266051 | — | Instafinancials | 2026-09-29 | Not found | Instafinancials separately lists a company "Registration No.: 266051" (the last 6 digits of the CIN, an MCA/ROC registration number). This is **not** the kind of ID the `reg_no` type is described as covering ("trust or society registration number") — SBI Foundation is a **Section 8 company**, not a trust or society, so it has no separate trust/society registration number. Recommend leaving `reg_no` empty for this funder rather than force-fitting the MCA registration number into it (that number is already captured as part of the `cin` value). |

*(`pan` moved out of this "not loaded" list and into the main table above — a real value was found via give.do during a later research pass in this session.)*

⚠️ **Registered-address discrepancy worth flagging:** Instafinancials' MCA-derived registered address is **"12th Floor, State Bank Bhavan, Barrister Rajani Patel Marg, Nariman Point, Mumbai 400021"** — this is **different** from the operational/correspondence address printed on SBI Foundation's own live website ("Office No. 35, Ground Floor, The Arcade, World Trade Center, Cuffe Parade, Mumbai 400005," used in the `governance_note` above). Both are likely genuine — one is the statutory MCA-registered office (inside SBI's own headquarters building), the other is where the Foundation's team actually operates day-to-day — but this should be kept in mind if a single "address" field is ever needed.

---
---

## 3. Registration history (`credential_events`)

*One row per check/event, for each of the 8 allowed `credential` values. All rows are for SBI Foundation (`funder_id` → the `funders.id` row above; `org_id` left empty — this is a funder, not an NGO).*

| funder_id | credential | event | event_date | valid_until | verified | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|---|
| → SBI Foundation | `cin` | `registered` | 2015-06-26 | — *(companies don't expire)* | **No** *(third-party aggregator, not confirmed directly on MCA)* | Incorporation date per Instafinancials' MCA-derived record: `U85100MH2015NPL266051`. | https://www.instafinancials.com/company/sbi-foundation-U85100MH2015NPL266051 | Instafinancials (MCA-data aggregator) | 2026-09-29 | Current |
| → SBI Foundation | `pan` | `registered` *(upgraded from `not_found`)* | 2026-09-29 | — | **No** *(single-source — give.do; not cross-verified against the Income Tax e-Filing PAN verification tool)* | **PAN: AAVCS9268A**, per give.do's "Registration Details" section for SBI Foundation, which rendered fully (not login-gated, unlike some other sections on the same page). Not yet independently confirmed via a second source. | https://give.do/discover/17LP/sbi-foundation | give.do — SBI Foundation profile | 2026-09-29 | Current |
| → SBI Foundation | `12a` | `registered` *(upgraded from `check_blocked`)* | 2026-09-29 | — | **No** *(single-source — give.do)* | **12A registration number: AAVCS9268AE20201**, per give.do (format matches the post-2020 Income-Tax unique-registration-number scheme: PAN + section-code letter "E" for 12A + year + serial). Not cross-verified against the Income Tax e-Filing portal directly (that portal's own search tool requires the PAN as input, which we now have — recommend a follow-up direct check). | https://give.do/discover/17LP/sbi-foundation | give.do — SBI Foundation profile | 2026-09-29 | Current |
| → SBI Foundation | `80g` | `registered` *(upgraded from `check_blocked`)* | 2026-09-29 | — | **No** *(single-source — give.do)* | **80G registration number: AAVCS9268AF20167**, per give.do (same PAN-based format, section-code letter "F" for 80G). Not cross-verified directly against the Income Tax portal. | https://give.do/discover/17LP/sbi-foundation | give.do — SBI Foundation profile | 2026-09-29 | Current |
| → SBI Foundation | `fcra` | `not_available` *(upgraded from `not_found` — now a positive statement from a source that explicitly lists the field, not just an absence of evidence)* | 2026-09-29 | — | **No** *(single-source — give.do; the FCRA Online "Validate Certificate" tool itself could not be used to confirm this independently, since it requires already knowing a registration number to check)* | give.do's own "Registration Details" section explicitly lists **"FCRA: Not Available"** for SBI Foundation — consistent with the inference already noted (its funding is entirely domestic, no foreign contributions identified) but now a direct statement from a source rather than pure inference. | https://give.do/discover/17LP/sbi-foundation | give.do — SBI Foundation profile | 2026-09-29 | Current |
| → SBI Foundation | `csr1` | **`registered` — RESOLVED. Number: CSR00001456** *(supersedes the `not_available` status below and in `funder_identifiers`; found directly in SBI Foundation's own Directors' Report, not give.do or the generic CSR Policy PDF)* | 2026-09-29 | not_found (registration itself has no stated expiry) | **Yes** *(primary source — SBI Foundation's own signed Directors' Report)* | SBI Foundation's own Annual Report 2023-24, Directors' Report, p.82: **"the Foundation has registered itself as an Implementing Agency for undertaking CSR activities vide registration number CSR00001456."** This resolves the earlier `not_available` finding (both SBI's CSR Policy PDF and give.do simply didn't have/print this number — it exists, just wasn't in either of those two sources). | https://sbifoundation.in/publication (Annual Report 2023-24, downloaded directly) | SBI Foundation Annual Report 2023-24 | 2026-09-29 | FY2023-24 |
| → SBI Foundation | `csr1` | `not_available` *(superseded — kept for audit trail only; see the resolved row immediately above)* | 2026-09-29 | — | No | give.do's own "Registration Details" section explicitly lists **"CSR Form 1: Not Available"** for SBI Foundation — matching SBI's own CSR Policy PDF, which describes the CSR-1 mechanism generally but never prints a number for SBI Foundation. This was accurate for those two sources, but SBI Foundation's own Annual Report (found later in this research) does print a real number — see the row above. | https://sbi.bank.in/documents/17826/9529227/130721-SBI_CSR_Policy+21+Ver+5+Final.pdf ; https://give.do/discover/17LP/sbi-foundation | SBI CSR Policy PDF + give.do (cross-checked) | 2026-09-29 | Current |
| → SBI Foundation | `darpan` | `check_blocked` | 2026-09-29 | — | No | NGO Darpan NPO Directory search (ngodarpan.gov.in/#/search-ngo) requires solving an image CAPTCHA before the Search button activates. "SBI Foundation" was entered into the name field, but the search could not be submitted without solving the CAPTCHA — not reliably solvable via this automated session. | https://ngodarpan.gov.in/#/search-ngo | NGO Darpan (NITI Aayog) | 2026-09-29 | — |
| → SBI Foundation | `reg_no` | `not_available` | 2026-09-29 | — | Yes *(fact of non-applicability is confirmed)* | **Not applicable in the trust/society sense.** SBI Foundation is a Section 8 company, not a trust or society, so it has no separate trust/society registration number. Its MCA registration number (266051) is already captured under the `cin` credential row above rather than duplicated here. | https://www.instafinancials.com/company/sbi-foundation-U85100MH2015NPL266051 | Instafinancials | 2026-09-29 | — |

---
---

## 4. Focus sectors (`funder_tags`)

*`tag_id` shown as tag names — map to your `tags.id`. All rows for SBI Foundation. **Primary source is now give.do's own "Cause Area" section** (`https://give.do/discover/17LP/sbi-foundation`), which is exactly the source this schema field points to ("Give 'Cause Area'") — this section is login-gated and did not render in the earlier logged-out fetch in this session, but the user has since logged in and shared the unlocked content directly, giving a real, structured Primary/Secondary sector breakdown rather than the informal 9-flagship-programme mapping used in the first draft of this table. That flagship-programme mapping is retained as supporting cross-reference/evidence in the `note` column rather than discarded.*

**give.do's own Primary Sectors (8):** Livelihoods · Energy & Environment · Specially Abled · Child & Youth Development · Sports · Gender · Health · Education
**give.do's own Secondary Sectors (5):** Health & Family Welfare · Vocational Training · Women Empowerment · Youth · Informal Education

| tag (→ tags.id) | role | is_inferred | tagged_by | note |
|---|---|---|---|---|
| Livelihoods | primary | No | agent-research (give.do Cause Area) | give.do Primary Sector. Corresponds to the "LEAP" (Livelihood and Entrepreneurship Accelerator Programme) flagship programme on SBI Foundation's own site, and the LinkedIn "livelihoods and skill development" thematic-area quote. |
| Energy & Environment | primary | No | agent-research (give.do Cause Area) | give.do Primary Sector. Corresponds to the "CONSERW" flagship programme (conservation/wildlife) — give.do's "Energy" framing is broader than CONSERW's stated wildlife/restoration focus, worth noting as a possible scope difference rather than a perfect match. |
| Specially Abled | primary | No | agent-research (give.do Cause Area) | give.do Primary Sector. Matches the "Centre of Excellence for PwDs" flagship programme exactly; also matches VP Shashi Bhushan's title, "Disability and Inclusion," confirmed on give.do's own Leadership Team list (see `leadership_note`). |
| Child & Youth Development | primary | No | agent-research (give.do Cause Area) | give.do Primary Sector. Corresponds to the "SBI Youth for India (YFI) Fellowship" flagship programme and elements of "Integrated Learning Mission" (which explicitly covers "children"). |
| Sports | primary | No | agent-research (give.do Cause Area) | give.do Primary Sector — **upgraded from `secondary` to `primary`** versus the first draft of this table, which had ranked Sports as secondary based on it being a less-emphasized item in a LinkedIn quote. give.do's structured Cause Area data is treated as more authoritative for `role`. Corresponds to the "ACE" flagship programme. |
| Gender | primary | No | agent-research (give.do Cause Area) | give.do Primary Sector. Corresponds to the "Sashakti" (women empowerment) flagship programme. |
| Health | primary | No | agent-research (give.do Cause Area) | give.do Primary Sector. Corresponds to the "Jivanam" flagship programme. |
| Education | primary | No | agent-research (give.do Cause Area) | give.do Primary Sector. Corresponds to the "Integrated Learning Mission" flagship programme. |
| Health & Family Welfare | secondary | No | agent-research (give.do Cause Area) | give.do Secondary Sector — a more specific sub-category sitting alongside the broader "Health" primary sector. |
| Vocational Training | secondary | No | agent-research (give.do Cause Area) | give.do Secondary Sector — sub-category of the "Livelihoods" primary sector. |
| Women Empowerment | secondary | No | agent-research (give.do Cause Area) | give.do Secondary Sector — sits alongside "Gender" as the broader primary sector; also the exact name of the "Sashakti" flagship programme's stated goal. |
| Youth | secondary | No | agent-research (give.do Cause Area) | give.do Secondary Sector — sub-category of "Child & Youth Development." |
| Informal Education | secondary | No | agent-research (give.do Cause Area) | give.do Secondary Sector — sub-category of "Education." |

**Not corroborated by give.do's Cause Area list, kept from the earlier flagship-programme-based mapping as lower-confidence / needs reconciliation:**
- **Rural Development / Community Development** — the "Gram Seva" flagship programme ("Building self-reliant and sustainable communities") doesn't map cleanly onto any single give.do sector above; closest fits would be Livelihoods or Child & Youth Development, but neither is an exact match. Flagged rather than force-mapped.
- **Culture & Heritage** — previously flagged as inferred/lower-confidence from a third-party grant guide; give.do's Cause Area list provides no support for this tag either. Recommend dropping unless a primary source confirms it.

---
---

## 5. Geography (`funder_locations`)

*One row per state (registered/operational office + real programme-linked evidence only — no unfounded rows created just to cover the homepage's generic "28 States & 8 UTs" pan-India claim, since that isn't tied to a specific, checkable location). All rows for SBI Foundation.*

| location (→ locations.id) | role | valid_from | valid_to | note | source_url | source_name | fetched_at | as_of | archive_url |
|---|---|---|---|---|---|---|---|---|---|
| Maharashtra (Mumbai) | `registered` | 2015-06-26 | — | MCA-registered office: 12th Floor, State Bank Bhavan, Nariman Point, Mumbai. | https://www.instafinancials.com/company/sbi-foundation-U85100MH2015NPL266051 | Instafinancials | 2026-09-29 | Current | Not found |
| Maharashtra (Mumbai) | `operates` | not_found | — | Separate, day-to-day operational address per the live website/give.do: Office No. 35, Ground Floor, The Arcade, World Trade Center, Cuffe Parade, Mumbai — different building from the MCA-registered office above. | https://sbifoundation.in ; https://give.do/discover/17LP/sbi-foundation | SBI Foundation website + give.do | 2026-09-29 | Current | Not found |
| Haryana | `funds` | 2022-10-02 | — | Gram Seva Phase 4 launch: 30 remote villages adopted across Aspirational Districts in this state (one of 6 states in the Phase-4 cohort). | https://www.aninews.in/news/business/business/sbi-chairman-announces-the-launch-of-sbi-foundations-gram-seva-program-across-6-states-of-india20221003100730 | ANI News (SBI Foundation Gram Seva Phase 4 launch) | 2026-09-29 | 2022-10-02 | Not found |
| Gujarat | `funds` | 2022-10-02 | — | Gram Seva Phase 4 launch, same cohort as above. | (same) | ANI News | 2026-09-29 | 2022-10-02 | Not found |
| Maharashtra | `funds` | 2022-10-02 | — | Gram Seva Phase 4 launch, same cohort — **in addition** to the `registered`/`operates` roles already listed for Maharashtra above (the HQ state is also a programme-funded state). | (same) | ANI News | 2026-09-29 | 2022-10-02 | Not found |
| Punjab | `funds` | 2022-10-02 | — | Gram Seva Phase 4 launch, same cohort. | (same) | ANI News | 2026-09-29 | 2022-10-02 | Not found |
| Tamil Nadu | `funds` | 2022-10-02 | — | Gram Seva Phase 4 launch, same cohort. | (same) | ANI News | 2026-09-29 | 2022-10-02 | Not found |
| West Bengal | `funds` | 2022-10-02 | — | Gram Seva Phase 4 launch, same cohort. | (same) | ANI News | 2026-09-29 | 2022-10-02 | Not found |
| Andhra Pradesh | `funds` | not_found | — | Named as an "SBI Youth for India (YFI) Fellowship" project-site state, per the programme's own support FAQ. | https://sbiyouthforindia.freshdesk.com/support/solutions/articles/44001195715-where-are-the-project-sites-located- | SBI YFI Fellowship support FAQ | 2026-09-29 | Undated (live FAQ page) | Not found |
| Assam | `funds` | not_found | — | Same YFI Fellowship project-site list. | (same) | SBI YFI Fellowship support FAQ | 2026-09-29 | Undated | Not found |
| Bihar | `funds` | not_found | — | Same YFI Fellowship project-site list. | (same) | SBI YFI Fellowship support FAQ | 2026-09-29 | Undated | Not found |
| Karnataka | `funds` | not_found | — | Same YFI Fellowship project-site list. | (same) | SBI YFI Fellowship support FAQ | 2026-09-29 | Undated | Not found |
| Kerala | `funds` | not_found | — | Same YFI Fellowship project-site list. | (same) | SBI YFI Fellowship support FAQ | 2026-09-29 | Undated | Not found |
| Madhya Pradesh | `funds` | not_found | — | Same YFI Fellowship project-site list. | (same) | SBI YFI Fellowship support FAQ | 2026-09-29 | Undated | Not found |
| Odisha | `funds` | not_found | — | Same YFI Fellowship project-site list. | (same) | SBI YFI Fellowship support FAQ | 2026-09-29 | Undated | Not found |
| Rajasthan | `funds` | not_found | — | Same YFI Fellowship project-site list. | (same) | SBI YFI Fellowship support FAQ | 2026-09-29 | Undated | Not found |
| Meghalaya | `funds` | not_found | — | Same YFI Fellowship project-site list. | (same) | SBI YFI Fellowship support FAQ | 2026-09-29 | Undated | Not found |
| Himachal Pradesh | `funds` | not_found | — | Same YFI Fellowship project-site list. | (same) | SBI YFI Fellowship support FAQ | 2026-09-29 | Undated | Not found |
| Uttarakhand | `funds` | not_found | — | Same YFI Fellowship project-site list. | (same) | SBI YFI Fellowship support FAQ | 2026-09-29 | Undated | Not found |
| Telangana | `funds` | not_found | — | Same YFI Fellowship project-site list. | (same) | SBI YFI Fellowship support FAQ | 2026-09-29 | Undated | Not found |
| Jharkhand | `funds` | not_found | — | Same YFI Fellowship project-site list. | (same) | SBI YFI Fellowship support FAQ | 2026-09-29 | Undated | Not found |

**Not itemised as individual rows (aggregate claim only, not tied to specific checkable evidence per state):** SBI Foundation's own homepage and LinkedIn page both claim reach across **"28 States & 8 Union Territories"** — i.e., literally all of India. This is the underlying source for the `funding_trend` note already in Part A. It has **not** been expanded into 36 individual `priority` rows here, since that would create rows with no specific evidence behind each one; only the states above (13 distinct: Haryana, Gujarat, Maharashtra, Punjab, Tamil Nadu, West Bengal, Andhra Pradesh, Assam, Bihar, Karnataka, Kerala, Madhya Pradesh, Odisha, Rajasthan, Meghalaya, Himachal Pradesh, Uttarakhand, Telangana, Jharkhand — 19 total, some overlapping between the two programmes) currently have real, named programme evidence behind them.

**Gram Seva's fuller footprint, not yet fully itemised:** the Oct 2022 news coverage states Gram Seva had, by Phase 3, already reached **"100 villages across 16 States"** and **"16 out of the total 17 SBI Circles"** — meaning **10 more states** beyond the 6 named Phase-4 states above are also Gram Seva locations, but their individual names were not given in any source checked in this pass. Flagged as a gap rather than guessed.

**Bonus find while researching this table:** the October 2022 ANI/Times of India/LiveMint coverage of the Gram Seva Phase 4 launch **independently names "Sanjay Prakash, MD & CEO, SBI Foundation"** as speaking at the event — this is a real, dated (2022-10-02) primary-adjacent confirmation that Sanjay Prakash held the MD & CEO title at least as far back as 2022, adding weight to give.do's current listing over the live website's "Swapan Dhar" in the unresolved leadership discrepancy flagged in `leadership_note` above. Still not fully conclusive for the *current* (2026) status, since either name could have changed since 2022 — but it shifts the balance of evidence. Recommend a fresh, dated news search ("SBI Foundation new MD 2025" or "2026") to close this out.

---
---

## 6. Yearly CSR filing (`funder_csr_years`)

⚠️ **Important attribution flag, same logic as `section_135_bound` in Part A:** these figures are **State Bank of India's (the parent's) own CSR disclosures**, not a standalone Section-135 filing by SBI Foundation itself (recall: SBI Foundation is the implementing Section 8 company; SBI is a statutory corporation under the SBI Act, 1955, with **"CIN: Not Applicable"** per its own BRSR — so even SBI's own Section 135 status is not a clean "Yes" the way it would be for an ordinary Section-135 private company). No source located in this pass prints a formal Annexure-II-style breakdown (average net profit / 2%-prescribed figure / admin-overhead cap / impact-assessment cost) for either SBI or SBI Foundation — SBI's own disclosures give only **total CSR spend** and activity counts, not the full a–f breakdown the schema asks for. Fields with no real source are left empty rather than calculated or guessed.

| fiscal_year | section_135_applicable | average_net_profit | prescribed_csr | spent_on_projects | admin_overheads | impact_assessment_cost | total_spent (₹) | unspent_transferred | excess_spent | impact_assessment_done | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2023-24 | **Not confirmed** *(SBI is not a Companies-Act entity; flagged rather than assumed Yes/No)* | *(empty — not disclosed)* | *(empty — not disclosed)* | *(empty)* | *(empty)* | *(empty)* | **5,023,200,000** (₹502.32 crore, State Bank of India total) | *(empty)* | *(empty)* | Not found | Of the ₹502.32 crore Bank-wide total, **₹301.24 crore (60%) was specifically allocated to SBI Foundation** "for undertaking CSR activities in project mode" — the clearest direct SBI→SBI Foundation figure found for any year. 173 CSR initiatives across 80 Aspirational Districts; ₹6.08 crore of the total was spent specifically within Aspirational Districts. | https://sbi.bank.in/documents/17836/39646794/Annual_Report_2024.pdf | State Bank of India Annual Report 2024 (covers FY2023-24) | 2026-09-29 | FY2023-24 |
| FY2024-25 | Not confirmed | *(empty)* | *(empty)* | *(empty)* | *(empty)* | *(empty)* | **6,107,700,000** (₹610.77 crore, State Bank of India total) | *(empty)* | *(empty)* | Not found | 1,408 CSR activities undertaken, Pan-India, 20,000+ villages covered, 65 lakh+ people benefitted. **The specific SBI→SBI Foundation portion for this year was not found** in the sources checked (unlike FY2023-24 and FY2025-26, where a specific Foundation-allocation figure was locatable) — flagged as a gap, not assumed proportional. | https://sbi.bank.in/corporate/SBIAR2425/SBI-AR-2024-25.pdf | State Bank of India Annual Report 2024-25 | 2026-09-29 | FY2024-25 |
| FY2025-26 | Not confirmed | *(empty)* | *(empty)* | *(empty)* | *(empty)* | *(empty)* | **7,090,100,000** (₹709.01 crore, State Bank of India total disbursed; **₹7,135,643,643.05 sanctioned** — the two figures differ because some sanctioned amounts had not yet been disbursed by period-end) | *(empty)* | *(empty)* | Not found | **Exact SBI→SBI Foundation transfers found, line by line, in SBI's own "CSR Initiatives Undertaken During FY 2025-26" disclosure**: ₹300,00,00,000 (2025-09-29) + ₹160,00,00,000 (2025-12-31) + ₹35,95,99,201.88 (2026-03-27) = **₹495,95,99,201.88 (₹495.96 crore) transferred to SBI Foundation** — i.e. **~70% of the Bank's total FY2025-26 CSR spend went to SBI Foundation**, with the remaining ~30% spent via "Direct activity by Bank" and direct donations to ~1,500+ other individual NGOs/institutions (a full donee-by-donee list runs to 126 pages). 58 lakh+ beneficiaries Bank-wide. | https://sbi.bank.in/documents/17826/0/26052026_CSR+ACTIVITIES+FY+2025-26.pdf | State Bank of India — "CSR Initiatives Undertaken During FY 2025-26" | 2026-09-29 | FY2025-26 |

**Reconciliation note on FY2025-26's own aggregate line, found on the PDF's final page:** the document's own grand total reads "Total ... 7,13,56,43,643.05" (sanctioned) / "7,09,01,00,000.00" (disbursed) — both figures **include** the ₹495.96 crore transferred to SBI Foundation as three of the ~1,528 line items, i.e. SBI Foundation is one (large) line among many, not a separate, deducted total. This confirms the ₹495.96 crore is a subset of, not additional to, the ₹709.01 crore Bank-wide figure.

---
---

## 7. Spend breakdown (`funder_csr_spend`)

**Major new source found in this pass: SBI Foundation's own Annual Report 2023-24** (140 pages, downloaded directly from sbifoundation.in/publication and read in full for this section) — its Directors' Report and audited financial statements give real, audited ₹ figures, resolving several earlier gaps.

⚠️ **Three different FY2023-24 totals exist across sources — presented together, not collapsed into one:**
| Figure | Amount | What it measures | Source |
|---|---|---|---|
| ₹301.24 crore | Allocated **by SBI (the Bank) to** SBI Foundation | The Bank's transfer to the Foundation | SBI's own Annual Report 2024 (Table 6 above) |
| ₹288.56 crore | **Sanctioned** across 145 projects | Commitments approved that year (not all necessarily disbursed same year) | SBI Foundation's own Directors' Report, AR2023-24, p.82 |
| ₹217.12 crore (₹21,711.73 Lakh) | **Grants towards Projects — actually disbursed** | Cash that actually left the Foundation for projects, per its own audited Income & Expenditure statement | SBI Foundation's own audited financials, AR2023-24, p.81 |

These are plausibly reconcilable (allocated > sanctioned > disbursed-in-year, since sanctioned amounts can be disbursed across multiple years) but are **not stated as reconciling to each other anywhere in the source** — presented as three real, distinct figures rather than picking one.

**(A) Category-level totals for FY2023-24 — sector-wise % breakdown from SBI Foundation's own "Year at a Glance" infographic (AR2023-24, p.12), converted to ₹ against the ₹217.12 crore disbursed total.** ⚠️ **The ₹ figures below are calculated by us** (% × ₹217.12 cr) — the source itself prints only percentages, not rupee amounts, per sector:

| fiscal_year | csr_sector_id (Schedule VII mapping) | amount (₹) | via_agency | is_ongoing | project_count | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|---|
| FY2023-24 | Health (Jivanam) | **666,500,000** *(30.65% of ₹217.12cr — calculated by us)* | Yes | Yes | not_found | Largest single category by spend share. | https://sbifoundation.in/publication | SBI Foundation Annual Report 2023-24 (p.12) | 2026-09-29 | FY2023-24 |
| FY2023-24 | Women Empowerment (Sashakti) | **453,100,000** *(20.87% — calculated by us)* | Yes | Yes | not_found | — | (same) | (same) | 2026-09-29 | FY2023-24 |
| FY2023-24 | Livelihood (LEAP) | **309,000,000** *(14.23% — calculated by us)* | Yes | Yes | not_found | — | (same) | (same) | 2026-09-29 | FY2023-24 |
| FY2023-24 | Environmental Sustainability (CONSERW) | **233,000,000** *(10.73% — calculated by us)* | Yes | Yes | not_found | Pledged 1 crore trees by 2025; 6,730+ metric tonnes of waste diverted/recycled; conservation work in 22+ protected areas (per the MD's message, same report). | (same) | (same) | 2026-09-29 | FY2023-24 |
| FY2023-24 | Disability Inclusion (Centre of Excellence for PwDs) | **226,900,000** *(10.45% — calculated by us)* | Yes | Yes | 12 *(named explicitly: "12 impactful projects," per the MD's message)* | — | (same) | (same) | 2026-09-29 | FY2023-24 |
| FY2023-24 | Education (Integrated Learning Mission) | **182,000,000** *(8.38% — calculated by us)* | Yes | Yes | not_found | — | (same) | (same) | 2026-09-29 | FY2023-24 |
| FY2023-24 | Sports (ACE) | **67,800,000** *(3.12% — calculated by us)* | Yes | Yes | not_found | — | (same) | (same) | 2026-09-29 | FY2023-24 |
| FY2023-24 | Rural Development (Gram Seva / Gram Saksham) | **29,100,000** *(1.34% — calculated by us)* | Yes | Yes | not_found | ⚠️ Surprisingly small share (1.34%) for what is one of SBI Foundation's most publicised flagship programmes (expanded to 180 villages this year, per the MD's message) — flagged as a genuine oddity worth double-checking against the Gram Seva chapter (AR2023-24 pp.21-30) directly rather than assumed to be an error. | (same) | (same) | 2026-09-29 | FY2023-24 |
| FY2023-24 | Miscellaneous | **6,100,000** *(0.28% — calculated by us)* | Yes | Yes | not_found | — | (same) | (same) | 2026-09-29 | FY2023-24 |

**(B) Named individual projects/initiatives — real counts found, but no per-project ₹ amount located for any of them (left genuinely blank rather than estimated):**

| fiscal_year | project_name | csr_sector_id | amount | via_agency | notes | source_url |
|---|---|---|---|---|---|---|
| FY2023-24 | SBI Gram Seva (incl. new "SBI Samman" sub-initiative) | Rural Development | **not disclosed** | Yes | Expanded to 180 villages this year; SBI Samman launched to identify/develop villages of freedom fighters, war veterans & public heroes. | https://sbifoundation.in/publication |
| FY2023-24 | SBIF Sashakti (women empowerment vertical) | Gender/Women Empowerment | **not disclosed** | Yes | Newly designated as its own vertical this year (previously folded into other programmes). | https://sbifoundation.in/publication |
| FY2023-24 | SBI Youth for India (YFI) Fellowship | Youth Development | **not disclosed** | Yes | 55 new fellows placed this year (580 cumulative since inception, per the Chairman's message). | https://sbifoundation.in/publication |
| FY2023-24 | Jivanam — 49 new SBI Sanjeevani Mobile medical units + 66 new initiatives | Health | **not disclosed** | Yes | — | https://sbifoundation.in/publication |
| FY2023-24 | Centre of Excellence for PwDs (12 projects) | Disability Inclusion | **not disclosed** | Yes | — | https://sbifoundation.in/publication |

**State/district-level (`state_location_id`/`district_location_id`) breakdown, MCA-CSV granularity:** **not found.** SBI Foundation's own Annual Report gives only the aggregate "28 States & 7 UTs" reach figure and a "Geographic Focus" page (p.13) that is a map graphic, not a data table — no per-state ₹ breakdown exists in this report. `implementing_agency` and `agency_csr1` for individual NGO partners: also not found at this level of detail in the sections read so far (the report's later programme-specific chapters, pp.15-79, were not yet read in full — flagged as a next step, not assumed absent).

---
---

## 8. Programmes (`programs`)

*All rows for SBI Foundation, sourced from its own Annual Report 2023-24 (read in full for this section — pp.15-79 cover all 9 flagship programmes). `org_id` left empty throughout (these are funder programmes, not NGO programmes). `funder_id` → SBI Foundation for every row.*

### Top level — the 9 Flagship Programmes (`kind = programme`)

| name | description | status | start_date | end_date | details (JSON) | source_url | source_name | fetched_at | as_of | kind | is_enabler |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SBIF Jivanam | Healthcare vertical addressing primary care, TB, maternal/child health, eye care, mental health, palliative care, cancer screening, organ donation and health-infrastructure support for underserved communities. Delivered via 80 "SBI Sanjeevani" Mobile Medical Units and multiple specialised sub-projects. | active | not_found | — | `{"beneficiaries_cumulative": "9.4 lakh+", "states": 26, "sdgs": ["No Poverty","Good Health and Well-being","Reduced Inequalities","Zero Hunger","Industry Innovation & Infrastructure"]}` | https://sbifoundation.in/publication (AR2023-24, pp.15-20) | SBI Foundation Annual Report 2023-24 | 2026-09-29 | FY2023-24 | programme | No |
| SBI Gram Seva | Integrated rural development programme adopting entire villages (esp. NITI Aayog Aspirational Districts) for holistic intervention across digitalisation, education, health and WASH. Launched 2017; expanded to 180 villages by FY2023-24, including a new "SBI Samman" sub-initiative honouring villages of freedom fighters/war veterans. | active | 2017-01-01 *(year confirmed via Oct-2022 news coverage; exact day/month not disclosed)* | — | `{"beneficiaries_cumulative": "4 lakh+", "states": 27, "villages_fy2023-24": 180}` | https://sbifoundation.in/publication (AR2023-24, pp.21-30) | SBI Foundation Annual Report 2023-24 | 2026-09-29 | FY2023-24 | programme | No |
| SBI Youth for India (YFI) Fellowship | A 13-month fellowship placing India's young professionals with grassroots NGOs to work directly in rural communities across 12 thematic areas (education, health, food security, livelihoods, women's empowerment, environment, self-governance, etc.). Running since 2011. | active | 2011-01-01 | — | `{"beneficiaries_cumulative": "1.5 lakh+", "states_cumulative": 20, "alumni_cumulative": "580+", "fy2023-24_batch_size": 54, "fy2023-24_locations": 40, "fy2023-24_states": 11}` | https://sbifoundation.in/publication (AR2023-24, pp.31-36) | SBI Foundation Annual Report 2023-24 | 2026-09-29 | FY2023-24 | programme | **Yes** *(builds people/capacity for the development sector broadly, rather than delivering a single direct service)* |
| Integrated Learning Mission (ILM) | Education vertical focused on improving learning outcomes via curriculum/pedagogical content development, teacher capacity-building, strengthening government school systems, and improving access to higher education via scholarships for meritorious underprivileged students. | active | not_found | — | `{"beneficiaries_cumulative": "2.4 crore+", "states": "not_found (cut off in source table)"}` | https://sbifoundation.in/publication (AR2023-24, pp.37-42) | SBI Foundation Annual Report 2023-24 | 2026-09-29 | FY2023-24 | programme | No |
| Centre of Excellence (CoE) for Persons with Disabilities (PwDs) | Centralised support hub for PwDs, spanning inclusive employment at SBI itself, skill development, assistive technology distribution, inclusive education, and family/child support — delivered through 4 named sub-programmes (Samarthya, Samagra Shiksha, Swavlamban, CARE). 30 projects sanctioned in FY2023-24. | active | 2017-01-01 *(training initiatives explicitly stated as running "since 2017")* | — | `{"beneficiaries_cumulative": 50000, "states": 20, "projects_fy2023-24": 30}` | https://sbifoundation.in/publication (AR2023-24, pp.43-50) | SBI Foundation Annual Report 2023-24 | 2026-09-29 | FY2023-24 | programme | No |
| Livelihood and Entrepreneurship Accelerator Program (LEAP) | Livelihoods vertical combining climate-resilient agriculture/integrated livestock development, micro-entrepreneurship support, startup incubation (Innovators for Bharat), skilling for BFSI/IT sector jobs, and strengthening community institutions (SHGs/FPOs). Aligned to UN SDG 1 (poverty eradication). | active | not_found | — | `{"beneficiaries_cumulative": "10.5 lakh+", "states": 16}` | https://sbifoundation.in/publication (AR2023-24, pp.51-60) | SBI Foundation Annual Report 2023-24 | 2026-09-29 | FY2023-24 | programme | No |
| CONSERW (CONservation through Sustainable Engagement, Restoration and Wildlife-Protection) | Environment vertical covering afforestation/ecosystem restoration (ARANYA), sustainable waste management ("Waste No More"), and wildlife conservation (incl. Red Panda and vulture conservation, human-wildlife conflict mitigation). | active | not_found | — | `{"beneficiaries_cumulative": "29.52 lakh+", "states": 21, "trees_planted_cumulative": "7 lakh", "acres_restored": 1300}` | https://sbifoundation.in/publication (AR2023-24, pp.61-68) | SBI Foundation Annual Report 2023-24 | 2026-09-29 | FY2023-24 | programme | No |
| ACE (sports vertical, name not expanded in source) | Sports vertical supporting elite and para-athletes via financial support, specialised coaching, sports science, and infrastructure — including a dedicated Para Athlete Grant Program (100 athletes) run in partnership with the Abhinav Bindra Foundation Trust. | active | not_found | — | `{"beneficiaries_cumulative": 235, "states": 19, "medals_won_cumulative": "400+", "asian_para_games_2022_medals": 28}` | https://sbifoundation.in/publication (AR2023-24, pp.69-72) | SBI Foundation Annual Report 2023-24 | 2026-09-29 | FY2023-24 | programme | No |
| SBIF Sashakti | Women's empowerment vertical (newly designated as its own standalone vertical in FY2023-24, having previously been folded into other programmes) covering financial/digital/legal literacy, menstrual hygiene, elderly-women shelter support, and tribal women's economic independence. Smallest geographic footprint of all 9 flagship programmes. | active | 2023-01-01 *(approximate — "designated" as its own vertical this FY, per the MD's message; underlying component projects like "Unnati" may predate this formal designation)* | — | `{"beneficiaries_cumulative": 29000, "states": 5}` | https://sbifoundation.in/publication (AR2023-24, pp.73-76) | SBI Foundation Annual Report 2023-24 | 2026-09-29 | FY2023-24 | programme | No |

### Second level — named sub-projects with the clearest standalone evidence (`kind = project`, `parent_id` → the flagship programme above)

| name | parent | description | status | start_date | details (JSON) | source_url |
|---|---|---|---|---|---|---|
| SBI Sanjeevani — Clinic on Wheels | SBIF Jivanam | 80 Mobile Medical Units (MMUs) delivering primary healthcare across 20 states + 2 UTs. Won CSR Summit & Awards and Indian CSR Awards. | active | not_found | `{"mmus": 80, "states": 20, "uts": 2, "beneficiaries": "9.6 lakh"}` | AR2023-24, p.17 |
| SBIF TB Care | SBIF Jivanam | Mobile-unit-based TB detection, treatment and nutritional support in Chhattisgarh and Madhya Pradesh. | active | not_found | `{"beneficiaries": "2,800+", "states": ["Chhattisgarh","Madhya Pradesh"]}` | AR2023-24, p.17 |
| SBIF Matrichhaya | SBIF Jivanam | Maternal and child health, equipping healthcare centres in Odisha and Jharkhand. | active | not_found | `{"states": ["Odisha","Jharkhand"]}` | AR2023-24, p.17 |
| SBIF Eye Care | SBIF Jivanam | Eye-care screenings, surgeries and follow-up in West Bengal, Andhra Pradesh and Rajasthan. | active | not_found | `{"states": ["West Bengal","Andhra Pradesh","Rajasthan"]}` | AR2023-24, p.17 |
| SBI Samman | SBI Gram Seva | Identifies and develops villages connected to freedom fighters, war veterans and public heroes; launched under Gram Seva in FY2023-24. | active | 2023-01-01 *(approximate)* | `{}` | AR2023-24, p.6 |
| YFI Sahyog (Pitch Fest) | SBI Youth for India (YFI) Fellowship | Seed-funding competition for YFI Alumni's social ventures; 8 Alumni secured ₹30 lakh (Alumni track) and 25 Fellows secured ₹15.16 lakh (current-Fellows track) in FY2023-24. | active | not_found | `{"amount_alumni_inr": 3000000, "amount_fellows_inr": 1516000}` | AR2023-24, p.33 |
| Innovators for Bharat (I4B) | Livelihood and Entrepreneurship Accelerator Program (LEAP) | Startup-incubation initiative; worked with 3 incubators, supported 60+ startups at a cumulative outlay of ₹15+ crore, incl. a large AI/ML/Data-Science research hub with IIT Bombay for the BFSI sector. | active | not_found | `{"incubators": 3, "startups_supported": "60+", "outlay_inr": 150000000}` | AR2023-24, p.55 |
| SAMEIP | Livelihood and Entrepreneurship Accelerator Program (LEAP) | Employability-focused skill training for 1,500 young Persons with Disabilities for BFSI-sector careers, across Bengaluru, Chennai, Delhi, Mumbai and Kolkata. Launched 2020. | active | 2020-01-01 | `{"target_beneficiaries": 1500}` | AR2023-24, p.57 |
| SAMARTHYA | Centre of Excellence (CoE) for Persons with Disabilities (PwDs) | Assistive-technology distribution (artificial limbs, calipers — target 8,000+ devices) plus therapy services and Digital Labs for visually-impaired schoolchildren. | active | not_found | `{"assistive_devices_target": 8000}` | AR2023-24, p.45 |
| Swavlamban | Centre of Excellence (CoE) for Persons with Disabilities (PwDs) | Skill development, vocational training and employment support for PwDs across IT, retail, culinary and other sectors, including entrepreneurial support. | active | not_found | `{}` | AR2023-24, pp.45-46 |
| CARE (Child Assistance, Relief and Empowerment) | Centre of Excellence (CoE) for Persons with Disabilities (PwDs) | Support across the disability life-cycle: family relief, clinical/eye-care services, clubfoot/ulcer treatment, support for abandoned children with disabilities, and neurodevelopmental-disorder care. | active | not_found | `{}` | AR2023-24, p.46 |
| SBIF ARANYA | CONSERW | Afforestation/ecosystem restoration: indigenous tree plantation, mangrove restoration, springshed management. 7 lakh trees planted, 1,300 acres restored so far; 28 lakh more trees planned across 12 states. | active | not_found | `{"trees_planted": "7 lakh", "acres_restored": 1300, "trees_planned": "28 lakh", "states_ongoing": 12}` | AR2023-24, p.63 |
| Waste No More | CONSERW | End-to-end sustainable waste management via public-private partnerships; transformed 3 Karnataka towns into model sanitation towns; active in Madhya Pradesh (Panna) and Maharashtra (Aurangabad). | active | not_found | `{}` | AR2023-24, pp.64-65 |
| SBIF ACE: Para Athlete Grant Program | ACE | Financial support, coaching, nutrition and equipment for 100 promising para-athletes, run with the Abhinav Bindra Foundation Trust, targeting the Paralympic Games and Asian Para Games. | active | not_found | `{"athletes": 100, "partner": "Abhinav Bindra Foundation Trust"}` | AR2023-24, p.70 |
| SBIF ACE: Olympic Development Program | ACE | Residential weightlifting training programme for 35 athletes plus a sports-science centre at the Karnam Malleswari Weightlifting Academy (~100 athletes). | active | not_found | `{"athletes_residential": 35, "athletes_sports_science_centre": 100}` | AR2023-24, p.70 |
| SBIF - She Leads | SBIF Sashakti | Financial, legal and digital literacy for 3,000 women SHG members in Kalahandi and Nuapada districts, Odisha. | active | not_found | `{"beneficiaries": 3000, "state": "Odisha"}` | AR2023-24, p.75 |
| SBIF Garima | SBIF Sashakti | Shelter homes for 40 elderly women in Krishna District, Andhra Pradesh. | active | not_found | `{"beneficiaries": 40, "state": "Andhra Pradesh"}` | AR2023-24, p.75 |
| Unnati (with SUVIDHA) | SBIF Sashakti | Skill-development programme in Solan district, Himachal Pradesh, transitioning women from agricultural labour into entrepreneurship (e.g. fruit processing); 500 women across 50 villages. Won a 2023 CSR Journal Award. | active | not_found | `{"beneficiaries": 500, "villages": 50, "state": "Himachal Pradesh"}` | AR2023-24, p.76 |

**Not yet mapped into this table (real, but lower-priority given time constraints):** several more named sub-initiatives were seen in the report but not fully detailed here — e.g. Jivanam's mental-health projects, palliative care, cancer-screening; ILM's "Learn Play Grow" (with Sesame Workshop India) and SIMHA (with TISS); LEAP's "Skilling for Future" and micro-entrepreneurship district coalitions; CONSERW's Red Panda/vulture/human-elephant-conflict wildlife work; Sashakti's Saarthi and Project Naya Savera. These exist in the same source and can be added in a follow-up pass if a fuller sub-project list is wanted.

---
---

## 9. Where programmes ran (`funder_footprints`)

*One row per named place with real evidence (not the bare aggregate "X states" counts, which have no itemised list in the source — see note at the end). All rows: FY2023-24, from SBI Foundation's own Annual Report 2023-24.*

| program | fiscal_year | location (name_as_printed) | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|
| SBIF TB Care (→ Jivanam) | FY2023-24 | Chhattisgarh | Mobile-unit TB detection/care, 2,800+ people. | https://sbifoundation.in/publication | SBI Foundation AR2023-24, p.17 | 2026-09-29 | FY2023-24 |
| SBIF TB Care (→ Jivanam) | FY2023-24 | Madhya Pradesh | Same project, same source. | (same) | (same) | 2026-09-29 | FY2023-24 |
| SBIF Matrichhaya (→ Jivanam) | FY2023-24 | Odisha | Maternal/child health centre equipping. | (same) | AR2023-24, p.17 | 2026-09-29 | FY2023-24 |
| SBIF Matrichhaya (→ Jivanam) | FY2023-24 | Jharkhand | Same project. | (same) | AR2023-24, p.17 | 2026-09-29 | FY2023-24 |
| SBIF Eye Care (→ Jivanam) | FY2023-24 | West Bengal | Eye-care screenings/surgeries. | (same) | AR2023-24, p.17 | 2026-09-29 | FY2023-24 |
| SBIF Eye Care (→ Jivanam) | FY2023-24 | Andhra Pradesh | Same project. | (same) | AR2023-24, p.17 | 2026-09-29 | FY2023-24 |
| SBIF Eye Care (→ Jivanam) | FY2023-24 | Rajasthan | Same project. | (same) | AR2023-24, p.17 | 2026-09-29 | FY2023-24 |
| Mental health support for destitute women (→ Jivanam) | FY2023-24 | Maharashtra | 300 destitute women. | (same) | AR2023-24, p.17 | 2026-09-29 | FY2023-24 |
| Decentralized Mental Healthcare (→ Jivanam) | FY2023-24 | Maharashtra | 9,000 patients — separate project, same state. | (same) | AR2023-24, p.17 | 2026-09-29 | FY2023-24 |
| Climate-Resilient Agriculture & Integrated Livestock (→ LEAP) | FY2023-24 | Uttarakhand | 2.5 lakh+ farmers across this 5-state cluster. | (same) | AR2023-24, p.53 | 2026-09-29 | FY2023-24 |
| Climate-Resilient Agriculture & Integrated Livestock (→ LEAP) | FY2023-24 | Maharashtra | Same 5-state cluster. | (same) | AR2023-24, p.53 | 2026-09-29 | FY2023-24 |
| Climate-Resilient Agriculture & Integrated Livestock (→ LEAP) | FY2023-24 | Madhya Pradesh | Same cluster. | (same) | AR2023-24, p.53 | 2026-09-29 | FY2023-24 |
| Climate-Resilient Agriculture & Integrated Livestock (→ LEAP) | FY2023-24 | Jharkhand | Same cluster. | (same) | AR2023-24, p.53 | 2026-09-29 | FY2023-24 |
| Climate-Resilient Agriculture & Integrated Livestock (→ LEAP) | FY2023-24 | Bihar | Same cluster. | (same) | AR2023-24, p.53 | 2026-09-29 | FY2023-24 |
| Micro-Entrepreneurship district coalitions (→ LEAP) | FY2023-24 | Uttar Pradesh | "Eastern Uttar Pradesh" — 8 district-level coalitions, 1,207 microenterprises. | (same) | AR2023-24, p.54 | 2026-09-29 | FY2023-24 |
| Micro-Entrepreneurship district coalitions (→ LEAP) | FY2023-24 | Madhya Pradesh | Same coalitions/project. | (same) | AR2023-24, p.54 | 2026-09-29 | FY2023-24 |
| FPO community-institution building (→ LEAP) | FY2023-24 | Maharashtra | 80+ FPOs, 20,000+ farmers, across this 4-state+region cluster. | (same) | AR2023-24, p.56 | 2026-09-29 | FY2023-24 |
| FPO community-institution building (→ LEAP) | FY2023-24 | Andhra Pradesh | Same cluster. | (same) | AR2023-24, p.56 | 2026-09-29 | FY2023-24 |
| FPO community-institution building (→ LEAP) | FY2023-24 | Odisha | Same cluster. | (same) | AR2023-24, p.56 | 2026-09-29 | FY2023-24 |
| FPO community-institution building (→ LEAP) | FY2023-24 | Uttar Pradesh | Same cluster (also overlaps with the micro-entrepreneurship project above, but distinct sub-project). | (same) | AR2023-24, p.56 | 2026-09-29 | FY2023-24 |
| SBIF ARANYA — indigenous tree plantation (→ CONSERW) | FY2023-24 | Rajasthan | "Over 1 lakh trees" planted. | (same) | AR2023-24, p.63 | 2026-09-29 | FY2023-24 |
| SBIF ARANYA — Miyawaki forests (→ CONSERW) | FY2023-24 | Gujarat | 250 Miyawaki forests across this 2-state cluster. | (same) | AR2023-24, p.63 | 2026-09-29 | FY2023-24 |
| SBIF ARANYA — Miyawaki forests (→ CONSERW) | FY2023-24 | Madhya Pradesh | Same cluster. | (same) | AR2023-24, p.63 | 2026-09-29 | FY2023-24 |
| SBIF ARANYA — springshed management (→ CONSERW) | FY2023-24 | Uttarakhand | Himalayan spring recharge. | (same) | AR2023-24, p.63 | 2026-09-29 | FY2023-24 |
| SBIF ARANYA — springshed management (→ CONSERW) | FY2023-24 | Himachal Pradesh | Same project. | (same) | AR2023-24, p.63 | 2026-09-29 | FY2023-24 |
| SBIF ARANYA — mangrove restoration (→ CONSERW) | FY2023-24 | Kerala | 30 acres of mangrove forest restored. | (same) | AR2023-24, p.63 | 2026-09-29 | FY2023-24 |
| Waste No More — model sanitation towns (→ CONSERW) | FY2023-24 | Karnataka | 3 towns transformed; also a separate Dakshina Kannada waste project. | (same) | AR2023-24, pp.64-65 | 2026-09-29 | FY2023-24 |
| Waste No More — Panna (→ CONSERW) | FY2023-24 | Madhya Pradesh | Municipal solid-waste management, Panna. | (same) | AR2023-24, p.64 | 2026-09-29 | FY2023-24 |
| Waste No More — Aurangabad (→ CONSERW) | FY2023-24 | Maharashtra | 1 lakh residents educated on waste segregation, Aurangabad city. | (same) | AR2023-24, p.64 | 2026-09-29 | FY2023-24 |
| Red Panda conservation (→ CONSERW) | FY2023-24 | Sikkim | Interpretation centre, conservation mapping. | (same) | AR2023-24, p.65 | 2026-09-29 | FY2023-24 |
| Red Panda conservation (→ CONSERW) | FY2023-24 | West Bengal | "Darjeeling-Kalimpong" — same project. | (same) | AR2023-24, pp.65-66 | 2026-09-29 | FY2023-24 |
| Solar-powered wildlife patrolling camps (→ CONSERW) | FY2023-24 | Madhya Pradesh | Human-wildlife conflict mitigation. | (same) | AR2023-24, p.65 | 2026-09-29 | FY2023-24 |
| Human-elephant conflict mitigation (→ CONSERW) | FY2023-24 | Assam | "Baksa and Udalguri districts" specifically named. | (same) | AR2023-24, p.66 | 2026-09-29 | FY2023-24 |
| Wheelchair-accessible e-rickshaws (→ CoE for PwDs) | FY2023-24 | Goa | 30 e-rickshaws; launched by the Goa Chief Minister on 2024-03-11. | (same) | AR2023-24, pp.47-48 | 2026-09-29 | FY2023-24 |
| Para Athlete Grant Program (→ ACE) | FY2023-24 | Arunachal Pradesh | Named via athlete Biri Takar's case study. | (same) | AR2023-24, p.71 | 2026-09-29 | FY2023-24 |
| SBIF - She Leads (→ Sashakti) | FY2023-24 | Odisha | "Kalahandi and Nuapada districts" specifically named. | (same) | AR2023-24, p.75 | 2026-09-29 | FY2023-24 |
| Saarthi (→ Sashakti) | FY2023-24 | Haryana | "Jind and Kaithal districts" specifically named. | (same) | AR2023-24, p.75 | 2026-09-29 | FY2023-24 |
| SBIF Garima (→ Sashakti) | FY2023-24 | Andhra Pradesh | "Krishna District" specifically named; 40 elderly women. | (same) | AR2023-24, p.75 | 2026-09-29 | FY2023-24 |
| Project Naya Savera (→ Sashakti) | FY2023-24 | Uttar Pradesh | "Meerut district," 24 government schools. | (same) | AR2023-24, p.75 | 2026-09-29 | FY2023-24 |
| Unnati (→ Sashakti) | FY2023-24 | Himachal Pradesh | "Silhari village," Solan district; 500 women, 50 villages. | (same) | AR2023-24, p.76 | 2026-09-29 | FY2023-24 |

**Not itemised (aggregate counts only, no named list in source):** each flagship programme's own top-level "States: N" figure (Jivanam 26, Gram Seva 27, YFI 20 cumulative/11 this year, CoE 20, LEAP 16, CONSERW 21, ACE 19, Sashakti 5) is a bare count with **no accompanying itemised state list** anywhere in the 140-page report — only the sub-project-level states shown above are individually named. The rows above therefore undercount each programme's true footprint; they are the real, checkable subset, not the whole.

---
---

## 10. Partners named (`funder_partners`)

*Real, individually-named partners found in the AR2023-24's narrative text (not the "Our Partners" logo-grid pages, which render as images and did not extract as text via this session's PDF reader — flagged as a genuine gap, not skipped). All rows: FY2023-24. `partner_csr1` not printed for any partner in this source.*

| program | fiscal_year | partner_name | partner_canonical | partner_kind | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|
| Integrated Learning Mission (ILM) | FY2023-24 | Sesame Workshop India Trust | Sesame Workshop India Trust | foundation | "Learn, Play, Grow" project — 96,000+ students in Meghalaya; also trained 3,378 educators. | https://sbifoundation.in/publication | SBI Foundation AR2023-24, p.39 | 2026-09-29 | FY2023-24 |
| Integrated Learning Mission (ILM) | FY2023-24 | SCERT Uttar Pradesh | State Council of Educational Research and Training, Uttar Pradesh | government | New Grades 4-7 curriculum deployed in all UP government schools. | (same) | p.39 | 2026-09-29 | FY2023-24 |
| Integrated Learning Mission (ILM) | FY2023-24 | Education Support Organisation | Education Support Organisation | ngo | Co-partner with SCERT UP on the same curriculum project. | (same) | p.39 | 2026-09-29 | FY2023-24 |
| Integrated Learning Mission (ILM) | FY2023-24 | SCERT Punjab | State Council of Educational Research and Training, Punjab | government | Localized Punjabi-language Math content, Grades 6-12, ~6,500 schools. | (same) | p.39 | 2026-09-29 | FY2023-24 |
| Integrated Learning Mission (ILM) | FY2023-24 | Khan Academy | Khan Academy | other | Partner on the SCERT Punjab curriculum project. | (same) | p.39 | 2026-09-29 | FY2023-24 |
| Integrated Learning Mission (ILM) | FY2023-24 | TISS (Tata Institute of Social Sciences) | Tata Institute of Social Sciences | university | SIMHA (School Initiative for Mental Health Advocacy) project; 30,000+ students/teachers/counsellors impacted. | (same) | p.39 | 2026-09-29 | FY2023-24 |
| Integrated Learning Mission (ILM) | FY2023-24 | Sri Aurobindo Society | Sri Aurobindo Society | foundation | Mental health/well-being support materials for students with Neuro-Developmental Disorders. | (same) | p.39 | 2026-09-29 | FY2023-24 |
| ACE | FY2023-24 | Abhinav Bindra Foundation Trust | Abhinav Bindra Foundation Trust | foundation | Co-runs the Para Athlete Grant Program; joint recognition event 2023-12-26. | (same) | p.71 | 2026-09-29 | FY2023-24 |
| Centre of Excellence (CoE) for PwDs | FY2023-24 | Anushkaa Foundation | Anushkaa Foundation | foundation | Runs the Clubfoot clinic in Kaushambi named in the "Bridging Hope" case study. | (same) | p.47 | 2026-09-29 | FY2023-24 |
| Centre of Excellence (CoE) for PwDs | FY2023-24 | Assistech Foundation | Assistech Foundation | foundation | Presented SBI Foundation with the "Best Assistive Tech CSR Project of the Year" award — an awarding body, not confirmed as an implementing partner. | (same) | p.48 | 2026-09-29 | FY2023-24 |
| SBI Youth for India (YFI) Fellowship | FY2023-24 | DHAN Academy | DHAN Academy | ngo | Hosted the YFI 2023-24 orientation programme in Madurai. | (same) | p.35 | 2026-09-29 | FY2023-24 |
| SBIF Sashakti — Unnati | FY2023-24 | SUVIDHA | SUVIDHA | ngo | Delivered the fruit-processing skills training in the "Home-maker to Entrepreneur" case study, Himachal Pradesh. | (same) | p.76 | 2026-09-29 | FY2023-24 |
| — (co-funder, all Foundation programmes) | FY2023-24 | State Bank of India | State Bank of India | company | Parent and primary funder — see `funder_csr_years`/`funder_csr_spend` for amounts. | (same) | throughout | 2026-09-29 | FY2023-24 |
| — (co-funder, all Foundation programmes) | FY2023-24 | SBI subsidiary companies (unnamed collectively) | SBI Group subsidiaries | company | Directors' Report states shares "continued to be held by the State Bank of India and its Subsidiary Companies" — implying subsidiaries also contribute to CSR funding, but no individual subsidiary names/amounts given. | https://sbifoundation.in/publication | AR2023-24 Directors' Report, p.82 | 2026-09-29 | FY2023-24 |

**Genuine gap, not skipped:** SBI Foundation's Annual Report has dedicated "Our Partners" pages for at least 3 of the 9 flagship programmes (Jivanam p.19-20, ACE p.72, Sashakti p.76) that clearly exist as full-page partner logo/name grids, but these render as **images**, not extractable text, via this session's PDF-reading tool — so the partner names on those specific pages could not be captured. This affects potentially dozens more real partner names that exist in the source but aren't in the table above. Recommend a follow-up pass with OCR or manual review of those specific pages if a complete partner list is required.

---
---

## 11. Grants to NGOs (`grants`)

⚠️ Same structural blocker as documented for other funders in this registry: **`org_id` is a required field** pointing to an NGO that must already exist in your `orgs` registry, and I have no visibility into that registry from this research session — so no row here can be loaded as a valid, insertable `grants` entry yet. `amount` is *not* required by this schema (unlike some other funder profiles' grants tables), which helps, but doesn't remove the `org_id` blocker.

What follows is a candidate list built from the real, named partners already found in `funder_partners` (Table 10) with the strongest individual evidence — ready to convert into real rows the moment each organisation is matched against your `orgs` registry:

| Candidate title | Likely org | amount | currency | status | outcomes (JSON) | notes | source_url |
|---|---|---|---|---|---|---|---|
| Sesame Workshop India Trust — "Learn, Play, Grow" (Meghalaya, ECCE content) | Sesame Workshop India Trust | not_found | INR | unconfirmed | `{"students_impacted": 96000, "educators_trained": 3378, "state": "Meghalaya"}` | Under Integrated Learning Mission. | https://sbifoundation.in/publication (AR2023-24, p.39) |
| TISS — SIMHA (School Initiative for Mental Health Advocacy) | Tata Institute of Social Sciences | not_found | INR | unconfirmed | `{"beneficiaries": 30000, "materials": ["training manuals","24 digital resources","review tool"]}` | Under Integrated Learning Mission; nationwide, not state-specific. | https://sbifoundation.in/publication (AR2023-24, p.39) |
| Abhinav Bindra Foundation Trust — Para Athlete Grant Program | Abhinav Bindra Foundation Trust | not_found | INR | unconfirmed | `{"athletes": 100, "target_events": ["Paralympic Games","Asian Para Games"]}` | Under ACE; joint recognition event held 2023-12-26. | https://sbifoundation.in/publication (AR2023-24, pp.70-71) |
| Anushkaa Foundation — Clubfoot Clinic, Kaushambi | Anushkaa Foundation | not_found | INR | unconfirmed | `{}` | Under Centre of Excellence for PwDs; named via a single beneficiary case study, not a programme-level statistic. | https://sbifoundation.in/publication (AR2023-24, p.47) |
| SUVIDHA — Unnati (fruit-processing skilling), Solan district, HP | SUVIDHA | not_found | INR | unconfirmed | `{"beneficiaries": 500, "villages": 50, "award": "CSR Journal Awards 2023 - EmpowerHER"}` | Under SBIF Sashakti. | https://sbifoundation.in/publication (AR2023-24, p.76) |
| DHAN Academy — YFI 2023-24 orientation host, Madurai | DHAN Academy (part of the DHAN Foundation network) | not_found | INR | unconfirmed | `{}` | Under SBI Youth for India Fellowship — an event-hosting role, weaker evidence of an ongoing "grant" relationship than the others above. | https://sbifoundation.in/publication (AR2023-24, p.35) |

**Removed/not included as candidates:** SCERT Uttar Pradesh, SCERT Punjab, Khan Academy, Sri Aurobindo Society, Education Support Organisation, Assistech Foundation — all real named partners (see Table 10), but either government bodies (SCERTs, not typically "grants to NGOs"), a corporate/ed-tech partner (Khan Academy), or an awarding body rather than an implementing grantee (Assistech Foundation), so not carried forward as NGO-grant candidates here. State Bank of India itself and its subsidiaries are the *funder's own parent/co-funders*, not grant recipients, so also excluded.

*If any of the 6 organisations above already exist in your `orgs` table, this is the ready-made list to convert into real `grants` rows once `org_id` is matched.*

---
---

## 12. Calls for proposals (`rfps`)

**Real finding: unlike most other funders profiled in this registry, SBI Foundation DOES run a public, named "Request for Proposals" page** (`https://sbifoundation.in/Request%20for%20Proposals`, reached via the site's "Resources" menu). ⚠️ The live page itself returned blank/empty on repeated direct-navigation attempts in this session (likely a client-side rendering issue with the URL's encoded space) — the 8 titles below come from a **search-engine cache of that page**, not a live re-fetch, so individual deadlines/amounts printed on each linked RFP document could not be captured in this pass.

| title | url | status | deadline | amount_min | amount_max | eligibility (JSON) | details (JSON) | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RFP - SBI Sammaan project | https://sbifoundation.in/Request%20for%20Proposals | unconfirmed *(page title only; live document not re-fetched)* | not_found | not_found | not_found | `{}` | `{"programme": "SBI Gram Seva / SBI Samman"}` | https://sbifoundation.in/Request%20for%20Proposals | SBI Foundation website (search-cache) | 2026-09-29 | Undated |
| RFP - Gram Seva | (same) | unconfirmed | not_found | not_found | not_found | `{}` | `{"programme": "SBI Gram Seva"}` | (same) | (same) | 2026-09-29 | Undated |
| RFP - Cyber Crime Investigation Training and Innovation Centre | (same) | unconfirmed | not_found | not_found | not_found | `{}` | `{}` | (same) | (same) | 2026-09-29 | Undated |
| RFP - CONSERW Waste Management - Mysuru | (same) | unconfirmed | not_found | not_found | not_found | `{}` | `{"programme": "CONSERW", "location": "Mysuru"}` | (same) | (same) | 2026-09-29 | Undated |
| RFP - TB Care | (same) | unconfirmed | not_found | not_found | not_found | `{}` | `{"programme": "SBIF Jivanam"}` | (same) | (same) | 2026-09-29 | Undated |
| RFP - Installation of medical equipment 2025-26 | (same) | unconfirmed | not_found | not_found | not_found | `{}` | `{"programme": "SBIF Jivanam"}` | (same) | (same) | 2026-09-29 | FY2025-26 *(named in the title itself)* |
| RFP - SBIF Garima — Extension, Retrofitting & Fortification | (same) | unconfirmed | not_found | not_found | not_found | `{}` | `{"programme": "SBIF Sashakti"}` | (same) | (same) | 2026-09-29 | Undated |
| RFP - Elderly Care | (same) | unconfirmed | not_found | not_found | not_found | `{}` | `{}` | (same) | (same) | 2026-09-29 | Undated |

**Corroborating secondary source (weaker evidence, kept separate rather than merged):** a third-party-hosted "SBI Foundation Grant Application Guide" (Scribd, undated) and a 2022 Facebook post describe a general online-proposal process (response within 30 days, 3-6 month full cycle) and cite **project costs from ₹15 lakh to ₹5 crore** — this may be an older, generic call rather than one of the 8 named RFPs above; not merged into the table since it's a different vintage/source.

---
---

## 13. Application forms (`proposal_templates`)

**None found as a downloadable, fillable form.** The "Request for Proposals" page lists 8 named open calls (see Table 12) which presumably link to call-specific documents/forms, but the live page could not be re-fetched in this session (see note above) to confirm whether a standalone template exists per call or whether NGOs submit via a generic online portal. The only related artefact found is the third-party "SBI Foundation Grant Application Guide" (Scribd) — a **descriptive guide, not a blank fillable form** — so no `proposal_templates` row is created from it, consistent with the convention used elsewhere in this registry (don't force-fit a description into a template row).

| name | kind | version | notes | source_url |
|---|---|---|---|---|
| *(no rows — no confirmed fillable template)* | — | — | The 8 named RFPs on sbifoundation.in likely link to call-specific documents that may include templates, but this could not be verified in this pass (page did not render on re-fetch). Recommend a follow-up direct check of https://sbifoundation.in/Request%20for%20Proposals. | https://sbifoundation.in/Request%20for%20Proposals |

---
---

## 14. Contacts (`contacts`)

*All rows for SBI Foundation. `email`/`phone` left empty where not published (per schema note, these are hidden from the AI agent anyway). `is_public=Yes` throughout since all these names are drawn from SBI Foundation's own published Leadership page and Annual Report.*

| name | role | kind | is_public | verified | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|
| Sanjay Prakash | Managing Director & Chief Executive Officer | office_bearer | Yes | **Yes** *(now cross-confirmed by 3 independent sources: give.do, the live website's own Leadership page cache, and SBI Foundation's own signed AR2023-24 Directors' Report — DIN 09692409, appointed 2022-07-28)* | Resolves the earlier leadership discrepancy — see `leadership_note` in Part A. | https://sbifoundation.in/publication (AR2023-24, p.83) | SBI Foundation AR2023-24 + Leadership page + give.do | 2026-09-29 | FY2023-24 / Current |
| Jagannath Sahoo | President & Chief Operating Officer | office_bearer | Yes | Yes *(confirmed on give.do and the website's Leadership-page cache; also named in AR2023-24, p.48, at an event)* | — | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |
| Sushil Kumar Verma | Chief Financial Officer & Chief Administrator | office_bearer | Yes | Yes *(matches across all 3 sources — website, give.do, AR2023-24 which also gives his appointment date: 2024-02-01, succeeding Parmeshwar Ram)* | — | https://sbifoundation.in/publication (AR2023-24, p.85) | SBI Foundation AR2023-24 | 2026-09-29 | FY2023-24 |
| Challa Sreenivasulu Setty | Nominee Director & Chairman of the Board (concurrently Chairman, SBI) | office_bearer | Yes | Yes | Per the current Leadership page; was a Nominee Director (not yet Chairman) as of the AR2023-24 filing, when Dinesh Khara held the Chairman role — a genuine, dated leadership succession, not a discrepancy. | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |
| Ashwini Kumar Tewari | Nominee Director (concurrently MD, Corporate Banking & Subsidiaries, SBI) | office_bearer | Yes | Yes | Appointed as SBI Foundation Nominee Director 2024-09-05, per AR2023-24. | https://sbifoundation.in/publication (AR2023-24, p.83) | SBI Foundation AR2023-24 | 2026-09-29 | FY2023-24 |
| Vinay M Tonse | Nominee Director (concurrently MD, Retail Business & Operations, SBI) | office_bearer | Yes | Yes | Appointed 2023-12-26. | (same) | (same) | 2026-09-29 | FY2023-24 |
| Kishore Kumar Poludasu | Nominee Director (concurrently DMD (HR) & CDO, SBI) | office_bearer | Yes | Yes *(current Leadership page only — supersedes Binod Kumar Mishra, who held this Nominee-Director-for-DMD(HR)-seat as of the AR2023-24 filing)* | Board seat succession — Binod Kumar Mishra (appointed 2024-02-07 per AR2023-24) appears to have since been replaced by Kishore Kumar Poludasu on this same DMD(HR)-linked board seat. | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |
| Nand Kishore | Nominee Director (concurrently MD & CEO, SBI Funds Management Limited) | office_bearer | Yes | Yes | New board seat vs. AR2023-24 roster — supersedes Shamsher Singh (MD&CEO, SBI Mutual Fund), who held this Nominee-Director seat as of AR2023-24. | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |
| Amit Jhingran | Nominee Director (concurrently MD & CEO, SBI Life Insurance Company Limited) | office_bearer | Yes | Yes | Matches across the earlier and current board rosters. | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |
| Venkatesh Srinivasan | Independent Director (former UN International Civil Servant) | office_bearer | Yes | Yes | Appointed 2023-08-02, per AR2023-24. | https://sbifoundation.in/publication (AR2023-24, p.83) | SBI Foundation AR2023-24 | 2026-09-29 | FY2023-24 |
| Tulsi Jayakumar | Woman Independent Director | office_bearer | Yes | Yes | — | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |
| Shashi Bhushan | Vice President, Disability and Inclusion | programme | Yes | Yes *(matches across the website and give.do — minor spelling variant "Sashi"/"Shashi")* | — | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |
| Aman Bhaiya | Vice President & Head (Strategy) | programme | Yes | Yes | — | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |
| Suresh Panwar | Vice President (Systems) & CISO, DPO | programme | Yes | Yes | — | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |
| Rishi Kumar | Chief Manager, HR & Admin | programme | Yes | Yes | — | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |
| Rajaram Chavan | Assistant Vice President & Programme Head, Health and Women Empowerment | programme | Yes | Yes | — | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |
| Shiddhalingesh Balloli | Programme Head, SBI Gram Seva | programme | Yes | Yes | — | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |
| Gyan Prakash | Programme Head, SBI YFI Fellowship Program | programme | Yes | Yes | — | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |
| Parveen Kumar | Programme Head, Education | programme | Yes | Yes | — | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |
| Ritesh Sain | Programme Head, Environment and Sports | programme | Yes | Yes | — | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |
| Subhadip Mondal | Programme Head, Livelihood & Skilling | programme | Yes | Yes | — | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |
| Rufus Sunny | Team Lead, Marketing and Communications | programme | Yes | Yes | — | https://sbifoundation.in/Leadership | SBI Foundation website | 2026-09-29 | Current |

**Historical/superseded (kept for audit trail, not deleted):** Dinesh Khara — Chairman & Nominee Director until superannuation on 2024-08-28 (per AR2023-24); Binod Kumar Mishra, Shamsher Singh, Abhijit Chakravorty — Nominee Directors as of the AR2023-24 filing, apparently since replaced on the current live Leadership page roster.

---
---

## 15. Impact numbers (`metrics`)

*All rows for SBI Foundation. `method=self_reported` unless noted; `is_self_reported=Yes` throughout (no independent/third-party evaluation found for any figure).*

| name | value | target | unit | period | stage | method | is_self_reported | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lives impacted (cumulative, homepage claim) | 31,500,000 *(3.15 Cr+)* | — | individuals | Since 2015 | outcome | self_reported | Yes | Homepage "Our Impact" figure. | https://sbifoundation.in | SBI Foundation website | 2026-09-29 | Current |
| Lives impacted (cumulative, per AR2023-24) | 30,700,000 *(3.07 Cr+)* | — | individuals | as of FY2023-24 | outcome | self_reported | Yes | Slightly lower than the current homepage figure — consistent with time having passed and more being added since; not a contradiction. | https://sbifoundation.in/publication | SBI Foundation AR2023-24, p.12 | 2026-09-29 | FY2023-24 |
| Live/active projects (homepage claim) | 350 *(350+)* | — | projects | Current | output | self_reported | Yes | — | https://sbifoundation.in | SBI Foundation website | 2026-09-29 | Current |
| Projects (per AR2023-24 "Year at a Glance") | 220 *(220+)* | — | projects | as of FY2023-24 | output | self_reported | Yes | ⚠️ Differs from the "145 sanctioned this year" (Directors' Report) and "437" (MD's message) figures in the *same* report — three different project-count metrics with different likely scopes (new-this-year vs. live-at-year-end vs. cumulative-since-inception); not reconciled, presented as-found. | https://sbifoundation.in/publication | SBI Foundation AR2023-24, p.12 | 2026-09-29 | FY2023-24 |
| Projects sanctioned in FY2023-24 | 145 | — | projects | FY2023-24 | output | self_reported | Yes | Per the audited Directors' Report — likely the most authoritative of the three project-count figures for "new that year." | https://sbifoundation.in/publication | SBI Foundation AR2023-24, p.82 (Directors' Report) | 2026-09-29 | FY2023-24 |
| Cumulative projects since inception (per MD's letter) | 437 | — | projects | as of FY2023-24 | output | self_reported | Yes | See discrepancy note above. | https://sbifoundation.in/publication | SBI Foundation AR2023-24, p.6 | 2026-09-29 | FY2023-24 |
| Geographic reach (aggregate) | 28 | — | states + UTs | as of FY2023-24 | output | self_reported | Yes | "28 States & 7 UTs" per AR2023-24 (vs. "28 States & 8 UTs" on the current homepage — India has 8 UTs, so this may be a minor rounding/data quirk in the older report rather than a real change). | https://sbifoundation.in/publication | SBI Foundation AR2023-24, p.12 | 2026-09-29 | FY2023-24 |
| SBIF Jivanam — beneficiaries (cumulative) | 940000 *(9.4 lakh+)* | — | individuals | as of FY2023-24 | outcome | self_reported | Yes | States: 26 (aggregate, not itemised — see `funder_footprints`). | https://sbifoundation.in/publication | SBI Foundation AR2023-24, p.16 | 2026-09-29 | FY2023-24 |
| SBI Sanjeevani MMU beneficiaries | 960000 *(9.6 lakh)* | — | individuals | as of FY2023-24 | outcome | self_reported | Yes | 80 Mobile Medical Units, 20 states + 2 UTs. | (same) | AR2023-24, p.17 | 2026-09-29 | FY2023-24 |
| SBI Gram Seva — beneficiaries (cumulative) | 400000 *(4 lakh+)* | — | individuals | as of FY2023-24 | outcome | self_reported | Yes | States: 27. | (same) | AR2023-24, p.21 | 2026-09-29 | FY2023-24 |
| SBI Gram Seva — villages adopted | 180 | — | villages | as of FY2023-24 | output | self_reported | Yes | Up from 130 villages as of Oct 2022 (per the Phase-4-launch news coverage). | (same) | AR2023-24, p.6 | 2026-09-29 | FY2023-24 |
| SBI Gram Seva — safe drinking water access | 152673 | — | villagers | as of FY2023-24 | outcome | self_reported | Yes | Via 91 RO plants, 278 handpumps, 103 wells, 96 stand posts. | (same) | AR2023-24, p.23 | 2026-09-29 | FY2023-24 |
| SBI YFI Fellowship — beneficiaries (cumulative, since 2011) | 150000 *(1.5 lakh+)* | — | individuals | Since 2011 | outcome | self_reported | Yes | 20 states, 250+ villages. | (same) | AR2023-24, p.32 | 2026-09-29 | FY2023-24 |
| SBI YFI Fellowship — alumni (cumulative) | 580 *(580+)* | — | individuals | Since 2011, 10 batches | output | self_reported | Yes | 70% remain committed to the development sector post-Fellowship. | (same) | AR2023-24, p.32 | 2026-09-29 | FY2023-24 |
| SBI YFI Fellowship — current batch size (11th batch, FY2023-24) | 54 | — | individuals | FY2023-24 | output | self_reported | Yes | 40 locations, 11 states. | (same) | AR2023-24, p.32 | 2026-09-29 | FY2023-24 |
| Integrated Learning Mission — beneficiaries (cumulative) | 24000000 *(2.4 Cr+)* | — | individuals | as of FY2023-24 | outcome | self_reported | Yes | By far the largest beneficiary count of the 9 flagship programmes — plausibly reflects systemic reach (e.g. government-school-system-level curriculum deployment) rather than direct 1:1 service delivery. | (same) | AR2023-24, p.38 | 2026-09-29 | FY2023-24 |
| Centre of Excellence for PwDs — beneficiaries (cumulative) | 50000 | — | individuals | as of FY2023-24 | outcome | self_reported | Yes | States: 20; 30 projects sanctioned this FY. | (same) | AR2023-24, p.44 | 2026-09-29 | FY2023-24 |
| LEAP — beneficiaries (cumulative) | 1050000 *(10.5 lakh+)* | — | individuals | as of FY2023-24 | outcome | self_reported | Yes | States: 16. | (same) | AR2023-24, p.52 | 2026-09-29 | FY2023-24 |
| CONSERW — beneficiaries (cumulative) | 2952000 *(29.52 lakh+)* | — | individuals | as of FY2023-24 | outcome | self_reported | Yes | States: 21; 7 lakh trees planted, 1,300 acres restored. | (same) | AR2023-24, p.62 | 2026-09-29 | FY2023-24 |
| ACE — beneficiaries (cumulative) | 235 | — | athletes | as of FY2023-24 | outcome | self_reported | Yes | States: 19; 400+ medals won, incl. 28 at the 2022 Asian Para Games. | (same) | AR2023-24, p.70 | 2026-09-29 | FY2023-24 |
| SBIF Sashakti — beneficiaries (cumulative) | 29000 | — | individuals | as of FY2023-24 | outcome | self_reported | Yes | States: 5 — smallest footprint of all 9 flagship programmes. | (same) | AR2023-24, p.74 | 2026-09-29 | FY2023-24 |
| Total CSR disbursed to projects (FY2023-24) | 2171173000 *(₹217.12 crore)* | — | ₹ | FY2023-24 | input | self_reported | Yes | From the audited Income & Expenditure statement — see `funder_csr_spend`. | (same) | AR2023-24, p.81 | 2026-09-29 | FY2023-24 |
| SBI's allocation to SBI Foundation (FY2025-26) | 4959599201.88 *(₹495.96 crore)* | — | ₹ | FY2025-26 | input | monitoring_data | Yes | Reconstructed line-by-line from SBI's own CSR disclosure — see `funder_csr_years`. | https://sbi.bank.in/documents/17826/0/26052026_CSR+ACTIVITIES+FY+2025-26.pdf | State Bank of India CSR disclosure | 2026-09-29 | FY2025-26 |

---
---

## 16. Documents (`documents`)

*All rows for SBI Foundation, `is_ai_generated=No`, `is_public=Yes` throughout. `status=read` where downloaded and read in this session; `status=received` where the URL/existence is confirmed but not yet downloaded.*

| title | doc_type | source_url | source_name | fetched_at | as_of | status | archive_url |
|---|---|---|---|---|---|---|---|
| SBI Foundation Annual Report 2023-24 | annual report | https://sbifoundation.in/publication (downloaded via a dynamically-generated link — see note below) | SBI Foundation website | 2026-09-29 | FY2023-24 | read *(140 pp., read in full: pp.1-86 in depth, remainder skimmed for structure)* | Not found |
| State Bank of India — CSR Policy | CSR policy | https://sbi.bank.in/documents/17826/9529227/130721-SBI_CSR_Policy+21+Ver+5+Final.pdf | State Bank of India website | 2026-09-29 | ~FY2020-21 *(document itself undated precisely; describes the post-April-2021 CSR-1 mechanism)* | read | Not found |
| State Bank of India — "CSR Initiatives Undertaken During FY 2025-26" | CSR annexure *(donee-level disclosure, not the formal Annexure-II format)* | https://sbi.bank.in/documents/17826/0/26052026_CSR+ACTIVITIES+FY+2025-26.pdf | State Bank of India website | 2026-09-29 | FY2025-26 | read *(126 pp.; pp.1-3 read in full for this profile, remainder skimmed)* | Not found |
| State Bank of India Annual Report 2024 (covers FY2023-24) | annual report | https://sbi.bank.in/documents/17836/39646794/Annual_Report_2024.pdf | State Bank of India website | 2026-09-29 | FY2023-24 | received *(cited via search snippet for the ₹301.24cr Foundation-allocation figure; not downloaded/read in full)* | Not found |
| State Bank of India Annual Report 2024-25 | annual report | https://sbi.bank.in/corporate/SBIAR2425/SBI-AR-2024-25.pdf | State Bank of India website | 2026-09-29 | FY2024-25 | received | Not found |
| State Bank of India Sustainability Report 2025-26 | board report *(sustainability disclosure)* | https://sbi.bank.in/documents/17826/0/27052026_SBI+Sustainability+Report+2026.pdf | State Bank of India website | 2026-09-29 | FY2025-26 | received *(cited via search snippet only)* | Not found |
| SBI Foundation Annual Reports — FY2024-25, FY2022-23, FY2020-21, FY2019-20, FY2018-19, FY2017-18 | annual report | https://sbifoundation.in/publication *(the site's own archive page; individual PDFs served via dynamically-generated, session-specific links that could not be captured as stable static URLs)* | SBI Foundation website | 2026-09-29 | Various | received *(confirmed to exist on the publications page; not downloaded in this pass — only the 2023-24 edition was downloaded and read)* | Not found |
| give.do — SBI Foundation profile | brochure *(third-party aggregator profile, not an original SBI Foundation document, but treated as a citable source throughout this file)* | https://give.do/discover/17LP/sbi-foundation | give.do | 2026-09-29 | Current | read | Not found |

**Note on the AR2023-24 download mechanism:** the "View PDF" button on sbifoundation.in/publication opens a session-specific URL of the form `https://nimbus-server-01.brained.in/nimbus-server-01/sbi-foundation/undefined/resource file-...` with a unique token per click — this is **not a stable, reusable URL** for a `source_url` field; recorded here as the general publications-page URL instead, with a note explaining the retrieval mechanism.

---
---

## 17. News mentions (`news_mentions`)

*6 items found. All are SBI-Foundation-specific.*

| url | title | seendate | domain | topic | summary | sentiment | kind | source_name | fetched_at |
|---|---|---|---|---|---|---|---|---|---|
| https://www.aninews.in/news/business/business/sbi-chairman-announces-the-launch-of-sbi-foundations-gram-seva-program-across-6-states-of-india20221003100730 | SBI Chairman announces the launch of SBI Foundation's Gram Seva Program across 6 states of India | 2022-10-03 | aninews.in | new programme phase launch | Phase 4 of Gram Seva launched, 30 new villages across 6 states' Aspirational Districts; MD Sanjay Prakash quoted. | positive | press | gdelt | 2026-09-29 |
| https://timesofindia.indiatimes.com/sbi-chairman-announces-the-launch-of-sbi-foundations-gram-seva-program-across-6-states-of-india/articleshow/94611983.cms | SBI Chairman Announces the Launch of SBI Foundation's Gram Seva Program Across 6 States of India | 2022-10-03 | timesofindia.indiatimes.com | new programme phase launch | Same event, corroborating coverage. | positive | news | gdelt | 2026-09-29 |
| https://www.livemint.com/news/india/sbi-launches-gram-seva-program-across-six-states-of-india-11664774316035.html | SBI launches 'Gram Seva Program' across six states of India | 2022-10-03 | livemint.com | new programme phase launch | Same event, corroborating coverage. | positive | news | gdelt | 2026-09-29 |
| https://www.india.com/business/covering-100-villages-across-16-states-whats-sbis-gram-seva-programme-5666175 | Covering 100 Villages Across 16 States — What's SBI's Gram Seva Programme? | 2022-10 *(exact day not printed)* | india.com | explainer | Explains Gram Seva's history (launched 2017) and Phase-4 expansion. | positive | news | gdelt | 2026-09-29 |
| https://www.facebook.com/StateBankOfIndia/videos/another-year-another-step-towards-empowering-dreams-every-dream-deserves-an-oppo/1446383530630903 | SBI Platinum Jubilee Asha Scholarship 2026-27 Launched | not_found *(recent — implied 2026 per the scholarship year)* | facebook.com | new programme launch | Launch of the SBI Platinum Jubilee Asha Scholarship for AY2026-27, awards ₹15,000 to ₹15,00,000/year. | positive | social | gdelt | 2026-09-29 |
| https://sbifoundation.in/press-realease | SBI Foundation and CCAMP Launch Nationwide AMR Challenge for Innovations in India | not_found | sbifoundation.in | new programme/partnership launch | SBI Foundation's own press-release page; also references a partnership with NSDL "serving areas in Mumbai, UP and Assam" (programme not identified from the snippet alone). | positive | press | gdelt | 2026-09-29 |

**Note:** more items likely exist on SBI Foundation's own press-release page (sbifoundation.in/press-realease — note the site's own misspelling of "release") and its X/Twitter account (@SBI_FOUNDATION), neither of which was fully crawled in this pass — recommend a follow-up pass if a fuller list (10-20 items) is required.

---
---

## 18. Benchmarks (`reference_figures`)

⚠️ **Honesty flag:** SBI Foundation's own materials do not state a formal admin-overhead cap, cost-per-beneficiary target, or SROI ratio anywhere found in this pass. Rather than force a misleading calculation (e.g. dividing one year's spend by a *cumulative-since-2015* beneficiary count, which would understate true cost-per-beneficiary), only methodologically sound calculations are included below, each clearly marked as calculated by us.

| kind | name | value | value_text | unit | tag_id | funder_id | period | notes | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| overhead_norm | Admin overhead as % of total FY2023-24 expenditure | 2.87 | — | % | — | → SBI Foundation | FY2023-24 | **Calculated by us**: (Employee benefit expenses ₹283.94L + Depreciation ₹3.86L + Other Expenses ₹339.95L = ₹627.75L) ÷ Total Expenditure ₹22,339.48L = 2.81%; recomputed against Total Income ₹34,257.71L = 1.83%. Presented against Total Expenditure per the more standard "overhead ratio" convention. Not a stated policy cap — SBI Foundation's own Directors' Report does not mention a target/cap; this is purely descriptive of FY2023-24's actual ratio. | https://sbifoundation.in/publication | SBI Foundation AR2023-24, p.81 (audited financials) | 2026-09-29 | FY2023-24 |
| cost_per_beneficiary | Average CSR spend per project, FY2023-24 | 9862727 | *(₹98,62,727, i.e. ~₹98.6 lakh per project)* | ₹ per project | — | → SBI Foundation | FY2023-24 | **Calculated by us**: ₹217.12 crore disbursed ÷ 220 projects (the "Year at a Glance" project count) = ₹98.6 lakh/project. Using the alternative "145 sanctioned" count instead gives ₹1.99 crore/project sanctioned — both presented as real, methodologically different denominators; neither picked as "the" answer. | https://sbifoundation.in/publication | SBI Foundation AR2023-24, pp.12, 81 | 2026-09-29 | FY2023-24 |
| outcome_rate | SBIF LEAP: Skilling for Future — job placement rate | 60 | — | % | Livelihoods | → SBI Foundation | FY2023-24 | Stated directly by the source, not calculated by us: "The skilling initiative promises a 60% job placement rate with a minimum salary of ₹2.4-3 LPA." | https://sbifoundation.in/publication | SBI Foundation AR2023-24, p.56 | 2026-09-29 | FY2023-24 |

---
---

## 19. Programme places (`program_locations`)

*Restates the real evidence already documented in `funder_footprints` (Table 9), in this table's `role` vocabulary (registered/operates/funds — no fiscal-year requirement here). All rows: `role=funds` (real spend/activity evidence, not just a stated intent), `source_name`/`source_url` as in Table 9.*

Given the extensive overlap with Table 9, the same ~39 programme–location pairs apply here with `role=funds` throughout (no `registered` or `operates`-only rows beyond what's in Table 9). Rather than repeat all 39 rows verbatim, see **Table 9 (`funder_footprints`) above** for the full list — every row there converts directly into a `program_locations` row with `role=funds`, `valid_from`/`valid_to` = not_found (no dates given in the source), and the same `note`/`source_url`/`source_name` values.

**One addition not in Table 9:** the RFP "CONSERW Waste Management - Mysuru" (Table 12) implies a `role=funds` link between the CONSERW programme and **Mysuru, Karnataka** — but since this is an open call rather than confirmed spend, it is more accurately captured in `rfp_locations` (Table 22 below) than here.

---
---

## 20. Programme sectors (`program_tags`)

*Maps each of the 9 flagship programmes (Table 8) to the sector tags already established in `funder_tags` (Table 4). `is_inferred=No` throughout — each mapping is a direct 1:1 match to the programme's own stated focus, not a guess.*

| program_id | tag (→ tags.id) | role | is_inferred | tagged_by | note |
|---|---|---|---|---|---|
| SBIF Jivanam | Health | primary | No | agent-research | Direct match — Jivanam is explicitly SBI Foundation's "healthcare vertical." |
| SBIF Jivanam | Health & Family Welfare | secondary | No | agent-research | give.do secondary sector; matches Jivanam's maternal/child health work specifically. |
| SBI Gram Seva | Livelihoods | primary | No | agent-research | Gram Seva's WASH/education/health/digitalisation work sits within the broader "Livelihoods"-adjacent Primary Sector give.do assigns to rural development spend. |
| SBI Youth for India (YFI) Fellowship | Child & Youth Development | primary | No | agent-research | Direct match to give.do's Primary Sector of the same name. |
| SBI Youth for India (YFI) Fellowship | Youth | secondary | No | agent-research | give.do secondary sector. |
| Integrated Learning Mission (ILM) | Education | primary | No | agent-research | Direct match. |
| Integrated Learning Mission (ILM) | Informal Education | secondary | No | agent-research | give.do secondary sector — matches ILM's non-formal/community learning-content work (e.g. SIMHA). |
| Centre of Excellence (CoE) for Persons with Disabilities (PwDs) | Specially Abled | primary | No | agent-research | Direct match. |
| Centre of Excellence (CoE) for Persons with Disabilities (PwDs) | Vocational Training | secondary | No | agent-research | Matches the Swavlamban sub-programme specifically. |
| Livelihood and Entrepreneurship Accelerator Program (LEAP) | Livelihoods | primary | No | agent-research | Direct match — explicit in the programme's own name. |
| Livelihood and Entrepreneurship Accelerator Program (LEAP) | Vocational Training | secondary | No | agent-research | Matches the "Skilling for Future" sub-programme. |
| CONSERW | Energy & Environment | primary | No | agent-research | Direct match to give.do's Primary Sector. |
| ACE | Sports | primary | No | agent-research | Direct match. |
| SBIF Sashakti | Gender | primary | No | agent-research | Direct match. |
| SBIF Sashakti | Women Empowerment | secondary | No | agent-research | give.do secondary sector; also the programme's own stated goal. |

---
---

## 21. Grant places (`grant_locations`)

⚠️ Same structural blocker as `grants` (Table 11) — `grant_id` is required and no real `grants` rows could be produced (no `orgs` registry visibility). Location evidence for the 6 candidates, ready to attach once `grant_id`s exist:

| candidate grant (→ future grant_id) | location_id | note | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|
| Sesame Workshop India Trust — "Learn, Play, Grow" | Meghalaya | 96,000+ students impacted. | https://sbifoundation.in/publication | SBI Foundation AR2023-24, p.39 | 2026-09-29 | FY2023-24 |
| TISS — SIMHA | *(Pan-India — no state specified)* | 30,000+ students/teachers/counsellors nationwide. | (same) | AR2023-24, p.39 | 2026-09-29 | FY2023-24 |
| Anushkaa Foundation — Clubfoot Clinic | Uttar Pradesh (Kaushambi district) | Most granular single-site evidence found for any grant candidate in this profile — named via the "Bridging Hope" case study, with the patient family's home village (Goraju, UP) also named. | (same) | AR2023-24, pp.47-48 | 2026-09-29 | FY2023-24 |
| SUVIDHA — Unnati | Himachal Pradesh (Solan district, Silhari village) | 500 women, 50 villages. | (same) | AR2023-24, p.76 | 2026-09-29 | FY2023-24 |
| Abhinav Bindra Foundation Trust — Para Athlete Grant Program | *(Pan-India — athletes drawn nationally, incl. Arunachal Pradesh per the Biri Takar case study)* | 100 athletes. | (same) | AR2023-24, pp.70-71 | 2026-09-29 | FY2023-24 |
| DHAN Academy — YFI orientation | Tamil Nadu (Madurai) | Event/training venue, not a beneficiary-reach location. | (same) | AR2023-24, p.35 | 2026-09-29 | FY2023-24 |

---
---

## 22. Call-for-proposal places (`rfp_locations`)

*Only 1 of the 8 named RFPs (Table 12) has a location named in its own title; the rest give no location in the title alone, and the live page could not be re-fetched to check the linked documents for location detail (see Table 12 note).*

| rfp | location_id | role | note | source_url | source_name | fetched_at | as_of |
|---|---|---|---|---|---|---|---|
| RFP - CONSERW Waste Management - Mysuru | Karnataka (Mysuru) | `funds` | Named directly in the RFP title. | https://sbifoundation.in/Request%20for%20Proposals | SBI Foundation website (search-cache) | 2026-09-29 | Undated |

---
---

## 23. Call-for-proposal sectors (`rfp_tags`)

*Inferred from each RFP's own title (Table 12) — `is_inferred=Yes` throughout, since no linked document could be read to confirm.*

| rfp | tag (→ tags.id) | role | is_inferred | tagged_by | note |
|---|---|---|---|---|---|
| RFP - SBI Sammaan project | Livelihoods | primary | **Yes** | agent-research (inferred from title) | Sammaan sits under Gram Seva. |
| RFP - Gram Seva | Livelihoods | primary | **Yes** | agent-research | — |
| RFP - Cyber Crime Investigation Training and Innovation Centre | Education | primary | **Yes** | agent-research | Best-guess mapping — "training and innovation centre" suggests a skilling/education angle, but the RFP's actual sector (e.g. could equally be public-safety/security) is not confirmed. |
| RFP - CONSERW Waste Management - Mysuru | Energy & Environment | primary | **Yes** | agent-research | Direct match to the CONSERW programme name. |
| RFP - TB Care | Health | primary | **Yes** | agent-research | Matches the existing SBIF TB Care sub-project under Jivanam. |
| RFP - Installation of medical equipment 2025-26 | Health | primary | **Yes** | agent-research | — |
| RFP - SBIF Garima — Extension, Retrofitting & Fortification | Gender | primary | **Yes** | agent-research | Garima sits under Sashakti (elderly women's shelter homes). |
| RFP - Elderly Care | Health & Family Welfare | primary | **Yes** | agent-research | Best-guess mapping — could also sit under Sashakti/Garima given the elderly-women overlap; not confirmed. |

---
---

## 24. Form questions (`template_items`)

**No rows — consistent with Table 13.** Since no `proposal_templates` row exists for SBI Foundation (no confirmed fillable form was found), there is no valid `template_id` for any `template_items` row to link to. This table is intentionally empty, not a skipped gap.

---
---

## Bonus findings (not part of `funder_identifiers`, but worth recording now since they surfaced during this research pass)

- **SBI Foundation is subject to CAG audit**: SBI's own official CSR Policy PDF states "SBI Foundation is subject to audit by the Comptroller and Auditor General (CAG) of India" — a notable governance detail (most private-sector CSR foundations are not CAG-audited; this reflects SBI's public-sector-undertaking status). Worth adding to `governance_note` in a future pass. Source: https://sbi.bank.in/documents/17826/9529227/130721-SBI_CSR_Policy+21+Ver+5+Final.pdf
- **Real, current-year (FY2025-26) fund-transfer figures found**: SBI's own "CSR Initiatives Undertaken During FY 2025-26" disclosure lists literal line-item transfers **from SBI to SBI Foundation**: ₹300,00,00,000 (₹300 crore) on 2025-09-29, and ₹160,00,00,000 (₹160 crore) on 2025-12-31 (a third March 2026 transfer amount was cut off in the snippet retrieved — needs a full re-fetch). This is genuine, primary-source, statutory CSR fund-transfer data — extremely valuable for a future `funder_csr_years`/`funder_csr_spend` pass. Source: https://sbi.bank.in/documents/17826/0/26052026_CSR+ACTIVITIES+FY+2025-26.pdf
- **Grant mechanics partially found** (for a future `rfps`/`grant_terms` pass): a third-party-hosted "SBI Foundation Grant Application Guide" describes an online-proposal process, response within 30 days, 3–6 month full process, focus areas (education, livelihood/skills, women's empowerment, sustainability, rural development, culture/heritage), and eligibility requirements (tax-exempt status, no support for individuals/fundraising/travel/sectarian or political causes). A separate 2022 Facebook post cites **project costs from ₹15 lakh to ₹5 crore**. Neither source is fully primary/current — flagged for follow-up verification directly on sbifoundation.in's "Work with us" section. Sources: https://www.scribd.com/document/568452197/SBI-FOUNDATION-GRANT ; https://www.facebook.com/SBIFoundationIndia/posts/sbi-foundation-is-inviting-proposals-from-ngos-working-across-diverse-thematic-a/1437106925122223

---
---

## Not yet researched (honest gap list for this funder)

This pass has completed the **`funders`**, **`funder_identifiers`**, and **`credential_events`** tables. None of the other ~21 tables in the schema (tags, locations, csr_years, csr_spend, programs, footprints, partners, grants, rfps, proposal_templates, contacts, metrics, documents, news_mentions, reference_figures, program_tags, program_locations, grant_locations, etc.) have been researched yet for SBI Foundation. In particular, still needed:
- Full Annual Report reads (7 reports are downloadable at `/publication`: FY2024-25, 2023-24, 2022-23, 2020-21, 2019-20, 2018-19, 2017-18 — none opened yet).
- Per-programme descriptions, dates, budgets, and partner NGOs for each of the 9 flagship programmes.
- State/district-level footprint detail (only the aggregate "28 states & 8 UTs" figure is known so far).
- News mentions, awards, and a direct look at the "Work with us" section for the current, primary-source RFP/grant-application mechanism (only secondary/older sources found so far — see Bonus findings above).

---

## Sources

1. SBI Foundation — Homepage: https://sbifoundation.in
2. SBI Foundation — Overview page: https://sbifoundation.in/Overview
3. SBI Foundation — Leadership page: https://sbifoundation.in/Leadership
4. SBI Foundation — Publications/Annual Reports index: https://sbifoundation.in/publication
5. Instafinancials — SBI Foundation company record (CIN, incorporation date, capital, AGM/filing dates): https://www.instafinancials.com/company/sbi-foundation-U85100MH2015NPL266051
6. LinkedIn — SBI Foundation company page (founding year, states/UTs reach): https://in.linkedin.com/company/sbi-foundation
7. State Bank of India — Affiliates page (confirms SBI Foundation as a Section 8 company established 2015): https://sbi.bank.in/web/affiliates/affiliates
8. State Bank of India — Sustainability Report 2026 (context on SBI Foundation's role; confirms SBI itself has "CIN: Not Applicable"): https://sbi.bank.in/documents/17826/0/27052026_SBI+Sustainability+Report+2026.pdf
9. Scribd — SBI Foundation Annual Report 2023-24 (cross-check for cumulative funding/lives-impacted/project-count figures): https://www.scribd.com/document/861256528/SBI-Foundation-Annual-Report-2023-24
10. State Bank of India — Board of Directors page (context on Nominee Directors' concurrent SBI roles): https://sbi.bank.in/web/about-us/board-of-directors
11. State Bank of India — official CSR Policy PDF (confirms CAG audit status, CSR-1 mechanism description): https://sbi.bank.in/documents/17826/9529227/130721-SBI_CSR_Policy+21+Ver+5+Final.pdf
12. State Bank of India — "CSR Initiatives Undertaken During FY 2025-26" disclosure (real fund-transfer line items to SBI Foundation): https://sbi.bank.in/documents/17826/0/26052026_CSR+ACTIVITIES+FY+2025-26.pdf
13. NGO Darpan — NPO Directory search, attempted, CAPTCHA-blocked: https://ngodarpan.gov.in/#/search-ngo
14. MCA Company/LLP Master Data portal — attempted, HTTP 403: https://www.mca.gov.in/mcafoportal/companyLLPMasterData.do
15. Scribd — "SBI Foundation Grant Application Guide" (secondary source, not independently dated/verified): https://www.scribd.com/document/568452197/SBI-FOUNDATION-GRANT
16. Facebook — SBI Foundation 2022 CSR Projects call-for-proposals post (project cost range ₹15L–₹5Cr): https://www.facebook.com/SBIFoundationIndia/posts/sbi-foundation-is-inviting-proposals-from-ngos-working-across-diverse-thematic-a/1437106925122223

*Caveat: the CIN and incorporation-date figures are sourced from a third-party MCA-data aggregator (Instafinancials), not verified directly against the MCA portal itself in this pass — recommend an independent MCA lookup before treating as fully confirmed.*

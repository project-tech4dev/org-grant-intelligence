# Comment posted on Sangam issue #324

Context for the funder type vocabulary, the india_csr flag and the pending follow-up. Posted by the user on 13 Nov 2026.

## Foreign funders: what this issue also needs to settle

We plan to load US and European funders next, starting with OECD philanthropy data and IRS 990-PF filings. Three changes belong in this issue. Three more belong in a follow-up issue.

### Added to this issue

1. Rename `section_135_bound` to `india_csr`. True means the money counts as Section 135 spend, so the NGO needs CSR-1. False for foreign funders and for Indian companies giving voluntarily unless they report Section 135 spend. NULL is unknown.
2. The CSR-1 rule reads `india_csr` only. Delete `SECTION_135_TYPES`. Backfill true for the 15 funders typed corporate_csr or corporate_foundation, except EdelGive, which is marked for review. NULL gives a "Not judged" line.
3. Neutral corporate labels: "Corporate · run by the company" and "Corporate · through its foundation". The roll-up "CSR" becomes "Corporate". Values csr_company and csr_foundation stay.

### How foreign funders map to the nine types

| Source label (Kindora, Candid, IRS) | funder_type | Note |
|---|---|---|
| Family or independent foundation | private_foundation | |
| Operating foundation | private_foundation or other | funds_external = false |
| Faith-based foundation (US) | private_foundation | |
| European church or development agency | international_agency | |
| Community foundation, DAF sponsor, re-granting public charity | intermediary | Foreign money cannot be re-granted by an Indian intermediary (FCRA 2020) |
| Corporate (company-sponsored) foundation | csr_foundation | india_csr = false, money_origin = foreign |
| Corporate giving program | csr_company | Same flags |
| Individual or UHNI | hni | |
| Bilateral or multilateral donor | bilateral_multilateral | |
| Lotteries, other | other | |

Keep the source's own label in funders.profile as source_funder_type.

### Follow-up issue: foreign funder loading (depends on this one)

| # | Gap | Proposal |
|---|---|---|
| 1 | funder_identifiers was dropped in D2, so a US foundation's EIN has no home | Add funders.external_ids jsonb NOT NULL DEFAULT '{}', kept out of profile. A CHECK limits keys to ein, uk_charity_no, rsin, iati_org_id, oecd_donor_code. Partial unique index on ein now, one per key as each source loads. cin stays a column. |
| 2 | funder_activity.amount is INR only | Add amount_original and currency. Keep amount as the INR conversion and record the rate and its source in notes |
| 3 | fiscal_year must match FYyyyy-yy | Map each grant to the Indian year containing its payment date, or the tax year end when there is no date. Keep the original period in as_of |

Load rules: new source_key values irs_990pf and oecd_philanthropy. Thin records enter as registry_status placeholder. Funders with no India evidence stay hidden.


*This document was structured and edited with AI assistance but the frameworks, insights, and approaches presented are the author's own.*

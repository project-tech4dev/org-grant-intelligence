# Help file: Indian HNIs, family foundations and charitable trusts

## 1. Scope

Indian high net worth individuals and giving networks (hni), family and private foundations and public charitable trusts (private_foundation). money_origin is domestic. india_csr is false unless a foundation spends a company's Section 135 money, which is a csr_foundation and belongs to indian-csr.md.

## 2. Where the data lives

| source_key | Source | Access | Format | Key fields | Refresh | Licence |
|---|---|---|---|---|---|---|
| hurun_india | EdelGive Hurun India Philanthropy List: individuals who gave Rs 5 crore or more in the financial year. The 2025 edition is the 12th and lists 191 donors. A 2026 edition may be out. Press coverage: https://yourstory.com/socialstory/2025/11/shiv-nadar-family-retains-top-spot-in-edelgive-hurun-list | Manual M8 (full list from Hurun India's site) | PDF or table | Rank, name, family, foundation, donation (Rs crore), five-year total, cause, city | Each November | Check Hurun terms |
| oecd_india | OECD India family and other foundations: Annex B 2019 (Arghyam, Piramal Foundation, Rohini Nilekani Philanthropies, Independent and Public-Spirited Media Foundation), Third Edition sample (Tata Trusts, EdelGive, ATE Chandra Foundation) | seeds/ and M3, M4 | CSV, table | Name, type | Static | OECD |
| foundation_site | Foundation websites and annual reports (Azim Premji Foundation, Shiv Nadar Foundation, Tata Trusts, Rohini Nilekani Philanthropies, Piramal Foundation and others) | Automated, after the roster exists | HTML, PDF | Programmes, grants, geographies, grant disclosure | Annual | Public |
| manual_seed | seeds/domestic_oecd_annex_b_and_later.csv | In this package | CSV | Draft types | Static | n/a |

Not researched: state charity commissioners, Income Tax 12A and 80G approval lists, MCA Section 8 company data, and the Bain and Dasra India Philanthropy Report. The attached OECD report says no single body consolidates information on Indian philanthropic organisations.

## 3. How to get the data

1. Ask the user for M8. Ask for earlier years if they exist, to count list appearances.
2. Build the roster from M8 plus the OECD seeds. Deduplicate donor and foundation.
3. Enrich from foundation sites in a later phase.

## 4. Pool filter (cost only)

Keep every named donor and foundation on the source lists.

## 5. Signals and ranking

Weights are in config/weights.yaml (hni_family).

| Signal | How to compute |
|---|---|
| annual_giving_latest | Latest Hurun donation in Rs crore |
| five_year_giving_total | Hurun five-year total in Rs crore |
| list_appearances_5y | Number of the last five editions where the donor appears |
| has_named_foundation | A foundation or trust name is recorded |
| funds_ngos_externally | true if the foundation states it grants to other organisations, false if it only runs its own programmes, unknown otherwise. OECD terms: grant-making, operating, hybrid. |
| ingest_readiness | 3 public grant list with amounts, 2 programmes and geographies, 1 profile only, 0 name only |

## 6. Field extraction and Sangam mapping

| Pool field | Sangam target |
|---|---|
| Donor name as published | funders.name (hni) or alias of the foundation |
| Foundation or trust | funders.name (private_foundation) |
| Donation by year | metrics with funder_id (unit INR crore, period financial year) |
| Cause | funder_tags |
| City | funder_locations |

Store only what the list publishes: name, rank, amount, cause, foundation and city. No age, contact details, addresses or inferred attributes.

## 7. Traps

1. Hurun amounts are donations in the financial year, including giving to the donor's own institutions. They are not grants to NGOs. Keep funds_ngos_externally separate.
2. "Shiv Nadar & family" and the Shiv Nadar Foundation are one funder. "Mukesh Ambani & family" and Reliance Foundation are linked, and Reliance Foundation is already in Sangam as a corporate foundation, so mark it related, not new.
3. Rank by foundation where one exists. List only the individual when no foundation exists.
4. Financial years run April to March. Match Sangam's FYyyyy-yy labels.
5. Legal flag: a name is personal data under India's DPDP Act. The user decided named individuals from public lists are acceptable. The exemption for publicly available data is unsettled for third-party lists, so add this to the legal review.

## 8. Notes for the import agent

- Read the Hurun file and OECD seed first. Create a foundation funder and add the individual as an alias.
- Type an individual with no foundation as hni.
- Skip anything already in Sangam (Tata Trusts, Azim Premji Foundation and Caring Friends are there).

## 9. Not yet researched

Hurun's full-list access and terms, registry routes, the Bain and Dasra report.


*This document was structured and edited with AI assistance but the frameworks, insights, and approaches presented are the author's own.*

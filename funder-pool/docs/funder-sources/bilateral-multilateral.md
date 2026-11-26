# Help file: foreign governments and multilaterals

## 1. Scope

Foreign government development agencies and multilateral bodies: GIZ and KfW (Germany), FCDO (UK), JICA (Japan), AFD (France), SDC, Sida, the World Bank, ADB, UN agencies and the EU. funder_type is bilateral_multilateral. money_origin is foreign and india_csr is false.

## 2. Where the data lives

| source_key | Source | Access | Format | Key fields | Refresh | Licence |
|---|---|---|---|---|---|---|
| iati | IATI Datastore Classic, https://datastore.codeforiati.org/ , with recipient country IN. Publisher organisation types separate government and multilateral publishers. | Automated | CSV, JSON | Reporting org, participating orgs and roles, activities, transactions, sector | Continuous | Varies by publisher |
| devtracker | FCDO DevTracker, India page with IATI activity data and implementing partners, https://devtracker.fcdo.gov.uk/countries/in | Automated | CSV, XML | Programmes, partners, budgets | Current | Open data |
| giz | GIZ project data pages, https://www.giz.de/India , and the GIZ IATI publisher page, https://iatiregistry.org/publisher/about/giz . GIZ publishes project data daily and monthly IATI data through BMZ. | Automated | HTML, IATI XML | Project, commissioning party, partners | Daily and monthly | Data licence Germany, attribution |
| oecd_crs | OECD Creditor Reporting System (ODA), activity level, via the OECD Data Explorer. The OECD stopped the cloud copy of the CRS datasets in the Data Explorer on 1 Feb 2026, so confirm how to get the file. | Manual M1-style download if needed | CSV | Donor, recipient, channel of delivery, sector, commitments, disbursements | Annual | Free |
| budget_annex | Union Budget Receipt Budget annex on external assistance, https://indiabudget.gov.in/budget2024-25/doc/rec/annex13.pdf | Automated | PDF | Bilateral partners and their channels | Annual | Public |
| other | World Bank, ADB, UN agencies, EU delegation portals | Not researched | | | | |

## 3. How to get the data

1. Automated: IATI, DevTracker, GIZ and the Budget annex.
2. Try the CRS through the Data Explorer or its API. If blocked, add it to the manual request list.
3. Research the multilateral portals in Phase 6 and verify each URL before use.

## 4. Pool filter (cost only)

Keep reporting organisations with at least one activity where recipient country is India.

## 5. Signals and ranking

Weights are in config/weights.yaml (bilateral_multilateral).

| Signal | How to compute |
|---|---|
| india_usd_5y | Commitments to India over the window by default. Record the basis (commitment or disbursement) and keep the two apart. |
| ngo_channel_share | Share of India money whose channel of delivery or implementing partner is an NGO or civil society organisation. Verify the CRS channel code list. Blank where the channel is missing. |
| recency_3y | Activity in the last three years |
| activity_count | Number of India activities |
| ingest_readiness | 3 activity lines with partners and amounts, 2 sector and geography, 1 profile, 0 name only |
| evidence_quality | 2 activity-level data, 1 country totals only, 0 inferred |

## 6. Field extraction and Sangam mapping

| Pool field | Sangam target |
|---|---|
| Donor agency | funders (bilateral_multilateral) |
| Implementing agency | funders linked through parent_name, never summed with the donor |
| Activities with NGO partners | funder_activity kind partner |
| Budgets by year | metrics |

## 7. Traps

1. Donor and implementer are different entities (for example BMZ commissions and GIZ implements). Record both and link them. Never add their amounts.
2. IATI and CRS describe the same money. Do not add them. Prefer IATI for activity detail and CRS for totals.
3. Most of this money goes to governments and large partners. My judgment is that few of these funders will fund small CSOs directly, so expect low ngo_channel_share.
4. Check the status of US foreign assistance data before using it.
5. FCRA treats this money as foreign contribution. It matters for matching later.

## 8. Notes for the import agent

Read the IATI and CRS columns recorded in sources_log.csv. Write the donor as the funder and the implementer as a linked funder. Use placeholder registry_status.

## 9. Not yet researched

World Bank, ADB, UN and EU portals, the CRS channel code list and the Data Explorer API.


*This document was structured and edited with AI assistance but the frameworks, insights, and approaches presented are the author's own.*

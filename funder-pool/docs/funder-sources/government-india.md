# Help file: Indian government funders

## 1. Scope

Indian central and state agencies and schemes that fund NGOs. funder_type is government. money_origin is domestic and india_csr is false. The funder is the agency. Schemes are programmes under it.

## 2. Where the data lives

| source_key | Source | Access | Format | Key fields | Refresh | Licence |
|---|---|---|---|---|---|---|
| ngo_darpan | NGO-DARPAN (NITI Aayog) scheme directory: ministries and departments that offer grants to NGOs, with schemes and nodal officers. NGO-DARPAN does not give grants itself. https://ngodarpan.gov.in/index.php/home/about | Manual M9 (the scheme list itself was not opened) | Web table | Ministry, scheme, nodal officer | Current | Public |
| nabard | NABARD promotional funds: Farm Sector Promotion Fund, Watershed Development Fund, Tribal Development Fund, Producers Organisation Development Fund, Rural Innovation Fund and others. https://www.nabard.org/content.aspx?id=579 | Automated | HTML, PDF | Fund, objectives, eligible institutions, guidelines | Current | Public |
| parliament_qa | Lok Sabha and Rajya Sabha answers on scheme releases, for example https://eparlib.sansad.in/bitstream/123456789/2988960/1/AU168_RBXtCl.pdf | Automated per answer | PDF | State-wise and scheme-wise releases | Per session | Public |
| ministry_site | Scheme pages of ministries and bodies below | To research in Phase 5. Verify each URL. | HTML, PDF | Scheme, budget, eligibility, calls | Current | Public |

Ministries and bodies to research in Phase 5: Social Justice and Empowerment, Women and Child Development, Tribal Affairs, Health and Family Welfare, Environment, Rural Development (NRLM and state rural livelihood missions), Science and Technology, Biotechnology, Electronics and IT, Culture, DoNER, North Eastern Council, NEDFi, SIDBI. State governments follow later. Do not rank by region.

## 3. How to get the data

1. Ask the user for M9. Fetch the NABARD pages automatically.
2. Research each ministry's scheme page and record its URL in sources_log.csv before use.
3. Use Parliament answers for budget and release evidence only.

## 4. Pool filter (cost only)

Keep schemes that name NGOs or voluntary organisations as eligible, or where eligibility is unclear.

## 5. Signals and ranking

Weights are in config/weights.yaml (government_india).

| Signal | How to compute |
|---|---|
| scheme_budget | Latest budget in Rs crore |
| ngo_eligible_explicit | true only where the scheme text names NGOs or voluntary organisations |
| active_call_12m | A call or application window within twelve months |
| recurrence | Calls in at least three of the last five years |
| ingest_readiness | 3 scheme page with eligibility, amounts and process, 2 eligibility only, 1 name only, 0 unknown |

## 6. Field extraction and Sangam mapping

| Pool field | Sangam target |
|---|---|
| Agency | funders (government) |
| Scheme | programs |
| Eligibility text | documents (doc_type funder_eligibility) |
| Open call | rfps |
| State-wise releases | funder_activity kind footprint and metrics |

## 7. Traps

1. A scheme budget is the total for the scheme, not the share that reaches NGOs.
2. Central grant schemes require a Darpan ID, so recipients must be registered there.
3. Schemes get renamed and merged. Record the date and URL of each reading.
4. State schemes differ from central ones in amounts and compliance.

## 8. Notes for the import agent

Create the agency as the parent funder and add schemes as programmes. Do not create a funder per scheme.

## 9. Not yet researched

Every ministry site, North East bodies, state governments, PFMS and the Expenditure Budget.

## 10. Route as built (2026-11-25)

- ministry_site: the agencies and scheme pages read are listed in config/government_schemes.yaml. Each URL was checked on 2026-11-25. Pages are read with rules only (no LLM): NGO wording sets ngo_eligible_explicit, call wording near a year sets active_call_12m and recurrence. Pages that fail (timeouts, 403, 404) are recorded in schemes.csv and the review queue. Home pages marked roster_only only confirm that the agency exists.
- Some gov.in sites send an incomplete TLS certificate chain. The pipeline verifies certificates against the operating system trust store (the truststore package). Verification is never switched off.
- scheme_budget stays blank: no budget source has been parsed yet (Parliament answers and the budget annex are future work).
- ngo_darpan (M9): not supplied. Logged as blocked.
- parliament_qa: skipped. Answers are per question and need a chosen list first.
- fcra (M12, optional): skipped. The public dashboard lists recipient associations (NGOs), not donors, and is filtered one year and one state at a time. Its API uses client-side encryption, which the pipeline will not work around.


*This document was structured and edited with AI assistance but the frameworks, insights, and approaches presented are the author's own.*

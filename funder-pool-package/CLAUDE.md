# Funder pool: instructions for Claude Code

If this repo already has a CLAUDE.md, append this file under a heading "Funder pool" and keep the existing rules.

## Goal

Build, in this repo (org-grant-intelligence), a ranked pool of funders to India in five categories. The team uses the ranking to decide what to ingest and seed first. This is a research output. It does not load anything into Sangam.

## Categories and utilities

| Utility | Category | Help file | Draft funder_type values |
|---|---|---|---|
| western_funders | Foreign private philanthropy: foundations, corporate foundations, intermediaries, church and development agencies, lotteries | docs/funder-sources/western-funders.md | private_foundation, intermediary, csr_foundation, csr_company, international_agency, other |
| indian_csr | Indian companies and corporate foundations spending under Section 135 | docs/funder-sources/indian-csr.md | csr_company, csr_foundation |
| hni_family | Indian HNIs, family foundations and private or public charitable trusts | docs/funder-sources/hni-family-foundations.md | hni, private_foundation |
| government_india | Indian central and state agencies and schemes that fund NGOs | docs/funder-sources/government-india.md | government |
| bilateral_multilateral | Foreign government agencies and multilaterals (GIZ, FCDO, JICA, World Bank and similar) | docs/funder-sources/bilateral-multilateral.md | bilateral_multilateral |

Read docs/funder-sources/00-index.md first. Build each utility from its help file. The help files are also read by the future import agent, so keep them accurate.

## Hard rules

1. Work only in this repo. Do not clone, modify or connect to the Sangam repo or database. context/sangam-schema-notes.md describes Sangam for mapping only.
2. Plan first. Write PLAN.md and stop for approval. Stop again before any download over 1 GB, any LLM spend, and the start of each phase.
3. India giving is a signal, never a gate. A cost filter may drop funders that cannot be relevant (for example 990-PF filers with no foreign grants). Never drop a funder because its India giving is unknown.
4. Unknown is not zero. Set india_evidence_status to known_positive, known_zero or unknown. Use known_zero only where grantee-level data exists for that funder and shows no India grant.
5. Never add the same money across sources. Keep one column per source and choose india_usd_best by the source preference order in the help file. Flag funders where sources disagree by more than 50 percent.
6. Record provenance on every fact: source_key, source_url, retrieved_at, file_hash, as_of and the row reference. Write them to evidence.csv and sources_log.csv.
7. Respect robots.txt and each source's terms. Use official downloads or APIs, rate-limit, and cache. If a source blocks you, add it to manual/MANIFEST.md as a request to the user and continue with what you have. Never bypass a CAPTCHA, login or paywall.
8. Named individuals are allowed only from the public lists named in the help files. Store the name, rank, amount, cause, the foundation they give through and the city as published. Do not store age, contact details, addresses or inferred attributes.
9. Do not commit raw data. data/ is git-ignored. Commit code, config, docs and small test fixtures.
10. LLM use: rules and keyword mapping first. Use an LLM only for text that rules cannot resolve (for example grant purposes), with the cheapest suitable model, cached results and the budget in config/thresholds.yaml. Stop and ask when the budget is reached.
11. No regional weighting. Do not weight the ranking by North East or any other region. Ranking is for ingest prioritisation.
12. Do not assign final priority bands. Produce the distribution report. The user sets cutoffs after reading it.
13. If a help file is wrong or a source has changed, fix the help file and record the change in docs/funder-sources/CHANGELOG.md.

## Phases and stop points

| Phase | Work | Deliverable | Then |
|---|---|---|---|
| 0 | Read this package and the repo. Match the repo's language, layout and test conventions. Write PLAN.md with the folder layout, run commands, a source-by-source access check and a list of files you need from manual/MANIFEST.md. | PLAN.md | Stop for approval |
| 1 | Core: pool and signals schema, provenance logging, manifest checker, entity matching, scoring, config loader. | Core code with tests | Report |
| 2 | western_funders utility. | data/western/pool.csv, signals.csv, review_queue.csv, distribution_report.md | Report |
| 3 | hni_family utility. | Same outputs under data/hni_family/ | Report |
| 4 | indian_csr utility. | Same under data/indian_csr/ | Report |
| 5 | government_india utility. | Same under data/government_india/ | Report |
| 6 | bilateral_multilateral utility. | Same under data/bilateral_multilateral/ | Report |
| 7 | Merge and cross-category dedupe, then the combined distribution report and the review workbook. | data/combined/pool_all.csv, ingest_queue.csv, review.xlsx | Done |

## Outputs per utility

pool.csv, signals.csv, review_queue.csv (ambiguous matches and unknowns), evidence.csv, sources_log.csv, ingest_queue.csv (ranked, excluding funders already in Sangam) and distribution_report.md. Column definitions are in schemas/pool_schema.md.

## Definition of done for a utility

1. Every acceptance check for that utility in tests/acceptance.md passes.
2. Every source in the help file is marked used, blocked (with the reason) or skipped (with the reason) in sources_log.csv.
3. The distribution report exists and shows funder counts at each threshold in config/thresholds.yaml.
4. The help file matches what the code does.

## Style

Keep status notes short. Ask a question only when blocked. Work in small steps and show a result after each.

*This document was structured and edited with AI assistance but the frameworks, insights, and approaches presented are the author's own.*

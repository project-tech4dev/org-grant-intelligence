# Funder pool package

A package of instructions, configuration and seed data for Claude Code. It builds a ranked pool of funders to India in five categories, so the team can decide what to ingest and seed first. It runs in the org-grant-intelligence repo only and writes nothing to Sangam.

## How to use it

1. In the org-grant-intelligence repo, create a branch and copy this package into the repo root. If the repo already has a CLAUDE.md, add this package's CLAUDE.md under a "Funder pool" heading.
2. Open Claude Code in the repo.
3. Paste the prompt in KICKOFF_PROMPT.md.
4. Read PLAN.md when Claude Code writes it. Approve it or send corrections.
5. Supply the files in manual/MANIFEST.md when Claude Code asks. It proceeds with partial data.
6. After each phase, read the distribution report. After the last phase, set the priority cutoffs yourself.

## What is in the package

| Path | What it is |
|---|---|
| CLAUDE.md | Master rules, phases and stop points |
| KICKOFF_PROMPT.md | The prompt to paste |
| docs/funder-sources/ | An index plus one help file per category. They tell Claude Code, and the future import agent, where data lives and how it maps to Sangam. |
| config/weights.yaml, thresholds.yaml | Ranking weights, cost filters, distribution bins. Priority bands and quotas are left for you. |
| schemas/pool_schema.md | Output column definitions and the target mapping to Sangam |
| manual/MANIFEST.md | Files you download, their names and why they are manual |
| seeds/ | Draft lists from the OECD review: domestic funders, international seed, evidence by year, and a partial list of funders already in Sangam |
| context/ | Decisions log, Sangam schema notes, research summary, the issue #324 comment, the two workbooks and the 2019 OECD report |
| tests/acceptance.md | Checks each utility must pass |
| data/ | Git-ignored output folder. The working copy (~600 MB, without the large raw downloads) is on the team Google Shared Drive; copy it here with rsync -a or cp -p |

## What you get

Per category: pool.csv, signals.csv, review_queue.csv, evidence.csv, sources_log.csv, ingest_queue.csv and distribution_report.md. Then a combined pool and a review workbook.

## What it will not do

Write to Sangam, bypass any login or CAPTCHA, assign final priority bands, weight by region, or use paid databases.

## Known gaps

I could not read the org-grant-intelligence repo when building this (the GitHub connector returned an error), so Claude Code inspects the repo in Phase 0 and adapts the layout. The seeds/sangam_existing_funders_partial.csv list is incomplete. Replace it with the export in manual/MANIFEST.md (M11).


*This document was structured and edited with AI assistance but the frameworks, insights, and approaches presented are the author's own.*

# PLAN: funder pool build (Phase 0)

Status: **awaiting approval**. Nothing has been downloaded and no code has been written. No LLM calls have been made.
Branch: `funder-pool` (local only; not committed or pushed yet).

## 1. Repo inspection and conventions

| Finding | Consequence |
|---|---|
| The repo is a monorepo of independent projects, one top-level folder each (`gdelt-monitoring/`, `hand-vetting/`, `deep-agent-app/`, `Funder/`, `ngos/`, `scripts/`) | The package lives in **`funder-pool/`**, not at the repo root. The package README would otherwise overwrite the repo's root README.md. |
| There is no root CLAUDE.md | The package CLAUDE.md stays at `funder-pool/CLAUDE.md`. I will add a short root `CLAUDE.md` with a "Funder pool" section that points to it. |
| Python is the main language (`gdelt-monitoring/*.py`; `deep-agent-app/backend` uses `requires-python >=3.11`) | Python, packaged under `funder-pool/src/funder_pool/`. |
| There is no test suite anywhere in the repo | Adding pytest is a new convention, scoped to `funder-pool/tests/`. |
| Root .gitignore covers `__pycache__`, `.DS_Store` and node_modules. `funder-pool/data/.gitignore` ignores everything under data/. | Raw downloads, manual files and outputs stay out of git (hard rule 9). I'll add `.venv/` to the ignores. |
| Python: the system `python3` is 3.15, and pandas, openpyxl and pyyaml are not installed. `python3.12` exists. | Create `funder-pool/.venv` with **Python 3.12**. Pin `requirements.txt`: pandas, openpyxl, pyyaml, requests, lxml, rapidfuzz, pdfplumber, pytest. Nothing is installed yet. |

## 2. Folder layout

```
funder-pool/
  CLAUDE.md  README.md  PLAN.md  KICKOFF_PROMPT.md
  requirements.txt  pyproject.toml          # pytest config, package metadata
  config/        weights.yaml thresholds.yaml theme_map.yaml (new, Phase 1, user reviews)
  docs/funder-sources/   help files + CHANGELOG.md
  schemas/  manual/MANIFEST.md  seeds/  context/
  src/funder_pool/
    core/        config.py  provenance.py (evidence + sources_log writers, file hashing, cache)
                 manifest.py (checks data/manual/ against MANIFEST)  matching.py (ids, name normalisation, fuzzy match -> review_queue)
                 scoring.py (percentile-within-category, unknown penalty)  fx.py (annual average rates, cached)
                 fiscal.py (FYyyyy-yy)  schema.py (column lists + validators)  report.py (distribution_report.md)
                 sangam.py (in_sangam from M11 export or partial seed; file read only, no DB)
    sources/     iati.py  irs990.py  threesixty.py  oecd.py  devtracker.py  giz.py  nabard.py  hurun.py  mca_csr.py  seeds.py
    utilities/   western.py  hni_family.py  indian_csr.py  government_india.py  bilateral_multilateral.py  combine.py
    cli.py
  tests/         acceptance.md  fixtures/  test_core_*.py  test_<utility>.py   # acceptance checks as pytest
  data/          (git-ignored) raw/<source_key>/  manual/  cache/  <utility>/  combined/
```

## 3. Run commands

```bash
cd funder-pool
python3.12 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
python -m funder_pool.cli check-manifest              # lists which M-files are present or missing
python -m funder_pool.cli fetch <source_key> [--dry-run]   # cached, hashed, rate-limited download
python -m funder_pool.cli build <utility>             # western_funders | hni_family | indian_csr | government_india | bilateral_multilateral
python -m funder_pool.cli combine                     # Phase 7: pool_all.csv, ingest_queue.csv, review.xlsx
pytest                                                # unit + acceptance checks (fixtures; plus data checks when data/ exists)
```

`build` runs only from the cache in data/raw/. That makes reruns deterministic (acceptance check 8).

## 4. Source-by-source access check (tested 25 Nov 2026, headers and robots only, no data pulled)

| source_key | URL tested | Result | Method planned | robots / terms | Notes |
|---|---|---|---|---|---|
| iati | datastore.codeforiati.org/api/1/access/activity.csv?recipient-country=IN | 200, CSV returned | API, paged, cached | No robots.txt; publisher licences vary and are recorded per row | Used by both western_funders (non-government publishers) and bilateral_multilateral (government and multilateral publishers). Routed by reporting-org-type code. |
| irs_990pf / irs_990_sched_f | irs.gov form-990-series-downloads | 200; 53 monthly zips listed for 2021 to 2026 | Download index CSV, then zips | Public domain; no robots.txt on apps.irs.gov | **Size: index_2025.csv is 93 MB, and a monthly zip is 100 to 500 MB. Five years is about 15 to 25 GB, well over the 1 GB stop.** Plan: (1) stream the yearly index CSVs (about 0.5 GB total) and filter to 990-PF plus 990s with Schedule F; (2) stream each zip, parse only matching XML members, keep the extracted grant rows and delete the zip. **Your approval is needed for the multi-GB transfer**, or supply M13 instead. Part XV element names are checked against the IRS e-file schema before parsing. |
| irs_990pf (BMF) | EO BMF extract | Not yet tested | Download (about 4 regional CSVs, under 1 GB) | Public domain | For foundation codes, so funder types can be drafted |
| threesixtygiving | grantnav.threesixtygiving.org | 200, but **robots.txt disallows /search, /recipients and /funders for all agents**, and search.csv returned 503 | **Changed route:** the 360Giving data registry (data.threesixtygiving.org) publisher files, filtered locally for India | Open licences with attribution | The help file says "search India" in GrantNav. That conflicts with robots.txt, so I will fix western-funders.md and log the change in CHANGELOG.md. |
| oecd_philanthropy (M1) | oecd-ilibrary.org | **403** | I try the direct CSV link once; if blocked, the file stays manual (M1) | OECD terms not yet read (open item) | Blocked, as the package warned |
| oecd_philanthropy (M2, M3, M5, M6) | oecd.org | Not fetched (needs a browser) | Manual | | |
| oecd_crs | OECD Data Explorer | Not tested. The cloud copy of the CRS datasets was stopped on 1 Feb 2026. | Try the SDMX API in Phase 6; otherwise manual | | IATI covers activity detail without it |
| devtracker | devtracker.fcdo.gov.uk/countries/in | 200 | HTML/IATI export, rate-limited | No robots.txt; open data | Overlaps with FCDO IATI data: dedupe by IATI identifier, never sum |
| giz | giz.de/India | 200; robots allows public pages | IATI XML through the IATI registry preferred over HTML | Data licence Germany (attribution) | Linked to BMZ as donor, never summed |
| budget_annex | indiabudget.gov.in annex13.pdf | Not tested | Download one PDF | Public | |
| nabard | nabard.org/content.aspx?id=579 | 200 | HTML + guideline PDFs | No robots.txt | |
| ngo_darpan (M9) | ngodarpan.gov.in | 200 (home page) | Manual M9 as specified; I will also check whether the scheme list is a plain public page | | |
| ministry_site, parliament_qa | various | Not tested; researched in Phase 5 | Per-page, cached | Each URL is logged before use | |
| hurun_india (M8) | n/a | Manual | | Hurun terms not checked (open item) | Names only, as published (rule 8) |
| mca_csr (M10) | csr.gov.in | Manual (CAPTCHA, never bypassed) | | | See the CSRAnalytics question in section 6 |
| oecd_india | context PDF + seeds | Local | | | Annex B is already in seeds/ |
| fcra_disclosure (M12) | fcraonline.nic.in | Not tested | Manual, optional | Public visibility unclear | |
| manual_seed | seeds/*.csv | Local | | | |

## 5. Files I need from you (manual/MANIFEST.md), ranked by what each one blocks

Save them in `funder-pool/data/manual/` with these names. Every utility still runs with partial data and logs the gaps.

| Priority | File | Blocks | Without it |
|---|---|---|---|
| 1 | **M11 sangam_funders_export.csv** (read-only export: name, aliases, funder_type, website, cin) | in_sangam for all utilities; ingest_queue | I fall back to the 33-row partial seed, so in_sangam will be incomplete |
| 2 | **M1 oecd_pp4d_crs_2023.csv** | western_funders India amounts for the 41 largest foundations; bilateral checks | Gates, IKEA, CIFF and Hewlett fall back to the seed figures in evidence_by_year.csv (enough for western acceptance check 1, but thin) |
| 3 | **M8 hurun_india_philanthropy_list_2025** (+ earlier years if possible) | hni_family (most of the pool) | hni_family holds only the roughly 8 OECD-seed foundations |
| 4 | **M10 mca_csr_export_FYyyyy-yy.csv** (last 3 FYs) | indian_csr pool filter and spend signals | indian_csr is limited to the 53 seed companies, with spend unknown |
| 5 | **M3 oecd_third_edition_annex_b.xlsx** | Roster for western, hni and csr (506 orgs) | Smaller rosters |
| 6 | **M9 ngo_darpan_schemes.xlsx** | government_india roster | NABARD + researched ministry pages only |
| 7 | M2, M4 | Third Edition amounts; 183-org domestic roster | Smaller coverage |
| — | M5, M6, M7, M12 (optional); M13 only if the IRS bulk route is not approved | | |

## 6. Decisions I need from you

1. **Location:** `funder-pool/` subfolder plus a root CLAUDE.md pointer (recommended), or the repo root as the package README says?
2. **IRS bulk download:** approve roughly 15 to 25 GB of streamed transfer, about 1 to 2 GB kept on disk after filtering (you have about 700 GB free)? Or limit it to the last 3 tax years? Or supply M13?
3. **LLM budget:** `config/thresholds.yaml` llm.budget_usd is null. It's only needed for grant purposes that the theme rules can't map. Recommendation: USD 20 with Claude Haiku, cached. Or 0, so unmapped themes stay blank.
4. **`~/Downloads/CSRAnalytics-Report-FY-2014-2025.xlsx` (72 MB)** looks like a possible stand-in for M10. Its source and licence are unknown, and it could come from a third-party aggregator. Is it an export from the National CSR Data Portal, and may I use it? I have not opened it.
5. **Sangam:** I found `~/Downloads/sangam-master` and a `.pem` key. I will **not** open either (hard rule 1). in_sangam comes only from the M11 export you supply, or the partial seed.

## 7. Phase sequence (each phase ends with a short report and a stop)

| Phase | Work | Depends on |
|---|---|---|
| 1 | Core modules + theme_map.yaml draft + tests with fixtures | Approval of this plan |
| 2 | western_funders: seeds, IATI (non-government), 360Giving registry, IRS 990-PF/Schedule F, OECD M1/M2 if present | Decisions 2 and 3; M1 and M11 preferred |
| 3 | hni_family: M8 + OECD seeds; donor and foundation merged as aliases | M8 |
| 4 | indian_csr: M10 + seed; companies and foundations linked by parent_name | M10 (or decision 4), M11 |
| 5 | government_india: NABARD, M9, ministry pages; agency is the funder, schemes are programmes | M9 preferred |
| 6 | bilateral_multilateral: IATI (government and multilateral publishers), DevTracker, GIZ, budget annex; CRS if obtainable | — |
| 7 | Combine, cross-category dedupe, review.xlsx | All prior phases |

Priority bands stay blank. You set cutoffs after reading each distribution_report.md.

## 8. Known risks

- IRS XML schema varies across years; Part XV recipient country is only in foreign-address blocks, so US-addressed grants to India-focused intermediaries are flagged `indirect` by name list, not counted.
- IATI double counting (donor + implementer publish the same activity): dedupe by iati-identifier and transaction ref; donor and implementer linked, never summed.
- FX: annual average rates need a source; plan is IMF/World Bank official annual averages, cached and recorded per evidence row.
- OECD terms of use, Hurun terms and FCRA public visibility remain open items from decisions.md.
- DPDP legal flag on named individuals is carried into the hni_family report.

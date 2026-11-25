# Output schemas

All outputs are CSV, UTF-8, one folder per utility under data/<utility>/ and a combined folder under data/combined/.

## pool.csv (one row per funder)

| Column | Meaning |
|---|---|
| funder_id | Stable internal ID (slug of the normalised name plus category). Never reuse. |
| category | One of western_funders, indian_csr, hni_family, government_india, bilateral_multilateral |
| name | Canonical name |
| aliases | Pipe-separated other names seen |
| country | Home country (ISO 3166 alpha-2) |
| website | Official site if known |
| ein, uk_charity_no, rsin, iati_org_id, oecd_donor_code, cin | External identifiers, blank if unknown |
| funder_type_draft | One of the nine values in docs/funder-sources/00-index.md |
| money_origin_draft | foreign, domestic, mixed or unknown |
| india_csr_draft | true, false or review. True only where the money counts as Section 135 spend. |
| parent_name | Parent organisation, for example the company behind a corporate foundation |
| in_sangam | yes, related or no. Computed from manual/sangam_funders_export.csv, or from seeds/sangam_existing_funders_partial.csv if the export is missing. |
| sources | Pipe-separated source_key values that name this funder |
| notes | Free text |

## signals.csv (one row per funder)

| Column | Meaning |
|---|---|
| funder_id | Join key |
| india_evidence_status | known_positive, known_zero or unknown |
| india_usd_5y, india_usd_3y | India giving in USD over the windows in config/thresholds.yaml. Blank if unknown. |
| india_inr_crore_5y | For Indian sources that report in rupees |
| india_grants_count_5y | Number of India grants or activities |
| india_recipients_distinct_5y | Distinct Indian recipients |
| total_giving_usd_5y | All-country giving where the source gives it |
| india_share | india_usd_5y divided by total_giving_usd_5y, blank if either is blank |
| funds_ngos_share | Share of India money going to non-government recipients, blank if unknown |
| last_india_year | Most recent year with India giving |
| themes | Up to three themes (Schedule VII top level or OECD sector mapped) |
| india_usd_by_source | JSON of per-source India USD, never summed |
| source_preference_used | Source behind india_usd_best |
| india_usd_best | Value chosen by the help file's preference order |
| sources_disagree | true if sources differ by more than 50 percent |
| ingest_readiness | 0 names only, 1 profile fields, 2 programme or theme plus geography, 3 grantee-level lines with amounts |
| unknown_signals | Pipe-separated signals that were unknown when scored |
| score_total | Weighted percentile score from config/weights.yaml |
| rank_in_category | 1 is highest |
| priority_band | Always blank. The user sets it later. |

Category-specific signals (for example csr_spend_3y_average, annual_giving_latest, scheme_budget) are added as extra columns and named in the help files.

## review_queue.csv

funder_id, issue (ambiguous_match, unknown_india, intermediary, source_disagree, classification), candidates (pipe-separated), suggested_action, decision (blank for the user).

## evidence.csv (one row per dated fact)

funder_id, year_or_period, measure, amount, currency, amount_usd, fx_rate, fx_source, basis (disbursed, committed, estimate), recipient_name, recipient_country, recipient_state, purpose_text, source_key, source_url, retrieved_at, file_hash, row_ref.

## sources_log.csv (one row per source run)

source_key, source_name, url, access_method (api, download, manual_file), status (used, blocked, skipped), reason, retrieved_at, file_hash, rows_read, terms_checked (yes or no), notes.

## ingest_queue.csv

funder_id, category, name, rank_in_category, score_total, in_sangam, ingest_readiness, india_evidence_status, notes. Excludes funders already in Sangam (in_sangam = yes). Related funders stay in the queue with a note.

## distribution_report.md

For each utility: funder counts at each bin in config/thresholds.yaml, counts by india_evidence_status, counts by ingest_readiness, the top 25 by score, and the 25 largest unknowns by total giving.

## Target mapping to Sangam (documentation only)

| Pool field | Sangam target |
|---|---|
| name, aliases, website, parent_name | funders.name, aliases, website, parent_id |
| funder_type_draft | funders.funder_type (pending issue #324) |
| india_csr_draft | funders.india_csr (renamed from section_135_bound in #324) |
| money_origin_draft | funders.money_origin (pending #324) |
| ein and other identifiers | funders.external_ids (pending follow-up issue) |
| evidence rows for a recipient | funder_activity kind partner (amount in INR, fiscal_year as FYyyyy-yy, original period in as_of) |
| funding by state or district | funder_activity kind footprint |
| giving totals | metrics with funder_id |
| schemes and programmes | programs |
| eligibility text | documents |
| open calls | rfps |
| ambiguous recipients | resolution_queue |

Write none of these. They are for the import agent later.


*This document was structured and edited with AI assistance but the frameworks, insights, and approaches presented are the author's own.*

# Sangam schema notes (for mapping only)

Read from the Sangam repo (project-tech4dev/sangam) on 13 Nov 2026: db/init/02_schema.sql, migrations to 0056 and the funder consolidation spec. It may have drifted. Do not connect to Sangam. These notes tell you what the import agent will later expect.

## funders

Columns of note: name, slug, aliases (text array), cin (unique, corporate funders), funder_type (free text today; nine values proposed in issue #324), section_135_bound (to be renamed india_csr in #324), money_origin (proposed), registry_status (placeholder, in_vetting, full_profile, hidden), parent_id, website, profile (jsonb for leftovers), intake_mode, funds_external, typical_duration_months, grant_size_min and grant_size_max (INR), and provenance columns (source_url, source_name, fetched_at, content_hash, extractor_version, as_of, archive_url).

No identifier table exists for EIN, UK charity number, RSIN or IATI ID. A funders.external_ids jsonb column is proposed in a follow-up to #324.

## funder_activity

One row per fact, by kind: spend, footprint, partner, programme. Foreign grants to Indian NGOs fit kind partner with partner_name, partner_kind ngo, partner_org_id only if the NGO is in the orgs registry, amount, fiscal_year, as_of, source_key, source_url, fetched_at.

Constraints: amount is INR only with no currency column (an amount_original and currency pair is proposed). fiscal_year must match FYyyyy-yy (April to March).

## Other tables the import agent uses

metrics (funder_id, unit, period), funder_tags and taxonomy tags (cells carry OECD CRS codes in meta.refs), funder_locations, programs, documents (doc_type funder_eligibility), rfps, resolution_queue (entity kinds org, funder, location, partner), ingest_runs and ingest_run_items.

Provenance is on every fact row, so no separate evidence table is needed in Sangam.

## Pending in issue #324

Funder type vocabulary, money_origin, the india_csr rename, the CSR-1 rule reading india_csr only, and neutral corporate labels. Foreign funders load only after it merges.


*This document was structured and edited with AI assistance but the frameworks, insights, and approaches presented are the author's own.*

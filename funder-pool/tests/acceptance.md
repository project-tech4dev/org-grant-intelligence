# Acceptance checks

Run these per utility before reporting a phase as done. Put them in the repo's test suite where possible, with small fixtures.

## All utilities

1. No duplicate funder_id. No two rows share an identifier (ein, uk_charity_no, rsin, iati_org_id, cin).
2. Every row in evidence.csv has source_key, source_url, retrieved_at and file_hash.
3. india_evidence_status is one of the three allowed values. known_zero rows have grantee-level source data recorded.
4. No funder was dropped because India giving was unknown. The drop log lists only cost-filter reasons.
5. priority_band is blank in every output.
6. No code path imports, calls or connects to the Sangam repo or database.
7. No contact details, addresses or ages appear in any output.
8. Rerunning the utility from cached downloads gives identical output.
9. Funders already in Sangam (yes) are excluded from ingest_queue.csv and kept in pool.csv.

## western_funders

1. The pool contains the Gates Foundation, IKEA Foundation, CIFF and the Hewlett Foundation, each with India evidence known_positive.
2. india_usd_by_source never sums sources. sources_disagree is set when two sources differ by more than 50 percent.
3. Grants to known US intermediaries (American India Foundation, Give2Asia, Charities Aid Foundation America, Tides Foundation, GlobalGiving Foundation) appear as indirect and are not counted as India giving.
4. Rows tagged "Developing countries, unspecified" are not counted as India.
5. A sample of 20 990-PF grants was checked by hand against the XML.

## indian_csr

1. A company is in the pool only if it has CSR spend in the last three financial years.
2. Companies and their foundations are linked through parent_name.
3. HDFC Bank, ITC and TCS show in_sangam yes. Axis Bank, Infosys, Reliance and Tata Steel show related.
4. india_csr_draft is true for every row.

## hni_family

1. The 2025 Hurun list gives 191 donors or the count in the file you were given. Report any difference.
2. A donor and the foundation they give through are one funder with an alias, not two.
3. Output rows hold no age, contact details or address.

## government_india

1. Every scheme row has an agency parent and the source page it came from.
2. ngo_eligible_explicit is true only where the scheme text names NGOs or voluntary organisations.

## bilateral_multilateral

1. Implementing agencies and donors are linked (for example GIZ with its donor ministry) and never summed together.
2. CRS and IATI amounts are never added.
3. ngo_channel_share is blank, not zero, where the channel of delivery is missing.


*This document was structured and edited with AI assistance but the frameworks, insights, and approaches presented are the author's own.*

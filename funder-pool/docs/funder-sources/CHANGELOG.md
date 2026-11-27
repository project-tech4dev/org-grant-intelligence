# Changelog for the help files

Record every correction here: date, file, what changed, why.

| Date | File | Change | Why |
|---|---|---|---|
| 2026-11-13 | all | Initial version | Built from the Sangam and Kindora comparison, the OECD review workbook and the sources index |
| 2026-11-25 | western-funders.md | 360Giving route changed from GrantNav search to the data registry publisher files | GrantNav robots.txt disallows /search, /funders and /recipients for all agents (checked 2026-11-25) |
| 2026-11-25 | western-funders.md (via config) | IRS 990 XML downloaded by the user with scripts/download_irs.sh, not by the pipeline | ~19 GB for filing years 2022-2026, over the 1 GB stop; user chose to download |
| 2026-11-25 | indian-csr.md | M10 is read as the Dynamic CSR Report project-level export (company spend = sum of project rows); a CSRAnalytics xlsx is a fallback | The format the user supplied |
| 2026-11-25 | indian-csr.md, hni-family-foundations.md, western-funders.md | M3 is extracted from the Third Edition report PDF (Annex B, 556 rows not 506); M4 has no organisation annex | The web table did not load; the PDF has it |
| 2026-11-25 | western-funders.md | China and Mexico Annex B rows from national domestic data (col C = No) are dropped as a cost filter | They report no cross-border giving |
| 2026-11-25 | western-funders.md | 360Giving India filter, FX, text-only mentions to review, UK public bodies out of scope; theme overrides file | Implementation detail the import agent needs |
| 2026-11-25 | hni-family-foundations.md | M8 supplied as an HTML shell with no list: logged as blocked; M11 family trusts and private foundations used | The page loads its table by script |
| 2026-11-25 | government-india.md | Agency and scheme pages listed in config/government_schemes.yaml; rule-based reading; truststore for incomplete gov.in certificate chains; M9 blocked; parliament_qa and fcra skipped | Phase 5 research; FCRA dashboard lists recipients and encrypts its API |
| 2026-11-25 | hni-family-foundations.md | hurun_india read from PDF printouts (2024, 2025, 2026 and the 2024 women list) through an in-session transcription (data/manual/hurun_transcribed.csv); featured tables only, so appearances and amounts are lower bounds; donor-to-foundation resolution rules | User supplied the Hurun web articles as PDFs; the 2026 tables are images |
| 2026-11-25 | hni-family-foundations.md, western-funders.md | Sangam private_foundation rows with a foreign legal form are routed from hni_family to western_funders | Paul Hamlyn Foundation and Stiftung Childaid Network were in hni_family |
| 2026-11-25 | hni-family-foundations.md | Hurun donor resolution: corporate-vehicle prefix and "Group" rules, fuzzy vehicle match, token-containment donor merge; latest amount from the latest edition that has one | Duplicates (Chittilappilly, Bagchi, Surana) and corporate vehicles typed as private foundations in the first Hurun build |
| 2026-11-26 | western-funders.md | irs_990pf built (990-PF Part XV from TEOS XML, foreign-address filter, India = CountryCd IN, known_zero for filers with foreign grants but none to India); BMF row given its own key irs_bmf and logged skipped; element names confirmed | IRS bulk files downloaded |
| 2026-11-26 | western-funders.md | IRS name matching: spacing-free exact match; fuzzy duplicates queued only when names agree beyond philanthropy words (same rule in the combine step's cross-category check); Deflate64 zips read with system unzip | 647 noisy duplicate queue items and 118 cross-category pairs on the first full IRS build; Wal-Mart Foundation not merged |
| 2026-11-26 | western-funders.md | 990-PF grants to individuals (RecipientPersonNm) stored as 'individual recipient' with no name, city or province; 964 India grant purposes the keyword rules could not map classified once in-session and stored in config/theme_overrides.csv (990:{object_id}:{grant_no}) | Rule 8: individual recipients are not on a named public list |
| 2026-11-26 | 00-index.md | Added the export for the ingest agent (scripts/export_for_ingest.py, data/export/<date>/ with MANIFEST.json) | Lets the Sangam ingest agent reuse parsed IRS 990-PF, IATI and OECD data instead of downloading again |
| 2026-11-27 | (all categories) in_sangam matching | Sangam aliases split on ';' (commas kept inside an alias); a short Sangam alias no longer matches by initials or parenthetical; a company name with a legal-form suffix does not match a bare acronym alias. indian_csr in_sangam yes fell from 1,523 to 23 | 1,385 companies matched 'J.P. Morgan India' through an alias 'India' split from 'JPMorgan Chase Bank N.A., India'; others matched 'CF' (Caring Friends) and 'RF' (Reliance Foundation) by initials. They were wrongly kept out of the ingest queue |


*This document was structured and edited with AI assistance but the frameworks, insights, and approaches presented are the author's own.*

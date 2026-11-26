# Decisions log (to 13 Nov 2026)

| Decision | Detail |
|---|---|
| Where this runs | Only in the org-grant-intelligence repo. Nothing runs in the Sangam repo or against its database for now. |
| What the ranking is for | Prioritising ingest and seeding. No North East or other regional weighting. |
| Named individuals | Allowed from public lists. The user's view is that a name alone is not personal data. Legal flag: DPDP treats a name as personal data, and the publicly-available exemption is unsettled. Add to the legal review. |
| India giving | A signal, not a gate. The pool is built first. Tiers are set from the distribution afterwards. |
| Unknown versus zero | Unknown is not zero. known_zero only with grantee-level data. |
| Tier cutoffs | Not set. Config holds proposals only. |
| Funder types | The nine values proposed in Sangam issue #324. |
| india_csr | Replaces section_135_bound. True where the money counts as Section 135 spend. |
| Identifiers | A narrow external_ids store (EIN and others) is proposed in a follow-up to #324. Not yet in Sangam. |
| Currency and fiscal year | Sangam amounts are INR only and fiscal years are April to March. Original amount and period are kept in notes and as_of until columns exist. |
| Paid sources | Candid, Daanveda and Stiftungssuche are out of scope. Kindora is for spot checks only. |
| Open items | FCRA portal public visibility, OECD terms, IRS file sizes, theme mapping review, quotas per category. |


*This document was structured and edited with AI assistance but the frameworks, insights, and approaches presented are the author's own.*

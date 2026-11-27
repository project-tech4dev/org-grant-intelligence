# Manual files

Claude Code tries every automated route first. Where a source blocks automation or needs a login, ask the user for the file named here. Proceed with what you have if a file is missing, and record the gap in sources_log.csv.

Save files in data/manual/ (git-ignored) using the names below.

| # | File name | Needed by | Required? | Where to get it | Why manual |
|---|---|---|---|---|---|
| M1 | oecd_pp4d_crs_2023.csv | western_funders, bilateral_multilateral | Required | https://www.oecd-ilibrary.org/development/data/oecd-international-development-statistics/creditor-reporting-system-private-philanthropy-for-development-edition-2023_dd620077-en (CSV button, 31.34 MB). Keep global rows. | Try the official download link first. The OECD blocked automated page fetches in testing. |
| M2 | oecd_pp4d_third_edition.xlsx | western_funders | Required | https://oecd.org/development/philanthropy-centre/data (dashboard export, 2020 to 2023) | Needs a browser |
| M3 | oecd_third_edition_annex_b.xlsx | western_funders, hni_family, indian_csr | Required | https://www.oecd.org/en/publications/private-philanthropy-for-development-third-edition_98e676c0-en/full-report/sample-list-of-organisations_0435916a.html (copy the 506-organisation table) | Table did not load in testing |
| M4 | oecd_india_taking_stock_2022.pdf | indian_csr, hni_family | Required | https://www.oecd.org/en/publications/taking-stock_0c192616-en.html (look for an annex listing the 183 organisations) | PDF blocked by robots.txt |
| M5 | oecd_pp4d_second_edition.xlsx | western_funders | Optional | https://search.oecd.org/development/philanthropy-centre/researchprojects ("Download the entire dataset (.xlsx)", Second Edition) | Link not exposed to automation |
| M6 | oecd_pp4d_first_edition.xls | western_funders | Optional | Same page, First Edition | Same |
| M7 | oecd_india_private_giving_2019.xlsx | indian_csr, hni_family | Optional | Same page, India's Private Giving dataset. The 2019 PDF is already in context/. | Same |
| M8 | hurun_india_philanthropy_list_YYYY.pdf | hni_family | Required (2025 edition; earlier years optional) | Hurun India's site. Search "EdelGive Hurun India Philanthropy List 2025". A 2026 edition may exist. | Not tested |
| M9 | ngo_darpan_schemes.xlsx | government_india | Required | https://ngodarpan.gov.in/index.php/home/about (scheme list) | Not tested |
| M10 | mca_csr_export_FYyyyy-yy.csv | indian_csr | Required | National CSR Data Portal, company-wise CSR spend export | CAPTCHA |
| M11 | sangam_funders_export.csv | all | Required | Read-only export of Sangam's funders table (name, aliases, funder_type, website, cin). Replaces seeds/sangam_existing_funders_partial.csv. | Claude Code must not connect to Sangam |
| M12 | fcra_portal/ | western_funders, bilateral_multilateral | Optional | https://fcraonline.nic.in/ . The user checks what is public and downloads what is. | Not retrievable in testing; public visibility unclear |
| M13 | irs_990pf_grants.csv | western_funders | Fallback only | A filtered 990-PF extract if automated download of the IRS zips is not possible | Disk or bandwidth |

Status on 2026-11-25: M3 (extracted from the Third Edition report PDF), M4 (no organisation annex), M10 and M11 supplied and used. M8 was supplied as an HTML page with no list data: a CSV, XLSX or PDF of the table is still needed. M1, M2, M5, M6, M7 (xlsx), M9 and M12 are not supplied. For M12, the FCRA dashboard lists recipient NGOs by year and state, not donors, so it is not pursued.

Automated sources (no manual file needed): IRS Form 990 series (https://www.irs.gov/charities-non-profits/form-990-series-downloads), IATI Datastore Classic (https://datastore.codeforiati.org/), 360Giving GrantNav (https://grantnav.threesixtygiving.org/), FCDO DevTracker India (https://devtracker.fcdo.gov.uk/countries/in), GIZ project data (https://www.giz.de/India), NABARD funds page (https://www.nabard.org/content.aspx?id=579).


*This document was structured and edited with AI assistance but the frameworks, insights, and approaches presented are the author's own.*

"""OECD Private Philanthropy for Development (Third Edition), Annex B 'Sample: List of organisations' (M3).

The user supplied the full report PDF (data/manual/oecd_pp4d_third_edition_report.pdf) instead of a table export.
This module extracts Table A B.1 with `pdftotext -layout` into data/manual/oecd_third_edition_annex_b.csv.
Columns as printed: A name, B country, C respondent to the OECD organisational survey, D respondent to the third
edition or identified through secondary data sources.
"""
import re
import subprocess

import pandas as pd

from ..core.paths import MANUAL
from ..core.provenance import local_file_meta

PDF = MANUAL / "oecd_pp4d_third_edition_report.pdf"
OUT = MANUAL / "oecd_third_edition_annex_b.csv"
ROW = re.compile(r"^\s*(\S.*?)\s{2,}(\S.*?)\s{2,}(Yes|No)\s+(Yes|No)\s*$")


def extract() -> pd.DataFrame:
    txt = subprocess.run(["pdftotext", "-layout", str(PDF), "-"], capture_output=True, text=True, check=True).stdout
    end = txt.index("Note: Organisations are listed in alphabetical order")
    start = txt.rindex("Table A B.1. Sample", 0, end)  # the table itself, not the contents page
    rows, pending = [], ""
    for line in txt[start:end].splitlines():
        m = ROW.match(line)
        if m:
            name = (pending + " " + m.group(1)).strip() if pending else m.group(1).strip()
            rows.append({"name": name, "country": m.group(2).strip(), "survey_respondent": m.group(3),
                         "third_edition_or_secondary": m.group(4)})
            pending = ""
        elif line.strip() and not re.search(r"PRIVATE PHILANTHROPY|©|\uf07c|^\s*\d+\s*$|Table A B\.1|^\s*A\s+B\s+C\s+D\s*$", line):
            pending = (pending + " " + line.strip()).strip()  # a name wrapped onto two lines
    df = pd.DataFrame(rows)
    meta = local_file_meta(PDF)
    df["source_pdf_hash"] = meta["file_hash"]
    df.to_csv(OUT, index=False)
    return df


if __name__ == "__main__":
    d = extract()
    print(len(d), d["country"].value_counts().head(8).to_dict())

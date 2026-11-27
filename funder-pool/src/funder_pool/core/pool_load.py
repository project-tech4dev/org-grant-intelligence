"""funder_pool_load.csv: the pool as rows for a Sangam queue table (funder_pool).

The queue table holds only what is needed before a funder exists in Sangam: the name and CIN to resolve it,
the category and rank to order the queue, the CSR spend floor, and the ingest status. Every other pool column
goes into one `signals` JSON object, so nothing is lost but the table does not copy the columns of `funders`.
Once a row is ingested, Sangam's `funders` row is the source of truth and the queue row only links to it.

Starting ingest_status: in_sangam 'yes' -> skipped, 'related' -> needs_review, otherwise pending.
"""
import json
import re

import pandas as pd

from . import schema

COLUMNS = ["pool_funder_id", "category", "name", "cin", "rank_in_category", "score_total",
           "csr_spend_3y_avg_cr", "in_sangam_at_load", "ingest_status", "export_version", "signals"]
STATUS = {"yes": "skipped", "related": "needs_review"}
LISTS = {"aliases", "sources", "themes", "unknown_signals", "also_in"}
TEXT = set(schema.IDENTIFIERS) | {"oecd_donor_code", "last_india_year", "name", "parent_name", "notes", "website"}
TOP = {"funder_id", "category", "name", "cin", "rank_in_category", "score_total", "csr_spend_3y_average",
       "in_sangam", "priority_band"}
NUMBER = re.compile(r"-?\d+(\.\d+)?([eE][-+]?\d+)?")


def _value(col: str, v: str):
    if col in LISTS:
        return [x for x in v.split("|") if x]
    if col == "india_usd_by_source" and v.startswith("{"):
        return json.loads(v)
    if v in {"True", "False"}:
        return v == "True"
    if col not in TEXT and NUMBER.fullmatch(v):
        f = float(v)
        return int(f) if f.is_integer() and "." not in v else f
    return v


def signals(row: dict) -> str:
    out = {c: _value(c, v) for c, v in row.items() if c not in TOP and v != ""}
    return json.dumps(out, ensure_ascii=False, sort_keys=True)


def to_load(pool_all: pd.DataFrame, export_version: str) -> pd.DataFrame:
    rows = []
    for r in pool_all.to_dict("records"):
        rows.append({"pool_funder_id": r["funder_id"], "category": r["category"], "name": r["name"],
                     "cin": r.get("cin", ""), "rank_in_category": r["rank_in_category"],
                     "score_total": r["score_total"], "csr_spend_3y_avg_cr": r.get("csr_spend_3y_average", ""),
                     "in_sangam_at_load": r["in_sangam"], "ingest_status": STATUS.get(r["in_sangam"], "pending"),
                     "export_version": export_version, "signals": signals(r)})
    df = pd.DataFrame(rows, columns=COLUMNS)
    df["_r"] = pd.to_numeric(df["rank_in_category"], errors="coerce")
    return df.sort_values(["category", "_r"], kind="stable").drop(columns="_r").reset_index(drop=True)

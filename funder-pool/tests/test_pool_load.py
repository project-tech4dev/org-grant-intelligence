import json

import pandas as pd

from funder_pool.core import pool_load


def _pool(**kw):
    row = {"funder_id": "acme--indian_csr", "category": "indian_csr", "name": "ACME LIMITED", "aliases": "Acme|ACME Ltd",
           "cin": "", "ein": "", "in_sangam": "no", "rank_in_category": "7", "score_total": "41.5",
           "csr_spend_3y_average": "12.3", "priority_band": "", "themes": "education|health",
           "has_foundation_arm": "True", "india_grants_count_5y": "3.0", "last_india_year": "FY2024-25",
           "india_usd_by_source": '{"irs_990pf": 750000.0}', "notes": ""}
    row.update(kw)
    return pd.DataFrame([row])


def test_columns_status_and_signals():
    df = pool_load.to_load(_pool(), "2026-11-27")
    assert list(df.columns) == pool_load.COLUMNS
    r = df.iloc[0]
    assert (r.pool_funder_id, r.ingest_status, r.csr_spend_3y_avg_cr, r.export_version) == (
        "acme--indian_csr", "pending", "12.3", "2026-11-27")
    s = json.loads(r.signals)
    assert s["aliases"] == ["Acme", "ACME Ltd"] and s["themes"] == ["education", "health"]
    assert s["has_foundation_arm"] is True and s["india_grants_count_5y"] == 3.0
    assert s["last_india_year"] == "FY2024-25" and s["india_usd_by_source"] == {"irs_990pf": 750000.0}
    assert not {"name", "rank_in_category", "priority_band", "notes", "ein"} & set(s)  # top level, blank or empty


def test_in_sangam_sets_starting_status():
    assert pool_load.to_load(_pool(in_sangam="yes"), "v").ingest_status[0] == "skipped"
    assert pool_load.to_load(_pool(in_sangam="related"), "v").ingest_status[0] == "needs_review"


def test_identifiers_stay_text():
    s = json.loads(pool_load.to_load(_pool(ein="012345678"), "v").signals[0])
    assert s["ein"] == "012345678"

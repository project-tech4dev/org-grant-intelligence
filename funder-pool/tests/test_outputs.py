"""Acceptance checks (tests/acceptance.md) run on the real outputs in data/. Skipped when an output is not built.

Run after the utilities: PYTHONPATH=src .venv/bin/python -m pytest tests/test_outputs.py
"""
import json

import pandas as pd
import pytest

from acceptance_helpers import (check_drop_log, check_evidence, check_ingest_queue, check_known_zero,
                                check_no_contacts, check_no_sangam_connection, check_pool, check_signals)
from funder_pool.core.paths import DATA

UTILS = ["western", "indian_csr", "hni_family", "government_india", "bilateral_multilateral"]


def load(util: str, name: str) -> pd.DataFrame:
    p = DATA / util / f"{name}.csv"
    if not p.exists():
        pytest.skip(f"{util} not built")
    return pd.read_csv(p, dtype=str, keep_default_na=False)


def joined(util: str) -> pd.DataFrame:
    return load(util, "pool").merge(load(util, "signals"), on="funder_id")


@pytest.mark.parametrize("util", UTILS)
def test_all_utilities(util):
    pool, sig, ev = load(util, "pool"), load(util, "signals"), load(util, "evidence")
    errs = check_pool(pool) + check_signals(sig) + check_evidence(ev) + check_known_zero(sig, ev)
    errs += check_ingest_queue(pool, load(util, "ingest_queue")) + check_drop_log(load(util, "drop_log"))
    errs += check_no_contacts(pool, ev)
    assert not errs, errs[:20]
    assert set(sig["india_evidence_status"]) <= {"known_positive", "known_zero", "unknown"}
    assert (sig["priority_band"] == "").all()
    assert (load(util, "ingest_queue").get("priority_band", pd.Series(dtype=str)) == "").all()


@pytest.mark.parametrize("util", UTILS)
def test_every_help_file_source_logged(util):
    log = load(util, "sources_log")
    assert set(log["status"]) <= {"used", "blocked", "skipped"}
    missing = log[log["status"].isin(["blocked", "skipped"]) & (log["reason"] == "")]
    assert missing.empty, missing["source_key"].tolist()


def test_no_sangam_connection():
    assert not check_no_sangam_connection()


def test_western_known_funders():
    j = joined("western")
    for needle in ["Gates Foundation", "IKEA Foundation", "Children's Investment Fund Foundation", "Hewlett"]:
        hit = j[j["name"].str.contains(needle, case=False, regex=False)
                | j["aliases"].str.contains(needle, case=False, regex=False)]
        assert not hit.empty, needle
        assert (hit["india_evidence_status"] == "known_positive").any(), needle
    kp = set(j.loc[j["india_evidence_status"] == "known_positive", "funder_id"])
    assert kp <= set(load("western", "evidence")["funder_id"])


def test_western_never_sums_sources():
    j = joined("western")
    for r in j.itertuples():
        vals = json.loads(r.india_usd_by_source.replace("'", '"')) if r.india_usd_by_source else {}
        if r.india_usd_best:
            assert float(r.india_usd_best) in {round(float(v), 2) for v in vals.values()} | {float(v) for v in vals.values()}


def test_western_intermediaries_indirect():
    j = joined("western")
    for name in ["American India Foundation", "Give2Asia"]:
        hit = j[j["name"].str.lower() == name.lower()]
        if not hit.empty:
            assert hit["notes"].str.contains("indirect").all(), name


def test_indian_csr():
    j = joined("indian_csr")
    assert (j["india_csr_draft"] == "true").all()
    found = j.set_index(j["name"].str.upper())["in_sangam"]
    assert found.get("HDFC BANK LIMITED") == "yes"


def test_government_schemes_have_parent_and_page():
    p = DATA / "government_india" / "schemes.csv"
    if not p.exists():
        pytest.skip("government_india not built")
    s = pd.read_csv(p, dtype=str, keep_default_na=False)
    assert (s["agency"] != "").all() and (s["url"] != "").all()
    assert set(s["ngo_eligible_explicit"]) <= {"True", ""}

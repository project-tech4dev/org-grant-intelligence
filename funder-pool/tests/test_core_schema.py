import pandas as pd
from conftest import FIXTURES
from funder_pool.core import schema
import acceptance_helpers as ah


def test_pool_fixture_valid():
    pool = pd.read_csv(FIXTURES / "pool_ok.csv", dtype=str).fillna("")
    assert list(pool.columns) == schema.POOL
    assert ah.check_pool(pool) == []


def test_duplicate_identifier_detected():
    pool = pd.read_csv(FIXTURES / "pool_ok.csv", dtype=str).fillna("")
    pool.loc[1, "ein"] = "562618866"
    assert any("duplicate ein" in e for e in schema.duplicate_ids(pool))
    pool.loc[2, "funder_id"] = pool.loc[0, "funder_id"]
    assert any("duplicate funder_id" in e for e in schema.duplicate_ids(pool))


def test_invalid_values_and_priority_band():
    sig = schema.conform(pd.DataFrame([{"funder_id": "a", "india_evidence_status": "maybe", "priority_band": "P1"}]),
                         schema.SIGNALS)
    errs = ah.check_signals(sig)
    assert any("india_evidence_status" in e for e in errs)
    assert "priority_band must be blank" in errs


def test_evidence_provenance_required():
    ev = schema.conform(pd.DataFrame([{"funder_id": "a", "source_key": "iati", "source_url": "",
                                       "retrieved_at": "x", "file_hash": "h"}]), schema.EVIDENCE)
    assert "evidence rows missing source_url" in ah.check_evidence(ev)


def test_contact_leaks():
    df = pd.DataFrame({"name": ["A Donor", "B"], "notes": ["write to a@b.org", "call +91 98765 43210"]})
    assert len(schema.contact_leaks(df)) == 2
    clean = pd.DataFrame({"name": ["Shiv Nadar"], "notes": ["Rs 2,153 crore, FY2024-25"],
                          "source_url": ["https://x.org/a@b"]})
    assert schema.contact_leaks(clean) == []


def test_known_zero_needs_grantee_data():
    sig = pd.DataFrame({"funder_id": ["a", "b"], "india_evidence_status": ["known_zero", "known_zero"]})
    ev = pd.DataFrame({"funder_id": ["a"], "recipient_name": ["Some NGO"]})
    assert ah.check_known_zero(sig, ev) == ["known_zero without grantee data: b"]


def test_ingest_queue_excludes_sangam_yes():
    pool = pd.read_csv(FIXTURES / "pool_ok.csv", dtype=str).fillna("")
    q = pool[["funder_id"]].copy()
    assert ah.check_ingest_queue(pool, q) == ["in_sangam=yes in ingest_queue: ikea--western_funders"]
    assert ah.check_ingest_queue(pool, q[q.funder_id != "ikea--western_funders"]) == []


def test_drop_log_has_no_india_reasons():
    drops = pd.DataFrame({"funder_id": ["x", "y"], "reason": ["990-PF: no grants outside US", "no India giving"]})
    assert ah.check_drop_log(drops) == ["dropped for India reason: y"]


def test_no_sangam_connection_in_src():
    assert ah.check_no_sangam_connection() == []

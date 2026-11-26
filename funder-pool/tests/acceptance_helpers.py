"""Generic acceptance checks (tests/acceptance.md, 'All utilities') reusable on fixtures and on real outputs."""
import re
from pathlib import Path

import pandas as pd

from funder_pool.core import schema

SRC = Path(__file__).resolve().parents[1] / "src"


def check_pool(pool: pd.DataFrame) -> list[str]:
    return schema.duplicate_ids(pool) + schema.validate(pool, schema.POOL)


def check_signals(signals: pd.DataFrame) -> list[str]:
    errs = schema.validate(signals, schema.SIGNALS)
    if "india_evidence_status" in signals.columns and signals["india_evidence_status"].isna().any():
        errs.append("india_evidence_status blank")
    return errs


def check_known_zero(signals: pd.DataFrame, evidence: pd.DataFrame) -> list[str]:
    """known_zero only where grantee-level evidence for that funder is recorded."""
    zero = set(signals.loc[signals["india_evidence_status"] == "known_zero", "funder_id"])
    grantee = set(evidence.loc[evidence["recipient_name"].fillna("").astype(str) != "", "funder_id"])
    return [f"known_zero without grantee data: {f}" for f in sorted(zero - grantee)]


def check_evidence(evidence: pd.DataFrame) -> list[str]:
    return schema.validate(evidence, schema.EVIDENCE)


def check_ingest_queue(pool: pd.DataFrame, queue: pd.DataFrame) -> list[str]:
    yes = set(pool.loc[pool["in_sangam"] == "yes", "funder_id"])
    errs = [f"in_sangam=yes in ingest_queue: {f}" for f in sorted(yes & set(queue["funder_id"]))]
    errs += [f"in_sangam=yes missing from pool: {f}" for f in sorted(yes - set(pool["funder_id"]))]
    return errs


def check_drop_log(drops: pd.DataFrame) -> list[str]:
    bad = drops[drops["reason"].astype(str).str.contains(r"india giving|unknown|no india", case=False)]
    return [f"dropped for India reason: {r.get('name') or r.get('funder_id')}" for r in bad.to_dict("records")]


def check_no_contacts(*frames: pd.DataFrame) -> list[str]:
    return [h for df in frames for h in schema.contact_leaks(df)]


def check_no_sangam_connection(src: Path = SRC) -> list[str]:
    """No code path imports, calls or connects to the Sangam repo or database."""
    pat = re.compile(r"(import\s+sangam|from\s+sangam|psycopg|sqlalchemy|postgres(ql)?://|sangam-master|"
                     r"github\.com/project-tech4dev/sangam|\.pem\b)", re.I)
    return [f"{p.relative_to(src)}:{i}" for p in src.rglob("*.py")
            for i, line in enumerate(p.read_text().splitlines(), 1) if pat.search(line)]

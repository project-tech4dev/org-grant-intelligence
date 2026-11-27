"""Output column lists (schemas/pool_schema.md) and validators."""
import re
import pandas as pd

POOL = ["funder_id", "category", "name", "aliases", "country", "website", "ein", "uk_charity_no", "rsin",
        "iati_org_id", "oecd_donor_code", "cin", "funder_type_draft", "money_origin_draft", "india_csr_draft",
        "parent_name", "in_sangam", "sources", "notes"]
SIGNALS = ["funder_id", "india_evidence_status", "india_usd_5y", "india_usd_3y", "india_inr_crore_5y",
           "india_grants_count_5y", "india_recipients_distinct_5y", "total_giving_usd_5y", "india_share",
           "funds_ngos_share", "last_india_year", "themes", "india_usd_by_source", "source_preference_used",
           "india_usd_best", "sources_disagree", "ingest_readiness", "unknown_signals", "score_total",
           "rank_in_category", "priority_band"]
REVIEW_QUEUE = ["funder_id", "issue", "candidates", "suggested_action", "decision"]
EVIDENCE = ["funder_id", "year_or_period", "measure", "amount", "currency", "amount_usd", "fx_rate", "fx_source",
            "basis", "recipient_name", "recipient_country", "recipient_state", "purpose_text", "source_key",
            "source_url", "retrieved_at", "file_hash", "row_ref"]
SOURCES_LOG = ["source_key", "source_name", "url", "access_method", "status", "reason", "retrieved_at",
               "file_hash", "rows_read", "terms_checked", "notes"]
INGEST_QUEUE = ["funder_id", "category", "name", "rank_in_category", "score_total", "in_sangam",
                "ingest_readiness", "india_evidence_status", "notes"]

IDENTIFIERS = ["ein", "uk_charity_no", "rsin", "iati_org_id", "cin"]

ALLOWED = {
    "category": {"western_funders", "indian_csr", "hni_family", "government_india", "bilateral_multilateral"},
    "funder_type_draft": {"csr_company", "csr_foundation", "private_foundation", "hni", "intermediary",
                          "international_agency", "bilateral_multilateral", "government", "other", "review"},
    "money_origin_draft": {"foreign", "domestic", "mixed", "unknown"},
    "india_csr_draft": {"true", "false", "review"},
    "in_sangam": {"yes", "related", "no"},
    "india_evidence_status": {"known_positive", "known_zero", "unknown"},
    "issue": {"ambiguous_match", "unknown_india", "intermediary", "source_disagree", "classification"},
    "basis": {"disbursed", "committed", "estimate", ""},
    "access_method": {"api", "download", "manual_file"},
    "status": {"used", "blocked", "skipped"},
}
PROVENANCE_REQUIRED = ["source_key", "source_url", "retrieved_at", "file_hash"]

EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE_RE = re.compile(r"(?:\+?\d[\d\s().-]{8,}\d)")
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}")
TEXT_FROM_SOURCE = {"purpose_text", "name", "aliases", "recipient_name", "measure", "parent_name"}
AGE_RE = re.compile(r"\b(?:aged?|years old)\b\s*:?\s*\d{1,3}", re.I)


def basis_enum(text: str) -> str:
    """Map a free-text basis to the schema enum (disbursed, committed, estimate or blank)."""
    t = str(text or "").lower()
    if t in ALLOWED["basis"]:
        return t
    if any(k in t for k in ("estimate", "share applied", "lower bound", "approx")):
        return "estimate"
    if any(k in t for k in ("commit", "awarded", "sanction", "approved", "pledge")):
        return "committed"
    if any(k in t for k in ("disburse", "expenditure", "spent", "spend", "paid")):
        return "disbursed"
    return ""


def issue_enum(text: str) -> str:
    """Map a free-text review issue to the schema enum."""
    t = str(text or "").lower()
    if t in ALLOWED["issue"]:
        return t
    if "disagree" in t:
        return "source_disagree"
    if "intermediar" in t or "indirect" in t:
        return "intermediary"
    if "ambiguous" in t or "candidate" in t or "same organisation" in t or "match" in t:
        return "ambiguous_match"
    if "unknown" in t or "not counted" in t or "no domestic source" in t or "india" in t:
        return "unknown_india"
    return "classification"


def empty(columns: list[str]) -> pd.DataFrame:
    return pd.DataFrame(columns=columns)


def conform(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Add missing columns (blank), drop unknown extras unless listed, keep order. Extra signal columns are kept after."""
    out = df.copy()
    for c in columns:
        if c not in out.columns:
            out[c] = ""
    extras = [c for c in out.columns if c not in columns]
    return out[columns + extras]


def _blank(v) -> bool:
    return v is None or (isinstance(v, float) and pd.isna(v)) or str(v).strip() == ""


def validate(df: pd.DataFrame, columns: list[str]) -> list[str]:
    """Return a list of problems (empty list = valid)."""
    errs = [f"missing column {c}" for c in columns if c not in df.columns]
    for col, allowed in ALLOWED.items():
        if col in df.columns:
            bad = sorted({str(v) for v in df[col] if not _blank(v) and str(v) not in allowed})
            if bad:
                errs.append(f"{col}: invalid values {bad[:5]}")
    if "priority_band" in df.columns and not all(_blank(v) for v in df["priority_band"]):
        errs.append("priority_band must be blank")
    if columns is EVIDENCE:
        for c in PROVENANCE_REQUIRED:
            if c in df.columns and any(_blank(v) for v in df[c]):
                errs.append(f"evidence rows missing {c}")
    return errs


def duplicate_ids(pool: pd.DataFrame) -> list[str]:
    """funder_id must be unique; no two rows may share any external identifier."""
    errs = []
    d = pool["funder_id"][pool["funder_id"].duplicated()]
    if len(d):
        errs.append(f"duplicate funder_id: {sorted(set(d))[:5]}")
    for c in IDENTIFIERS:
        if c in pool.columns:
            vals = pool[c].astype(str).str.strip()
            vals = vals[(vals != "") & (vals != "nan")]
            dup = vals[vals.duplicated()]
            if len(dup):
                errs.append(f"duplicate {c}: {sorted(set(dup))[:5]}")
    return errs


def contact_leaks(df: pd.DataFrame) -> list[str]:
    """Find emails, phone numbers or ages in any text cell (rule 8)."""
    hits = []
    for col in df.columns:
        if col in {"amount", "amount_usd", "fx_rate", "file_hash", "row_ref", "score_total", "retrieved_at",
                   "funder_id", "iati_org_id", "cin", "ein", "candidates", "fx_source"} or col.startswith("india_") \
                or col.endswith("_usd") or col.endswith("_5y") or col.endswith("_3y"):
            continue
        for v in df[col].dropna().astype(str):
            if v.startswith("http") or ISO_DATE_RE.search(v):
                continue
            phone = any(sum(ch.isdigit() for ch in m.group()) >= 10 for m in PHONE_RE.finditer(v))
            if col in TEXT_FROM_SOURCE:  # grant titles and registered names: numbers and "aged 15-26" are not contact data
                phone = False
                if EMAIL_RE.search(v):
                    hits.append(f"{col}: {v[:60]}")
                continue
            if EMAIL_RE.search(v) or AGE_RE.search(v) or phone:
                hits.append(f"{col}: {v[:60]}")
    return hits

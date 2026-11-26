"""IATI Datastore Classic (datastore.codeforiati.org): India activities and transactions.

Fetches paged CSVs (recipient-country=IN) into data/raw/iati/ via cached_fetch, then loads
them as DataFrames. Used by western_funders (non-government publishers) and
bilateral_multilateral (government and multilateral publishers)."""
import csv
from pathlib import Path

import pandas as pd

from ..core.paths import RAW
from ..core.provenance import cached_fetch

BASE = "https://datastore.codeforiati.org/api/1/access"
PAGE = 1000
URL_TERMS = "https://datastore.codeforiati.org/ (data licences vary by publisher; see each publisher's IATI registry record)"

# IATI OrganisationType codes
GOVERNMENT_TYPES = {"10", "11", "15"}          # government, local government, other public sector
MULTILATERAL_TYPES = {"40"}                    # multilateral
NGO_TYPES = {"21", "22", "23", "24"}           # international / national / regional / partner-country NGO
OTHER_PRIVATE = {"30", "60", "70", "71", "72", "73", "80", "90"}  # PPP, foundation, private sector, academic, other
BILATERAL_TYPES = GOVERNMENT_TYPES | MULTILATERAL_TYPES


def _fetch_kind(kind: str, refresh: bool = False) -> list[dict]:
    metas, offset = [], 0
    while True:
        url = f"{BASE}/{kind}.csv?recipient-country=IN&limit={PAGE}&offset={offset}"
        m = cached_fetch(url, "iati", f"{kind}_IN_{offset:07d}.csv", refresh=refresh, interval=1.0)
        metas.append(m)
        with open(m["path"], newline="", encoding="utf-8") as f:
            n = sum(1 for _ in csv.reader(f)) - 1
        if n < PAGE:
            return metas
        offset += PAGE


def fetch(refresh: bool = False) -> dict[str, list[dict]]:
    return {k: _fetch_kind(k, refresh) for k in ("activity", "transaction")}


def cached_pages(kind: str, raw: Path = RAW) -> list[Path]:
    return sorted((raw / "iati").glob(f"{kind}_IN_*.csv"))


def load(kind: str, raw: Path = RAW) -> pd.DataFrame:
    """Concatenate cached pages; keeps page file name in _page and the row number in _row for provenance."""
    frames = []
    for p in cached_pages(kind, raw):
        df = pd.read_csv(p, dtype=str, keep_default_na=False)
        df["_page"], df["_row"] = p.name, range(2, len(df) + 2)
        frames.append(df)
    if not frames:
        return pd.DataFrame()
    df = pd.concat(frames, ignore_index=True)
    key = ["iati-identifier"] if kind == "activity" else [
        "iati-identifier", "transaction-type", "transaction-date", "transaction-value", "transaction_ref",
        "transaction_receiver-org", "transaction_provider-org"]
    return df.drop_duplicates(subset=key, keep="first").reset_index(drop=True)


def india_fraction(codes: str, pcts: str) -> float | None:
    """India share of a (possibly multi-country) activity. Single-country IN -> 1.0.
    Multi-country with an IN percentage -> that percentage. Multi-country without percentages -> None (unknown)."""
    cs = [c.strip() for c in (codes or "").split(";")]
    ps = [p.strip() for p in (pcts or "").split(";")]
    if "IN" not in cs:
        return None
    if len(cs) == 1:
        return 1.0
    i = cs.index("IN")
    try:
        return float(ps[i]) / 100.0 if i < len(ps) and ps[i] else None
    except ValueError:
        return None


if __name__ == "__main__":
    out = fetch()
    print({k: len(v) for k, v in out.items()})

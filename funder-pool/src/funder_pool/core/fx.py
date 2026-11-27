"""Annual average FX conversion. Rates live in config/fx_rates.yaml (units of currency per 1 USD)."""
from functools import lru_cache
from .config import load_yaml


@lru_cache(maxsize=None)
def table() -> dict:
    return load_yaml("fx_rates.yaml")


def rate(currency: str, year: int, tbl: dict | None = None) -> tuple[float, str]:
    """Return (units per USD, source note). Raises KeyError if the rate is missing."""
    tbl = tbl if tbl is not None else table()
    cur = currency.upper()
    if cur == "USD":
        return 1.0, "identity"
    return float(tbl["rates"][cur][int(year)]), tbl["source"]


def to_usd(amount: float, currency: str, year: int, tbl: dict | None = None) -> tuple[float, float, str]:
    """Return (amount_usd, rate_used, source)."""
    r, src = rate(currency, year, tbl)
    return float(amount) / r, r, src


CRORE = 10_000_000


def inr_to_crore(inr: float) -> float:
    return float(inr) / CRORE

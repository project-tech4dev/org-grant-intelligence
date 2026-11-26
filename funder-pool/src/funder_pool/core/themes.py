"""Map OECD purpose codes and purpose text to Schedule VII themes (config/theme_map.yaml)."""
import re
from functools import lru_cache

from .config import load_yaml


@lru_cache(maxsize=None)
def theme_map() -> dict:
    return load_yaml("theme_map.yaml")


def from_purpose_code(code, tm: dict | None = None) -> str:
    tm = tm or theme_map()
    code = str(code or "").split(".")[0].strip()
    best = ""
    for prefix in tm["purpose_code_prefixes"]:
        if code.startswith(str(prefix)) and len(str(prefix)) > len(best):
            best = str(prefix)
    return tm["purpose_code_prefixes"][best] if best else ""


def from_text(text: str, tm: dict | None = None) -> str:
    tm = tm or theme_map()
    t = str(text or "").lower()
    for rule in tm["keywords"]:
        if any(re.search(r"\b" + re.escape(k), t) for k in rule["any"]):
            return rule["theme"]
    return ""


def classify(code=None, text: str = "", tm: dict | None = None) -> str:
    """Purpose code first, then keywords. '' means unresolved (goes to in-session classification)."""
    th = from_purpose_code(code, tm) if code else ""
    if th and th != "other":
        return th
    return from_text(text, tm) or th


@lru_cache(maxsize=None)
def overrides() -> dict:
    """In-session classifications for purposes the rules leave unresolved: config/theme_overrides.csv (key, theme)."""
    import csv
    from .paths import CONFIG
    p = CONFIG / "theme_overrides.csv"
    if not p.exists():
        return {}
    with p.open(newline="", encoding="utf-8") as f:
        return {r["key"]: r["theme"] for r in csv.DictReader(f) if r.get("theme")}


def override(key: str) -> str:
    return overrides().get(str(key), "")

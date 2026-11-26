import re
import unicodedata


def slug(text: str) -> str:
    t = unicodedata.normalize("NFKD", str(text)).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return t or "unnamed"


def funder_id(normalised_name: str, category: str) -> str:
    """Stable ID: slug of the normalised name plus category. Never reuse."""
    return f"{slug(normalised_name)}--{category}"

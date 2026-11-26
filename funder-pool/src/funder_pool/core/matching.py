"""Entity matching: identifiers first, then normalised name plus country, then fuzzy (ambiguous -> review)."""
import re
import unicodedata
from dataclasses import dataclass

from rapidfuzz import fuzz

AUTO_THRESHOLD = 95
REVIEW_THRESHOLD = 85

LEGAL_SUFFIXES = {"limited", "ltd", "pvt", "private", "inc", "incorporated", "llc", "plc", "co", "company",
                  "corp", "corporation", "gmbh", "ag", "sa", "bv", "nv", "the", "and"}
PHILANTHROPY_WORDS = {"foundation", "foundations", "trust", "trusts", "charitable", "philanthropies",
                      "philanthropy", "fund", "fonds", "stiftung", "stichting", "public", "society"}
SPELLINGS = {"fuer": "fur", "für": "fur", "centre": "center", "organisation": "organization"}


def _ascii(s: str) -> str:
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()


def tokens(name: str) -> list[str]:
    s = _ascii(str(name)).lower().replace("&", " and ").replace("'s", "s")
    s = re.sub(r"\([^)]*\)", " ", s)              # drop parenthetical abbreviations "(TCS)"
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return [SPELLINGS.get(t, t) for t in s.split()]


def normalise(name: str) -> str:
    """Identity key: lowercased, ascii, '&'='and', no punctuation or parentheticals, legal suffixes removed.
    Keeps 'foundation' and 'trust' because a company and its foundation are two funders."""
    return " ".join(t for t in tokens(name) if t not in LEGAL_SUFFIXES)


def stem(name: str) -> str:
    """Normalised name without philanthropy words: 'Axis Bank Foundation' and 'Axis Bank Limited' -> 'axis bank'."""
    return " ".join(t for t in normalise(name).split() if t not in PHILANTHROPY_WORDS)


def acronym(name: str) -> str:
    return "".join(t[0] for t in normalise(name).split())


def parenthetical(name: str) -> list[str]:
    return [p.strip().lower() for p in re.findall(r"\(([^)]*)\)", str(name))]


def same_by_acronym(a: str, b: str) -> bool:
    """'TCS' vs 'Tata Consultancy Services (TCS) Limited'."""
    na, nb = normalise(a), normalise(b)
    for short, long_raw, long_n in ((na, b, nb), (nb, a, na)):
        if " " not in short and 2 <= len(short) <= 5 and " " in long_n:
            if short == acronym(long_raw) or short in parenthetical(long_raw):
                return True
    return False


@dataclass
class Candidate:
    key: str
    name: str
    score: float
    how: str


def score(a: str, b: str) -> float:
    return fuzz.token_sort_ratio(normalise(a), normalise(b))


def match(name: str, candidates: dict[str, str], *, ids: dict[str, str] | None = None,
          candidate_ids: dict[str, dict[str, str]] | None = None) -> tuple[str, list[Candidate]]:
    """Match one name against {key: name}. Returns (decision, candidates) with decision in
    'id' | 'exact' | 'acronym' | 'fuzzy' (auto, >= AUTO_THRESHOLD) | 'ambiguous' (to review_queue) | 'none'."""
    ids = {k: v for k, v in (ids or {}).items() if v}
    if ids and candidate_ids:
        hits = [k for k, cid in candidate_ids.items() if any(cid.get(t) == v for t, v in ids.items())]
        if len(hits) == 1:
            return "id", [Candidate(hits[0], candidates.get(hits[0], ""), 100, "id")]
    n = normalise(name)
    exact = [k for k, v in candidates.items() if normalise(v) == n]
    if len(exact) == 1:
        return "exact", [Candidate(exact[0], candidates[exact[0]], 100, "exact")]
    if len(exact) > 1:
        return "ambiguous", [Candidate(k, candidates[k], 100, "exact") for k in sorted(exact)]
    acr = [k for k, v in candidates.items() if same_by_acronym(name, v)]
    if len(acr) == 1:
        return "acronym", [Candidate(acr[0], candidates[acr[0]], 100, "acronym")]
    scored = sorted((Candidate(k, v, score(name, v), "fuzzy") for k, v in candidates.items()),
                    key=lambda c: (-c.score, c.key))
    top = [c for c in scored if c.score >= REVIEW_THRESHOLD][:5]
    if not top:
        return "none", []
    if top[0].score >= AUTO_THRESHOLD and (len(top) == 1 or top[1].score < AUTO_THRESHOLD):
        return "fuzzy", top[:1]
    return "ambiguous", top

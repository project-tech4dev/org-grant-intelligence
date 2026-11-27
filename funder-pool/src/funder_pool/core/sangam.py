"""in_sangam = yes | related | no, from a read-only file export. Never connects to Sangam."""
import re
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from . import matching
from .paths import MANUAL, SEEDS

EXPORT = MANUAL / "sangam_funders_export.csv"
PARTIAL_SEED = SEEDS / "sangam_existing_funders_partial.csv"
CORPORATE_TYPES = {"csr_company", "csr_foundation", "corporate_csr", "corporate_foundation"}


@dataclass
class SangamFunder:
    name: str
    funder_type: str
    aliases: list[str]
    cin: str = ""


def _split_aliases(v) -> list[str]:
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return []
    s = str(v).strip().strip("{}[]")
    # The M11 export separates aliases with ';' and an alias may contain a comma ('JPMorgan Chase Bank N.A., India').
    # Split on commas only when there is no ';' or '|' (Postgres array literals such as {a,b}).
    sep = r"[|;]" if re.search(r"[|;]", s) else ","
    return [a.strip().strip('"\'') for a in re.split(sep, s) if a.strip().strip('"\'')]


def load(export: Path = EXPORT, partial: Path = PARTIAL_SEED) -> tuple[list[SangamFunder], str]:
    """Returns (funders, source_path_used)."""
    if export.exists():
        df = pd.read_csv(export, dtype=str).fillna("")
        rows = [SangamFunder(r["name"], r.get("funder_type", ""), _split_aliases(r.get("aliases", "")), r.get("cin", ""))
                for _, r in df.iterrows()]
        return rows, str(export)
    df = pd.read_csv(partial, dtype=str).fillna("")
    return [SangamFunder(r["name"], r["funder_type_as_listed_in_324"], []) for _, r in df.iterrows()], str(partial)


FOREIGN_FORM = re.compile(r"\b(stiftung|stichting|ggmbh|e\.\s?v\.|fondation|fundaci[oó]n|fondazione|funda[cç][aã]o"
                          r"|company limited by guarantee|charitable incorporated organisation)(?=\W|$)", re.I)


def foreign_form(f: SangamFunder) -> str:
    """The foreign legal form in a Sangam funder's name or aliases ('' if none). The M11 export has no country,
    so this is how a private_foundation row is recognised as foreign (e.g. 'Stiftung Childaid Network',
    'Paul Hamlyn Foundation (company limited by guarantee)')."""
    for n in [f.name, *f.aliases]:
        m = FOREIGN_FORM.search(n)
        if m:
            return m.group(1).lower()
    return ""


LEGAL_FORM = re.compile(r"\b(limited|ltd|private|pvt|llp|inc|corporation|company)\b", re.I)


def _corporate_like(f: SangamFunder) -> bool:
    return f.funder_type in CORPORATE_TYPES or (not f.funder_type and "foundation" in f.name.lower())


def _prefix(a: str, b: str) -> bool:
    ta, tb = a.split(), b.split()
    short, long_ = (ta, tb) if len(ta) <= len(tb) else (tb, ta)
    return bool(short) and len(" ".join(short)) >= 3 and long_[:len(short)] == short


def status(name: str, funders: list[SangamFunder], cin: str = "") -> tuple[str, str]:
    """Return (in_sangam, matched Sangam name)."""
    if cin:
        for f in funders:
            if f.cin and f.cin == cin:
                return "yes", f.name
    n = matching.normalise(name)
    # Acronym match when the name being checked is the acronym ('ABF' vs 'Axis Bank Foundation'), or when Sangam's
    # canonical name is ('TCS', 'ITC Limited'). A short Sangam *alias* ('CF', 'RF') must not match every company
    # with those initials.
    # A name with a legal-form suffix ('SNF(INDIA) PRIVATE LIMITED') is a company, not an acronym of a Sangam funder.
    short = " " not in n and not LEGAL_FORM.search(name)
    for f in funders:
        for i, alias in enumerate([f.name, *f.aliases]):
            if matching.normalise(alias) == n:
                # 'SNF(INDIA) PRIVATE LIMITED' normalises to 'snf'; a company does not match a bare acronym alias
                if i == 0 or " " in n or not LEGAL_FORM.search(name) or LEGAL_FORM.search(alias):
                    return "yes", f.name
            if short and matching.same_by_acronym(name, alias):
                return "yes", f.name
            # Sangam's canonical name is the acronym: match the initials only, not a parenthetical
            # ('ITC Limited' must not match 'International Trade Centre (ITC)').
            fa = matching.normalise(alias)
            if (i == 0 and " " not in fa and " " in n and fa == matching.acronym(name)
                    and _corporate_like(f) and LEGAL_FORM.search(name)):
                return "yes", f.name
    s = matching.stem(name)
    for f in funders:
        if not _corporate_like(f):
            continue
        fs = matching.stem(f.name)
        if s and fs and (s == fs or _prefix(s, fs)):
            return "related", f.name
    return "no", ""

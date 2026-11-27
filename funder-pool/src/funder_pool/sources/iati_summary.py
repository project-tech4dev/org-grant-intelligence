"""Per-publisher India summary from cached IATI pages (activity + transaction CSVs).

Rules (docs/funder-sources/western-funders.md and bilateral-multilateral.md):
- Spend = disbursements (type 3) + expenditure (type 4) inside the window. Commitments (type 2) are kept separately.
- A transaction counts for India when its own recipient country is IN, or when it has none and the activity's
  India share is known (single-country IN, or IN percentage given). Multi-country activities without a percentage
  are NOT counted (trap: "developing countries, unspecified" / multi-country is not India); they are counted in
  multi_country_unsplit_usd for the review queue.
- Donor and implementer may both publish the same money. Each publisher is summarised on its own; never summed.
"""
from collections import Counter, defaultdict
from dataclasses import dataclass, field

import pandas as pd

from ..core import fx, matching, themes
from ..core.provenance import file_hash
from ..core.paths import RAW
from . import iati

SPEND_TYPES = {"3", "4"}
COMMIT_TYPES = {"2"}
NGO_TYPES = {"21", "22", "23", "24"}
US_INTERMEDIARIES = ["American India Foundation", "Give2Asia", "Charities Aid Foundation America",
                     "Tides Foundation", "GlobalGiving Foundation"]
CHANNEL = {"10": "government", "11": "government", "15": "government", "21": "ngo", "22": "ngo", "23": "ngo",
           "24": "ngo", "30": "ppp", "40": "multilateral", "60": "foundation", "70": "private_sector",
           "71": "private_sector", "72": "private_sector", "73": "private_sector", "80": "academic", "90": "other"}


@dataclass
class Publisher:
    ref: str
    name: str
    type_code: str
    usd_5y: float = 0.0
    usd_3y: float = 0.0
    commit_5y: float = 0.0
    unsplit_usd: float = 0.0
    indirect_usd: float = 0.0
    activities: set = field(default_factory=set)
    commit_activities: set = field(default_factory=set)
    commit_3y: float = 0.0
    receivers: set = field(default_factory=set)
    last_year: str = ""
    ngo_usd: float = 0.0
    typed_usd: float = 0.0
    theme_usd: dict = field(default_factory=lambda: defaultdict(float))
    unresolved_purposes: dict = field(default_factory=dict)
    evidence: dict = field(default_factory=lambda: defaultdict(lambda: {"usd": 0.0, "rows": []}))


def _first_dac_sector(codes: str, vocabs: str) -> str:
    cs = [c.strip() for c in (codes or "").split(";")]
    vs = [v.strip() for v in (vocabs or "").split(";")]
    for i, c in enumerate(cs):
        v = vs[i] if i < len(vs) else (vs[0] if vs else "")
        if c and v in ("", "1", "2", "DAC", "DAC-3"):
            return c
    return ""


confirmed_india_activities: set[str] = set()  # filled by summarise()


def fy_label(date: str) -> str:
    y, m = int(date[:4]), int(date[5:7])
    s = y if m >= 4 else y - 1
    return f"FY{s}-{str(s + 1)[-2:]}"


def summarise(start: str, end: str, recent_start: str, raw=RAW) -> tuple[dict[str, Publisher], dict]:
    """Returns {publisher_key: Publisher} and page metadata {page_name: file_hash}."""
    act = iati.load("activity", raw)
    tx = iati.load("transaction", raw)
    pages = {p.name: file_hash(p) for k in ("activity", "transaction") for p in iati.cached_pages(k, raw)}
    a = act.set_index("iati-identifier") if len(act) else pd.DataFrame()
    impl_type = a["participating-org-type-code (Implementing)"].to_dict() if len(a) else {}
    pubs: dict[str, Publisher] = {}
    skips: Counter = Counter()
    tx = tx[(tx["transaction-date"] >= start) & (tx["transaction-date"] <= end)]
    # pre-compute activity-level India share; only confirmed-India activities (share > 0) give known_positive
    india_acts = set()
    for r in act[["iati-identifier", "recipient-country-code", "recipient-country-percentage"]].to_dict("records"):
        f = iati.india_fraction(r["recipient-country-code"], r["recipient-country-percentage"])
        if f:
            india_acts.add(r["iati-identifier"])
    confirmed_india_activities.clear()
    confirmed_india_activities.update(india_acts)
    for d in tx.to_dict("records"):
        g = lambda c: str(d.get(c, "") or "")  # noqa: E731
        ttype = g("transaction-type")
        if ttype not in SPEND_TYPES | COMMIT_TYPES:
            continue
        ref, name = g("reporting-org-ref").strip(), g("reporting-org").strip()
        key = ref or name
        p = pubs.setdefault(key, Publisher(ref, name, g("reporting-org-type-code").strip()))
        usd, rate_note = _usd(g, skips)
        if usd is None:
            skips[(p.type_code, "no_value")] += 1
            continue
        tc = g("transaction_recipient-country-code").strip()
        if tc:
            frac = 1.0 if tc == "IN" else (iati.india_fraction(tc, "") if "IN" in tc.split(";") else 0.0)
        else:
            frac = iati.india_fraction(g("recipient-country-code"), g("recipient-country-percentage"))
        if frac is None:
            if ttype in SPEND_TYPES:
                p.unsplit_usd += usd
            skips[(p.type_code, "multi_country_unsplit")] += 1
            continue
        if frac == 0:
            skips[(p.type_code, "other_country")] += 1
            continue
        val = usd * frac
        if ttype in COMMIT_TYPES:
            p.commit_5y += val
            if g("transaction-date") >= recent_start:
                p.commit_3y += val
            p.commit_activities.add(g("iati-identifier"))
            continue
        aid = g("iati-identifier")
        date = g("transaction-date")
        recv = g("transaction_receiver-org").strip()
        if is_intermediary(recv):
            p.indirect_usd += val
            skips[(p.type_code, "indirect_us_intermediary")] += 1
            continue
        skips[(p.type_code, "counted")] += 1
        p.usd_5y += val
        if date >= recent_start:
            p.usd_3y += val
        p.activities.add(aid)
        if recv:
            p.receivers.add(recv.lower())
        p.last_year = max(p.last_year, fy_label(date))
        it = str(impl_type.get(aid, "")).split(";")[0].strip()
        if it:
            p.typed_usd += val
            if it in NGO_TYPES:
                p.ngo_usd += val
        sector = g("transaction_sector-code") or _first_dac_sector(g("sector-code"), g("sector-vocabulary-code"))
        text = g("title")
        th = themes.classify(sector, text) or themes.override(aid)
        if th:
            p.theme_usd[th] += val
        elif text:
            p.unresolved_purposes[aid] = text[:200]
        ev = p.evidence[(aid, fy_label(date))]
        ev["usd"] += val
        ev["rows"].append(f"{g('_page')}:{g('_row')}")
        ev.setdefault("receiver", recv)
        ev.setdefault("purpose", text[:200])
        ev.setdefault("multi", tc == "" and frac < 1.0)
        ev.setdefault("fx", rate_note)
    return pubs, pages, skips


def _usd(g, skips) -> tuple[float | None, str]:
    """USD value: datastore USD column, else transaction value converted at the annual average rate."""
    v = g("transaction-value-USD")
    if v:
        try:
            return float(v), "IATI datastore USD"
        except ValueError:
            pass
    try:
        amt = float(g("transaction-value"))
    except ValueError:
        return None, ""
    cur = (g("transaction_value_currency") or g("default-currency")).strip().upper()
    if not cur:
        return None, ""
    year = int(g("transaction-date")[:4])
    tbl = fx.table()["rates"]
    if cur != "USD" and cur not in tbl:
        skips[("", f"no_fx_{cur}")] += 1
        return None, ""
    if cur != "USD" and year not in tbl[cur]:
        year = max(tbl[cur])
    usd, rate, src = fx.to_usd(amt, cur, year)
    return usd, f"{cur} {rate} ({year} annual average, {src})"


def is_intermediary(name: str) -> bool:
    n = matching.normalise(name)
    return bool(n) and any(n == matching.normalise(x) for x in US_INTERMEDIARIES)

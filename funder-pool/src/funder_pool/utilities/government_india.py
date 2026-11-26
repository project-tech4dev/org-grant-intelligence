"""government_india: Indian central agencies and the schemes under them that fund NGOs.
Help file: docs/funder-sources/government-india.md.

The funder is the agency; schemes go to data/government_india/schemes.csv with the agency's funder_id (help file §8).
Agencies and scheme pages are listed in config/government_schemes.yaml (each URL checked before use).

Sources:
- ministry_site: scheme pages, fetched once and cached under data/raw/ministry_site/. A page that fails (403, 5xx,
  timeout) is recorded in data/raw/ministry_site/_failures.json and not retried unless REFRESH is set, so reruns
  are identical. 403s are never retried around (hard rule 7).
- nabard: NABARD FSDD page (content.aspx?id=579), split into its fund sections.
- ngo_darpan (M9): manual; blocked until supplied.
- parliament_qa: skipped (budget and release evidence per answer; not needed for the roster).

Signals are read from the scheme text by rules. Anything the text does not state stays unknown (None), never False.
"""
import json
import os
import re

import lxml.html
import pandas as pd
import requests

from ..core import config
from ..core.paths import DATA, RAW
from ..core.provenance import RobotsDisallowed, cached_fetch, now_iso, write_csv
from .common import Build, finalize

CATEGORY = "government_india"
FAIL_PATH = RAW / "ministry_site" / "_failures.json"
REFRESH = bool(os.environ.get("REFRESH"))

NGO_RE = re.compile(r"\b(NGOs?|non[- ]?governmental organi[sz]ations?|voluntary organi[sz]ations?|voluntary agenc(y|ies)"
                    r"|civil society organi[sz]ations?)\b", re.I)
NGO_ABBR = re.compile(r"\bVOs\b")
ELIG_RE = re.compile(r"eligib", re.I)
AMOUNT_RE = re.compile(r"(Rs\.?|₹|INR)\s*[\d,.]+|\b\d[\d,.]*\s*(lakhs?|crores?)\b", re.I)
PROCESS_RE = re.compile(r"\b(apply|application|proposals?|submi(t|ssion)|online portal)\b", re.I)
CALL_RE = re.compile(r"\b(call for proposals?|invit\w+ (proposals?|applications?)|advertisement|applications? (are|is) "
                     r"invited|proposals? (are|is) invited|last date)\b", re.I)
YEAR_RE = re.compile(r"\b(20[12]\d)(?:\s*[-–/]\s*(\d{2,4}))?\b")
CRORE_RE = re.compile(r"(?:Rs\.?|₹)\s*([\d,]+(?:\.\d+)?)\s*crore", re.I)

CURRENT_FY_START = 2026  # FY2026-27; a call dated in FY2025-26 or later is within twelve months


def _failures() -> dict:
    return json.loads(FAIL_PATH.read_text()) if FAIL_PATH.exists() else {}


def _fname(url: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", url.split("://", 1)[1]).strip("_")[:120] + ".html"


def _fetch(url: str, source_key: str) -> tuple[dict | None, str]:
    """Return (meta, "") or (None, reason). Failures are cached so reruns do not differ."""
    fails = _failures()
    if url in fails and not REFRESH:
        return None, fails[url]["reason"]
    try:
        return cached_fetch(url, source_key, _fname(url), timeout=30, interval=2.0), ""
    except RobotsDisallowed:
        reason = "robots.txt disallows"
    except requests.HTTPError as e:
        code = e.response.status_code if e.response is not None else "?"
        reason = f"HTTP {code}" + (" (access refused; not bypassed)" if code == 403 else "")
    except requests.RequestException as e:
        reason = type(e).__name__
    fails[url] = {"reason": reason, "at": now_iso()}
    FAIL_PATH.parent.mkdir(parents=True, exist_ok=True)
    FAIL_PATH.write_text(json.dumps(fails, indent=2, sort_keys=True))
    return None, reason


def _text(path) -> str:
    raw = path.read_bytes()
    if not raw.strip():
        return ""
    doc = lxml.html.fromstring(raw)
    for e in doc.iter("script", "style", "noscript"):
        e.drop_tree()
    return " ".join(doc.text_content().split())


def _section(text: str, start: str | None, until: str | None) -> str:
    if not start:
        return text
    i = text.find(start)
    if i < 0:
        return ""
    j = text.find(until, i + len(start)) if until else -1
    return text[i: j if j > 0 else i + 6000]


def _fy_starts(seg: str) -> set[int]:
    """Financial-year start years named in a text segment ('2024-25' -> 2024; a bare '2024' -> 2024)."""
    return {int(m.group(1)) for m in YEAR_RE.finditer(seg)}


def read_scheme(text: str) -> dict:
    """Rule-based signals from a scheme's text. None = the text does not say."""
    ngo = bool(NGO_RE.search(text) or NGO_ABBR.search(text))
    elig, amt, proc = bool(ELIG_RE.search(text) or ngo), bool(AMOUNT_RE.search(text)), bool(PROCESS_RE.search(text))
    call_years = set()
    for m in CALL_RE.finditer(text):
        call_years |= _fy_starts(text[max(0, m.start() - 150): m.end() + 150])
    call_years = {y for y in call_years if y <= CURRENT_FY_START}
    last5 = set(range(CURRENT_FY_START - 4, CURRENT_FY_START + 1))
    budgets = [float(x.replace(",", "")) for x in CRORE_RE.findall(text) if re.search(r"budget|allocat|outlay", text, re.I)]
    return {
        "ngo_eligible_explicit": True if ngo else None,
        "active_call_12m": True if any(y >= CURRENT_FY_START - 1 for y in call_years) else None,
        "recurrence": True if len(call_years & last5) >= 3 else None,
        "call_years": sorted(call_years),
        # a crore figure is taken as a budget only when the scheme text speaks of a budget, allocation or outlay;
        # corpus figures (e.g. NABARD fund corpora) are not budgets and are left out (trap 1)
        "scheme_budget": None,
        "budget_mentions_crore": budgets,
        "ingest_readiness": 3 if (elig and amt and proc) else 2 if elig else 1,
        "has_eligibility": elig, "has_amounts": amt, "has_process": proc,
    }


def build() -> dict:
    b = Build(CATEGORY)
    cfg = config.load_yaml("government_schemes.yaml")
    schemes, used, blocked = [], {}, {}

    for ag in cfg["agencies"]:
        sk = ag.get("source_key", "ministry_site")
        fid = b.add_funder(ag["name"], source_key=sk, aliases=ag.get("aliases", []), country="IN",
                           funder_type_draft="government", money_origin_draft="domestic", india_csr_draft="false")
        sigs = []
        for s in ag["schemes"]:
            meta, why = _fetch(s["page"], sk)
            row = {"funder_id": fid, "agency": ag["name"], "scheme": s["scheme"], "url": s["page"],
                   "roster_only": bool(s.get("roster_only")), "fetch_status": "used" if meta else f"blocked: {why}",
                   "retrieved_at": meta["retrieved_at"] if meta else "", "file_hash": meta["file_hash"] if meta else ""}
            if not meta:
                blocked.setdefault((sk, s["page"]), why)
                b.queue(fid, f"scheme page not readable: {s['scheme']}", s["page"], f"{why}; read by hand or supply M9")
                schemes.append({**row, "ngo_eligible_explicit": None, "ingest_readiness": 1})
                continue
            used.setdefault((sk, s["page"]), meta)
            text = _section(_text(meta["path"]), s.get("section"), s.get("until"))
            if s.get("roster_only"):
                schemes.append({**row, "ngo_eligible_explicit": None, "ingest_readiness": 0})
                b.ledger.add_evidence(funder_id=fid, year_or_period="", measure="agency home page (roster)",
                                      basis="page exists; no scheme read", recipient_country="IN", source_key=sk,
                                      source_url=s["page"], retrieved_at=meta["retrieved_at"],
                                      file_hash=meta["file_hash"], row_ref=_fname(s["page"]))
                continue
            if not text:
                b.queue(fid, f"scheme section not found on page: {s['scheme']}", s["page"], "check the page layout")
            sig = read_scheme(text)
            sigs.append(sig)
            schemes.append({**row, **{k: sig[k] for k in ("ngo_eligible_explicit", "active_call_12m", "recurrence",
                                                          "scheme_budget", "ingest_readiness")},
                            "call_years": "|".join(map(str, sig["call_years"])),
                            "eligibility_excerpt": _excerpt(text)})
            b.ledger.add_evidence(funder_id=fid, year_or_period=", ".join(map(str, sig["call_years"])),
                                  measure=f"scheme page: {s['scheme']}",
                                  basis=("names NGOs/VOs as eligible" if sig["ngo_eligible_explicit"]
                                         else "NGO eligibility not stated"),
                                  purpose_text=_excerpt(text), recipient_country="IN", source_key=sk,
                                  source_url=s["page"], retrieved_at=meta["retrieved_at"],
                                  file_hash=meta["file_hash"], row_ref=f"{_fname(s['page'])}#{s.get('section', '')}")
            if sig["ngo_eligible_explicit"] is None:
                b.queue(fid, f"NGO eligibility unclear: {s['scheme']}", s["page"], "kept (help file §4); confirm by hand")

        def any_true(k):
            return True if any(x[k] for x in sigs) else None

        b.signals[fid] = {
            "scheme_budget": None,  # no scheme page states a current budget; Expenditure Budget not yet read (§9)
            "ngo_eligible_explicit": any_true("ngo_eligible_explicit"),
            "active_call_12m": any_true("active_call_12m"),
            "recurrence": any_true("recurrence"),
            "ingest_readiness": max([x["ingest_readiness"] for x in sigs], default=1 if not all(
                s.get("roster_only") for s in ag["schemes"]) else 0),
            # an agency that runs NGO grant schemes funds within India by definition; amounts are unknown
            "india_evidence_status": "known_positive" if any_true("ngo_eligible_explicit") else "unknown",
            "schemes_read": len(sigs),
        }
        if not sigs:
            b.queue(fid, "no scheme page read for this agency", "", "supply M9 (NGO-DARPAN scheme list) or read by hand")

    for (sk, url), meta in sorted(used.items()):
        b.ledger.log_source(sk, "NABARD FSDD funds page" if sk == "nabard" else "Ministry scheme page", url,
                            "download", "used", retrieved_at=meta["retrieved_at"], file_hash=meta["file_hash"],
                            rows_read=1, terms_checked="yes")
    for (sk, url), why in sorted(blocked.items()):
        b.ledger.log_source(sk, "Ministry scheme page", url, "download", "blocked", reason=why)
    b.ledger.log_source("ngo_darpan", "NGO-DARPAN scheme directory (M9)", "https://ngodarpan.gov.in/", "manual_file",
                        "blocked", reason="M9 not supplied; the scheme directory is manual (help file §3)")
    b.ledger.log_source("parliament_qa", "Lok Sabha and Rajya Sabha answers", "https://eparlib.sansad.in/",
                        "download", "skipped", reason="budget and release evidence only, per answer; not needed "
                                                      "for the agency roster (help file §3.3)")

    out = DATA / "government_india"
    write_csv(pd.DataFrame(schemes), out / "schemes.csv")
    notes = ["The funder is the agency. Schemes are in schemes.csv with the agency's funder_id.",
             "scheme_budget is unknown for every agency: scheme pages do not state current budgets and the "
             "Expenditure Budget has not been read. NABARD fund corpora are not budgets.",
             "Signals are read by rules from the scheme text. Where the text is silent the signal is unknown.",
             f"Scheme pages read: {sum(1 for s in schemes if s['fetch_status'] == 'used')} of {len(schemes)}; "
             "pages refused (403) were not bypassed.",
             "M9 (NGO-DARPAN scheme directory) not supplied; the agency list is from the help file.",
             "Priority bands are blank by design."]
    return finalize(b, "government_india", value_col="schemes_read", bins=[0, 1, 2, 3, 5], unit="schemes read",
                    size_col="schemes_read", notes=notes,
                    extra_signal_cols=["scheme_budget", "ngo_eligible_explicit", "active_call_12m", "recurrence",
                                       "schemes_read"])


def _excerpt(text: str) -> str:
    m = NGO_RE.search(text) or NGO_ABBR.search(text) or ELIG_RE.search(text)
    if not m:
        return text[:200]
    return text[max(0, m.start() - 120): m.end() + 180]


if __name__ == "__main__":
    r = build()
    print(r["joined"][["name", "score_total", "rank_in_category", "ingest_readiness", "unknown_signals"]].to_string())

"""360Giving publisher files from the 360Giving data registry, filtered locally for India.

Route change (CHANGELOG 2026-11-25): GrantNav's robots.txt disallows /search, /funders and /recipients, so the
help file's "search India in GrantNav" is replaced by the registry (https://registry.threesixtygiving.org/data.json).

Download: every registry distribution, once, cached under data/raw/threesixtygiving/. A hard cap (CAP_BYTES) stops
the run before 1 GB in total (hard rule 2); files past the cap are listed as skipped.
India filter (local): Recipient Org:Country is India, or Beneficiary Location:Country Code is IN, or a
Beneficiary Location:Name is India. Grants that mention India only in the title or description go to review.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

import pandas as pd

from ..core.paths import RAW
from ..core.provenance import RobotsDisallowed, cached_fetch, now_iso

REGISTRY = "https://registry.threesixtygiving.org/data.json"
CAP_BYTES = 950_000_000
DIR = RAW / "threesixtygiving"
INDIA_WORD = re.compile(r"\bIndia(?:n)?\b")


def _fname(url: str) -> str:
    ext = Path(url.split("?")[0]).suffix.lower() or ".dat"
    return hashlib.sha1(url.encode()).hexdigest()[:16] + ext


def registry() -> list[dict]:
    m = cached_fetch(REGISTRY, "threesixtygiving", "registry_data.json")
    out = []
    for x in json.loads(Path(m["path"]).read_text()):
        for d in x.get("distribution", []):
            out.append({"publisher": x["publisher"]["name"], "publisher_id": x["publisher"].get("prefix", ""),
                        "url": d["downloadURL"].strip(), "licence": x.get("license", ""), "modified": x.get("modified", "")})
    return out


def download() -> None:
    items = registry()
    total = sum(p.stat().st_size for p in DIR.glob("*") if not p.name.endswith(".json") and not p.name.startswith("_"))
    log = []
    for it in items:
        f = _fname(it["url"])
        if (DIR / f).exists():
            log.append({**it, "file": f, "status": "cached"})
            continue
        if total >= CAP_BYTES:
            log.append({**it, "file": f, "status": "skipped: 0.95 GB cap reached"})
            continue
        try:
            m = cached_fetch(it["url"], "threesixtygiving", f, interval=1.0)
            total += Path(m["path"]).stat().st_size
            log.append({**it, "file": f, "status": "used"})
        except RobotsDisallowed:
            log.append({**it, "file": f, "status": "blocked: robots.txt"})
        except Exception as e:  # noqa: BLE001 - per-file failures are logged, not fatal
            log.append({**it, "file": f, "status": f"blocked: {type(e).__name__}"})
        print(f"{len(log)}/{len(items)} {total / 1e9:.3f} GB", flush=True)
        if len(log) % 25 == 0:
            pd.DataFrame(log).to_csv(DIR / "_download_log.csv", index=False)
    pd.DataFrame(log).to_csv(DIR / "_download_log.csv", index=False)


def _read(path: Path) -> pd.DataFrame:
    s = path.suffix.lower()
    if s == ".csv":
        for enc in ("utf-8-sig", "cp1252"):
            try:
                return pd.read_csv(path, dtype=str, keep_default_na=False, encoding=enc, on_bad_lines="skip")
            except UnicodeDecodeError:
                continue
    if s in (".xlsx", ".xls"):
        sheets = pd.read_excel(path, sheet_name=None, dtype=str, keep_default_na=False)
        frames = [df for df in sheets.values() if any("Identifier" in str(c) for c in df.columns)]
        return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
    if s == ".json":
        d = json.loads(path.read_text(encoding="utf-8"))
        return pd.json_normalize(d.get("grants", []), sep=":")
    return pd.DataFrame()


def _col(df, *names):
    low = {str(c).strip().lower(): c for c in df.columns}
    for n in names:
        if n.lower() in low:
            return low[n.lower()]
    return None


def india_rows() -> pd.DataFrame:
    """Scan every cached file; return India rows (match='country') and mention-only rows (match='text')."""
    logp = DIR / "_download_log.csv"
    if not logp.exists():
        return pd.DataFrame()
    log = pd.read_csv(logp, dtype=str, keep_default_na=False)
    out = []
    for it in log.to_dict("records"):
        p = DIR / it["file"]
        if not p.exists():
            continue
        try:
            df = _read(p)
        except Exception as e:  # noqa: BLE001
            print("unreadable", p.name, type(e).__name__, file=sys.stderr)
            continue
        if df.empty:
            continue
        df.columns = [str(c).strip() for c in df.columns]
        c_rc = _col(df, "Recipient Org:Country", "recipientOrganization:0:addressCountry")
        c_bc = [c for c in df.columns if "beneficiary location" in c.lower() and "country code" in c.lower()] + \
               [c for c in df.columns if c.startswith("beneficiaryLocation") and c.endswith("countryCode")]
        c_bn = [c for c in df.columns if "beneficiary location" in c.lower() and c.lower().endswith(":name")] + \
               [c for c in df.columns if c.startswith("beneficiaryLocation") and c.endswith(":name")]
        c_title = _col(df, "Title", "title")
        c_desc = _col(df, "Description", "description")
        mask = pd.Series(False, index=df.index)
        if c_rc:
            mask |= df[c_rc].str.strip().str.lower().isin(["india", "in"])
        for c in c_bc:
            mask |= df[c].astype(str).str.strip().str.upper() == "IN"
        for c in c_bn:
            mask |= df[c].astype(str).str.strip().str.lower() == "india"
        text = (df[c_title].astype(str) if c_title else "") + " " + (df[c_desc].astype(str) if c_desc else "")
        tmask = (~mask) & text.str.contains(INDIA_WORD) if (c_title or c_desc) else pd.Series(False, index=df.index)
        for match, m in (("country", mask), ("text", tmask)):
            sub = df[m]
            for i, r in sub.iterrows():
                g = lambda *n: str(r.get(_col(df, *n), "") or "")  # noqa: E731
                out.append({"publisher": it["publisher"], "url": it["url"], "file": it["file"], "licence": it["licence"],
                            "row": int(i) + 2, "match": match,
                            "identifier": g("Identifier", "id"), "title": g("Title", "title")[:200],
                            "description": g("Description", "description")[:300],
                            "currency": g("Currency", "currency"), "amount": g("Amount Awarded", "amountAwarded"),
                            "award_date": g("Award Date", "awardDate"),
                            "recipient": g("Recipient Org:Name", "recipientOrganization:0:name"),
                            "recipient_country": g("Recipient Org:Country", "recipientOrganization:0:addressCountry"),
                            "funder": g("Funding Org:Name", "fundingOrganization:0:name") or it["publisher"],
                            "funder_id": g("Funding Org:Identifier", "fundingOrganization:0:id")})
    return pd.DataFrame(out)


if __name__ == "__main__":
    download()
    print("done", now_iso())

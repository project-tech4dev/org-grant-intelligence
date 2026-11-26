"""Build the versioned export that the Sangam ingest agent reads: data/export/<YYYY-MM-DD>/.

Run from funder-pool/:   .venv/bin/python -I scripts/export_for_ingest.py
Run the utility builds and `combine` first; this script only packages what they and the source caches hold.

Contents (see docs/funder-sources/00-index.md, "Export for the ingest agent"):
  funders/<category>/  pool, signals, evidence, sources_log (one folder per utility)
  funders/combined/    pool_all, ingest_queue, cross_category_matches
  grants/              irs990_returns, irs990_grants (all extracted years, all foreign grants plus India intermediaries),
                       iati_activity, iati_transaction (India, deduplicated), oecd_annex_b (the Annex B organisation list)
  MANIFEST.json        rows, bytes and sha256 per file, source licences, git commit, build window

Not exported: data/raw (re-downloadable), data/manual third-party files (Hurun, CSRAnalytics, MCA, OECD PDFs)
and the Sangam funder export.
"""
import hashlib
import json
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import pandas as pd  # noqa: E402

from funder_pool.core.paths import DATA, MANUAL  # noqa: E402
from funder_pool.sources import iati, irs990  # noqa: E402

UTILS = ["western", "indian_csr", "hni_family", "government_india", "bilateral_multilateral"]
PER_UTIL = ["pool", "signals", "evidence", "sources_log"]
COMBINED = ["pool_all", "ingest_queue", "cross_category_matches"]
WINDOW = {"start": "2021-04-01", "end": "2026-03-31", "recent_start": "2023-04-01"}
LICENCES = {
    "irs990": "US IRS Form 990-PF e-file data (TEOS XML): public domain. Individual recipients redacted to "
              "'individual recipient' with no place.",
    "iati": "IATI Datastore Classic (datastore.codeforiati.org); licence set by each publisher (mostly open, "
            "attribution required): see the publisher's IATI Registry record.",
    "oecd_annex_b": "OECD Private Philanthropy for Development, Third Edition, Annex B organisation list "
                    "(transcribed). Reuse with attribution under OECD terms.",
    "funders": "Derived outputs of this repo; each fact carries source_key, source_url, retrieved_at and "
               "file_hash in evidence.csv.",
}


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return "sha256:" + h.hexdigest()


def write(df: pd.DataFrame, path: Path, files: list, group: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, compression="gzip" if path.suffix == ".gz" else None)
    files.append({"path": str(path.relative_to(OUT)), "group": group, "rows": len(df),
                  "bytes": path.stat().st_size, "sha256": sha256(path)})
    print(f"  {path.relative_to(OUT)}: {len(df):,} rows")


def read(p: Path) -> pd.DataFrame:
    return pd.read_csv(p, dtype=str, keep_default_na=False)


def main() -> None:
    files: list[dict] = []
    missing = []
    for util in UTILS:
        for name in PER_UTIL:
            p = DATA / util / f"{name}.csv"
            if p.exists():
                write(read(p), OUT / "funders" / util / f"{name}.csv", files, "funders")
            else:
                missing.append(str(p.relative_to(DATA)))
    for name in COMBINED:
        p = DATA / "combined" / f"{name}.csv"
        if p.exists():
            write(read(p), OUT / "funders" / "combined" / f"{name}.csv", files, "funders")
        else:
            missing.append(str(p.relative_to(DATA)))

    rets, grants = irs990.load()
    if rets.empty:
        missing.append("cache/irs990 (run scripts/extract_irs.py)")
    else:
        meta = irs990.zip_meta()
        for df in (rets, grants):
            df["retrieved_at"] = df["zip"].map(lambda z: meta.get(z, {}).get("retrieved_at", ""))
            df["file_hash"] = df["zip"].map(lambda z: meta.get(z, {}).get("file_hash", ""))
        rets["website"] = rets["website"].where(~rets["website"].str.contains("@"), "")  # filers also enter emails
        write(rets, OUT / "grants" / "irs990_returns.csv.gz", files, "irs990")
        write(grants, OUT / "grants" / "irs990_grants.csv.gz", files, "irs990")

    for kind in ("activity", "transaction"):
        df = iati.load(kind)
        if df.empty:
            missing.append(f"raw/iati/{kind}_IN_*.csv")
        else:
            write(df, OUT / "grants" / f"iati_{kind}.csv.gz", files, "iati")

    p = MANUAL / "oecd_third_edition_annex_b.csv"
    if p.exists():
        write(read(p), OUT / "grants" / "oecd_annex_b.csv", files, "oecd_annex_b")
    else:
        missing.append(str(p.relative_to(DATA)))

    try:
        commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True,
                                check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        commit = ""
    manifest = {
        "export_version": OUT.name,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "git_commit": commit,
        "window": WINDOW,
        "licences": LICENCES,
        "not_exported": ["data/raw (re-download with scripts/download_irs.sh and the help files)",
                         "data/manual third-party files (Hurun, CSRAnalytics, MCA, OECD PDFs)",
                         "data/manual/sangam_funders_export.csv"],
        "missing": missing,
        "notes": ["Ranks are within each category; scores are not comparable across categories.",
                  "india_evidence_status 'unknown' is not zero.",
                  "OECD grant-level data (CRS private philanthropy) was blocked to scripts and is not included; "
                  "only the Annex B organisation list is.",
                  "irs990 and iati tables cover all extracted rows; apply the window above for India totals."],
        "files": files,
    }
    (OUT / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"wrote {OUT} ({len(files)} files, {sum(f['bytes'] for f in files) / 1e6:.0f} MB)")
    if missing:
        print("missing:", *missing, sep="\n  ")


OUT = DATA / "export" / (sys.argv[1] if len(sys.argv) > 1 else date.today().isoformat())

if __name__ == "__main__":
    main()

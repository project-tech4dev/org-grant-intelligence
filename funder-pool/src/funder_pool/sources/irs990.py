"""IRS Form 990-PF XML (TEOS bulk downloads), Part XV grants paid, filtered locally for foreign recipients.

Files: data/raw/irs_990pf/<filing year>/index_<year>.csv and <year>_TEOS_XML_*.zip (scripts/download_irs.sh).
The index gives RETURN_TYPE and OBJECT_ID; each zip member is <OBJECT_ID>_public.xml (some zips put members in a
folder). Only 990PF returns are parsed.

Element names were confirmed against 300 filed 990-PF returns with foreign grants in 2022_TEOS_XML_01A.zip:
  ReturnHeader/Filer/EIN, Filer/BusinessName/BusinessNameLine1Txt, ReturnHeader/TaxPeriodEndDt
  IRS990PF/AnalysisOfRevenueAndExpenses/ContriPaidRevAndExpnssAmt          (Part I line 25, grants paid)
  IRS990PF/Form990PFBalanceSheetsGrp/TotalAssetsEOYFMVAmt                  (Part II line 16 col c)
  IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp      (Part XV 3a, one per grant)
      RecipientPersonNm (stored only as 'individual recipient', no place) | RecipientBusinessName/BusinessNameLine1Txt
      RecipientUSAddress/... | RecipientForeignAddress/{CityNm, ProvinceOrStateNm, CountryCd}
      RecipientFoundationStatusTxt, GrantOrContributionPurposeTxt, Amt
Grants with a RecipientForeignAddress are kept (all countries, so the pool filter can count foreign granters).
US-address grants are counted, and kept (country "US") only when the recipient name suggests an India re-granter.

Output (cache, one set per zip, keyed on the zip's size and mtime): data/cache/irs990/<zip stem>.returns.csv
(one row per 990-PF return), .grants.csv (foreign-address grants) and .meta.json (the zip's hash and mtime). Run: .venv/bin/python -I scripts/extract_irs.py
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import pandas as pd
from lxml import etree

from ..core.paths import CACHE, RAW
from ..core.provenance import local_file_meta

DIR = RAW / "irs_990pf"
OUT = CACHE / "irs990"
NS = {"e": "http://www.irs.gov/efile"}
# US-address grants kept only when the recipient may re-grant to India (help file trap 2): flagged indirect, never counted
INDIRECT = re.compile(r"\bindia\b|give ?2 ?asia|charities aid foundation america|globalgiving|tides foundation", re.I)
INDIVIDUAL = "individual recipient"
PARSER = etree.XMLParser(resolve_entities=False, no_network=True, huge_tree=False, remove_blank_text=True)


def _t(node, path: str) -> str:
    r = node.xpath(path, namespaces=NS)
    return (r[0].text or "").strip() if r and r[0] is not None and r[0].text else ""


def parse_return(xml: bytes, object_id: str) -> tuple[dict, list[dict], int]:
    """(return row, foreign grants, count of US-address grants)."""
    root = etree.fromstring(xml, PARSER)
    h = "e:ReturnHeader"
    ret = {"object_id": object_id,
           "ein": _t(root, f"{h}/e:Filer/e:EIN"),
           "name": _t(root, f"{h}/e:Filer/e:BusinessName/e:BusinessNameLine1Txt"),
           "name2": _t(root, f"{h}/e:Filer/e:BusinessName/e:BusinessNameLine2Txt"),
           "state": _t(root, f"{h}/e:Filer/e:USAddress/e:StateAbbreviationCd"),
           "tax_period_end": _t(root, f"{h}/e:TaxPeriodEndDt"),
           "tax_year": _t(root, f"{h}/e:TaxYr"),
           "grants_paid": _t(root, "e:ReturnData/e:IRS990PF/e:AnalysisOfRevenueAndExpenses/e:ContriPaidRevAndExpnssAmt"),
           "assets_fmv": _t(root, "e:ReturnData/e:IRS990PF/e:Form990PFBalanceSheetsGrp/e:TotalAssetsEOYFMVAmt"),
           "website": _t(root, "e:ReturnData/e:IRS990PF/e:StatementsRegardingActyGrp/e:WebsiteAddressTxt")}
    grants, us = [], 0
    for i, g in enumerate(root.xpath("e:ReturnData/e:IRS990PF/e:SupplementaryInformationGrp/e:GrantOrContributionPdDurYrGrp",
                                     namespaces=NS)):
        # grants to private individuals (scholarships, relief): the person's name and place are never stored (rule 8)
        person = bool(g.xpath("e:RecipientPersonNm", namespaces=NS))
        name = INDIVIDUAL if person else " ".join(
            x for x in (_t(g, "e:RecipientBusinessName/e:BusinessNameLine1Txt"),
                        _t(g, "e:RecipientBusinessName/e:BusinessNameLine2Txt")) if x)
        fa = g.xpath("e:RecipientForeignAddress", namespaces=NS)
        if not fa:
            us += 1
            if not INDIRECT.search(name):
                continue
            ua = g.xpath("e:RecipientUSAddress", namespaces=NS)
            fa, country = (ua[0] if ua else g), "US"
        else:
            fa = fa[0]
            country = _t(fa, "e:CountryCd")
        grants.append({"object_id": object_id, "ein": ret["ein"], "grant_no": i + 1, "recipient": name,
                       "city": "" if person else _t(fa, "e:CityNm"),
                       "province": "" if person else (_t(fa, "e:ProvinceOrStateNm") or _t(fa, "e:StateAbbreviationCd")),
                       "country": country, "status": _t(g, "e:RecipientFoundationStatusTxt"),
                       "purpose": _t(g, "e:GrantOrContributionPurposeTxt"), "amount": _t(g, "e:Amt")})
    ret["n_grants_us"], ret["n_grants_foreign"] = us, sum(1 for x in grants if x["country"] != "US")
    return ret, grants, us


def _pf_ids(year_dir: Path) -> set[str]:
    idx = next(year_dir.glob("index_*.csv"), None)
    if idx is None:
        return set()
    ids = set()
    for ch in pd.read_csv(idx, dtype=str, keep_default_na=False, chunksize=200_000, usecols=lambda c: c.upper() in
                          {"RETURN_TYPE", "OBJECT_ID"}):
        ch.columns = [c.upper() for c in ch.columns]
        ids |= set(ch.loc[ch["RETURN_TYPE"].str.upper() == "990PF", "OBJECT_ID"])
    return ids


def _members(zp: Path, pf_ids: set[str]):
    """Yield (member name, object id, xml bytes) for the 990-PF members of a zip. Some TEOS zips use Deflate64, which
    Python's zipfile cannot read; those members are unpacked with the system unzip (paths junked, so nothing lands
    outside a temporary folder under the cache) in batches, read, and deleted."""
    with zipfile.ZipFile(zp) as z:
        want = []
        for m in z.infolist():
            base = m.filename.rsplit("/", 1)[-1]
            oid = base[: -len("_public.xml")] if base.endswith("_public.xml") else ""
            if oid in pf_ids:
                want.append((m, oid))
        if all(m.compress_type in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED) for m, _ in want):
            for m, oid in want:
                yield m.filename, oid, z.read(m)
            return
    unz = shutil.which("unzip")
    if not unz:
        raise RuntimeError(f"{zp.name} uses Deflate64; install unzip (Info-ZIP 6) to read it")
    OUT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=OUT, prefix=f"tmp_{zp.stem}_") as tmp:
        for i in range(0, len(want), 500):
            batch = want[i:i + 500]
            # these zips have a central-directory quirk: unzip warns and exits 3 but still extracts the members,
            # so the exit code is not trusted; each member is checked instead and a missing one is reported
            rc = subprocess.run([unz, "-qq", "-o", "-j", str(zp), *[m.filename for m, _ in batch], "-d", tmp],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
            if rc not in (0, 1, 2, 3):
                raise RuntimeError(f"unzip failed on {zp.name} (exit {rc})")
            for m, oid in batch:
                f = Path(tmp) / m.filename.rsplit("/", 1)[-1]
                if not f.exists() or f.stat().st_size != m.file_size:
                    yield m.filename, oid, None
                    continue
                yield m.filename, oid, f.read_bytes()
                f.unlink()


def extract_zip(zp: Path, pf_ids: set[str]) -> tuple[Path, Path]:
    st = zp.stat()
    tag = f"{st.st_size}_{int(st.st_mtime)}"
    ro, go = OUT / f"{zp.stem}.{tag}.returns.csv", OUT / f"{zp.stem}.{tag}.grants.csv"
    mo = OUT / f"{zp.stem}.{tag}.meta.json"
    if ro.exists() and go.exists() and mo.exists():
        return ro, go
    rets, grants, errors = [], [], 0
    missing = 0
    for name, oid, xml in _members(zp, pf_ids):
        if xml is None:
            missing += 1
            continue
        try:
            r, g, _ = parse_return(xml, oid)
        except etree.XMLSyntaxError:
            errors += 1
            continue
        r["zip"], r["member"] = zp.name, name
        rets.append(r)
        grants += [{**x, "zip": zp.name} for x in g]
    OUT.mkdir(parents=True, exist_ok=True)
    for old in [*OUT.glob(f"{zp.stem}.*.csv"), *OUT.glob(f"{zp.stem}.*.json")]:
        old.unlink()
    meta = local_file_meta(zp)  # hashed once here, not on every build
    mo.write_text(json.dumps({"retrieved_at": meta["retrieved_at"], "file_hash": meta["file_hash"]}))
    pd.DataFrame(rets).to_csv(ro.with_suffix(".part"), index=False)
    pd.DataFrame(grants, columns=["object_id", "ein", "grant_no", "recipient", "city", "province", "country", "status",
                                  "purpose", "amount", "zip"]).to_csv(go.with_suffix(".part"), index=False)
    ro.with_suffix(".part").rename(ro)
    go.with_suffix(".part").rename(go)
    if errors or missing:
        print(f"{zp.name}: {errors} unparseable, {missing} not extracted", file=sys.stderr)
    return ro, go


def zips() -> list[tuple[Path, Path]]:
    """(zip, its year dir) for complete zips (curl writes in place, so a zip is only read once the index file for
    its year exists and the zip opens cleanly)."""
    out = []
    for yd in sorted(p for p in DIR.glob("20*") if p.is_dir()):
        for zp in sorted(yd.glob("*.zip")):
            out.append((zp, yd))
    return out


def extract_all(workers: int = 8) -> list[tuple[Path, Path]]:
    jobs = []
    ids_by_year = {}
    for zp, yd in zips():
        if yd not in ids_by_year:
            ids_by_year[yd] = _pf_ids(yd)
        if not ids_by_year[yd]:
            print(f"skip {zp.name}: no index for {yd.name}", file=sys.stderr)
            continue
        try:
            zipfile.ZipFile(zp).close()
        except zipfile.BadZipFile:
            print(f"skip {zp.name}: incomplete zip", file=sys.stderr)
            continue
        jobs.append((zp, ids_by_year[yd]))
    with ProcessPoolExecutor(max_workers=workers) as ex:
        res = list(ex.map(extract_zip, [j[0] for j in jobs], [j[1] for j in jobs]))
    for (zp, _), (ro, _) in zip(jobs, res):
        print(f"{zp.name}: {sum(1 for _ in open(ro)) - 1} 990-PF returns", file=sys.stderr)
    return res


def zip_meta() -> dict[str, dict]:
    """{zip file name: {retrieved_at, file_hash}} recorded at extraction."""
    return {p.name.split(".")[0] + ".zip": json.loads(p.read_text()) for p in sorted(OUT.glob("*.meta.json"))}


def load() -> tuple[pd.DataFrame, pd.DataFrame]:
    """All extracted returns and foreign grants (cache only; run extract_all first)."""
    rs = sorted(OUT.glob("*.returns.csv"))
    gs = sorted(OUT.glob("*.grants.csv"))
    if not rs:
        return pd.DataFrame(), pd.DataFrame()
    r = pd.concat([pd.read_csv(p, dtype=str, keep_default_na=False) for p in rs], ignore_index=True)
    g = pd.concat([pd.read_csv(p, dtype=str, keep_default_na=False) for p in gs], ignore_index=True)
    return r, g


if __name__ == "__main__":
    extract_all()

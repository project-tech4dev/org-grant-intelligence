"""Provenance: file hashing, cached and polite fetching, evidence and sources_log writers."""
import hashlib
import json
import time
import urllib.robotparser
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd
import requests
import truststore

# verify TLS against the OS trust store: some gov.in sites send incomplete chains that the OS completes (still verified)
truststore.inject_into_ssl()

from . import schema
from .paths import RAW

USER_AGENT = "funder-pool-research/0.1"
MIN_INTERVAL_S = 2.0
_last_hit: dict[str, float] = {}
_robots: dict[str, urllib.robotparser.RobotFileParser] = {}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def file_hash(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while b := f.read(chunk):
            h.update(b)
    return "sha256:" + h.hexdigest()


class RobotsDisallowed(Exception):
    pass


def robots_allows(url: str, session: requests.Session | None = None) -> bool:
    p = urlparse(url)
    base = f"{p.scheme}://{p.netloc}"
    if base not in _robots:
        rp = urllib.robotparser.RobotFileParser()
        try:
            r = (session or requests).get(base + "/robots.txt", headers={"User-Agent": USER_AGENT}, timeout=20)
            rp.parse(r.text.splitlines() if r.status_code == 200 else [])
        except requests.RequestException:
            rp.parse([])
        _robots[base] = rp
    return _robots[base].can_fetch(USER_AGENT, url)


def _throttle(host: str, interval: float) -> None:
    wait = _last_hit.get(host, 0) + interval - time.monotonic()
    if wait > 0:
        time.sleep(wait)
    _last_hit[host] = time.monotonic()


def cached_fetch(url: str, source_key: str, filename: str, *, raw_dir: Path = RAW, refresh: bool = False,
                 interval: float = MIN_INTERVAL_S, session: requests.Session | None = None,
                 timeout: float = 120) -> dict:
    """Download url once into raw/<source_key>/<filename>; reuse the cache afterwards.
    Returns metadata {path, url, retrieved_at, file_hash}. Metadata is stored next to the file so reruns are identical."""
    dest = raw_dir / source_key / filename
    meta_path = dest.with_suffix(dest.suffix + ".meta.json")
    if dest.exists() and meta_path.exists() and not refresh:
        return {**json.loads(meta_path.read_text()), "path": dest}
    if not robots_allows(url, session):
        raise RobotsDisallowed(url)
    _throttle(urlparse(url).netloc, interval)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with (session or requests).get(url, headers={"User-Agent": USER_AGENT}, timeout=timeout, stream=True) as r:
        r.raise_for_status()
        tmp = dest.with_suffix(dest.suffix + ".part")
        with open(tmp, "wb") as f:
            for chunk in r.iter_content(1 << 20):
                f.write(chunk)
        tmp.replace(dest)
    meta = {"url": url, "retrieved_at": now_iso(), "file_hash": file_hash(dest)}
    meta_path.write_text(json.dumps(meta, indent=2))
    return {**meta, "path": dest}


def local_file_meta(path: Path, url: str = "") -> dict:
    """Provenance for a manual or seed file: retrieved_at is the file's mtime so reruns are identical."""
    st = path.stat()
    ts = datetime.fromtimestamp(st.st_mtime, timezone.utc).replace(microsecond=0).isoformat()
    return {"path": path, "url": url or f"file://{path.name}", "retrieved_at": ts, "file_hash": file_hash(path)}


@dataclass
class Ledger:
    """Collects evidence rows and sources_log rows for one utility run."""
    evidence: list[dict] = field(default_factory=list)
    sources: list[dict] = field(default_factory=list)

    def add_evidence(self, **row) -> None:
        missing = [k for k in schema.PROVENANCE_REQUIRED if not row.get(k)]
        if missing:
            raise ValueError(f"evidence row missing provenance {missing}: {row.get('funder_id')}")
        raw = str(row.get("basis", "") or "")
        row["basis"] = schema.basis_enum(raw)
        if raw and raw.lower() != row["basis"]:  # keep the detail: the schema's basis is an enum
            row["measure"] = f"{row.get('measure', '')} ({raw})".strip()
        self.evidence.append({c: row.get(c, "") for c in schema.EVIDENCE})

    def log_source(self, source_key: str, source_name: str, url: str, access_method: str, status: str,
                   reason: str = "", retrieved_at: str = "", file_hash: str = "", rows_read: int | str = "",
                   terms_checked: str = "no", notes: str = "") -> None:
        if access_method not in schema.ALLOWED["access_method"] or status not in schema.ALLOWED["status"]:
            raise ValueError(f"bad access_method/status: {access_method}/{status}")
        if status in {"blocked", "skipped"} and not reason:
            raise ValueError(f"{source_key}: {status} needs a reason")
        self.sources.append(dict(source_key=source_key, source_name=source_name, url=url,
                                 access_method=access_method, status=status, reason=reason,
                                 retrieved_at=retrieved_at, file_hash=file_hash, rows_read=rows_read,
                                 terms_checked=terms_checked, notes=notes))

    def evidence_df(self) -> pd.DataFrame:
        df = pd.DataFrame(self.evidence, columns=schema.EVIDENCE)
        return df.sort_values(["funder_id", "source_key", "year_or_period", "row_ref"], kind="stable").reset_index(drop=True)

    def sources_df(self) -> pd.DataFrame:
        return pd.DataFrame(self.sources, columns=schema.SOURCES_LOG)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8", lineterminator="\n")

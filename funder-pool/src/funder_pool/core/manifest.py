"""Check data/manual/ against manual/MANIFEST.md."""
import re
from dataclasses import dataclass
from pathlib import Path

from .paths import MANUAL, ROOT

MANIFEST_MD = ROOT / "manual" / "MANIFEST.md"

# Files whose names carry a year or are folders get a pattern.
PATTERNS = {
    "M8": r"hurun_india_philanthropy_list_\d{4}\.(pdf|xlsx|csv)$",
    "M10": r"(mca_csr_export_FY\d{4}-\d{2}\.csv|CSRAnalytics-Report-FY-\d{4}-\d{4}\.xlsx)$",  # CSRAnalytics accepted as substitute (user, 2026-11-25)
    "M12": r"fcra_portal$",
}


@dataclass
class Entry:
    id: str
    name: str
    needed_by: str
    required: str
    found: list[str]

    @property
    def present(self) -> bool:
        return bool(self.found)


def parse_manifest(md: Path = MANIFEST_MD) -> list[tuple[str, str, str, str]]:
    rows = []
    for line in md.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(M\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
        if m:
            rows.append(m.groups())
    return rows


def check(manual_dir: Path = MANUAL, md: Path = MANIFEST_MD) -> list[Entry]:
    names = sorted(p.name for p in manual_dir.iterdir()) if manual_dir.exists() else []
    out = []
    for mid, name, needed, req in parse_manifest(md):
        pat = PATTERNS.get(mid, re.escape(name.rstrip("/")) + "$")
        out.append(Entry(mid, name, needed, req, [n for n in names if re.match(pat, n)]))
    return out


def format_report(entries: list[Entry]) -> str:
    lines = ["id   status   required        file"]
    for e in entries:
        lines.append(f"{e.id:<4} {'present' if e.present else 'MISSING':<8} {e.required[:15]:<15} "
                     f"{', '.join(e.found) if e.found else e.name}")
    return "\n".join(lines)

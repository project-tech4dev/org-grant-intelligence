"""Extract 990-PF returns and foreign grants from the downloaded TEOS zips into data/cache/irs990/.

Run from funder-pool/ in isolated mode (the zips are untrusted downloads):
    .venv/bin/python -I scripts/extract_irs.py [workers]
Zips still downloading (no central directory yet) are skipped; rerun when the download finishes. Finished zips are cached.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from funder_pool.sources import irs990  # noqa: E402

if __name__ == "__main__":
    irs990.extract_all(int(sys.argv[1]) if len(sys.argv) > 1 else 4)

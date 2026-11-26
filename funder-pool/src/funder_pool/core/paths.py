from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]          # funder-pool/
CONFIG = ROOT / "config"
DATA = ROOT / "data"
RAW = DATA / "raw"
MANUAL = DATA / "manual"
CACHE = DATA / "cache"
SEEDS = ROOT / "seeds"

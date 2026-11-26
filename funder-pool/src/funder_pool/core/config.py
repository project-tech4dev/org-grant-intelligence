"""Load weights.yaml, thresholds.yaml, theme_map.yaml and fx_rates.yaml."""
from functools import lru_cache
from pathlib import Path
import yaml
from .paths import CONFIG

CATEGORIES = ["western_funders", "indian_csr", "hni_family", "government_india", "bilateral_multilateral"]


def load_yaml(name: str, config_dir: Path = CONFIG) -> dict:
    with open(config_dir / name, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


@lru_cache(maxsize=None)
def weights() -> dict:
    return load_yaml("weights.yaml")


@lru_cache(maxsize=None)
def thresholds() -> dict:
    return load_yaml("thresholds.yaml")


def category_weights(category: str, cfg: dict | None = None) -> dict[str, float]:
    cfg = cfg if cfg is not None else weights()
    if category not in cfg:
        raise KeyError(f"no weights for category {category!r}")
    w = {k: float(v) for k, v in cfg[category].items()}
    total = sum(w.values())
    if abs(total - 100) > 1e-6:
        raise ValueError(f"weights for {category} sum to {total}, expected 100")
    return w

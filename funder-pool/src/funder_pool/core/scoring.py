"""Weighted percentile score within a category (config/weights.yaml)."""
import numpy as np
import pandas as pd

from . import config


def score(signals: pd.DataFrame, category: str, *, weights_cfg: dict | None = None) -> pd.DataFrame:
    """signals: one row per funder with 'funder_id' and one column per weight key. NaN = unknown.
    Booleans are treated as 0/1. Adds score_total, rank_in_category, unknown_signals and blank priority_band."""
    cfg = weights_cfg if weights_cfg is not None else config.weights()
    w = config.category_weights(category, cfg)
    penalty = float(cfg.get("unknown_signal_penalty", 0.5))
    out = signals.copy()
    total = pd.Series(0.0, index=out.index)
    unknown = {i: [] for i in out.index}
    for sig, wt in w.items():
        col = out[sig] if sig in out.columns else pd.Series(np.nan, index=out.index)
        col = pd.to_numeric(col.map(lambda v: {True: 1, False: 0, "true": 1, "false": 0}.get(v, v)), errors="coerce")
        known = col.notna()
        pct = col[known].rank(pct=True, method="average")
        fill = penalty * (float(pct.median()) if len(pct) else 0.5)
        pct = pct.reindex(out.index).fillna(fill)
        total += pct * wt
        for i in out.index[~known]:
            unknown[i].append(sig)
    out["score_total"] = total.round(4)
    out["unknown_signals"] = [ "|".join(unknown[i]) for i in out.index]
    order = out.sort_values(["score_total", "funder_id"], ascending=[False, True], kind="stable").index
    out.loc[order, "rank_in_category"] = range(1, len(order) + 1)
    out["rank_in_category"] = out["rank_in_category"].astype(int)
    out["priority_band"] = ""
    return out

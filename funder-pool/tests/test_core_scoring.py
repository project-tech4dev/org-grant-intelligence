import numpy as np
import pandas as pd
from funder_pool.core import scoring

CFG = {"unknown_signal_penalty": 0.5, "cat": {"a": 60, "b": 40}}


def test_percentile_scoring_and_ranks():
    df = pd.DataFrame({"funder_id": ["x", "y", "z", "w"], "a": [10, 20, 30, np.nan], "b": [True, False, True, True]})
    out = scoring.score(df, "cat", weights_cfg=CFG).set_index("funder_id")
    assert out.loc["z", "rank_in_category"] == 1
    # unknown 'a' gets half the median known percentile: median of (1/3, 2/3, 1) = 2/3 -> 1/3; b: three tied Trues of four -> 0.75
    assert np.isclose(out.loc["w", "score_total"], 60 * (1 / 3) + 40 * 0.75, atol=1e-3)
    assert out.loc["w", "unknown_signals"] == "a"
    assert (out["priority_band"] == "").all()
    assert sorted(out["rank_in_category"]) == [1, 2, 3, 4]


def test_ties_break_by_funder_id_and_deterministic():
    df = pd.DataFrame({"funder_id": ["b", "a"], "a": [1, 1], "b": [1, 1]})
    r1 = scoring.score(df, "cat", weights_cfg=CFG)
    r2 = scoring.score(df.iloc[::-1], "cat", weights_cfg=CFG)
    assert r1.set_index("funder_id")["rank_in_category"].to_dict() == {"a": 1, "b": 2}
    assert r1.sort_values("funder_id").equals(r2.sort_values("funder_id"))


def test_real_weights_sum_to_100():
    from funder_pool.core import config
    for cat in config.CATEGORIES:
        assert sum(config.category_weights(cat).values()) == 100

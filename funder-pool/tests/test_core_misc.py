import json
from datetime import date

import pandas as pd
import pytest

from conftest import FIXTURES
from funder_pool.core import config, fiscal, fx, manifest, provenance, report, themes


def test_fiscal_year():
    assert fiscal.fiscal_year(date(2024, 3, 31)) == "FY2023-24"
    assert fiscal.fiscal_year("2024-04-01") == "FY2024-25"
    assert fiscal.fiscal_year("1999-12-01") == "FY1999-00"
    assert fiscal.fy_start_year("FY2023-24") == 2023


def test_fx():
    usd, r, src = fx.to_usd(8368, "INR", 2024)
    assert r == 83.6693 and round(usd) == 100 and src
    assert fx.to_usd(5, "usd", 2020)[0] == 5
    with pytest.raises(KeyError):
        fx.rate("XYZ", 2020)
    assert fx.inr_to_crore(25_000_000) == 2.5
    assert config.load_yaml("fx_rates.yaml")["status"] == "official"


def test_themes():
    assert themes.classify("12220") == "hunger_poverty_health"
    assert themes.classify("15170") == "gender_equality"
    assert themes.classify("99810", "Scholarships for girls") == "education_livelihood"
    assert themes.classify(None, "Flood relief in Assam") == "disaster_management"
    assert themes.classify(None, "general operating support") == ""


def test_manifest(tmp_path):
    (tmp_path / "oecd_pp4d_crs_2023.csv").write_text("x")
    (tmp_path / "hurun_india_philanthropy_list_2025.pdf").write_text("x")
    (tmp_path / "CSRAnalytics-Report-FY-2014-2025.xlsx").write_text("x")
    e = {x.id: x for x in manifest.check(manual_dir=tmp_path)}
    assert len(e) == 13
    assert e["M1"].present and e["M8"].present and e["M10"].present
    assert not e["M11"].present
    assert "MISSING" in manifest.format_report(list(e.values()))


def test_ledger_and_local_meta(tmp_path):
    f = tmp_path / "seed.csv"
    f.write_text("a,b\n1,2\n")
    meta = provenance.local_file_meta(f)
    assert meta["file_hash"].startswith("sha256:") and meta == provenance.local_file_meta(f)
    led = provenance.Ledger()
    led.add_evidence(funder_id="x", source_key="manual_seed", source_url=meta["url"],
                     retrieved_at=meta["retrieved_at"], file_hash=meta["file_hash"], row_ref="row 2")
    with pytest.raises(ValueError):
        led.add_evidence(funder_id="y", source_key="iati")
    led.log_source("iati", "IATI", "u", "api", "used", rows_read=3)
    with pytest.raises(ValueError):
        led.log_source("oecd", "OECD", "u", "download", "blocked")      # blocked needs a reason
    assert len(led.evidence_df()) == 1 and len(led.sources_df()) == 1


def test_cached_fetch_uses_cache_without_network(tmp_path, monkeypatch):
    d = tmp_path / "iati"
    d.mkdir()
    (d / "f.csv").write_text("x")
    (d / "f.csv.meta.json").write_text(json.dumps({"url": "u", "retrieved_at": "t", "file_hash": "h"}))
    monkeypatch.setattr(provenance, "robots_allows", lambda *a, **k: pytest.fail("network used"))
    assert provenance.cached_fetch("u", "iati", "f.csv", raw_dir=tmp_path)["file_hash"] == "h"


def test_cached_fetch_respects_robots(tmp_path, monkeypatch):
    monkeypatch.setattr(provenance, "robots_allows", lambda *a, **k: False)
    with pytest.raises(provenance.RobotsDisallowed):
        provenance.cached_fetch("https://example.org/search", "x", "y.csv", raw_dir=tmp_path)


def test_distribution_report():
    df = pd.DataFrame({"funder_id": list("abcd"), "name": list("ABCD"),
                       "india_usd_best": [2_000_000, 60_000, None, None],
                       "total_giving_usd_5y": [None, None, 5e6, 1e6],
                       "india_evidence_status": ["known_positive", "known_positive", "unknown", "unknown"],
                       "ingest_readiness": [3, 2, 0, 1], "rank_in_category": [1, 2, 3, 4], "score_total": [90, 60, 30, 20],
                       "sources": ["x"] * 4})
    md = report.distribution_report(df, "western_funders", value_col="india_usd_best",
                                    bins=config.thresholds()["distribution_bins_usd"], unit="USD")
    assert "| >= 1,000,000 USD | 1 |" in md and "| >= 50,000 USD | 2 |" in md and "| value unknown | 2 |" in md
    assert "## 25 largest unknowns" in md and md.index("| C |") < md.index("| D |")


def test_cli_check_manifest(capsys):
    from funder_pool import cli
    assert cli.main(["check-manifest"]) == 0
    assert "M11" in capsys.readouterr().out

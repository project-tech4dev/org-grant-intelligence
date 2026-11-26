from conftest import FIXTURES
from funder_pool.core import sangam


def test_partial_seed_acceptance_cases():
    """tests/acceptance.md indian_csr 3: HDFC Bank, ITC, TCS yes; Axis, Infosys, Reliance, Tata Steel related."""
    funders, used = sangam.load(export=FIXTURES / "does_not_exist.csv")
    assert used.endswith("sangam_existing_funders_partial.csv")
    for n in ["HDFC Bank Limited", "ITC Limited", "Tata Consultancy Services Limited"]:
        assert sangam.status(n, funders)[0] == "yes", n
    for n in ["Axis Bank Limited", "Infosys Limited", "Reliance India Limited", "Tata Steel Limited"]:
        assert sangam.status(n, funders)[0] == "related", n
    for n in ["Wipro Limited", "Tata Power Company Limited", "Bill & Melinda Gates Foundation"]:
        assert sangam.status(n, funders)[0] == "no", n


def test_export_used_when_present():
    funders, used = sangam.load(export=FIXTURES / "sangam_export.csv")
    assert used.endswith("sangam_export.csv")
    assert sangam.status("HDFC Bank Limited", funders) == ("yes", "HDFC Bank")
    assert sangam.status("X", funders, cin="L65920MH1994PLC080618")[0] == "yes"
    assert sangam.status("ABF", funders)[0] == "yes"
    assert sangam.status("Axis Bank Ltd", funders)[0] == "related"

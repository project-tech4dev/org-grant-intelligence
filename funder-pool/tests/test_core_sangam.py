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


def test_alias_with_comma_not_split_when_semicolons_used():
    """M11 export separates aliases with ';'. 'JPMorgan Chase Bank N.A., India' must stay one alias,
    not create an alias 'India' that matches every '(India) Private Limited' company."""
    assert sangam._split_aliases("JPMCB; JPMorgan Chase Bank N.A., India; JPMSI") == [
        "JPMCB", "JPMorgan Chase Bank N.A., India", "JPMSI"]
    assert sangam._split_aliases("{HDFC Bank Limited,HDFC}") == ["HDFC Bank Limited", "HDFC"]


def test_short_sangam_alias_does_not_match_by_initials():
    """A Sangam acronym alias ('CF', 'RF', 'India') must not match any company whose initials agree."""
    funders = [sangam.SangamFunder("Caring Friends", "other", ["CF", "Mumbai Group of Friends"]),
               sangam.SangamFunder("Reliance Foundation", "corporate_foundation", ["RF", "RIL"]),
               sangam.SangamFunder("J.P. Morgan India Private Limited", "corporate_csr", ["India", "JPMCB"])]
    for n in ["Cosmo Ferrites Limited", "Regent First Private Limited", "A W Faber Castell (India) Private Limited"]:
        assert sangam.status(n, funders)[0] != "yes", n
    assert sangam.status("CF", funders) == ("yes", "Caring Friends")          # exact alias still matches
    assert sangam.status("RIL", funders) == ("yes", "Reliance Foundation")


def test_acronym_edge_cases():
    funders = [sangam.SangamFunder("ITC Limited", "corporate_csr", []),
               sangam.SangamFunder("Shiv Nadar Foundation", "private_foundation", ["SNF"]),
               sangam.SangamFunder("Tata Consultancy Services Limited", "corporate_csr", ["TCS"])]
    assert sangam.status("International Trade Centre (ITC)", funders)[0] == "no"   # parenthetical, Sangam side short
    assert sangam.status("SNF(INDIA) PRIVATE LIMITED", funders)[0] == "no"         # a company, not an acronym
    assert sangam.status("TCS", funders)[0] == "yes"

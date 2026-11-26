from funder_pool.core import matching as m
from funder_pool.core.ids import funder_id, slug


def test_normalise():
    assert m.normalise("Larsen & Toubro Limited") == "larsen toubro"
    assert m.normalise("Tata Consultancy Services (TCS) Limited") == "tata consultancy services"
    assert m.normalise("Brot für die Welt") == m.normalise("Brot fuer die Welt")
    assert m.normalise("Axis Bank Foundation") == "axis bank foundation"   # foundation kept: separate funder
    assert m.stem("Axis Bank Foundation") == m.stem("Axis Bank Ltd.") == "axis bank"


def test_acronym():
    assert m.same_by_acronym("TCS", "Tata Consultancy Services Limited")
    assert m.same_by_acronym("ITC", "Imperial Tobacco Company (ITC) Limited")
    assert not m.same_by_acronym("TCS", "Tata Steel Limited")


def test_match_paths():
    cands = {"1": "Bill & Melinda Gates Foundation", "2": "Gates Foundation Trust", "3": "IKEA Foundation"}
    assert m.match("Bill and Melinda Gates Foundation", cands)[0] == "exact"
    assert m.match("Ikea Foundation.", cands)[0] == "exact"
    assert m.match("Something Else Entirely", cands)[0] == "none"
    d, c = m.match("X", cands, ids={"ein": "562618866"}, candidate_ids={"1": {"ein": "562618866"}})
    assert (d, c[0].key) == ("id", "1")


def test_fuzzy_auto_vs_review():
    cands = {"a": "Michael and Susan Dell Foundation", "b": "Dell Technologies Foundation"}
    d, c = m.match("Michael & Susan Dell Foundatoin", cands)
    assert d == "fuzzy" and c[0].key == "a"
    d, c = m.match("Hewlett Foundation", {"a": "William and Flora Hewlett Foundation", "b": "Hewlett Packard Foundation"})
    assert d in {"ambiguous", "none"}


def test_ids():
    assert slug("Children's Investment Fund Foundation") == "children-s-investment-fund-foundation"
    assert funder_id("ikea foundation", "western_funders") == "ikea-foundation--western_funders"

"""IRS 990-PF parser on a hand-written return that uses the element names confirmed against 2022 TEOS filings."""
from funder_pool.sources import irs990

XML = b"""<?xml version="1.0" encoding="utf-8"?>
<Return xmlns="http://www.irs.gov/efile" returnVersion="2021v4.2">
 <ReturnHeader>
  <TaxPeriodEndDt>2022-12-31</TaxPeriodEndDt>
  <Filer><EIN>123456789</EIN><BusinessName><BusinessNameLine1Txt>EXAMPLE FAMILY FOUNDATION</BusinessNameLine1Txt></BusinessName>
   <USAddress><StateAbbreviationCd>CA</StateAbbreviationCd></USAddress></Filer>
  <TaxYr>2022</TaxYr>
 </ReturnHeader>
 <ReturnData>
  <IRS990PF>
   <AnalysisOfRevenueAndExpenses><ContriPaidRevAndExpnssAmt>500000</ContriPaidRevAndExpnssAmt></AnalysisOfRevenueAndExpenses>
   <Form990PFBalanceSheetsGrp><TotalAssetsEOYFMVAmt>9000000</TotalAssetsEOYFMVAmt></Form990PFBalanceSheetsGrp>
   <StatementsRegardingActyGrp><WebsiteAddressTxt>example.org</WebsiteAddressTxt></StatementsRegardingActyGrp>
   <SupplementaryInformationGrp>
    <GrantOrContributionPdDurYrGrp>
     <RecipientBusinessName><BusinessNameLine1Txt>LOCAL SCHOOL</BusinessNameLine1Txt></RecipientBusinessName>
     <RecipientUSAddress><CityNm>X</CityNm><StateAbbreviationCd>CA</StateAbbreviationCd></RecipientUSAddress>
     <GrantOrContributionPurposeTxt>GENERAL</GrantOrContributionPurposeTxt><Amt>1000</Amt>
    </GrantOrContributionPdDurYrGrp>
    <GrantOrContributionPdDurYrGrp>
     <RecipientBusinessName><BusinessNameLine1Txt>GIVE2ASIA</BusinessNameLine1Txt></RecipientBusinessName>
     <RecipientUSAddress><CityNm>SF</CityNm><StateAbbreviationCd>CA</StateAbbreviationCd></RecipientUSAddress>
     <GrantOrContributionPurposeTxt>RELIEF</GrantOrContributionPurposeTxt><Amt>2000</Amt>
    </GrantOrContributionPdDurYrGrp>
    <GrantOrContributionPdDurYrGrp>
     <RecipientBusinessName><BusinessNameLine1Txt>RURAL HEALTH TRUST</BusinessNameLine1Txt>
      <BusinessNameLine2Txt>INDIA</BusinessNameLine2Txt></RecipientBusinessName>
     <RecipientForeignAddress><CityNm>PUNE</CityNm><ProvinceOrStateNm>MAHARASHTRA</ProvinceOrStateNm><CountryCd>IN</CountryCd></RecipientForeignAddress>
     <RecipientFoundationStatusTxt>NONE</RecipientFoundationStatusTxt>
     <GrantOrContributionPurposeTxt>MATERNAL HEALTH</GrantOrContributionPurposeTxt><Amt>30000</Amt>
    </GrantOrContributionPdDurYrGrp>
    <GrantOrContributionPdDurYrGrp>
     <RecipientPersonNm>JANE STUDENT</RecipientPersonNm>
     <RecipientForeignAddress><CityNm>KOCHI</CityNm><ProvinceOrStateNm>KERALA</ProvinceOrStateNm><CountryCd>IN</CountryCd></RecipientForeignAddress>
     <GrantOrContributionPurposeTxt>SCHOLARSHIP</GrantOrContributionPurposeTxt><Amt>500</Amt>
    </GrantOrContributionPdDurYrGrp>
   </SupplementaryInformationGrp>
  </IRS990PF>
 </ReturnData>
</Return>"""


def test_parse_return():
    ret, grants, us = irs990.parse_return(XML, "1")
    assert (ret["ein"], ret["name"], ret["state"], ret["tax_period_end"]) == ("123456789", "EXAMPLE FAMILY FOUNDATION", "CA", "2022-12-31")
    assert (ret["grants_paid"], ret["assets_fmv"], ret["website"]) == ("500000", "9000000", "example.org")
    assert us == 2 and ret["n_grants_us"] == 2 and ret["n_grants_foreign"] == 2
    # the plain US grant is dropped; the US intermediary is kept as country US; the India grant keeps its address
    assert [(g["recipient"], g["country"], g["grant_no"]) for g in grants][:2] == [("GIVE2ASIA", "US", 2), ("RURAL HEALTH TRUST INDIA", "IN", 3)]
    ind = grants[1]
    assert (ind["city"], ind["province"], ind["amount"], ind["purpose"]) == ("PUNE", "MAHARASHTRA", "30000", "MATERNAL HEALTH")


def test_entities_not_resolved():
    evil = b'<?xml version="1.0"?><!DOCTYPE r [<!ENTITY x SYSTEM "file:///etc/passwd">]>' \
           b'<Return xmlns="http://www.irs.gov/efile"><ReturnHeader><Filer><EIN>&x;</EIN></Filer></ReturnHeader></Return>'
    ret, _, _ = irs990.parse_return(evil, "2")
    assert "root" not in ret["ein"]


def test_individual_recipient_not_stored():
    _, grants, _ = irs990.parse_return(XML, "1")
    p = grants[2]
    assert (p["recipient"], p["city"], p["province"], p["country"], p["amount"]) == ("individual recipient", "", "", "IN", "500")
    assert b"JANE" not in repr(grants).encode()

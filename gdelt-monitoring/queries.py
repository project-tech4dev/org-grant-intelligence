"""
Named, reusable GDELT queries for tracking CSOs, FCRA actions, and funders
in North East India.

Query text is copied verbatim from the source doc. The `keyword=` parameter
on gdeltdoc's Filters class can only build a single OR group, so queries that
need (OR group) AND (OR group) are built as raw query text and passed
directly as a query_params entry instead of going through `keyword=`.

Note: the source doc warns that boolean strings with five or six ORs get
unreliable. cso_ngo_activity and fcra_actions exceed that here because
they're copied as-is from the doc -- trim the OR list if results look thin.
"""

QUERIES = {
    "cso_ngo_activity": (
        '("North East India" OR Assam OR Meghalaya OR Nagaland OR Manipur OR '
        'Tripura OR "Arunachal Pradesh" OR Mizoram OR Sikkim) '
        '(NGO OR "civil society" OR "non-profit" OR "voluntary organisation")'
    ),
    "fcra_actions": (
        'FCRA ("registration cancelled" OR "licence cancelled" OR '
        '"licence suspended" OR "FCRA renewal" OR "prior permission" OR '
        '"show cause notice")'
    ),
    "fcra_policy": (
        '("FCRA amendment" OR "Foreign Contribution Regulation Rules")'
    ),
    "funders_grants": (
        '("grant" OR "funding announcement" OR "awarded a grant" OR '
        '"philanthropic support") (Assam OR "North East India" OR Nagaland OR '
        'Meghalaya)'
    ),
}

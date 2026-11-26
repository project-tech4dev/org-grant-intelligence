"""Indian fiscal year labels (April to March), Sangam format FYyyyy-yy."""
from datetime import date, datetime


def fiscal_year(d: date | datetime | str) -> str:
    if isinstance(d, str):
        d = datetime.fromisoformat(d[:10]).date()
    start = d.year if d.month >= 4 else d.year - 1
    return f"FY{start}-{str(start + 1)[-2:]}"


def fy_start_year(label: str) -> int:
    """'FY2023-24' -> 2023."""
    return int(label[2:6])

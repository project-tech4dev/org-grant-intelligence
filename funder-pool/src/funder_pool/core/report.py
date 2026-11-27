"""distribution_report.md for one utility."""
import pandas as pd


def _num(s):
    return pd.to_numeric(s, errors="coerce")


def _table(rows: list[list], header: list[str]) -> str:
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    lines += ["| " + " | ".join("" if pd.isna(c) else str(c) for c in r) + " |" for r in rows]
    return "\n".join(lines)


def distribution_report(df: pd.DataFrame, category: str, *, value_col: str, bins: list[float], unit: str,
                        size_col: str = "total_giving_usd_5y", notes: list[str] | None = None) -> str:
    """df: pool joined with signals. Counts funders at or above each bin of value_col."""
    v = _num(df.get(value_col, pd.Series(dtype=float)))
    out = [f"# Distribution report: {category}", "",
           f"Funders in pool: **{len(df)}**. Priority bands are not assigned; set cutoffs after reading this.", ""]
    if notes:
        out += ["## Notes", "", *[f"- {n}" for n in notes], ""]
    rows = [[f">= {b:,.0f} {unit}", int((v >= b).sum())] for b in bins]
    rows.append([f"value known, < {bins[0]:,.0f} {unit}", int(((v < bins[0]) & v.notna()).sum())])
    rows.append(["value unknown", int(v.isna().sum())])
    out += [f"## Funders by {value_col} ({unit})", "", _table(rows, ["threshold", "funders"]), ""]
    for col in ["india_evidence_status", "ingest_readiness", "in_sangam", "funder_type_draft"]:
        if col in df.columns:
            c = df[col].astype(str).replace({"": "(blank)", "nan": "(blank)"}).value_counts().sort_index()
            out += [f"## Counts by {col}", "", _table([[k, n] for k, n in c.items()], [col, "funders"]), ""]
    cols = [c for c in ["rank_in_category", "name", "score_total", value_col, "india_evidence_status",
                        "ingest_readiness", "in_sangam"] if c in df.columns]
    top = df.sort_values("rank_in_category").head(25) if "rank_in_category" in df.columns else df.head(25)
    out += ["## Top 25 by score", "", _table(top[cols].values.tolist(), cols), ""]
    if "india_evidence_status" in df.columns and size_col in df.columns:
        unk = df[df["india_evidence_status"] == "unknown"].assign(_s=_num(df[size_col]))
        unk = unk[unk["_s"].notna()].sort_values(["_s", "funder_id"], ascending=[False, True]).head(25)
        ucols = [c for c in ["name", size_col, "rank_in_category", "sources"] if c in df.columns]
        out += [f"## 25 largest unknowns by {size_col}", "",
                _table(unk[ucols].values.tolist(), ucols) if len(unk) else "_No unknown funders with a known size._", ""]
    return "\n".join(out)

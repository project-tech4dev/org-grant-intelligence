"""Refresh config/fx_rates.yaml from the World Bank WDI official exchange rate
(PA.NUS.FCRF, LCU per USD, period average). Run: .venv/bin/python scripts/refresh_fx.py"""
import datetime, json, pathlib, time, urllib.request

CODES = {"INR": "IND", "EUR": "EMU", "GBP": "GBR", "CHF": "CHE", "JPY": "JPN",
         "SEK": "SWE", "NOK": "NOR", "DKK": "DNK", "CAD": "CAN", "AUD": "AUS"}
URL = "https://api.worldbank.org/v2/country/{}/indicator/PA.NUS.FCRF?format=json&date=2009:2025&per_page=50"
out = pathlib.Path(__file__).resolve().parents[1] / "config" / "fx_rates.yaml"
lines, missing = [], []
for cur, iso in CODES.items():
    req = urllib.request.Request(URL.format(iso), headers={"User-Agent": "funder-pool-research/0.1"})
    for attempt in range(4):
        try:
            data = json.load(urllib.request.urlopen(req, timeout=90)); break
        except Exception:
            if attempt == 3: raise
            time.sleep(5 * (attempt + 1))
    vals = {int(r["date"]): round(r["value"], 4) for r in data[1] if r["value"] is not None}
    missing += [f"{cur} {y}" for y in range(2009, 2026) if y not in vals]
    lines.append(f"  {cur}: {{{', '.join(f'{y}: {v}' for y, v in sorted(vals.items()))}}}")
    time.sleep(1)
hdr = f"""# Annual average exchange rates, units of currency per 1 USD.
# Source: World Bank WDI, PA.NUS.FCRF (official exchange rate, period average). Retrieved {datetime.date.today()}.
# Regenerate with scripts/refresh_fx.py. Missing years: {', '.join(missing) or 'none'} (fx.rate raises KeyError for these).
status: official
source: "World Bank WDI PA.NUS.FCRF, https://api.worldbank.org/v2/country/<ISO3>/indicator/PA.NUS.FCRF, retrieved {datetime.date.today()}"
rates:
"""
out.write_text(hdr + "\n".join(lines) + "\n")
print(out.read_text())

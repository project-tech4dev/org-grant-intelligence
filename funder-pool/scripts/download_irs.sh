#!/usr/bin/env bash
# Downloads IRS Form 990 series XML (TEOS) for filing years 2022-2026 (~19 GB)
# into data/raw/irs_990pf/<year>/, plus the EO BMF extract into data/raw/irs_bmf/.
# Resumable and idempotent: a file whose local size equals the server's Content-Length is skipped; a partial one resumes.
# Usage (from funder-pool/):  bash scripts/download_irs.sh [years...]
#   e.g. bash scripts/download_irs.sh 2024 2025 2026   # last 3 years only (~12 GB)
# IRS_PARALLEL (default 3) sets how many files download at once; keep it small to be polite to irs.gov.
set -euo pipefail
cd "$(dirname "$0")/.."
years="${*:-2022 2023 2024 2025 2026}"
par="${IRS_PARALLEL:-3}"

fetch() {  # url dest
  local url="$1" dest="$2" remote local_size
  remote=$(curl -fsIL "$url" | tr -d '\r' | awk 'tolower($1)=="content-length:"{n=$2} END{print n}')
  local_size=$(stat -f%z "$dest" 2>/dev/null || stat -c%s "$dest" 2>/dev/null || echo 0)
  if [ -n "$remote" ] && [ "$local_size" = "$remote" ]; then echo "ok   $dest"; return 0; fi
  echo ">>   $url"
  curl -fsSL -C - --retry 5 --retry-delay 10 -o "$dest" "$url" && echo "done $dest"
}
export -f fetch

jobs=$(mktemp)
for y in $years; do
  mkdir -p "data/raw/irs_990pf/$y"
  grep "/$y/" scripts/irs_urls.txt | while read -r url; do echo "$url data/raw/irs_990pf/$y/$(basename "$url")"; done >> "$jobs"
done
# EO Business Master File extract (EIN, name, foundation code, NTEE), about 100 MB in four regional files
mkdir -p data/raw/irs_bmf
for i in 1 2 3 4; do echo "https://www.irs.gov/pub/irs-soi/eo$i.csv data/raw/irs_bmf/eo$i.csv" >> "$jobs"; done
xargs -P "$par" -L 1 bash -c 'fetch "$0" "$1"' < "$jobs"
rm -f "$jobs"
echo "Done. Files under data/raw/irs_990pf/ and data/raw/irs_bmf/"

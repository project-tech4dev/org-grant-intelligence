"""
Run named GDELT queries (see queries.py) and store results as CSV.

Usage:
    python3 named_queries.py                        # run every query, timespan=1d
    python3 named_queries.py cso_ngo_activity        # run just one query
    python3 named_queries.py --timespan 7d           # run every query over 7 days
    python3 named_queries.py --retries 3 fcra_policy
"""

import argparse
import logging
import os
import time

import pandas as pd

from gdeltdoc import GdeltDoc, Filters
from gdeltdoc.errors import RateLimitError

from queries import QUERIES

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

# GDELT allows only ~1 request every 5 seconds and seems to extend the
# cooldown after repeated hits, so every call -- first attempt or retry --
# is throttled to at least this many seconds after the previous one.
MIN_QUERY_INTERVAL_SECONDS = 10

logger = logging.getLogger(__name__)

_last_request_time = 0.0


def _throttle(min_interval: float = MIN_QUERY_INTERVAL_SECONDS) -> None:
    """Block until at least `min_interval` seconds have passed since the
    last call to this function, across all queries in this run."""
    global _last_request_time
    elapsed = time.monotonic() - _last_request_time
    if elapsed < min_interval:
        time.sleep(min_interval - elapsed)
    _last_request_time = time.monotonic()


def run_query(name: str, timespan: str = "1d", retries: int = 6) -> pd.DataFrame:
    """Run one of the named queries in queries.py and return the articles
    DataFrame.

    Retries with increasing backoff on GDELT's 429 rate limit rather than
    failing outright. Any other error propagates to the caller.
    """
    if name not in QUERIES:
        raise ValueError(f"Unknown query '{name}'. Choices: {list(QUERIES)}")

    f = Filters(timespan=timespan)
    f.query_params = [QUERIES[name]]

    gd = GdeltDoc()

    delay = 20
    for attempt in range(retries):
        _throttle()
        try:
            return gd.article_search(f)
        except RateLimitError:
            if attempt == retries - 1:
                raise
            logger.warning("rate limited, waiting %ss before retry...", delay)
            time.sleep(delay)
            delay *= 2

    raise RuntimeError(f"exhausted {retries} retries for '{name}'")  # unreachable


def save_results(name: str, df: pd.DataFrame) -> int:
    """
    Append new articles to data/<name>.csv, deduplicated by url.
    Does not re-pull or overwrite history -- only new rows are added, and
    only the url column of any existing history is read to check for
    duplicates rather than loading the whole file into memory.

    Returns the number of genuinely new rows written.
    """
    if df.empty:
        return 0

    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, f"{name}.csv")

    if os.path.exists(path):
        existing_urls = pd.read_csv(path, usecols=["url"])["url"]
        new_rows = df[~df["url"].isin(existing_urls)]
        if not new_rows.empty:
            new_rows.to_csv(path, mode="a", header=False, index=False)
    else:
        new_rows = df
        new_rows.to_csv(path, index=False)

    return len(new_rows)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "names",
        nargs="*",
        choices=list(QUERIES),
        help="Which named queries to run (default: all of them).",
    )
    parser.add_argument(
        "--timespan", default="1d", help="GDELT timespan filter, e.g. 1d, 7d, 1m (default: 1d)."
    )
    parser.add_argument(
        "--retries", type=int, default=6, help="Max retries per query on rate limit (default: 6)."
    )
    args = parser.parse_args()
    names = args.names or list(QUERIES)

    for name in names:
        try:
            df = run_query(name, timespan=args.timespan, retries=args.retries)
        except Exception:
            logger.exception("query '%s' failed, skipping", name)
            continue

        new_count = save_results(name, df)
        logger.info(
            "%s: %d articles fetched, %d new, saved to data/%s.csv",
            name, len(df), new_count, name,
        )
        if len(df):
            logger.info("\n%s", df[["title", "domain", "seendate"]].head().to_string())


if __name__ == "__main__":
    main()

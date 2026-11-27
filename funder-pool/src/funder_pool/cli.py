"""Command line entry: python -m funder_pool.cli <command>."""
import argparse
import sys

from .core import manifest
from .core.config import CATEGORIES


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="funder_pool")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check-manifest", help="list manual files present or missing in data/manual/")
    b = sub.add_parser("build", help="build one utility from cached data")
    b.add_argument("utility", choices=CATEGORIES)
    sub.add_parser("combine", help="Phase 7: merge utilities, dedupe, review workbook")
    args = ap.parse_args(argv)

    if args.cmd == "check-manifest":
        print(manifest.format_report(manifest.check()))
        return 0
    if args.cmd == "build":
        import importlib
        mod = {"western_funders": "western"}.get(args.utility, args.utility)
        out = importlib.import_module(f".utilities.{mod}", __package__).build()
        print(f"{args.utility}: {len(out['pool'])} funders, {len(out['evidence'])} evidence rows, "
              f"{len(out['review_queue'])} review items, {len(out['drop_log'])} dropped/routed")
        return 0
    if args.cmd == "combine":
        from .utilities import combine
        out = combine.build()
        print(f"combined: {len(out['pool_all'])} funders, {len(out['ingest_queue'])} in ingest queue, "
              f"{len(out['cross'])} cross-category pairs, {len(out['review'])} review items")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())

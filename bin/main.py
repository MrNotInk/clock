#!/usr/bin/env python3
"""Command line entry point for the clock app."""

from __future__ import annotations

import argparse
import sys

try:  # `python -m bin.main`
    from .lib import _clock as clock
except ImportError:  # `python bin/main.py`
    from lib import _clock as clock


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="clock",
        description="Print the current time. Designed for i3blocks, handy anywhere.",
    )
    parser.add_argument(
        "-f",
        "--format",
        default=clock.DEFAULT_FORMAT,
        metavar="FMT",
        help="strftime format string (default: %(default)s)",
    )
    parser.add_argument(
        "-u",
        "--utc",
        action="store_true",
        help="print UTC instead of local time",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    moment = clock.now(utc=args.utc)
    try:
        print(clock.timestamp(args.format, moment))
    except ValueError as exc:  # e.g. an unknown %-directive on some platforms
        parser.error(f"invalid format {args.format!r}: {exc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

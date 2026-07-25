"""Command-line interface for reproducible dataset generation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from industrial_ai_toolkit.generator import generate_shift_events


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="industrial-ai")
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate = subparsers.add_parser("generate", help="generate a synthetic shift dataset")
    generate.add_argument("--minutes", type=int, default=480)
    generate.add_argument("--seed", type=int, default=42)
    generate.add_argument("--site", default="demo-site")
    generate.add_argument("--machine", default="press-01")
    generate.add_argument("--output", type=Path, required=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "generate":
        events = generate_shift_events(
            minutes=args.minutes,
            seed=args.seed,
            site_id=args.site,
            machine_id=args.machine,
        )
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", encoding="utf-8") as handle:
            for event in events:
                handle.write(json.dumps(event.to_dict(), sort_keys=True) + "\n")
        print(f"Wrote {len(events)} events to {args.output}")
        return 0

    raise AssertionError("unreachable")


if __name__ == "__main__":
    raise SystemExit(main())

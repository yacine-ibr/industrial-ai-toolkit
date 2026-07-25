#!/usr/bin/env python3
"""Run Industrial AI Benchmark v0.1 against JSONL responses."""

from __future__ import annotations

import argparse
from pathlib import Path

from industrial_ai_toolkit.benchmark import (
    evaluate,
    load_response_records,
    load_scenarios,
    write_report,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--scenarios",
        type=Path,
        default=Path(__file__).with_name("scenarios.json"),
        help="Path to the versioned scenario JSON file.",
    )
    parser.add_argument("--responses", type=Path, required=True, help="JSONL response file.")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("benchmark-report.json"),
        help="Destination for the machine-readable report.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    version, scenarios = load_scenarios(args.scenarios)
    records = load_response_records(args.responses)
    report = evaluate(version, scenarios, records)
    write_report(report, args.output)
    print(f"Benchmark {version}: {len(report.scores)} scenarios")
    print(f"Mean score: {report.mean_score:.1%}")
    print(f"Pass rate:  {report.pass_rate:.1%}")
    print(f"Report:     {args.output}")
    return 0 if report.pass_rate == 1.0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

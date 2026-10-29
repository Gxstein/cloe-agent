"""Command-line interface for Mx Harness."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .cases import load_cases
from .providers import EchoProvider
from .runner import report_dict, run_cases


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="mx-harness", description="Evaluate GenAI responses against cases.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    run_parser = subparsers.add_parser("run", help="run a JSONL evaluation file")
    run_parser.add_argument("cases", type=Path, help="path to a JSONL case file")
    run_parser.add_argument("--output", type=Path, help="write the full JSON report to this path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        cases = load_cases(args.cases)
        results = run_cases(cases, EchoProvider())
        report = report_dict(results)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(
                json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"{status} {result.case_id} ({result.latency_ms:.3f} ms)")
        if result.missing_expectations:
            print(f"  missing: {', '.join(result.missing_expectations)}")

    summary = report["summary"]
    print(
        "\n"
        f"{summary['passed']}/{summary['total']} passed "
        f"({summary['pass_rate']:.0%})"
    )
    if args.output:
        print(f"Report written to {args.output}")
    return 0 if summary["failed"] == 0 else 1

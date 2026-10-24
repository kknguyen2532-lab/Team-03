
"""Command-line entry point for the shared study planner."""

import argparse
from datetime import date
from pathlib import Path
import sys

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def build_parser() -> argparse.ArgumentParser:
    """Build command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Create a study plan from a tasks CSV file."
    )
    parser.add_argument(
        "csv_path",
        type=Path,
        help="Path to the tasks CSV file.",
    )
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study hours.",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="Reference date in YYYY-MM-DD format.",
    )
    return parser


def main() -> int:
    """Run the study planner."""
    parser = build_parser()
    args = parser.parse_args()

    if args.hours <= 0:
        parser.error("--hours must be greater than 0")

    try:
        tasks = parse_csv(args.csv_path)

        if not tasks:
            print("No tasks found in the CSV file.")
            return 0

        prioritized_tasks = prioritise(tasks, args.today)
        blocks = allocate(prioritized_tasks, args.hours)

        print(render(blocks))
        return 0

    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

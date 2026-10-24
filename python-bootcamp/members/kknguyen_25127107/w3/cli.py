import argparse
import math
import sys
from datetime import date
from pathlib import Path

from members.kknguyen_25127107.w2.errors import InfeasiblePlan
from members.kknguyen_25127107.w2.io_utils import load_tasks
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Create a study plan from a tasks CSV file."
    )
    parser.add_argument("csv_path", type=Path, help="path to tasks CSV")
    parser.add_argument(
        "--hours", type=float, required=True, help="available study hours"
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        metavar="YYYY-MM-DD",
        help="reference date (defaults to today)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Load the CSV, build a plan, and return an exit status."""
    args = build_parser().parse_args(argv)

    try:
        tasks = load_tasks(args.csv_path)
    except FileNotFoundError:
        print(f"Error: file not found: {args.csv_path}", file=sys.stderr)
        return 1
    except (OSError, ValueError) as exc:
        print(f"Error: could not read tasks CSV: {exc}", file=sys.stderr)
        return 1

    if not tasks:
        print("Error: the CSV contains no tasks.", file=sys.stderr)
        return 1

    if not math.isfinite(args.hours) or args.hours <= 0:
        needed_h = min(task.effort_h for task in tasks)
        error = InfeasiblePlan(needed_h, args.hours)
        print(f"Error: infeasible plan: {error}", file=sys.stderr)
        return 1

    today = args.today or date.today()
    blocks = allocate(prioritise(tasks, today), args.hours)
    print(f"Tonight ({args.hours:.1f} h):")
    print(render(blocks))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

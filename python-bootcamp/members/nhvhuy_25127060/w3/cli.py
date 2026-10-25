"""Command-line interface for the personal study planner (W3-3)."""

import argparse
from datetime import date
from pathlib import Path
import sys

from ..w2.io_utils import load_tasks  # Đổi thành ..w2.utils nếu bạn giữ tên utils.py
from ..w2.models import Task


def prioritise_tasks(tasks: list[Task], today: date) -> list[Task]:
    """Order tasks by priority (importance / max(days_left, 1)) descending."""
    return sorted(
        tasks,
        key=lambda t: (t.importance / max(t.days_left(today), 1), t.importance),
        reverse=True,
    )


def allocate_hours(
    tasks: list[Task], available_h: float
) -> list[tuple[Task, float]]:
    """Greedily allocate available hours across prioritised tasks."""
    remaining = available_h
    plan: list[tuple[Task, float]] = []

    for task in tasks:
        if remaining <= 0:
            break
        if task.effort_h <= 0:
            continue
        allocated = min(task.effort_h, remaining)
        plan.append((task, allocated))
        remaining -= allocated

    return plan


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Generate a tonight study plan from a tasks CSV file."
    )
    parser.add_argument("csv_path", type=Path, help="Path to tasks CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study hours tonight",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="Reference date in YYYY-MM-DD format (default: today)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the study planner CLI."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.csv_path.is_file():
        print(f"Error: file not found: {args.csv_path}", file=sys.stderr)
        sys.exit(1)

    tasks = load_tasks(args.csv_path)
    ordered = prioritise_tasks(tasks, args.today)
    plan = allocate_hours(ordered, args.hours)

    print(f"Tonight ({args.hours:.1f} h):")
    for idx, (task, hours) in enumerate(plan, start=1):
        dots = "." * max(2, 16 - len(task.title))
        print(f"  {idx}. {task.title} {dots} {hours:.1f} h")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
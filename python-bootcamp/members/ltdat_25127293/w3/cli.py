"""Command line interface for task study planner."""

import argparse
from datetime import date
from pathlib import Path
import sys


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Study planner task allocator")
    parser.add_argument("tasks_file", type=Path, help="Path to tasks CSV file")
    parser.add_argument(
        "--hours", type=float, required=True, help="Available study hours tonight"
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="Base date in YYYY-MM-DD format (default: today)",
    )
    return parser.parse_args(args)


def main() -> None:
    args = parse_args()

    if not args.tasks_file.is_file():
        sys.stderr.write(f"Error: file not found: {args.tasks_file}\n")
        sys.exit(1)

    print(f"Tonight ({args.hours:.1f} h):")


if __name__ == "__main__":
    main()

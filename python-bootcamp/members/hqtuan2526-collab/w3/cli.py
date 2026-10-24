import argparse
import importlib
import sys
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise


def main() -> int:
    """Run the study planner command-line interface."""
    parser = argparse.ArgumentParser(
        description="Create a study plan from a tasks CSV file."
    )
    parser.add_argument("csv_file", help="Path to the tasks CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study hours",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="Reference date in YYYY-MM-DD format (default: today)",
    )
    args = parser.parse_args()

    if args.hours <= 0:
        parser.error("--hours must be greater than 0")

    csv_path = Path(args.csv_file)

    try:
        # The member folder contains a hyphen, so load W2 dynamically.
        io_utils = importlib.import_module("members.hqtuan2526-collab.w2.io_utils")
        tasks = io_utils.load_tasks(csv_path)
    except FileNotFoundError:
        print(f"Error: file not found: {csv_path}", file=sys.stderr)
        return 1
    except (ValueError, OSError) as exc:
        print(f"Error reading CSV: {exc}", file=sys.stderr)
        return 1

    ordered_tasks = prioritise(tasks, args.today)
    blocks = allocate(ordered_tasks, args.hours)

    print(f"Tonight ({args.hours:.1f} h):")
    for index, block in enumerate(blocks, start=1):
        print(f"  {index}. {block.task.title} ........ {block.hours:.1f} h")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

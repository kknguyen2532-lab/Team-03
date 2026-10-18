
import sys
from pathlib import Path

from .io_utils import load_tasks, save_json


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m members.student.w2 <tasks.csv>")
        raise SystemExit(2)

    csv_path = Path(sys.argv[1])

    try:
        tasks = load_tasks(csv_path)

        output_path = csv_path.with_suffix(".json")
        save_json(tasks, output_path)

        print(f"Loaded {len(tasks)} tasks")

        for task in tasks:
            print(
                f"{task.title}: importance={task.importance}, "
                f"effort={task.effort_h}h, deadline={task.deadline}"
            )

        print(f"Saved to {output_path}")

    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()

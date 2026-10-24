from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    bootcamp_root = Path(__file__).resolve().parents[3]
    sample_path = bootcamp_root / "samples" / "tasks.csv"

    try:
        tasks = load_tasks(sample_path)
    except (OSError, ValueError) as exc:
        raise SystemExit(
            f"Could not load sample tasks at {sample_path}: {exc}"
        ) from exc

    for task in tasks:
        print(
            f"{task.title} | importance={task.importance} | "
            f"effort={task.effort_h:g} h | deadline={task.deadline.isoformat()}"
        )


if __name__ == "__main__":
    main()

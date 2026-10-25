import os

from .io_utils import load_tasks


def main():
    current_dir = os.path.dirname(__file__)
    csv_path = os.path.join(current_dir, "sample.csv")

    if not os.path.exists(csv_path):
        print(f"Sample CSV not found at {csv_path}")
        return

    print(f"Loading tasks from {csv_path}...")
    tasks = load_tasks(csv_path)

    print("\n--- Loaded Tasks ---")
    for t in tasks:
        print(
            f"- [Importance: {t.importance}] {t.title} (Effort: {t.effort_h}h, Deadline: {t.deadline})"
        )


if __name__ == "__main__":
    main()

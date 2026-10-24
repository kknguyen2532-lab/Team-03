import csv
from datetime import date
from pathlib import Path

from shared.contract import Task


def parse_csv(path: str | Path) -> list[Task]:
    """Đọc file CSV và chuyển đổi thành danh sách các đối tượng Task."""
    tasks: list[Task] = []
    with open(path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for line_no, row in enumerate(reader, start=2):
            try:
                title = row["title"].strip()
                if not title:
                    raise ValueError("title cannot be empty")

                importance = int(row["importance"])
                if not 1 <= importance <= 5:
                    raise ValueError("importance must be 1-5")

                effort_h = float(row["effort_h"])
                if effort_h <= 0:
                    raise ValueError("effort_h must be positive")

                deadline = date.fromisoformat(row["deadline"].strip())
            except (KeyError, TypeError, ValueError) as exc:
                raise ValueError(f"Invalid row at line {line_no}: {exc}") from exc

            tasks.append(
                Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
            )
    return tasks

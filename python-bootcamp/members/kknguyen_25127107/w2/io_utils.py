import csv
import json
import math
from datetime import date
from pathlib import Path
from typing import Iterable

from .models import Task

_REQUIRED_COLUMNS = ("title", "importance", "effort_h", "deadline")


def load_tasks(path: str | Path) -> list[Task]:
    tasks: list[Task] = []
    with Path(path).open("r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None or any(
            column not in reader.fieldnames for column in _REQUIRED_COLUMNS
        ):
            raise ValueError(
                "line 1: CSV header must contain " + ",".join(_REQUIRED_COLUMNS)
            )

        for row in reader:
            line_number = reader.line_num
            try:
                # A blank row or missing value is treated as an invalid row.
                title = (row.get("title") or "").strip()
                if not title:
                    raise ValueError("title must not be empty")

                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                if not math.isfinite(effort_h) or effort_h < 0:
                    raise ValueError("effort_h must be finite and non-negative")

                deadline_text = (row.get("deadline") or "").strip()
                deadline = date.fromisoformat(deadline_text)
                tasks.append(
                    Task(
                        title=title,
                        importance=importance,
                        effort_h=effort_h,
                        deadline=deadline,
                    )
                )
            except (TypeError, ValueError, KeyError, OverflowError) as exc:
                raise ValueError(f"line {line_number}: {exc}") from exc

    return tasks


def save_json(tasks: Iterable[Task], path: str | Path) -> None:
    data = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]
    with Path(path).open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write("\n")

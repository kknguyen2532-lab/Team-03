
import csv
import json
from datetime import date

from .models import Task


def load_tasks(path) -> list[Task]:
    tasks = []

    with open(path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        required = {"title", "importance", "effort_h", "deadline"}

        if reader.fieldnames is None or not required.issubset(reader.fieldnames):
            raise ValueError("CSV header is missing required columns")

        for line_number, row in enumerate(reader, start=2):
            try:
                task = Task(
                    title=row["title"].strip(),
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"].strip()),
                )

                if not task.title:
                    raise ValueError("title must not be empty")
                if task.effort_h < 0:
                    raise ValueError("effort_h must not be negative")

                tasks.append(task)

            except (ValueError, TypeError, AttributeError) as exc:
                raise ValueError(
                    f"Invalid row at line {line_number}: {exc}"
                ) from exc

    return tasks


def save_json(tasks, path):
    data = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.write("\n")

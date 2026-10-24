import csv
import json
from datetime import date

from .models import Task


def load_tasks(path) -> list[Task]:
    tasks = []

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        required_columns = ["title", "importance", "effort_h", "deadline"]

        if reader.fieldnames != required_columns:
            raise ValueError("line 1: invalid CSV header")

        for row in reader:
            line_number = reader.line_num

            try:
                title = row["title"]
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = date.fromisoformat(row["deadline"])

                if not title:
                    raise ValueError("title cannot be empty")

                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )

                tasks.append(task)

            except (ValueError, TypeError, KeyError) as error:
                raise ValueError(f"line {line_number}: invalid task data") from error

    return tasks


def save_json(tasks: list[Task], path) -> None:
    data = []

    for task in tasks:
        data.append(
            {
                "title": task.title,
                "importance": task.importance,
                "effort_h": task.effort_h,
                "deadline": task.deadline.isoformat(),
            }
        )

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

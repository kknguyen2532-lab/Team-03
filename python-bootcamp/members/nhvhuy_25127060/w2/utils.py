"""CSV and JSON I/O utilities for tasks (W2-2)."""

import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from a CSV file and validate each row."""
    tasks: list[Task] = []

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        required = {"title", "importance", "effort_h", "deadline"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError("CSV is missing required columns")

        for line_number, row in enumerate(reader, start=2):
            try:
                if None in row or any(
                    row.get(key) is None or not row[key].strip() for key in required
                ):
                    raise ValueError("missing or extra fields")

                task = Task(
                    title=row["title"].strip(),
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"].strip()),
                )
                if task.effort_h < 0:
                    raise ValueError("effort_h must be non-negative")

                tasks.append(task)
            except (ValueError, TypeError, KeyError) as exc:
                raise ValueError(f"Invalid data at line {line_number}: {exc}") from exc

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Serialize a list of Task objects to a JSON file."""
    data = []
    for task in tasks:
        item = asdict(task)
        item["deadline"] = task.deadline.isoformat()
        data.append(item)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

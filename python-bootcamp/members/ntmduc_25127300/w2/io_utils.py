import csv
import json
from datetime import date

from .models import Task


def load_tasks(path: str) -> list[Task]:
    tasks = []
    with open(path, mode='r', encoding = 'utf-8') as file:
        reader = csv.reader(file)

        header = next(reader, None)
        if header is None:
            return tasks


    for line_num, row in enumerate(reader, 2):
        if len(row) < 4:
            raise ValueError(f"Line {line_num}: Invalid row format, expected 4 columns")

        title_str, importance_str, effort_str, deadline_str = row

        try:
            imp = int(importance_str)
            eff = float(effort_str)
            dl = date.fromisoformat(deadline_str.strip())

            task = Task(title = title_str.split(), importance=imp, effort_h=eff, deadline=dl)
            tasks.append(task)

        except (ValueError, TypeError) as e:
            raise ValueError(f"Line {line_num}: Invalid data values ({e})")

    return tasks

def save_json(tasks: list[Task], path: str) -> None:
    data = [
        {
            # Các trường của Task cần lưu
        }
        for task in tasks
    ]

    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

import csv
import json
from datetime import date

from .models import Task


def load_tasks(path: str) -> list[Task]:
    """
    Đọc dữ liệu từ file CSV và chuyển đổi thành danh sách các đối tượng Task.

    Args:
        path (str): Đường dẫn đến file CSV cần đọc.

    Returns:
        list[Task]: Danh sách các công việc (Task) được lấy từ file.

    Raises:
        ValueError: Nếu dòng không đủ 4 cột hoặc dữ liệu không đúng định dạng.
    """
    tasks = []
    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)

        header = next(reader, None)
        if header is None:
            return tasks

        # Lưu ý: Tôi đã đưa vòng lặp for này vào trong khối `with open` 
        # để tránh lỗi "I/O operation on closed file" khi đọc file.
        for line_num, row in enumerate(reader, 2):
            if len(row) < 4:
                raise ValueError(f"Line {line_num}: Invalid row format, expected 4 columns")

            title_str, importance_str, effort_str, deadline_str = row

            try:
                imp = int(importance_str)
                eff = float(effort_str)
                dl = date.fromisoformat(deadline_str.strip())

                task = Task(
                    title=title_str.split(), importance=imp, effort_h=eff, deadline=dl
                )
                tasks.append(task)

            except (ValueError, TypeError) as e:
                raise ValueError(f"Line {line_num}: Invalid data values ({e})")

    return tasks


def save_json(tasks: list[Task], path: str) -> None:
    """
    Lưu danh sách các đối tượng Task vào file dưới định dạng JSON.

    Args:
        tasks (list[Task]): Danh sách các công việc cần lưu.
        path (str): Đường dẫn tới file JSON đầu ra.
    """
    data = [
        {
            # Các trường của Task cần lưu
        }
        for task in tasks
    ]

    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
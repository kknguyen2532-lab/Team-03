import sys
from pathlib import Path

from members.ntmduc_25127300.w2.errors import InfeasiblePlan, check_feasible

from .parse import parse_csv


def validate_and_load_tasks(file_path_str: str, available_hours: float):
    file_path = Path(file_path_str)

    if not file_path.is_file():
        print(f"Lỗi: Không tìm thấy file '{file_path}'.", file=sys.stderr)
        sys.exit(1)

    try:
        tasks = parse_csv(file_path)
    except Exception as e: #noqa: BLE001
        print(f"Lỗi khi đọc file CSV: {e}", file=sys.stderr)
        sys.exit(1)

    if not tasks:
        print(f"Lỗi: File '{file_path}' rỗng hoặc không có task nào hợp lệ.", file=sys.stderr)
        sys.exit(1)

    try:
        check_feasible(tasks, available_hours)
    except InfeasiblePlan as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    return tasks
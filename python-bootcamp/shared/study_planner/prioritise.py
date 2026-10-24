from datetime import date

from shared.contract import Task


def prioritise(tasks: list[Task], today: date) -> list[Task]:
    def calculate_score(task: Task) -> float:
        days_left = (task.deadline - today).days
        
        # Xử lý trường hợp deadline là hôm nay hoặc đã quá hạn để tránh lỗi chia cho 0 (ZeroDivisionError)
        safe_days_left = days_left if days_left > 0 else 0.1
        
        # Công thức: importance / days_left
        return task.importance / safe_days_left

    # Sắp xếp danh sách với điểm số cao nhất lên đầu (reverse=True)
    return sorted(tasks, key=calculate_score, reverse=True)
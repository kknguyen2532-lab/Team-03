from .models import Task


class InfeasiblePlan(Exception):
    """
    Ngoại lệ (Exception) tùy chỉnh được ném ra khi tổng thời gian cần thiết
    để hoàn thành các task vượt quá số giờ khả dụng.
    """

    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(self.__str__())

    def __str__(self) -> str:
        return f"Infeasible plan: Needed {self.needed_h}h, but only {self.available_h}h available."


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """
    Kiểm tra tính khả thi của kế hoạch học tập.

    Args:
        tasks (list[Task]): Danh sách các công việc cần làm.
        available_h (float): Tổng số giờ khả dụng.

    Raises:
        InfeasiblePlan: Nếu tổng thời gian cần thiết (needed_h) lớn hơn thời gian khả dụng (available_h).
    """
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)

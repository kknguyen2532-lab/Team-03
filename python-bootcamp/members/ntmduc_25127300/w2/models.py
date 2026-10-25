from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """
    Lớp (dataclass) đại diện cho một công việc hoặc nhiệm vụ học tập.
    """
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self):
        """
        Tự động kiểm tra tính hợp lệ của dữ liệu ngay sau khi khởi tạo đối tượng.
        
        Raises:
            ValueError: Nếu mức độ quan trọng (importance) không nằm trong khoảng 1-5.
        """
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def day_left(self, today: date) -> int:
        """
        Tính số ngày còn lại từ ngày hiện tại cho đến hạn chót (deadline).

        Args:
            today (date): Ngày hiện tại dùng làm mốc để tính toán.

        Returns:
            int: Số ngày còn lại. Trả về 0 nếu ngày hiện tại đã vượt quá hạn chót.
        """
        delta_day = (self.deadline - today).days
        return max(0, delta_day)
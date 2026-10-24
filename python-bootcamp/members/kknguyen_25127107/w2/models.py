from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("title must not be empty")
        if (
            not isinstance(self.importance, int)
            or isinstance(self.importance, bool)
            or not 1 <= self.importance <= 5
        ):
            raise ValueError("importance must be 1-5")
        if not isinstance(self.effort_h, (int, float)) or isinstance(
            self.effort_h, bool
        ):
            raise TypeError("effort_h must be a number")
        if self.effort_h < 0:
            raise ValueError("effort_h must be non-negative")
        if not isinstance(self.deadline, date):
            raise TypeError("deadline must be a datetime.date")

    def days_left(self, today: date) -> int:
        return max((self.deadline - today).days, 0)

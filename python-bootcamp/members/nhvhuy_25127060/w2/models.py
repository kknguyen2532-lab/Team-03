"""Task data model for the study planner (W2-1)."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represent a study task with importance, effort, and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate task fields after initialization."""
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Return the number of days remaining until deadline (minimum 0)."""
        return max(0, (self.deadline - today).days)
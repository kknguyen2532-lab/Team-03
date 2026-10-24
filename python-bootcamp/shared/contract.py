
from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represent a task in the study planner."""

    title: str
    importance: int
    effort_h: float
    deadline: date


@dataclass
class Block:
    """Represent a scheduled block of study time."""

    task: Task
    hours: float

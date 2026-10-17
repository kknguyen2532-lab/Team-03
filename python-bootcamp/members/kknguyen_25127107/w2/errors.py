from collections.abc import Iterable

from .models import Task


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = float(needed_h)
        self.available_h = float(available_h)
        super().__init__(str(self))

    def __str__(self) -> str:
        return (
            f"Plan needs {self.needed_h:g} h, but only "
            f"{self.available_h:g} h are available."
        )


def check_feasible(tasks: Iterable[Task], available_h: float) -> None:
    if available_h < 0:
        raise ValueError("available_h must be non-negative")

    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)

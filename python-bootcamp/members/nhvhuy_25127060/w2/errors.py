"""Custom exceptions and feasibility checks for the study planner (W2-3)."""

from collections.abc import Iterable

from .models import Task


class InfeasiblePlan(Exception):
    """Raised when total required task effort exceeds available study hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        """Initialize with needed and available hours."""
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        """Return a human-readable error message."""
        return (
            f"Plan infeasible: need {self.needed_h:.2f} hours, "
            f"but only {self.available_h:.2f} hours available."
        )


def check_feasible(tasks: Iterable[Task], available_h: float) -> None:
    """Raise InfeasiblePlan if total effort of tasks exceeds available_h."""
    if available_h < 0:
        raise ValueError("available_h must be non-negative")

    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)

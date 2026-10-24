"""Utilities for tracking study progress."""


def completion_rate(total: int, completed: int) -> float:
    """Return the completion rate as a percentage."""
    if not isinstance(total, int) or isinstance(total, bool):
        raise TypeError("total must be a non-negative integer")

    if not isinstance(completed, int) or isinstance(completed, bool):
        raise TypeError("completed must be a non-negative integer")

    if total < 0:
        raise ValueError("total must be non-negative")

    if completed < 0 or completed > total:
        raise ValueError("completed must be between 0 and total")

    if total == 0:
        return 0.0

    return completed / total * 100


def remaining_tasks(total: int, completed: int) -> int:
    """Return the number of tasks that remain unfinished."""
    completion_rate(total, completed)
    return total - completed


def study_efficiency(planned_h: float, actual_h: float) -> float:
    """Return planned hours divided by actual hours."""
    if planned_h <= 0:
        raise ValueError("planned_h must be positive")

    if actual_h <= 0:
        raise ValueError("actual_h must be positive")

    return planned_h / actual_h

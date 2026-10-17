"""Validation utilities for study planner tasks."""

from shared.contract import Task


def validate_task(task: Task) -> list[str]:
    """Return validation errors for a task."""
    errors: list[str] = []

    if not task.title.strip():
        errors.append("title must not be empty")

    if not isinstance(task.importance, int) or isinstance(
        task.importance, bool
    ):
        errors.append("importance must be an integer between 1 and 5")
    elif not 1 <= task.importance <= 5:
        errors.append("importance must be between 1 and 5")

    if not isinstance(task.effort_h, (int, float)) or isinstance(
        task.effort_h, bool
    ):
        errors.append("effort_h must be a positive number")
    elif task.effort_h <= 0:
        errors.append("effort_h must be greater than 0")

    from datetime import date

    if not isinstance(task.deadline, date):
        errors.append("deadline must be a date")

    return errors
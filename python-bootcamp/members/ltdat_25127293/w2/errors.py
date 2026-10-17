from .models import Task


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"Infeasible plan: needed {needed_h}h, available {available_h}h"
        )

    def __str__(self) -> str:
        return f"Infeasible plan: needed {self.needed_h} hours, but only {self.available_h} hours are available."


def check_feasible(tasks: list[Task], available_h: float) -> None:
    total_needed = sum(t.effort_h for t in tasks)
    if total_needed > available_h:
        raise InfeasiblePlan(needed_h=total_needed, available_h=available_h)

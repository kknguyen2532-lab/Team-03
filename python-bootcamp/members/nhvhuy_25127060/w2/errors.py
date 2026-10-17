
# members/<your_id>/w2/errors.py

class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        return (
            f"Plan infeasible: need {self.needed_h:.2f} hours, "
            f"but only {self.available_h:.2f} hours available."
        )


def check_feasible(tasks, available_h: float) -> None:
    if available_h < 0:
        raise ValueError("available_h must be non-negative")

    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)

from datetime import date

import pytest

from shared.contract import Task
from shared.study_planner.allocate import allocate
from shared.study_planner.errors import InfeasiblePlan


def test_allocate_raises_infeasible_plan():
    tasks = [
        Task(title="Task 1", importance=5, effort_h=6.0, deadline=date(2026, 10, 30)),
        Task(title="Task 2", importance=3, effort_h=4.0, deadline=date(2026, 10, 31)),
    ]
    with pytest.raises(InfeasiblePlan):
        allocate(tasks, 8.0)

"""Integration tests for the shared study planner modules."""

import csv
from datetime import date

import pytest

from shared.contract import Task
from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


TODAY = date(2026, 10, 24)

@pytest.fixture
def sample_tasks():
    """Create sample tasks for integration tests."""
    return [
        Task(
            title="Assignment",
            importance=5,
            effort_h=3.0,
            deadline=date(2026, 10, 26),
        ),
        Task(
            title="Review",
            importance=3,
            effort_h=1.0,
            deadline=date(2026, 10, 25),
        ),
        Task(
            title="Exercise",
            importance=4,
            effort_h=2.0,
            deadline=date(2026, 10, 30),
        ),
    ]


def test_parse_csv_reads_tasks(tmp_path):
    """Check that CSV data is converted into Task objects."""
    csv_path = tmp_path / "tasks.csv"

    with csv_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "importance", "effort_h", "deadline"])
        writer.writerow(["Assignment", 5, 3.0, "2026-10-26"])
        writer.writerow(["Review", 3, 1.0, "2026-10-25"])

    tasks = parse_csv(csv_path)

    assert len(tasks) == 2
    assert tasks[0].title == "Assignment"
    assert tasks[0].importance == 5
    assert tasks[0].effort_h == 3.0
    assert tasks[0].deadline == date(2026, 10, 26)


def test_parse_csv_rejects_invalid_importance(tmp_path):
    """Check that invalid CSV data raises ValueError."""
    csv_path = tmp_path / "invalid.csv"

    with csv_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "importance", "effort_h", "deadline"])
        writer.writerow(["Assignment", 8, 2.0, "2026-10-26"])

    with pytest.raises(ValueError, match="importance must be 1-5"):
        parse_csv(csv_path)


def test_prioritise_orders_tasks(sample_tasks):
    """Check that tasks are ordered by the priority score."""
    result = prioritise(sample_tasks, TODAY)

    assert result[0].title == "Review"
    assert result[1].title == "Assignment"
    assert result[2].title == "Exercise"


def test_allocate_respects_available_hours(sample_tasks):
    """Check that allocated time does not exceed the available hours."""
    blocks = allocate(sample_tasks, 2.5)

    assert sum(block.hours for block in blocks) == pytest.approx(2.5)
    assert all(block.hours > 0 for block in blocks)
    assert all(block.hours <= block.task.effort_h for block in blocks)


def test_allocate_returns_empty_for_zero_hours(sample_tasks):
    """Check that zero available hours produce no blocks."""
    assert allocate(sample_tasks, 0) == []


def test_allocate_returns_empty_for_no_tasks():
    """Check that an empty task list produces no blocks."""
    assert allocate([], 5) == []


def test_render_handles_empty_blocks():
    """Check the output when no study blocks are available."""
    assert render([]) == "Chưa có kế hoạch nào được tạo."


def test_render_displays_allocated_blocks(sample_tasks):
    """Check that rendered output includes allocated task details."""
    blocks = allocate(sample_tasks, 2.5)

    output = render(blocks)

    assert "BẢNG KẾ HOẠCH HỌC TẬP" in output
    assert "Assignment" in output
    assert "2.5" in output or "1.5" in output

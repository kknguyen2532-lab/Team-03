"""End-to-end tests for the study_planner pipeline."""

import os
import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest
from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


@pytest.fixture
def sample_csv(tmp_path: Path) -> Path:
    """Create a temporary CSV file with reproducible test data using team schema."""
    csv_file = tmp_path / "tasks.csv"
    content = (
        "title,importance,effort_h,deadline\n"
        "Assignment,5,3.0,2026-10-26\n"
        "Review,3,1.0,2026-10-25\n"
        "Exercise,4,2.0,2026-10-30\n"
    )
    csv_file.write_text(content, encoding="utf-8")
    return csv_file


def test_pipeline_end_to_end(sample_csv: Path) -> None:
    """Verify full workflow: parse_csv -> prioritise -> allocate -> render."""
    base_date = date(2026, 10, 24)
    available_hours = 2.5

    # 1. Parse CSV
    tasks = parse_csv(sample_csv)
    assert len(tasks) == 3

    # 2. Prioritise tasks
    ordered_tasks = prioritise(tasks, base_date)
    assert len(ordered_tasks) == 3

    # 3. Allocate hours
    blocks = allocate(ordered_tasks, available_hours)
    assert len(blocks) > 0
    assert sum(block.hours for block in blocks) <= available_hours

    # 4. Render output string (chi truyen duy nhat blocks)
    output = render(blocks)
    assert isinstance(output, str)
    assert len(output) > 0


def test_cli_execution_end_to_end(sample_csv: Path) -> None:
    """Verify end-to-end invocation via Python CLI module."""
    cmd = [
        sys.executable,
        "-m",
        "shared.study_planner",
        str(sample_csv),
        "--hours",
        "2.5",
        "--today",
        "2026-10-24",
    ]

    env = os.environ.copy()
    env["PYTHONPATH"] = "."
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=False,
        env=env,
        encoding="utf-8",
    )

    assert result.returncode == 0
    assert len(result.stdout.strip()) > 0

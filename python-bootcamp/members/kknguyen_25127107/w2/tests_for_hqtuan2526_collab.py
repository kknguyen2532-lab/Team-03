
"""W2-4 cross-tests for hqtuan2526-collab's Week 1 code."""

import importlib.util
from pathlib import Path
from types import ModuleType

import pytest


def load_w1_module(filename: str, module_name: str) -> ModuleType:
    """Load a teammate's W1 module from its file path."""
    w1_dir = (
        Path(__file__).resolve().parents[3]
        / "members"
        / "hqtuan2526-collab"
        / "w1"
    )
    file_path = w1_dir / filename

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module: {file_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


grades = load_w1_module("grades.py", "reviewee_grades")
text_tools = load_w1_module("text_tools.py", "reviewee_text_tools")
rules = load_w1_module("rules.py", "reviewee_rules")
translate = load_w1_module("translate.py", "reviewee_translate")
timetable = load_w1_module("timetable.py", "reviewee_timetable")


# W1-1: grades.py

def test_summary_calculates_statistics() -> None:
    assert grades.summary([7.5, 9, 6, 8]) == {
        "min": 6,
        "max": 9,
        "mean": 7.62,
        "median": 7.75,
    }


def test_summary_rejects_empty_scores() -> None:
    with pytest.raises(ValueError):
        grades.summary([])


# W1-2: text_tools.py

def test_word_count_ignores_case_and_punctuation() -> None:
    assert text_tools.word_count("Git, git! Python.") == {
        "git": 2,
        "python": 1,
    }


def test_top_k_breaks_ties_alphabetically() -> None:
    text = "banana apple banana cherry apple"
    assert text_tools.top_k(text, 2) == [
        ("apple", 2),
        ("banana", 2),
    ]


def test_top_k_returns_empty_for_zero() -> None:
    assert text_tools.top_k("apple banana", 0) == []


# W1-3: rules.py

def test_can_register_thesis_at_minimum_requirements() -> None:
    assert rules.can_register_thesis(120, 2.0) is True


def test_missing_reports_both_requirements() -> None:
    assert rules.missing(118, 1.8) == [
        "need 2 more credits",
        "need GPA 0.2 more",
    ]


# W1-4: translate.py

def test_merge_sort_sorts_unsorted_values() -> None:
    assert translate.merge_sort([5, 2, 8, 1, 3]) == [
        1, 2, 3, 5, 8
    ]


def test_merge_sort_preserves_duplicate_values() -> None:
    assert translate.merge_sort([3, 1, 3, 2, 1]) == [
        1, 1, 2, 3, 3
    ]


def test_merge_sort_handles_empty_list_edge_case() -> None:
    assert translate.merge_sort([]) == []


# W1-5: timetable.py

def test_by_day_groups_and_sorts_courses() -> None:
    courses = [
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon"),
    ]
    assert timetable.by_day(courses) == {
        "Mon": ["CSC10001", "CSC10014"],
        "Tue": ["MTH00003"],
    }

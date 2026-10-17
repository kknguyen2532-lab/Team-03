
"""W2-4: Tests for hqtuan2526-collab's W1-4."""

import importlib.util
from pathlib import Path
from types import ModuleType


def load_translate_module() -> ModuleType:
    """Load the reviewee's W1-4 module."""
    w1_dir = (
        Path(__file__).resolve().parents[3]
        / "members"
        / "hqtuan2526-collab"
        / "w1"
    )
    file_path = w1_dir / "translate.py"

    spec = importlib.util.spec_from_file_location(
        "reviewee_translate", file_path
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module: {file_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


translate = load_translate_module()


def test_merge_sort_unsorted_list() -> None:
    assert translate.merge_sort([5, 2, 8, 1, 3]) == [1, 2, 3, 5, 8]


def test_merge_sort_already_sorted_list() -> None:
    assert translate.merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_merge_sort_duplicate_values() -> None:
    assert translate.merge_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]


def test_merge_sort_empty_list_edge_case() -> None:
    assert translate.merge_sort([]) == []


def test_merge_sort_single_element_edge_case() -> None:
    assert translate.merge_sort([42]) == [42]


def test_merge_sort_negative_numbers() -> None:
    assert translate.merge_sort([-3, 5, -1, 0, -8]) == [-8, -3, -1, 0, 5]

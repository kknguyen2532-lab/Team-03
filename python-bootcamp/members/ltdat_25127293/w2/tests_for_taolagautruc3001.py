"""W2-4: Tests for taolagautruc3001's W1-4."""

import importlib.util
from pathlib import Path


def _load_module():
    # Tìm file translate.py trong thư mục thành viên được review
    repo_root = Path(__file__).resolve().parents[2]
    # Thay 'lhphieu_25127049' bằng đúng tên thư mục của bạn ấy nếu khác
    target_path = repo_root / "members" / "lhphieu_25127049" / "w1" / "translate.py"

    spec = importlib.util.spec_from_file_location("translate_peer", target_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


insertion_sort = _load_module().insertion_sort


def test_insertion_sort_normal():
    arr = [5, 2, 4, 6, 1, 3]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5, 6]


def test_insertion_sort_already_sorted():
    arr = [1, 2, 3, 4, 5]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5]


def test_insertion_sort_reverse():
    arr = [5, 4, 3, 2, 1]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5]


def test_insertion_sort_duplicates():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert insertion_sort(arr) == [1, 1, 2, 3, 4, 5, 5, 6, 9]


def test_insertion_sort_edge_cases():
    assert insertion_sort([]) == []
    assert insertion_sort([42]) == [42]


def test_insertion_sort_negative_numbers():
    arr = [-3, 5, 0, -1, 2]
    assert insertion_sort(arr) == [-3, -1, 0, 2, 5]

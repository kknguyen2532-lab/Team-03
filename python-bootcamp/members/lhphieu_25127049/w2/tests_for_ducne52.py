"""Pytest tests for the binary_search function.

Replace `your_module` with the name of the Python file containing binary_search,
without the .py extension. For example, use `from search import binary_search`
if the implementation is in search.py.
"""

from your_module import binary_search


def test_key_in_middle():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_key_at_first_position():
    assert binary_search([1, 3, 5, 7, 9], 1) == 0


def test_key_at_last_position():
    assert binary_search([1, 3, 5, 7, 9], 9) == 4


def test_key_not_found():
    assert binary_search([1, 3, 5, 7, 9], 4) == -1


def test_empty_list():
    # Edge case: searching an empty list should return -1.
    assert binary_search([], 5) == -1


def test_single_element_list():
    assert binary_search([5], 5) == 0

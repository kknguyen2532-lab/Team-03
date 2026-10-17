import pytest

from .translate import max_subarray_sum


def test_max_subarray_mixed_numbers():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray_sum(arr) == 6


def test_max_subarray_all_positive():
    arr = [1, 2, 3, 4, 5]
    assert max_subarray_sum(arr) == 15


def test_max_subarray_all_negative():
    arr = [-5, -2, -9, -1]
    assert max_subarray_sum(arr) == -1


def test_max_subarray_single_element():
    arr = [42]
    assert max_subarray_sum(arr) == 42


def test_max_subarray_empty_list_raises_error():
    with pytest.raises(ValueError, match="Input list must not be empty"):
        max_subarray_sum([])

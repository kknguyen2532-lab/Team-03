import pytest

from .translate import max_subarray_sum


def test_max_subarray_mixed_numbers():
    """Kiểm tra tổng mảng con lớn nhất với danh sách chứa cả số âm và số dương."""
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray_sum(arr) == 6


def test_max_subarray_all_positive():
    """Kiểm tra trường hợp tất cả các phần tử trong danh sách đều là số dương."""
    arr = [1, 2, 3, 4, 5]
    assert max_subarray_sum(arr) == 15


def test_max_subarray_all_negative():
    """Kiểm tra trường hợp tất cả các phần tử đều là số âm (trả về giá trị lớn nhất)."""
    arr = [-5, -2, -9, -1]
    assert max_subarray_sum(arr) == -1


def test_max_subarray_single_element():
    """Kiểm tra trường hợp danh sách chỉ chứa một phần tử duy nhất."""
    arr = [42]
    assert max_subarray_sum(arr) == 42


def test_max_subarray_empty_list_raises_error():
    """Kiểm tra ngoại lệ ValueError được ném ra đúng với thông báo khi danh sách rỗng."""
    with pytest.raises(ValueError, match="Input list must not be empty"):
        max_subarray_sum([])

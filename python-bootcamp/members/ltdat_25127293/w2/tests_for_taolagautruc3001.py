from .translate import insertion_sort


def test_insertion_sort_normal():
    """Kiểm tra trường hợp danh sách bình thường, hỗn độn."""
    arr = [5, 2, 4, 6, 1, 3]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5, 6]


def test_insertion_sort_already_sorted():
    """Kiểm tra trường hợp danh sách đã được sắp xếp sẵn."""
    arr = [1, 2, 3, 4, 5]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5]


def test_insertion_sort_reverse():
    """Kiểm tra trường hợp danh sách sắp xếp theo chiều ngược lại."""
    arr = [5, 4, 3, 2, 1]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5]


def test_insertion_sort_duplicates():
    """Kiểm tra trường hợp có các phần tử trùng lặp."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert insertion_sort(arr) == [1, 1, 2, 3, 4, 5, 5, 6, 9]


def test_insertion_sort_edge_cases():
    """Trường hợp biên (edge case): Danh sách rỗng hoặc chỉ có 1 phần tử."""
    assert insertion_sort([]) == []
    assert insertion_sort([42]) == [42]


def test_insertion_sort_negative_numbers():
    """Kiểm tra trường hợp có số âm."""
    arr = [-3, 5, 0, -1, 2]
    assert insertion_sort(arr) == [-3, -1, 0, 2, 5]

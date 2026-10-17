from translate import binary_search


def test_binary_search_found_middle():
    """Kiểm tra tìm thấy phần tử ở giữa danh sách."""
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 5) == 2

def test_binary_search_found_edges():
    """Kiểm tra tìm thấy phần tử ở hai đầu mút (đầu và cuối)."""
    arr = [10, 20, 30, 40, 50]
    assert binary_search(arr, 10) == 0
    assert binary_search(arr, 50) == 4

def test_binary_search_not_found():
    """Kiểm tra trường hợp phần tử không tồn tại trong danh sách."""
    arr = [2, 4, 6, 8, 10]
    # Nhỏ hơn min, lớn hơn max, và nằm giữa các phần tử
    assert binary_search(arr, 1) == -1
    assert binary_search(arr, 5) == -1
    assert binary_search(arr, 11) == -1

def test_binary_search_empty_list():
    """Edge case 1: Danh sách rỗng."""
    assert binary_search([], 42) == -1

def test_binary_search_single_element():
    """Edge case 2: Danh sách chỉ có duy nhất 1 phần tử."""
    assert binary_search([7], 7) == 0
    assert binary_search([7], 3) == -1

def test_binary_search_even_length_and_negatives():
    """Kiểm tra mảng có độ dài chẵn và chứa số âm."""
    arr = [-15, -7, 0, 4, 8, 12]
    assert binary_search(arr, -15) == 0
    assert binary_search(arr, 0) == 2
    assert binary_search(arr, 12) == 5
    assert binary_search(arr, -1) == -1
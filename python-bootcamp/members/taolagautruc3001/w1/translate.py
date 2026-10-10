def insertion_sort(arr: list[int]) -> list[int]:
    """
    Sắp xếp danh sách (in place).
    Điểm khác C++: Python không cần khai báo kiểu dữ liệu cho biến, danh sách có thể tự quản lý bộ nhớ và tự động thay đổi kích thước.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
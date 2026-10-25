def max_subarray_sum(numbers: list[int]) -> int:
    """
    Tìm tổng lớn nhất của một mảng con liên tiếp (contiguous subarray) không rỗng.
    
    Sử dụng thuật toán Kadane để duyệt qua danh sách và tìm tổng lớn nhất 
    với độ phức tạp thời gian O(n).

    Args:
        numbers (list[int]): Danh sách các số nguyên đầu vào.

    Returns:
        int: Giá trị tổng lớn nhất của mảng con.

    Raises:
        ValueError: Nếu danh sách đầu vào rỗng.
    """
    if not numbers:
        raise ValueError("Input list must not be empty")

    current_sum = numbers[0]
    maximum_sum = numbers[0]

    for number in numbers[1:]:
        current_sum = max(number, current_sum + number)
        maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum
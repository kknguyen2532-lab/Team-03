# Maximum Subarray Sum
def max_subarray_sum(arr: list[int]) -> int:
    if not arr:
        raise ValueError("Input list must not be empty")

    current_sum = max_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

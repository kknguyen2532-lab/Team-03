def max_subarray_sum(numbers: list[int]) -> int:
    """Return the maximum sum of a non-empty contiguous subarray."""
    if not numbers:
        raise ValueError("Input list must not be empty")

    current_sum = numbers[0]
    maximum_sum = numbers[0]

    for number in numbers[1:]:
        current_sum = max(number, current_sum + number)
        maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum

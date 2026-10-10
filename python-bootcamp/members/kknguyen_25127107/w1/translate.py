def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Return the transpose of a matrix.

    Unlike C++, Python can use zip() to group elements
    from the same column into tuples.
    """
    if not matrix:
        return []

    return list(zip(*matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(transpose(matrix))
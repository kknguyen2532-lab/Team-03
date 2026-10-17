"""
    Performs binary search on a sorted list, returning the index or -1 if not found.
    
    Difference from C++:
    In Python, we use the built-in function `len(a)` to get the size of the list instead 
    of calling the `.size()` method as in C++, and variable data types (`int`, `list`) 
    do not need to be explicitly declared since Python manages them automatically.
    """

def binary_search(a: list[int], key: int) -> int:
    lo = 0
    hi = len(a) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            lo = mid + 1
        elif a[mid] > key:
            hi = mid - 1
        else:
            return -1
from members.kknguyen_25127107.w1.translate import transpose


def test_transpose_2x3():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [
        (1, 4), (2, 5), (3, 6)
    ]


def test_transpose_square_matrix():
    assert transpose([[1, 2], [3, 4]]) == [
        (1, 3), (2, 4)
    ]


def test_transpose_single_row():
    assert transpose([[1, 2, 3]]) == [
        (1,), (2,), (3,)
    ]


def test_transpose_single_column():
    assert transpose([[1], [2], [3]]) == [
        (1, 2, 3)
    ]


def test_transpose_empty_matrix():
    assert transpose([]) == []


def test_transpose_single_element():
    assert transpose([[7]]) == [(7,)]

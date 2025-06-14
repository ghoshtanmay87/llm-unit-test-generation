def get_row(lst, x):
    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])

import pytest

def test_single_occurrence_of_x_in_2d_list():
    lst = [[1, 2], [3, 4]]
    x = 3
    expected_output = [(1, 0)]
    assert get_row(lst, x) == expected_output

def test_no_occurrence_of_x_in_list():
    lst = [[1, 2], [3, 4]]
    x = 9
    expected_output = []
    assert get_row(lst, x) == expected_output

def test_multiple_occurrences_same_row_different_columns():
    lst = [[7, 7, 7], [1, 2, 3]]
    x = 7
    expected_output = [(0, 2), (0, 1), (0, 0)]
    assert get_row(lst, x) == expected_output

def test_multiple_occurrences_multiple_rows_same_columns():
    lst = [[4, 1], [4, 2], [4, 3]]
    x = 4
    expected_output = [(0, 0), (1, 0), (2, 0)]
    assert get_row(lst, x) == expected_output

def test_multiple_occurrences_different_rows_and_columns():
    lst = [[5, 3, 3], [3, 5, 3], [3, 3, 5]]
    x = 3
    expected_output = [(0, 2), (0, 1), (1, 2), (1, 0), (2, 1), (2, 0)]
    assert get_row(lst, x) == expected_output
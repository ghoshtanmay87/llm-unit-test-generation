def sum_column(list1, C):
    result = sum(row[C] for row in list1)
    return result

import pytest

def test_sum_first_column_multiple_rows():
    # Sum values in the first column of a 2D list with multiple rows
    list1 = [[1, 2], [3, 4], [5, 6]]
    C = 0
    expected = 9
    assert sum_column(list1, C) == expected

def test_sum_second_column_multiple_rows():
    # Sum values in the second column of a 2D list with multiple rows
    list1 = [[1, 2], [3, 4], [5, 6]]
    C = 1
    expected = 12
    assert sum_column(list1, C) == expected

def test_sum_single_row_list():
    # Sum values in a single-row list
    list1 = [[10, 20, 30]]
    C = 2
    expected = 30
    assert sum_column(list1, C) == expected

def test_sum_column_with_negative_and_positive_numbers():
    # Sum values in a list with negative and positive numbers
    list1 = [[-1, 2], [3, -4], [5, 6]]
    C = 0
    expected = 7
    assert sum_column(list1, C) == expected

def test_sum_empty_list():
    # Sum values in an empty list
    list1 = []
    C = 0
    expected = 0
    assert sum_column(list1, C) == expected

def test_sum_column_with_floating_point_numbers():
    # Sum values in a column with floating point numbers
    list1 = [[1.5, 2.5], [3.5, 4.5], [5.5, 6.5]]
    C = 1
    expected = 13.5
    assert sum_column(list1, C) == expected
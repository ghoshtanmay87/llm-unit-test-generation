def sum_three_smallest_nums(lst):
	return sum(sorted([x for x in lst if x > 0])[:3])

import pytest

def test_list_with_more_than_three_positive_numbers():
    lst = [5, 1, 3, 2, 4]
    expected_output = 6
    assert sum_three_smallest_nums(lst) == expected_output

def test_list_with_exactly_three_positive_numbers():
    lst = [7, 2, 9]
    expected_output = 18
    assert sum_three_smallest_nums(lst) == expected_output

def test_list_with_fewer_than_three_positive_numbers():
    lst = [0, -1, 4]
    expected_output = 4
    assert sum_three_smallest_nums(lst) == expected_output

def test_list_with_no_positive_numbers():
    lst = [-5, 0, -3]
    expected_output = 0
    assert sum_three_smallest_nums(lst) == expected_output

def test_list_with_positive_and_zero_values():
    lst = [0, 1, 0, 2, 3]
    expected_output = 6
    assert sum_three_smallest_nums(lst) == expected_output

def test_list_with_duplicate_positive_numbers():
    lst = [2, 2, 3, 1, 1]
    expected_output = 4
    assert sum_three_smallest_nums(lst) == expected_output

def test_list_with_large_positive_numbers():
    lst = [100, 50, 200, 10, 5]
    expected_output = 65
    assert sum_three_smallest_nums(lst) == expected_output

def test_list_with_all_zeros():
    lst = [0, 0, 0]
    expected_output = 0
    assert sum_three_smallest_nums(lst) == expected_output

def test_empty_list():
    lst = []
    expected_output = 0
    assert sum_three_smallest_nums(lst) == expected_output

def test_list_with_positive_floats():
    lst = [1.5, 2.5, 0.5, 3.5]
    expected_output = 4.5
    assert sum_three_smallest_nums(lst) == expected_output
def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element
	return total

import pytest

def test_sum_flat_list_of_integers():
    data_list = [1, 2, 3, 4, 5]
    expected_output = 15
    assert recursive_list_sum(data_list) == expected_output

def test_sum_nested_list_one_level():
    data_list = [1, [2, 3], 4]
    expected_output = 10
    assert recursive_list_sum(data_list) == expected_output

def test_sum_deeply_nested_list():
    data_list = [1, [2, [3, 4], 5], 6]
    expected_output = 21
    assert recursive_list_sum(data_list) == expected_output

def test_sum_empty_list():
    data_list = []
    expected_output = 0
    assert recursive_list_sum(data_list) == expected_output

def test_sum_list_with_empty_nested_lists():
    data_list = [[], [[], []], []]
    expected_output = 0
    assert recursive_list_sum(data_list) == expected_output

def test_sum_list_mixed_integers_and_empty_nested_lists():
    data_list = [1, [], 2, [3, []], 4]
    expected_output = 10
    assert recursive_list_sum(data_list) == expected_output

def test_sum_list_with_negative_and_positive_integers_nested():
    data_list = [1, [-2, [3, -4], 5], -6]
    expected_output = -3
    assert recursive_list_sum(data_list) == expected_output
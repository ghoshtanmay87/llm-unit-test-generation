def add_consecutive_nums(nums):
    result = [b+a for a, b in zip(nums[:-1], nums[1:])]
    return result

import pytest

def test_sum_of_consecutive_elements_positive_integers():
    nums = [1, 2, 3, 4]
    expected_output = [3, 5, 7]
    assert add_consecutive_nums(nums) == expected_output

def test_sum_of_consecutive_elements_negative_and_positive_integers():
    nums = [-1, 0, 1]
    expected_output = [-1, 1]
    assert add_consecutive_nums(nums) == expected_output

def test_sum_of_consecutive_elements_single_element():
    nums = [5]
    expected_output = []
    assert add_consecutive_nums(nums) == expected_output

def test_sum_of_consecutive_elements_empty_list():
    nums = []
    expected_output = []
    assert add_consecutive_nums(nums) == expected_output

def test_sum_of_consecutive_elements_repeated_elements():
    nums = [2, 2, 2]
    expected_output = [4, 4]
    assert add_consecutive_nums(nums) == expected_output
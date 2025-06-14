def big_sum(nums):
      sum= max(nums)+min(nums)
      return sum

import pytest

def test_sum_of_max_and_min_in_list_of_positive_integers():
    nums = [1, 2, 3, 4, 5]
    expected_output = 6
    assert big_sum(nums) == expected_output

def test_sum_of_max_and_min_in_list_with_negative_and_positive_integers():
    nums = [-10, 0, 10, 20]
    expected_output = 10
    assert big_sum(nums) == expected_output

def test_sum_of_max_and_min_in_list_with_all_negative_integers():
    nums = [-5, -3, -1, -7]
    expected_output = -8
    assert big_sum(nums) == expected_output

def test_sum_of_max_and_min_in_list_with_single_element():
    nums = [42]
    expected_output = 84
    assert big_sum(nums) == expected_output

def test_sum_of_max_and_min_in_list_with_repeated_elements():
    nums = [3, 3, 3, 3]
    expected_output = 6
    assert big_sum(nums) == expected_output
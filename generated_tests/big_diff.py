def big_diff(nums):
     diff= max(nums)-min(nums)
     return diff

import pytest

def test_big_diff_distinct_positive_integers():
    nums = [1, 2, 3, 4, 5]
    expected_output = 4
    assert big_diff(nums) == expected_output

def test_big_diff_all_identical_elements():
    nums = [7, 7, 7, 7]
    expected_output = 0
    assert big_diff(nums) == expected_output

def test_big_diff_negative_and_positive_integers():
    nums = [-10, 0, 10, 20]
    expected_output = 30
    assert big_diff(nums) == expected_output

def test_big_diff_single_element():
    nums = [42]
    expected_output = 0
    assert big_diff(nums) == expected_output

def test_big_diff_negative_integers_only():
    nums = [-5, -1, -9, -3]
    expected_output = 8
    assert big_diff(nums) == expected_output
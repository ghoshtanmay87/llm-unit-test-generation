def diff_consecutivenums(nums):
    result = [b-a for a, b in zip(nums[:-1], nums[1:])]
    return result

import pytest

def test_diff_consecutivenums_increasing_consecutive_integers():
    # Calculate differences for a list of increasing consecutive integers
    nums = [1, 2, 3, 4, 5]
    expected = [1, 1, 1, 1]
    assert diff_consecutivenums(nums) == expected

def test_diff_consecutivenums_negative_and_positive_integers():
    # Calculate differences for a list with negative and positive integers
    nums = [-2, 0, 3, 7]
    expected = [2, 3, 4]
    assert diff_consecutivenums(nums) == expected

def test_diff_consecutivenums_repeated_numbers():
    # Calculate differences for a list with repeated numbers
    nums = [5, 5, 5, 5]
    expected = [0, 0, 0]
    assert diff_consecutivenums(nums) == expected

def test_diff_consecutivenums_decreasing_numbers():
    # Calculate differences for a list with decreasing numbers
    nums = [10, 7, 3, 0]
    expected = [-3, -4, -3]
    assert diff_consecutivenums(nums) == expected

def test_diff_consecutivenums_single_element():
    # Calculate differences for a list with a single element
    nums = [42]
    expected = []
    assert diff_consecutivenums(nums) == expected

def test_diff_consecutivenums_empty_list():
    # Calculate differences for an empty list
    nums = []
    expected = []
    assert diff_consecutivenums(nums) == expected
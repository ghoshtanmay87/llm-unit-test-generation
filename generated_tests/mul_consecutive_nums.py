def mul_consecutive_nums(nums):
    result = [b*a for a, b in zip(nums[:-1], nums[1:])]
    return result

import pytest

def test_multiply_consecutive_positive_integers():
    nums = [1, 2, 3, 4]
    expected = [2, 6, 12]
    assert mul_consecutive_nums(nums) == expected

def test_multiply_consecutive_negative_and_positive_integers():
    nums = [-1, 3, -2, 4]
    expected = [-3, -6, -8]
    assert mul_consecutive_nums(nums) == expected

def test_multiply_consecutive_with_zeros():
    nums = [0, 5, 0, 7]
    expected = [0, 0, 0]
    assert mul_consecutive_nums(nums) == expected

def test_multiply_consecutive_single_element():
    nums = [10]
    expected = []
    assert mul_consecutive_nums(nums) == expected

def test_multiply_consecutive_empty_list():
    nums = []
    expected = []
    assert mul_consecutive_nums(nums) == expected

def test_multiply_consecutive_floats():
    nums = [1.5, 2.0, 3.5]
    expected = [3.0, 7.0]
    assert mul_consecutive_nums(nums) == expected
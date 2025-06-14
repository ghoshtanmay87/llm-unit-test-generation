def sum_negativenum(nums):
  sum_negativenum = list(filter(lambda nums:nums<0,nums))
  return sum(sum_negativenum)

import pytest

def test_sum_negativenum_mixed_positive_and_negative():
    # Sum of negative numbers in a list with mixed positive and negative values
    nums = [1, -2, 3, -4, 5]
    expected = -6
    assert sum_negativenum(nums) == expected

def test_sum_negativenum_all_positive():
    # Sum of negative numbers in a list with all positive values
    nums = [1, 2, 3, 4, 5]
    expected = 0
    assert sum_negativenum(nums) == expected

def test_sum_negativenum_all_negative():
    # Sum of negative numbers in a list with all negative values
    nums = [-1, -2, -3, -4, -5]
    expected = -15
    assert sum_negativenum(nums) == expected

def test_sum_negativenum_empty_list():
    # Sum of negative numbers in an empty list
    nums = []
    expected = 0
    assert sum_negativenum(nums) == expected

def test_sum_negativenum_with_zero_and_negative():
    # Sum of negative numbers in a list with zero and negative numbers
    nums = [0, -1, -2, 3]
    expected = -3
    assert sum_negativenum(nums) == expected
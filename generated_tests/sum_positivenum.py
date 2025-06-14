def sum_positivenum(nums):
  sum_positivenum = list(filter(lambda nums:nums>0,nums))
  return sum(sum_positivenum)

import pytest

def test_sum_positivenum_mixed_list():
    # Sum of all positive numbers in a mixed list
    nums = [1, -2, 3, 4, -5]
    expected = 8
    assert sum_positivenum(nums) == expected

def test_sum_positivenum_zero_and_negatives():
    # Sum of all positive numbers in a list with zero and negatives
    nums = [0, -1, -2, -3]
    expected = 0
    assert sum_positivenum(nums) == expected

def test_sum_positivenum_all_positives():
    # Sum of all positive numbers in a list with only positive numbers
    nums = [10, 20, 30]
    expected = 60
    assert sum_positivenum(nums) == expected

def test_sum_positivenum_empty_list():
    # Sum of all positive numbers in an empty list
    nums = []
    expected = 0
    assert sum_positivenum(nums) == expected

def test_sum_positivenum_all_negatives():
    # Sum of all positive numbers in a list with all negative numbers
    nums = [-10, -20, -30]
    expected = 0
    assert sum_positivenum(nums) == expected
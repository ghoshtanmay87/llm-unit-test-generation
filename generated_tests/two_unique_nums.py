def two_unique_nums(nums):
  return [i for i in nums if nums.count(i)==1]

import pytest

def test_two_unique_nums_two_unique_with_duplicates():
    # List with two unique numbers and duplicates
    nums = [1, 2, 2, 3, 4, 4]
    expected = [1, 3]
    assert two_unique_nums(nums) == expected

def test_two_unique_nums_all_unique():
    # List with all unique numbers
    nums = [5, 6, 7, 8]
    expected = [5, 6, 7, 8]
    assert two_unique_nums(nums) == expected

def test_two_unique_nums_no_unique():
    # List with no unique numbers
    nums = [9, 9, 10, 10]
    expected = []
    assert two_unique_nums(nums) == expected

def test_two_unique_nums_one_unique_with_duplicates():
    # List with one unique number and duplicates
    nums = [11, 12, 12, 13, 13]
    expected = [11]
    assert two_unique_nums(nums) == expected

def test_two_unique_nums_empty_list():
    # Empty list input
    nums = []
    expected = []
    assert two_unique_nums(nums) == expected

def test_two_unique_nums_multiple_unique_and_duplicates():
    # List with multiple unique numbers and multiple duplicates
    nums = [1, 2, 2, 3, 4, 4, 5, 6, 6]
    expected = [1, 3, 5]
    assert two_unique_nums(nums) == expected
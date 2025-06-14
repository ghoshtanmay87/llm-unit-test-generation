from array import array
def zero_count(nums):
    n = len(nums)
    n1 = 0
    for x in nums:
        if x == 0:
            n1 += 1
        else:
          None
    return round(n1/n,2)

import pytest

def test_zero_count_list_with_no_zeros():
    # List with no zeros
    nums = [1, 2, 3, 4, 5]
    expected = 0.0
    assert zero_count(nums) == expected

def test_zero_count_list_with_all_zeros():
    # List with all zeros
    nums = [0, 0, 0, 0]
    expected = 1.0
    assert zero_count(nums) == expected

def test_zero_count_list_with_some_zeros():
    # List with some zeros
    nums = [0, 1, 0, 2, 3]
    expected = 0.4
    assert zero_count(nums) == expected

def test_zero_count_list_with_one_zero():
    # List with one zero
    nums = [7, 0, 8]
    expected = 0.33
    assert zero_count(nums) == expected

def test_zero_count_list_with_zeros_and_negative_numbers():
    # List with zeros and negative numbers
    nums = [0, -1, 0, -2, 0]
    expected = 0.6
    assert zero_count(nums) == expected
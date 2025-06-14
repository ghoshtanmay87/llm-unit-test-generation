def minSubArraySum(nums):
    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        if s < 0:
            s = 0
        max_sum = max(s, max_sum)
    if max_sum == 0:
        max_sum = max((-i for i in nums))
    min_sum = -max_sum
    return min_sum

import pytest

def test_all_positive_numbers_in_array():
    nums = [1, 2, 3, 4, 5]
    expected = 1
    assert minSubArraySum(nums) == expected

def test_all_negative_numbers_in_array():
    nums = [-1, -2, -3, -4, -5]
    expected = -15
    assert minSubArraySum(nums) == expected

def test_mixed_positive_and_negative_numbers():
    nums = [3, -4, 2, -3, -1, 7, -5]
    expected = -6
    assert minSubArraySum(nums) == expected

def test_single_element_positive_number():
    nums = [10]
    expected = 10
    assert minSubArraySum(nums) == expected

def test_single_element_negative_number():
    nums = [-10]
    expected = -10
    assert minSubArraySum(nums) == expected

def test_array_with_zeros_and_positive_numbers():
    nums = [0, 0, 0, 5, 0]
    expected = 0
    assert minSubArraySum(nums) == expected

def test_array_with_zeros_and_negative_numbers():
    nums = [0, -1, 0, -2, 0]
    expected = -3
    assert minSubArraySum(nums) == expected

def test_array_with_all_zeros():
    nums = [0, 0, 0, 0]
    expected = 0
    assert minSubArraySum(nums) == expected

def test_array_with_one_large_negative_number_among_positives():
    nums = [2, 3, -100, 4, 5]
    expected = -100
    assert minSubArraySum(nums) == expected

def test_array_with_multiple_negative_subarrays_minimum_is_longer_subarray():
    nums = [1, -2, -3, 4, -1, -2, 1]
    expected = -5
    assert minSubArraySum(nums) == expected
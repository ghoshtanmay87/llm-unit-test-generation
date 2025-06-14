from array import array
def negative_count(nums):
    n = len(nums)
    n1 = 0
    for x in nums:
        if x < 0:
            n1 += 1
        else:
          None
    return round(n1/n,2)

import pytest

def test_negative_count_mixed_negative_and_positive_numbers():
    # List with mixed negative and positive numbers
    nums = [-1, 2, -3, 4, 5]
    expected = 0.4
    assert negative_count(nums) == expected

def test_negative_count_all_positive_numbers():
    # List with all positive numbers
    nums = [1, 2, 3, 4]
    expected = 0.0
    assert negative_count(nums) == expected

def test_negative_count_all_negative_numbers():
    # List with all negative numbers
    nums = [-1, -2, -3]
    expected = 1.0
    assert negative_count(nums) == expected

def test_negative_count_zero_and_positive_numbers():
    # List with zero and positive numbers
    nums = [0, 1, 2]
    expected = 0.0
    assert negative_count(nums) == expected

def test_negative_count_zero_and_negative_numbers():
    # List with zero and negative numbers
    nums = [0, -1, -2]
    expected = 0.67
    assert negative_count(nums) == expected

def test_negative_count_empty_list_raises_zero_division_error():
    # Empty list input should raise ZeroDivisionError
    nums = []
    with pytest.raises(ZeroDivisionError):
        negative_count(nums)
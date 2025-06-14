def increasing_trend(nums):
    if (sorted(nums)== nums):
        return True
    else:
        return False

import pytest

def test_increasing_trend_strictly_increasing():
    # List is strictly increasing
    nums = [1, 2, 3, 4, 5]
    expected = True
    assert increasing_trend(nums) == expected

def test_increasing_trend_non_decreasing_with_equal_elements():
    # List is non-decreasing (allows equal elements)
    nums = [1, 2, 2, 3, 4]
    expected = True
    assert increasing_trend(nums) == expected

def test_increasing_trend_strictly_decreasing():
    # List is not sorted (decreasing elements)
    nums = [5, 4, 3, 2, 1]
    expected = False
    assert increasing_trend(nums) == expected

def test_increasing_trend_unsorted_mixed_order():
    # List is unsorted with mixed order
    nums = [1, 3, 2, 4, 5]
    expected = False
    assert increasing_trend(nums) == expected

def test_increasing_trend_empty_list():
    # Empty list input
    nums = []
    expected = True
    assert increasing_trend(nums) == expected

def test_increasing_trend_single_element_list():
    # Single element list
    nums = [10]
    expected = True
    assert increasing_trend(nums) == expected

def test_increasing_trend_all_equal_elements():
    # List with all equal elements
    nums = [7, 7, 7, 7]
    expected = True
    assert increasing_trend(nums) == expected
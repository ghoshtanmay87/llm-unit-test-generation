def decreasing_trend(nums):
    if (sorted(nums)== nums):
        return True
    else:
        return False

import pytest

def test_decreasing_trend_strictly_increasing():
    # The input list is sorted in ascending order, so sorted(nums) == nums is True.
    nums = [1, 2, 3, 4, 5]
    expected = True
    assert decreasing_trend(nums) == expected

def test_decreasing_trend_strictly_decreasing():
    # The input list is sorted in descending order, so sorted(nums) != nums is True, hence False returned.
    nums = [5, 4, 3, 2, 1]
    expected = False
    assert decreasing_trend(nums) == expected

def test_decreasing_trend_unsorted_list():
    # The input list is not sorted ascending, so sorted(nums) != nums.
    nums = [3, 1, 4, 2]
    expected = False
    assert decreasing_trend(nums) == expected

def test_decreasing_trend_all_equal_elements():
    # All elements are equal, so the list is sorted ascending and sorted(nums) == nums.
    nums = [2, 2, 2, 2]
    expected = True
    assert decreasing_trend(nums) == expected

def test_decreasing_trend_empty_list():
    # An empty list is trivially sorted, so sorted(nums) == nums is True.
    nums = []
    expected = True
    assert decreasing_trend(nums) == expected

def test_decreasing_trend_single_element():
    # A single-element list is sorted, so sorted(nums) == nums is True.
    nums = [10]
    expected = True
    assert decreasing_trend(nums) == expected
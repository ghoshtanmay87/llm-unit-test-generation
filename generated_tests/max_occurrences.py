def max_occurrences(nums):
    max_val = 0
    result = nums[0] 
    for i in nums:
        occu = nums.count(i)
        if occu > max_val:
            max_val = occu
            result = i 
    return result

import pytest

def test_all_elements_unique_returns_first_element():
    # All elements are unique, so the first element is returned
    nums = [1, 2, 3, 4, 5]
    expected = 1
    assert max_occurrences(nums) == expected

def test_one_element_appears_more_times_than_others():
    # One element appears more times than others
    nums = [1, 2, 2, 3, 4]
    expected = 2
    assert max_occurrences(nums) == expected

def test_multiple_elements_same_max_occurrences_first_returned():
    # Multiple elements have the same max occurrences, first max occurrence element is returned
    nums = [3, 3, 2, 2, 1]
    expected = 3
    assert max_occurrences(nums) == expected

def test_all_elements_are_the_same():
    # All elements are the same
    nums = [7, 7, 7, 7]
    expected = 7
    assert max_occurrences(nums) == expected

def test_max_occurrence_element_at_the_end():
    # Max occurrence element is at the end
    nums = [1, 2, 3, 4, 4, 4]
    expected = 4
    assert max_occurrences(nums) == expected
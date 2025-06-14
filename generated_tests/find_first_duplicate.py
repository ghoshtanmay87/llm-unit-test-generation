def find_first_duplicate(nums):
    num_set = set()
    no_duplicate = -1

    for i in range(len(nums)):

        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_duplicate

import pytest

def test_single_duplicate_after_uniques():
    nums = [1, 2, 3, 2, 4]
    expected = 2
    assert find_first_duplicate(nums) == expected

def test_no_duplicates():
    nums = [1, 2, 3, 4, 5]
    expected = -1
    assert find_first_duplicate(nums) == expected

def test_immediate_duplicate_at_start():
    nums = [7, 7, 8, 9]
    expected = 7
    assert find_first_duplicate(nums) == expected

def test_multiple_duplicates_first_returned():
    nums = [5, 1, 5, 2, 1]
    expected = 5
    assert find_first_duplicate(nums) == expected

def test_empty_list():
    nums = []
    expected = -1
    assert find_first_duplicate(nums) == expected

def test_all_elements_same():
    nums = [3, 3, 3, 3]
    expected = 3
    assert find_first_duplicate(nums) == expected

def test_duplicates_at_end():
    nums = [10, 20, 30, 40, 10]
    expected = 10
    assert find_first_duplicate(nums) == expected
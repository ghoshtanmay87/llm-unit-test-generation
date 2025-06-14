from itertools import groupby
def consecutive_duplicates(nums):
    return [key for key, group in groupby(nums)]

import pytest

def test_empty_list_input_returns_empty_list():
    nums = []
    expected = []
    assert consecutive_duplicates(nums) == expected

def test_list_with_no_consecutive_duplicates_returns_same_list():
    nums = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert consecutive_duplicates(nums) == expected

def test_list_with_consecutive_duplicates_returns_unique_elements_in_order():
    nums = [1, 1, 2, 2, 2, 3, 3, 4]
    expected = [1, 2, 3, 4]
    assert consecutive_duplicates(nums) == expected

def test_list_with_all_elements_the_same_returns_single_element_list():
    nums = [7, 7, 7, 7, 7]
    expected = [7]
    assert consecutive_duplicates(nums) == expected

def test_list_with_alternating_duplicates_returns_each_unique_element_once():
    nums = [5, 5, 6, 6, 5, 5, 6, 6]
    expected = [5, 6, 5, 6]
    assert consecutive_duplicates(nums) == expected

def test_list_with_single_element_returns_list_with_that_element():
    nums = [42]
    expected = [42]
    assert consecutive_duplicates(nums) == expected
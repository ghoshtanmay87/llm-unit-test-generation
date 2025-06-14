def pancake_sort(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums

import pytest

def test_sort_multiple_distinct_elements():
    # Sort a list with multiple distinct elements
    input_nums = [3, 2, 4, 1]
    expected = [1, 2, 3, 4]
    assert pancake_sort(input_nums) == expected

def test_sort_already_sorted_list():
    # Sort an already sorted list
    input_nums = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert pancake_sort(input_nums) == expected

def test_sort_all_elements_equal():
    # Sort a list with all elements equal
    input_nums = [7, 7, 7, 7]
    expected = [7, 7, 7, 7]
    assert pancake_sort(input_nums) == expected

def test_sort_two_elements_descending():
    # Sort a list with two elements in descending order
    input_nums = [2, 1]
    expected = [1, 2]
    assert pancake_sort(input_nums) == expected

def test_sort_single_element_list():
    # Sort a single-element list
    input_nums = [42]
    expected = [42]
    assert pancake_sort(input_nums) == expected

def test_sort_elements_descending_order():
    # Sort a list with elements in descending order
    input_nums = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert pancake_sort(input_nums) == expected
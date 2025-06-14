def access_elements(nums, list_index):
    result = [nums[i] for i in list_index]
    return result

import pytest

def test_access_elements_valid_indices():
    nums = [10, 20, 30, 40, 50]
    list_index = [0, 2, 4]
    expected_output = [10, 30, 50]
    assert access_elements(nums, list_index) == expected_output

def test_access_elements_repeated_indices():
    nums = [5, 15, 25, 35]
    list_index = [1, 1, 3]
    expected_output = [15, 15, 35]
    assert access_elements(nums, list_index) == expected_output

def test_access_elements_descending_order_indices():
    nums = [100, 200, 300, 400]
    list_index = [3, 2, 1, 0]
    expected_output = [400, 300, 200, 100]
    assert access_elements(nums, list_index) == expected_output

def test_access_elements_empty_list_index():
    nums = [1, 2, 3]
    list_index = []
    expected_output = []
    assert access_elements(nums, list_index) == expected_output

def test_access_elements_empty_nums_and_list_index():
    nums = []
    list_index = []
    expected_output = []
    assert access_elements(nums, list_index) == expected_output
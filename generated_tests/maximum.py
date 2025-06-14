def maximum(arr, k):
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans

import pytest

def test_return_empty_list_when_k_is_zero():
    arr = [1, 2, 3, 4, 5]
    k = 0
    expected_output = []
    assert maximum(arr, k) == expected_output

def test_return_largest_element_when_k_is_one():
    arr = [1, 2, 3, 4]
    k = 1
    expected_output = [4]
    assert maximum(arr, k) == expected_output

def test_return_top_3_largest_elements_from_unsorted_array():
    arr = [3, 5, 8, 10, 12]
    k = 3
    expected_output = [8, 10, 12]
    assert maximum(arr, k) == expected_output

def test_return_all_elements_when_k_equals_length_of_array():
    arr = [2, 7, 9]
    k = 3
    expected_output = [2, 7, 9]
    assert maximum(arr, k) == expected_output

def test_return_largest_elements_when_array_contains_duplicates():
    arr = [2, 3, 4, 4, 4]
    k = 2
    expected_output = [4, 4]
    assert maximum(arr, k) == expected_output

def test_return_largest_elements_when_array_is_already_sorted_ascending():
    arr = [1, 2, 3, 4, 5]
    k = 4
    expected_output = [2, 3, 4, 5]
    assert maximum(arr, k) == expected_output

def test_return_largest_elements_when_array_is_sorted_descending():
    arr = [1, 3, 5, 7, 9]
    k = 3
    expected_output = [5, 7, 9]
    assert maximum(arr, k) == expected_output
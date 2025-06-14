def check_min_heap(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap(arr, 2 * i + 2))
    return left_child and right_child

import pytest

def test_empty_array_is_min_heap():
    arr = []
    i = 0
    expected = True
    assert check_min_heap(arr, i) == expected

def test_single_element_array_is_min_heap():
    arr = [10]
    i = 0
    expected = True
    assert check_min_heap(arr, i) == expected

def test_valid_min_heap_three_elements():
    arr = [1, 2, 3]
    i = 0
    expected = True
    assert check_min_heap(arr, i) == expected

def test_invalid_min_heap_left_child_smaller_than_parent():
    arr = [5, 3, 8]
    i = 0
    expected = False
    assert check_min_heap(arr, i) == expected

def test_invalid_min_heap_right_child_smaller_than_parent():
    arr = [5, 6, 4]
    i = 0
    expected = False
    assert check_min_heap(arr, i) == expected

def test_valid_min_heap_multiple_levels():
    arr = [1, 3, 2, 7, 6, 4, 5]
    i = 0
    expected = True
    assert check_min_heap(arr, i) == expected

def test_invalid_min_heap_violation_deep_in_tree():
    arr = [1, 3, 2, 7, 0, 4, 5]
    i = 0
    expected = False
    assert check_min_heap(arr, i) == expected

def test_array_with_only_left_child_last_node_valid():
    arr = [1, 2, 3, 4]
    i = 0
    expected = True
    assert check_min_heap(arr, i) == expected

def test_array_with_only_left_child_last_node_invalid():
    arr = [1, 5, 3, 4]
    i = 0
    expected = False
    assert check_min_heap(arr, i) == expected
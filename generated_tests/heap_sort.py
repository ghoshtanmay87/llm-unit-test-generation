def heap_sort(arr):
    heapify(arr)  
    end = len(arr) - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        shift_down(arr, 0, end - 1)
        end -= 1
    return arr

def heapify(arr):
    start = len(arr) // 2
    while start >= 0:
        shift_down(arr, start, len(arr) - 1)
        start -= 1
def shift_down(arr, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if child <= end and arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            return

import pytest

def test_heap_sort_empty_list_returns_empty_list():
    # Sorting an empty list returns an empty list
    input_arr = []
    expected = []
    assert heap_sort(input_arr) == expected

def test_heap_sort_single_element_list_returns_same_list():
    # Sorting a single-element list returns the same single-element list
    input_arr = [42]
    expected = [42]
    assert heap_sort(input_arr) == expected

def test_heap_sort_two_elements_ascending_order():
    # Sorting a list with two elements in ascending order
    input_arr = [1, 2]
    expected = [1, 2]
    assert heap_sort(input_arr) == expected

def test_heap_sort_two_elements_descending_order():
    # Sorting a list with two elements in descending order
    input_arr = [2, 1]
    expected = [1, 2]
    assert heap_sort(input_arr) == expected

def test_heap_sort_multiple_elements_with_duplicates():
    # Sorting a list with multiple elements including duplicates
    input_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert heap_sort(input_arr) == expected

def test_heap_sort_all_elements_equal():
    # Sorting a list with all elements equal
    input_arr = [7, 7, 7, 7]
    expected = [7, 7, 7, 7]
    assert heap_sort(input_arr) == expected

def test_heap_sort_already_sorted_ascending():
    # Sorting a list already sorted in ascending order
    input_arr = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert heap_sort(input_arr) == expected

def test_heap_sort_sorted_descending_order():
    # Sorting a list sorted in descending order
    input_arr = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert heap_sort(input_arr) == expected
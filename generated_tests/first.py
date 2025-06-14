def first(arr,x,n): 
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            high = mid - 1
    return res

import pytest

def test_first_occurrence_multiple_times():
    arr = [1, 2, 2, 2, 3, 4, 5]
    x = 2
    n = 7
    expected = 1
    assert first(arr, x, n) == expected

def test_first_occurrence_single_time():
    arr = [1, 3, 5, 7, 9]
    x = 5
    n = 5
    expected = 2
    assert first(arr, x, n) == expected

def test_return_minus_one_when_x_not_present():
    arr = [1, 2, 4, 5, 6]
    x = 3
    n = 5
    expected = -1
    assert first(arr, x, n) == expected

def test_first_occurrence_x_is_first_element():
    arr = [2, 2, 2, 3, 4]
    x = 2
    n = 5
    expected = 0
    assert first(arr, x, n) == expected

def test_first_occurrence_x_is_last_element():
    arr = [1, 2, 3, 4, 5]
    x = 5
    n = 5
    expected = 4
    assert first(arr, x, n) == expected

def test_return_minus_one_when_array_empty():
    arr = []
    x = 1
    n = 0
    expected = -1
    assert first(arr, x, n) == expected

def test_first_occurrence_all_elements_same_equal_x():
    arr = [7, 7, 7, 7, 7]
    x = 7
    n = 5
    expected = 0
    assert first(arr, x, n) == expected

def test_return_minus_one_all_elements_same_not_equal_x():
    arr = [8, 8, 8, 8]
    x = 7
    n = 4
    expected = -1
    assert first(arr, x, n) == expected
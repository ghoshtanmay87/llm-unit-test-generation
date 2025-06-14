def check(arr,n): 
    g = 0 
    for i in range(1,n): 
        if (arr[i] - arr[i - 1] > 0 and g == 1): 
            return False
        if (arr[i] - arr[i] < 0): 
            g = 1
    return True

import pytest

def test_strictly_increasing_array():
    arr = [1, 2, 3, 4, 5]
    n = 5
    expected = True
    assert check(arr, n) == expected

def test_strictly_decreasing_array():
    arr = [5, 4, 3, 2, 1]
    n = 5
    expected = True
    assert check(arr, n) == expected

def test_increasing_then_decreasing_array():
    arr = [1, 3, 2]
    n = 3
    expected = True
    assert check(arr, n) == expected

def test_decreasing_then_increasing_array():
    arr = [3, 2, 4]
    n = 3
    expected = False
    assert check(arr, n) == expected

def test_array_with_equal_consecutive_elements():
    arr = [2, 2, 2]
    n = 3
    expected = True
    assert check(arr, n) == expected

def test_single_element_array():
    arr = [10]
    n = 1
    expected = True
    assert check(arr, n) == expected

def test_array_with_multiple_decreases_no_increase_after():
    arr = [5, 4, 3, 2, 1, 0]
    n = 6
    expected = True
    assert check(arr, n) == expected

def test_array_with_increase_after_decrease_at_end():
    arr = [5, 4, 3, 2, 3]
    n = 5
    expected = False
    assert check(arr, n) == expected
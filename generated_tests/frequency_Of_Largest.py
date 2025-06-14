def frequency_Of_Largest(n,arr): 
    mn = arr[0] 
    freq = 1
    for i in range(1,n): 
        if (arr[i] >mn): 
            mn = arr[i] 
            freq = 1
        elif (arr[i] == mn): 
            freq += 1
    return freq

import pytest

def test_all_elements_are_the_same():
    n = 5
    arr = [3, 3, 3, 3, 3]
    expected = 5
    assert frequency_Of_Largest(n, arr) == expected

def test_largest_element_appears_once_at_the_end():
    n = 4
    arr = [1, 2, 3, 4]
    expected = 1
    assert frequency_Of_Largest(n, arr) == expected

def test_largest_element_appears_multiple_times_scattered():
    n = 6
    arr = [2, 5, 3, 5, 1, 5]
    expected = 3
    assert frequency_Of_Largest(n, arr) == expected

def test_single_element_array():
    n = 1
    arr = [10]
    expected = 1
    assert frequency_Of_Largest(n, arr) == expected

def test_largest_element_at_beginning_and_repeated_later():
    n = 7
    arr = [9, 1, 9, 3, 9, 2, 4]
    expected = 3
    assert frequency_Of_Largest(n, arr) == expected

def test_largest_element_is_negative_and_appears_multiple_times():
    n = 5
    arr = [-1, -3, -1, -2, -1]
    expected = 3
    assert frequency_Of_Largest(n, arr) == expected

def test_largest_element_is_zero_and_appears_once():
    n = 4
    arr = [-2, -3, 0, -1]
    expected = 1
    assert frequency_Of_Largest(n, arr) == expected
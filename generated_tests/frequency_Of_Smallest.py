def frequency_Of_Smallest(n,arr): 
    mn = arr[0] 
    freq = 1
    for i in range(1,n): 
        if (arr[i] < mn): 
            mn = arr[i] 
            freq = 1
        elif (arr[i] == mn): 
            freq += 1
    return freq

import pytest

def test_all_elements_are_the_same():
    n = 5
    arr = [2, 2, 2, 2, 2]
    expected = 5
    assert frequency_Of_Smallest(n, arr) == expected

def test_smallest_element_appears_once_at_the_beginning():
    n = 4
    arr = [1, 3, 4, 5]
    expected = 1
    assert frequency_Of_Smallest(n, arr) == expected

def test_smallest_element_appears_multiple_times_scattered():
    n = 6
    arr = [3, 1, 4, 1, 5, 1]
    expected = 3
    assert frequency_Of_Smallest(n, arr) == expected

def test_smallest_element_is_at_the_end_and_appears_twice():
    n = 7
    arr = [5, 6, 7, 8, 9, 2, 2]
    expected = 2
    assert frequency_Of_Smallest(n, arr) == expected

def test_array_with_negative_and_positive_numbers():
    n = 5
    arr = [0, -1, -1, 2, 3]
    expected = 2
    assert frequency_Of_Smallest(n, arr) == expected

def test_single_element_array():
    n = 1
    arr = [10]
    expected = 1
    assert frequency_Of_Smallest(n, arr) == expected

def test_smallest_element_appears_in_the_middle_once():
    n = 5
    arr = [5, 4, 1, 6, 7]
    expected = 1
    assert frequency_Of_Smallest(n, arr) == expected

def test_all_elements_distinct_and_sorted_ascending():
    n = 5
    arr = [1, 2, 3, 4, 5]
    expected = 1
    assert frequency_Of_Smallest(n, arr) == expected

def test_all_elements_distinct_and_sorted_descending():
    n = 5
    arr = [5, 4, 3, 2, 1]
    expected = 1
    assert frequency_Of_Smallest(n, arr) == expected

def test_multiple_smallest_elements_at_start():
    n = 6
    arr = [0, 0, 1, 2, 3, 4]
    expected = 2
    assert frequency_Of_Smallest(n, arr) == expected
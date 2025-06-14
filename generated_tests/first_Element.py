def first_Element(arr,n,k): 
    count_map = {}; 
    for i in range(0, n): 
        if(arr[i] in count_map.keys()): 
            count_map[arr[i]] += 1
        else: 
            count_map[arr[i]] = 1
        i += 1
    for i in range(0, n):  
        if (count_map[arr[i]] == k): 
            return arr[i] 
        i += 1 
    return -1

import pytest

def test_first_element_multiple_duplicates_k_2():
    arr = [1, 2, 2, 3, 1, 4, 2]
    n = 7
    k = 2
    expected = 1
    assert first_Element(arr, n, k) == expected

def test_first_element_multiple_duplicates_k_3():
    arr = [1, 2, 2, 3, 1, 4, 2]
    n = 7
    k = 3
    expected = 2
    assert first_Element(arr, n, k) == expected

def test_no_element_appears_exactly_k_times():
    arr = [1, 2, 3, 4, 5]
    n = 5
    k = 2
    expected = -1
    assert first_Element(arr, n, k) == expected

def test_single_element_list_k_1():
    arr = [10]
    n = 1
    k = 1
    expected = 10
    assert first_Element(arr, n, k) == expected

def test_multiple_elements_all_appear_once_k_1():
    arr = [5, 6, 7, 8]
    n = 4
    k = 1
    expected = 5
    assert first_Element(arr, n, k) == expected

def test_all_elements_appear_same_number_of_times_k_matches():
    arr = [9, 9, 8, 8]
    n = 4
    k = 2
    expected = 9
    assert first_Element(arr, n, k) == expected

def test_empty_array_input():
    arr = []
    n = 0
    k = 1
    expected = -1
    assert first_Element(arr, n, k) == expected

def test_element_appears_more_than_k_times_but_not_exactly_k():
    arr = [4, 4, 4, 4, 5, 5]
    n = 6
    k = 3
    expected = -1
    assert first_Element(arr, n, k) == expected

def test_first_element_appears_exactly_k_times_but_later_elements_also():
    arr = [7, 8, 7, 8, 7, 8]
    n = 6
    k = 3
    expected = 7
    assert first_Element(arr, n, k) == expected

def test_k_is_zero_no_element_can_appear_zero_times():
    arr = [1, 2, 3]
    n = 3
    k = 0
    expected = -1
    assert first_Element(arr, n, k) == expected
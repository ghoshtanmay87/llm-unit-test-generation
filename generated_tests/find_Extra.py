def find_Extra(arr1,arr2,n) : 
    for i in range(0, n) : 
        if (arr1[i] != arr2[i]) : 
            return i 
    return n

import pytest

def test_extra_element_at_end_of_second_array():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 4, 5, 6]
    n = 5
    expected_output = 5
    assert find_Extra(arr1, arr2, n) == expected_output

def test_extra_element_at_beginning_of_second_array():
    arr1 = [2, 3, 4, 5]
    arr2 = [1, 2, 3, 4, 5]
    n = 4
    expected_output = 0
    assert find_Extra(arr1, arr2, n) == expected_output

def test_extra_element_in_middle_of_second_array():
    arr1 = [1, 2, 4, 5]
    arr2 = [1, 2, 3, 4, 5]
    n = 4
    expected_output = 2
    assert find_Extra(arr1, arr2, n) == expected_output

def test_identical_first_n_elements_extra_element_at_end():
    arr1 = [10, 20, 30]
    arr2 = [10, 20, 30, 40]
    n = 3
    expected_output = 3
    assert find_Extra(arr1, arr2, n) == expected_output

def test_extra_element_first_element_single_element_arr1():
    arr1 = [2]
    arr2 = [1, 2]
    n = 1
    expected_output = 0
    assert find_Extra(arr1, arr2, n) == expected_output
def sum_even_and_even_index(arr,n):  
    i = 0
    sum = 0
    for i in range(0,n,2): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum

import pytest

def test_sum_even_elements_at_even_indices_mixed_even_odd():
    arr = [2, 3, 4, 5, 6, 7]
    n = 6
    expected = 8
    assert sum_even_and_even_index(arr, n) == expected

def test_sum_even_elements_at_even_indices_some_even_indices_odd_numbers():
    arr = [1, 2, 3, 4, 5, 6]
    n = 6
    expected = 0
    assert sum_even_and_even_index(arr, n) == expected

def test_sum_even_elements_at_even_indices_empty_array():
    arr = []
    n = 0
    expected = 0
    assert sum_even_and_even_index(arr, n) == expected

def test_sum_even_elements_at_even_indices_single_even_element_index_0():
    arr = [4]
    n = 1
    expected = 4
    assert sum_even_and_even_index(arr, n) == expected

def test_sum_even_elements_at_even_indices_single_odd_element_index_0():
    arr = [5]
    n = 1
    expected = 0
    assert sum_even_and_even_index(arr, n) == expected

def test_sum_even_elements_at_even_indices_negative_even_and_odd_numbers():
    arr = [-2, -3, -4, -5, -6, -7]
    n = 6
    expected = -12
    assert sum_even_and_even_index(arr, n) == expected

def test_sum_even_elements_at_even_indices_with_zero_included():
    arr = [0, 1, 2, 3, 4, 5]
    n = 6
    expected = 6
    assert sum_even_and_even_index(arr, n) == expected

def test_sum_even_elements_at_even_indices_n_less_than_length():
    arr = [2, 4, 6, 8, 10]
    n = 3
    expected = 8
    assert sum_even_and_even_index(arr, n) == expected
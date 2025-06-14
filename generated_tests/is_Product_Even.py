def is_Product_Even(arr,n): 
    for i in range(0,n): 
        if ((arr[i] & 1) == 0): 
            return True
    return False

import pytest

def test_array_contains_at_least_one_even_number():
    arr = [1, 3, 4, 7]
    n = 4
    expected = True
    assert is_Product_Even(arr, n) == expected

def test_array_contains_only_odd_numbers():
    arr = [1, 3, 5, 7]
    n = 4
    expected = False
    assert is_Product_Even(arr, n) == expected

def test_array_contains_single_even_number_at_start():
    arr = [2, 3, 5, 7]
    n = 4
    expected = True
    assert is_Product_Even(arr, n) == expected

def test_array_contains_single_even_number_at_end():
    arr = [1, 3, 5, 8]
    n = 4
    expected = True
    assert is_Product_Even(arr, n) == expected

def test_empty_array_input():
    arr = []
    n = 0
    expected = False
    assert is_Product_Even(arr, n) == expected

def test_array_with_one_odd_number():
    arr = [9]
    n = 1
    expected = False
    assert is_Product_Even(arr, n) == expected

def test_array_with_one_even_number():
    arr = [10]
    n = 1
    expected = True
    assert is_Product_Even(arr, n) == expected
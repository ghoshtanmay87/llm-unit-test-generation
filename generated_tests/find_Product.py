def find_Product(arr,n): 
    arr.sort() 
    prod = 1
    for i in range(0,n,1): 
        if (arr[i - 1] != arr[i]): 
            prod = prod * arr[i] 
    return prod;

import pytest

def test_all_distinct_positive_integers():
    arr = [1, 2, 3, 4]
    n = 4
    expected_output = 24
    assert find_Product(arr, n) == expected_output

def test_array_with_duplicates():
    arr = [2, 2, 3, 4]
    n = 4
    expected_output = 24
    assert find_Product(arr, n) == expected_output

def test_all_elements_are_the_same():
    arr = [5, 5, 5, 5]
    n = 4
    expected_output = 1
    assert find_Product(arr, n) == expected_output

def test_array_with_negative_and_positive_numbers():
    arr = [-1, -1, 2, 3]
    n = 4
    expected_output = -6
    assert find_Product(arr, n) == expected_output

def test_single_element_array():
    arr = [10]
    n = 1
    expected_output = 1
    assert find_Product(arr, n) == expected_output

def test_empty_array():
    arr = []
    n = 0
    expected_output = 1
    assert find_Product(arr, n) == expected_output
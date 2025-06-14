def sum_Pairs(arr,n): 
    sum = 0
    for i in range(n - 1,-1,-1): 
        sum += i*arr[i] - (n-1-i) * arr[i] 
    return sum

import pytest

def test_sum_pairs_simple_increasing_array_corrected():
    arr = [1, 2, 3]
    n = 3
    expected = 4
    assert sum_Pairs(arr, n) == expected

def test_sum_pairs_all_elements_equal():
    arr = [5, 5, 5, 5]
    n = 4
    expected = 0
    assert sum_Pairs(arr, n) == expected

def test_sum_pairs_zero_elements():
    arr = [0, 0, 0]
    n = 3
    expected = 0
    assert sum_Pairs(arr, n) == expected

def test_sum_pairs_mixed_positive_and_negative_values_corrected():
    arr = [1, -2, 3, -4]
    n = 4
    expected = -10
    assert sum_Pairs(arr, n) == expected

def test_sum_pairs_single_element_array():
    arr = [10]
    n = 1
    expected = 0
    assert sum_Pairs(arr, n) == expected

def test_sum_pairs_empty_array():
    arr = []
    n = 0
    expected = 0
    assert sum_Pairs(arr, n) == expected
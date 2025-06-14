def min_Ops(arr,n,k): 
    max1 = max(arr) 
    res = 0
    for i in range(0,n):  
        if ((max1 - arr[i]) % k != 0): 
            return -1 
        else: 
            res += (max1 - arr[i]) / k 
    return int(res)

import pytest

def test_all_elements_equal_no_operations_needed():
    arr = [5, 5, 5]
    n = 3
    k = 1
    expected = 0
    assert min_Ops(arr, n, k) == expected

def test_elements_cannot_be_equalized_difference_not_divisible_by_k():
    arr = [1, 5, 7]
    n = 3
    k = 3
    expected = -1
    assert min_Ops(arr, n, k) == expected

def test_single_element_array_no_operations_needed():
    arr = [10]
    n = 1
    k = 5
    expected = 0
    assert min_Ops(arr, n, k) == expected

def test_all_elements_zero_k_is_one():
    arr = [0, 0, 0]
    n = 3
    k = 1
    expected = 0
    assert min_Ops(arr, n, k) == expected

def test_large_differences_divisible_by_k():
    arr = [10, 20, 30]
    n = 3
    k = 10
    expected = 3
    assert min_Ops(arr, n, k) == expected

def test_elements_can_be_equalized_by_adding_k_multiple_times():
    arr = [2, 4, 6]
    n = 3
    k = 2
    expected = 3
    assert min_Ops(arr, n, k) == expected

def test_difference_zero_for_some_elements_others_divisible_by_k():
    arr = [7, 7, 13]
    n = 3
    k = 3
    expected = 4
    assert min_Ops(arr, n, k) == expected
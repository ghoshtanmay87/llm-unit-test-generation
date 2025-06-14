def max_Abs_Diff(arr,n): 
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle)

import pytest

def test_array_with_distinct_positive_integers():
    arr = [1, 2, 3, 4, 5]
    n = 5
    expected = 4
    assert max_Abs_Diff(arr, n) == expected

def test_array_with_negative_and_positive_integers():
    arr = [-10, 0, 10, 20]
    n = 4
    expected = 30
    assert max_Abs_Diff(arr, n) == expected

def test_array_with_all_elements_the_same():
    arr = [7, 7, 7, 7]
    n = 4
    expected = 0
    assert max_Abs_Diff(arr, n) == expected

def test_array_with_single_element():
    arr = [42]
    n = 1
    expected = 0
    assert max_Abs_Diff(arr, n) == expected

def test_array_with_mixed_positive_negative_and_zero_values():
    arr = [-3, 0, 2, -1, 5]
    n = 5
    expected = 8
    assert max_Abs_Diff(arr, n) == expected
def split_Arr(a,n,k):  
   b = a[:k] 
   return (a[k::]+b[::])

import pytest

def test_split_array_k_less_than_length():
    # Split array with k less than length of array
    a = [1, 2, 3, 4, 5]
    n = 5
    k = 2
    expected_output = [3, 4, 5, 1, 2]
    assert split_Arr(a, n, k) == expected_output

def test_split_array_k_zero_no_rotation():
    # Split array with k equal to zero (no rotation)
    a = [10, 20, 30, 40]
    n = 4
    k = 0
    expected_output = [10, 20, 30, 40]
    assert split_Arr(a, n, k) == expected_output

def test_split_array_k_equal_length_full_rotation():
    # Split array with k equal to length of array (full rotation)
    a = [7, 8, 9]
    n = 3
    k = 3
    expected_output = [7, 8, 9]
    assert split_Arr(a, n, k) == expected_output

def test_split_array_k_greater_than_length_no_explicit_handling():
    # Split array with k greater than length of array (no explicit handling)
    a = [1, 2, 3]
    n = 3
    k = 5
    expected_output = [1, 2, 3]
    assert split_Arr(a, n, k) == expected_output

def test_split_array_single_element_k_one():
    # Split array with single element and k=1
    a = [42]
    n = 1
    k = 1
    expected_output = [42]
    assert split_Arr(a, n, k) == expected_output

def test_split_array_empty_list():
    # Split array with empty list
    a = []
    n = 0
    k = 0
    expected_output = []
    assert split_Arr(a, n, k) == expected_output
def sum_Of_Subarray_Prod(arr,n):
    ans = 0
    res = 0
    i = n - 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)

import pytest

def test_sum_of_subarray_products_single_element():
    # Scenario: Sum of subarray products for a single element array
    arr = [5]
    n = 1
    expected = 5
    assert sum_Of_Subarray_Prod(arr, n) == expected

def test_sum_of_subarray_products_two_elements():
    # Scenario: Sum of subarray products for two elements array
    arr = [1, 2]
    n = 2
    expected = 5
    assert sum_Of_Subarray_Prod(arr, n) == expected

def test_sum_of_subarray_products_three_elements():
    # Scenario: Sum of subarray products for three elements array
    arr = [1, 2, 3]
    n = 3
    expected = 20
    assert sum_Of_Subarray_Prod(arr, n) == expected

def test_sum_of_subarray_products_with_zero():
    # Scenario: Sum of subarray products for array with zero
    arr = [0, 2, 3]
    n = 3
    expected = 11
    assert sum_Of_Subarray_Prod(arr, n) == expected

def test_sum_of_subarray_products_all_ones():
    # Scenario: Sum of subarray products for array with all ones
    arr = [1, 1, 1, 1]
    n = 4
    expected = 10
    assert sum_Of_Subarray_Prod(arr, n) == expected

def test_sum_of_subarray_products_descending_array():
    # Scenario: Sum of subarray products for descending array
    arr = [3, 2, 1]
    n = 3
    expected = 20
    assert sum_Of_Subarray_Prod(arr, n) == expected
def find_Min_Swaps(arr,n) : 
    noOfZeroes = [0] * n 
    count = 0 
    noOfZeroes[n - 1] = 1 - arr[n - 1] 
    for i in range(n-2,-1,-1) : 
        noOfZeroes[i] = noOfZeroes[i + 1] 
        if (arr[i] == 0) : 
            noOfZeroes[i] = noOfZeroes[i] + 1
    for i in range(0,n) : 
        if (arr[i] == 1) : 
            count = count + noOfZeroes[i] 
    return count

import pytest

def test_all_ones_no_zeros_to_swap():
    arr = [1, 1, 1, 1]
    n = 4
    expected = 0
    assert find_Min_Swaps(arr, n) == expected

def test_all_zeros_no_ones_to_swap():
    arr = [0, 0, 0, 0]
    n = 4
    expected = 0
    assert find_Min_Swaps(arr, n) == expected

def test_alternating_ones_zeros_starting_with_one():
    arr = [1, 0, 1, 0]
    n = 4
    expected = 3
    assert find_Min_Swaps(arr, n) == expected

def test_alternating_zeros_ones_starting_with_zero():
    arr = [0, 1, 0, 1]
    n = 4
    expected = 1
    assert find_Min_Swaps(arr, n) == expected

def test_single_element_array_with_one():
    arr = [1]
    n = 1
    expected = 0
    assert find_Min_Swaps(arr, n) == expected

def test_single_element_array_with_zero():
    arr = [0]
    n = 1
    expected = 0
    assert find_Min_Swaps(arr, n) == expected

def test_mixed_array_zeros_clustered_at_end():
    arr = [1, 1, 0, 0]
    n = 4
    expected = 4
    assert find_Min_Swaps(arr, n) == expected

def test_mixed_array_zeros_clustered_at_start():
    arr = [0, 0, 1, 1]
    n = 4
    expected = 0
    assert find_Min_Swaps(arr, n) == expected

def test_array_with_one_zero_between_ones():
    arr = [1, 0, 1]
    n = 3
    expected = 1
    assert find_Min_Swaps(arr, n) == expected
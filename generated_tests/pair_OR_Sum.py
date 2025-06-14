def pair_OR_Sum(arr,n) : 
    ans = 0 
    for i in range(0,n) :    
        for j in range(i + 1,n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans

import pytest

def test_pairwise_xor_sum_two_elements():
    # Calculate pairwise XOR sum for a small array of two elements
    arr = [1, 2]
    n = 2
    expected = 3
    assert pair_OR_Sum(arr, n) == expected

def test_pairwise_xor_sum_three_distinct_elements():
    # Calculate pairwise XOR sum for three elements with distinct values
    arr = [1, 2, 3]
    n = 3
    expected = 6
    assert pair_OR_Sum(arr, n) == expected

def test_pairwise_xor_sum_identical_elements():
    # Calculate pairwise XOR sum for an array with identical elements
    arr = [4, 4, 4]
    n = 3
    expected = 0
    assert pair_OR_Sum(arr, n) == expected

def test_pairwise_xor_sum_four_elements():
    # Calculate pairwise XOR sum for an array with four elements
    arr = [1, 2, 4, 8]
    n = 4
    expected = 30
    assert pair_OR_Sum(arr, n) == expected

def test_pairwise_xor_sum_zero_and_positive_integers():
    # Calculate pairwise XOR sum for an array with zero and positive integers
    arr = [0, 1, 3]
    n = 3
    expected = 4
    assert pair_OR_Sum(arr, n) == expected
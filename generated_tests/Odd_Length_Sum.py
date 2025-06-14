def Odd_Length_Sum(arr):
    Sum = 0
    l = len(arr)
    for i in range(l):
        Sum += ((((i + 1) *(l - i) + 1) // 2) * arr[i])
    return Sum

import pytest

def test_single_element_array():
    # Sum of odd-length subarray sums for a single-element array
    arr = [5]
    expected = 5
    assert Odd_Length_Sum(arr) == expected

def test_two_element_array():
    # Sum of odd-length subarray sums for a two-element array
    arr = [1, 2]
    expected = 3
    assert Odd_Length_Sum(arr) == expected

def test_three_element_array():
    # Sum of odd-length subarray sums for a three-element array
    arr = [1, 4, 2]
    expected = 14
    assert Odd_Length_Sum(arr) == expected

def test_empty_array():
    # Sum of odd-length subarray sums for an empty array
    arr = []
    expected = 0
    assert Odd_Length_Sum(arr) == expected

def test_all_zeros_array():
    # Sum of odd-length subarray sums for an array with all zeros
    arr = [0, 0, 0]
    expected = 0
    assert Odd_Length_Sum(arr) == expected

def test_four_element_array():
    # Sum of odd-length subarray sums for a four-element array
    arr = [1, 2, 3, 4]
    expected = 25
    assert Odd_Length_Sum(arr) == expected

def test_array_with_negative_numbers():
    # Sum of odd-length subarray sums for an array with negative numbers
    arr = [2, -1, 3]
    expected = 8
    assert Odd_Length_Sum(arr) == expected
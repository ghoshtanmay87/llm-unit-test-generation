def find_Min_Diff(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff

import pytest

def test_min_diff_sorted_positive_integers():
    arr = [1, 5, 3, 19, 18, 25]
    n = 6
    expected = 1
    assert find_Min_Diff(arr, n) == expected

def test_min_diff_negative_and_positive_integers():
    arr = [-10, -3, 0, 5, 9]
    n = 5
    expected = 3
    assert find_Min_Diff(arr, n) == expected

def test_min_diff_all_identical_elements():
    arr = [7, 7, 7, 7]
    n = 4
    expected = 0
    assert find_Min_Diff(arr, n) == expected

def test_min_diff_two_elements():
    arr = [100, 105]
    n = 2
    expected = 5
    assert find_Min_Diff(arr, n) == expected

def test_min_diff_floating_point_numbers():
    arr = [1.1, 1.2, 1.15, 2.0]
    n = 4
    expected = 0.05
    assert find_Min_Diff(arr, n) == expected
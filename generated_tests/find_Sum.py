def find_Sum(arr,n): 
    arr.sort() 
    sum = arr[0] 
    for i in range(0,n-1): 
        if (arr[i] != arr[i+1]): 
            sum = sum + arr[i+1]   
    return sum

import pytest

def test_sum_unique_elements_sorted_with_duplicates():
    # Sum of unique elements in a sorted array with duplicates
    arr = [1, 2, 2, 3]
    n = 4
    expected = 6
    assert find_Sum(arr, n) == expected

def test_sum_unique_elements_all_same():
    # Sum of unique elements when all elements are the same
    arr = [5, 5, 5, 5]
    n = 4
    expected = 5
    assert find_Sum(arr, n) == expected

def test_sum_unique_elements_unsorted_multiple_duplicates():
    # Sum of unique elements in an unsorted array with multiple duplicates
    arr = [4, 1, 2, 2, 3, 4]
    n = 6
    expected = 10
    assert find_Sum(arr, n) == expected

def test_sum_unique_elements_single_element():
    # Sum of unique elements in a single-element array
    arr = [7]
    n = 1
    expected = 7
    assert find_Sum(arr, n) == expected

def test_sum_unique_elements_negative_and_positive():
    # Sum of unique elements in an array with negative and positive numbers
    arr = [-1, -1, 0, 1, 1]
    n = 5
    expected = 0
    assert find_Sum(arr, n) == expected
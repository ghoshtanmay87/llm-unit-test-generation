def count_Pairs(arr,n): 
    cnt = 0; 
    for i in range(n): 
        for j in range(i + 1,n): 
            if (arr[i] == arr[j]): 
                cnt += 1; 
    return cnt;

import pytest

def test_count_pairs_no_duplicates():
    # Scenario: Count pairs in an array with no duplicates
    arr = [1, 2, 3, 4]
    n = 4
    expected = 0
    assert count_Pairs(arr, n) == expected

def test_count_pairs_all_elements_same():
    # Scenario: Count pairs in an array with all elements the same
    arr = [5, 5, 5, 5]
    n = 4
    expected = 6
    assert count_Pairs(arr, n) == expected

def test_count_pairs_some_duplicates():
    # Scenario: Count pairs in an array with some duplicates
    arr = [1, 2, 2, 3, 3, 3]
    n = 6
    expected = 4
    assert count_Pairs(arr, n) == expected

def test_count_pairs_two_duplicates():
    # Scenario: Count pairs in an array with two duplicates
    arr = [1, 1, 2, 3, 4]
    n = 5
    expected = 1
    assert count_Pairs(arr, n) == expected

def test_count_pairs_empty_array():
    # Scenario: Count pairs in an empty array
    arr = []
    n = 0
    expected = 0
    assert count_Pairs(arr, n) == expected

def test_count_pairs_one_element():
    # Scenario: Count pairs in an array with one element
    arr = [10]
    n = 1
    expected = 0
    assert count_Pairs(arr, n) == expected

def test_count_pairs_multiple_duplicates_different_values():
    # Scenario: Count pairs in an array with multiple duplicates of different values
    arr = [1, 2, 1, 2, 1]
    n = 5
    expected = 4
    assert count_Pairs(arr, n) == expected
def find_Diff(arr,n): 
    arr.sort()  
    count = 0; max_count = 0; min_count = n 
    for i in range(0,(n-1)): 
        if arr[i] == arr[i + 1]: 
            count += 1
            continue
        else: 
            max_count = max(max_count,count) 
            min_count = min(min_count,count) 
            count = 0
    return max_count - min_count

import pytest

def test_all_elements_distinct():
    # Scenario: All elements are distinct
    arr = [1, 2, 3, 4, 5]
    n = 5
    expected_output = 0
    assert find_Diff(arr, n) == expected_output

def test_all_elements_same():
    # Scenario: All elements are the same
    arr = [7, 7, 7, 7]
    n = 4
    expected_output = -4
    assert find_Diff(arr, n) == expected_output

def test_multiple_sequences_of_duplicates_with_different_lengths():
    # Scenario: Multiple sequences of duplicates with different lengths
    arr = [1, 1, 2, 3, 3, 3, 4, 4]
    n = 8
    expected_output = 2
    assert find_Diff(arr, n) == expected_output

def test_no_duplicates_except_one_pair():
    # Scenario: No duplicates except one pair
    arr = [5, 1, 2, 2, 3]
    n = 5
    expected_output = 1
    assert find_Diff(arr, n) == expected_output

def test_empty_array():
    # Scenario: Empty array
    arr = []
    n = 0
    expected_output = 0
    assert find_Diff(arr, n) == expected_output
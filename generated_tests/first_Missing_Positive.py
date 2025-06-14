def first_Missing_Positive(arr,n): 
    ptr = 0
    for i in range(n):
        if arr[i] == 1:
            ptr = 1
            break
    if ptr == 0:
        return(1)
    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = 1
    for i in range(n):
        arr[(arr[i] - 1) % n] += n
    for i in range(n):
        if arr[i] <= n:
            return(i + 1)
    return(n + 1)

import pytest

def test_array_missing_number_1():
    # Array missing the number 1
    arr = [2, 3, 4]
    n = 3
    expected = 1
    assert first_Missing_Positive(arr, n) == expected

def test_array_consecutive_positives_starting_from_1():
    # Array contains consecutive positive integers starting from 1
    arr = [1, 2, 3, 4, 5]
    n = 5
    expected = 6
    assert first_Missing_Positive(arr, n) == expected

def test_array_with_positive_integers_missing_middle_number():
    # Array with positive integers missing a number in the middle
    arr = [3, 4, -1, 1]
    n = 4
    expected = 2
    assert first_Missing_Positive(arr, n) == expected

def test_array_with_duplicates_and_missing_number_2():
    # Array with duplicates and missing number 2
    arr = [1, 1, 0, 2, 2]
    n = 5
    expected = 3
    assert first_Missing_Positive(arr, n) == expected

def test_array_with_all_negative_numbers():
    # Array with all negative numbers
    arr = [-3, -2, -1]
    n = 3
    expected = 1
    assert first_Missing_Positive(arr, n) == expected

def test_array_with_large_numbers_out_of_range():
    # Array with large numbers out of range
    arr = [7, 8, 9, 11, 12]
    n = 5
    expected = 1
    assert first_Missing_Positive(arr, n) == expected

def test_array_with_mixed_values_and_missing_number_5():
    # Array with mixed values and missing number 5
    arr = [1, 2, 3, 4, 6]
    n = 5
    expected = 5
    assert first_Missing_Positive(arr, n) == expected
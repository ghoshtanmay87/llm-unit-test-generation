def get_pairs_count(arr, n, sum):
    count = 0 
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
    return count

import pytest

def test_no_pairs_in_empty_array():
    arr = []
    n = 0
    sum_value = 5
    expected = 0
    assert get_pairs_count(arr, n, sum_value) == expected

def test_single_element_array_cannot_form_pairs():
    arr = [3]
    n = 1
    sum_value = 3
    expected = 0
    assert get_pairs_count(arr, n, sum_value) == expected

def test_two_elements_that_sum_to_target():
    arr = [2, 3]
    n = 2
    sum_value = 5
    expected = 1
    assert get_pairs_count(arr, n, sum_value) == expected

def test_two_elements_that_do_not_sum_to_target():
    arr = [2, 4]
    n = 2
    sum_value = 5
    expected = 0
    assert get_pairs_count(arr, n, sum_value) == expected

def test_multiple_pairs_with_duplicates():
    arr = [1, 5, 7, -1, 5]
    n = 5
    sum_value = 6
    expected = 3
    assert get_pairs_count(arr, n, sum_value) == expected

def test_all_elements_same_sum_to_twice_element():
    arr = [3, 3, 3, 3]
    n = 4
    sum_value = 6
    expected = 6
    assert get_pairs_count(arr, n, sum_value) == expected

def test_no_pairs_sum_to_target():
    arr = [1, 2, 3, 4]
    n = 4
    sum_value = 10
    expected = 0
    assert get_pairs_count(arr, n, sum_value) == expected

def test_negative_numbers_included():
    arr = [-2, -1, 0, 1, 2]
    n = 5
    sum_value = 0
    expected = 2
    assert get_pairs_count(arr, n, sum_value) == expected

def test_large_array_with_multiple_pairs():
    arr = [1, 2, 3, 4, 3]
    n = 5
    sum_value = 6
    expected = 2
    assert get_pairs_count(arr, n, sum_value) == expected
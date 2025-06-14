def find_last_occurrence(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            left = mid + 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result

import pytest

def test_find_last_occurrence_multiple_times():
    A = [1, 2, 2, 2, 3, 4, 5]
    x = 2
    expected = 3
    assert find_last_occurrence(A, x) == expected

def test_find_last_occurrence_single_time():
    A = [1, 2, 3, 4, 5]
    x = 4
    expected = 3
    assert find_last_occurrence(A, x) == expected

def test_return_minus_one_when_x_not_present():
    A = [1, 2, 3, 4, 5]
    x = 6
    expected = -1
    assert find_last_occurrence(A, x) == expected

def test_find_last_occurrence_first_element_repeated():
    A = [2, 2, 2, 3, 4, 5]
    x = 2
    expected = 2
    assert find_last_occurrence(A, x) == expected

def test_find_last_occurrence_last_element_repeated():
    A = [1, 2, 3, 4, 5, 5, 5]
    x = 5
    expected = 6
    assert find_last_occurrence(A, x) == expected

def test_find_last_occurrence_single_element_list():
    A = [7]
    x = 7
    expected = 0
    assert find_last_occurrence(A, x) == expected

def test_return_minus_one_empty_list():
    A = []
    x = 1
    expected = -1
    assert find_last_occurrence(A, x) == expected

def test_find_last_occurrence_all_elements_are_x():
    A = [4, 4, 4, 4, 4]
    x = 4
    expected = 4
    assert find_last_occurrence(A, x) == expected

def test_return_minus_one_x_smaller_than_all():
    A = [10, 20, 30, 40]
    x = 5
    expected = -1
    assert find_last_occurrence(A, x) == expected

def test_return_minus_one_x_larger_than_all():
    A = [10, 20, 30, 40]
    x = 50
    expected = -1
    assert find_last_occurrence(A, x) == expected
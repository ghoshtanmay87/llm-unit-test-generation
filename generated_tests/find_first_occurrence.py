def find_first_occurrence(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result

import pytest

def test_find_first_occurrence_multiple_times():
    A = [1, 2, 2, 2, 3, 4, 5]
    x = 2
    expected = 1
    assert find_first_occurrence(A, x) == expected

def test_find_first_occurrence_single_time():
    A = [1, 3, 5, 7, 9]
    x = 5
    expected = 2
    assert find_first_occurrence(A, x) == expected

def test_return_minus_one_when_x_not_present():
    A = [1, 2, 4, 5, 6]
    x = 3
    expected = -1
    assert find_first_occurrence(A, x) == expected

def test_find_first_occurrence_x_is_first_element():
    A = [2, 2, 3, 4, 5]
    x = 2
    expected = 0
    assert find_first_occurrence(A, x) == expected

def test_find_first_occurrence_x_is_last_element():
    A = [1, 2, 3, 4, 5, 5, 5]
    x = 5
    expected = 4
    assert find_first_occurrence(A, x) == expected

def test_empty_list_returns_minus_one():
    A = []
    x = 10
    expected = -1
    assert find_first_occurrence(A, x) == expected

def test_single_element_list_element_equals_x():
    A = [7]
    x = 7
    expected = 0
    assert find_first_occurrence(A, x) == expected

def test_single_element_list_element_not_equals_x():
    A = [7]
    x = 3
    expected = -1
    assert find_first_occurrence(A, x) == expected

def test_all_elements_same_equal_to_x():
    A = [4, 4, 4, 4, 4]
    x = 4
    expected = 0
    assert find_first_occurrence(A, x) == expected

def test_all_elements_same_not_equal_to_x():
    A = [4, 4, 4, 4, 4]
    x = 5
    expected = -1
    assert find_first_occurrence(A, x) == expected
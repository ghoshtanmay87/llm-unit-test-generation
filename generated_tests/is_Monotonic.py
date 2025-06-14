def is_Monotonic(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

import pytest

def test_list_strictly_increasing():
    A = [1, 2, 3, 4, 5]
    expected = True
    assert is_Monotonic(A) == expected

def test_list_strictly_decreasing():
    A = [5, 4, 3, 2, 1]
    expected = True
    assert is_Monotonic(A) == expected

def test_list_constant_all_elements_equal():
    A = [3, 3, 3, 3]
    expected = True
    assert is_Monotonic(A) == expected

def test_list_neither_increasing_nor_decreasing():
    A = [1, 3, 2, 4]
    expected = False
    assert is_Monotonic(A) == expected

def test_list_two_elements_increasing():
    A = [1, 2]
    expected = True
    assert is_Monotonic(A) == expected

def test_list_two_elements_decreasing():
    A = [2, 1]
    expected = True
    assert is_Monotonic(A) == expected

def test_list_single_element():
    A = [10]
    expected = True
    assert is_Monotonic(A) == expected

def test_list_equal_adjacent_elements_overall_increasing():
    A = [1, 2, 2, 3]
    expected = True
    assert is_Monotonic(A) == expected

def test_list_equal_adjacent_elements_overall_decreasing():
    A = [3, 3, 2, 1]
    expected = True
    assert is_Monotonic(A) == expected

def test_empty_list():
    A = []
    expected = True
    assert is_Monotonic(A) == expected
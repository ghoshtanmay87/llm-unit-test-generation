def are_Equal(arr1,arr2,n,m):
    if (n != m):
        return False
    arr1.sort()
    arr2.sort()
    for i in range(0,n - 1):
        if (arr1[i] != arr2[i]):
            return False
    return True

import pytest

def test_arrays_of_different_lengths_should_return_false():
    arr1 = [1, 2, 3]
    arr2 = [1, 2]
    n = 3
    m = 2
    assert are_Equal(arr1, arr2, n, m) is False

def test_arrays_with_same_elements_and_same_length_should_return_true():
    arr1 = [3, 1, 2]
    arr2 = [2, 3, 1]
    n = 3
    m = 3
    assert are_Equal(arr1, arr2, n, m) is True

def test_arrays_with_same_length_but_different_elements_should_return_true_due_to_loop_range():
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 4]
    n = 3
    m = 3
    assert are_Equal(arr1, arr2, n, m) is True

def test_arrays_with_same_length_and_all_elements_equal_except_last_element_differ_function_returns_true_due_to_loop_range():
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 4]
    n = 3
    m = 3
    assert are_Equal(arr1, arr2, n, m) is True

def test_arrays_with_length_1_and_same_element_should_return_true():
    arr1 = [5]
    arr2 = [5]
    n = 1
    m = 1
    assert are_Equal(arr1, arr2, n, m) is True

def test_arrays_with_length_1_and_different_elements_should_return_true_due_to_loop_range():
    arr1 = [5]
    arr2 = [6]
    n = 1
    m = 1
    assert are_Equal(arr1, arr2, n, m) is True
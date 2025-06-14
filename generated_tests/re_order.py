def re_order(A):
    k = 0
    for i in A:
        if i:
            A[k] = i
            k = k + 1
    for i in range(k, len(A)):
        A[i] = 0
    return A

import pytest

def test_re_order_mixed_zeros_and_nonzero_integers():
    A = [1, 0, 2, 0, 3]
    expected = [1, 2, 3, 0, 0]
    assert re_order(A) == expected

def test_re_order_all_zeros():
    A = [0, 0, 0]
    expected = [0, 0, 0]
    assert re_order(A) == expected

def test_re_order_all_nonzero_elements():
    A = [4, 5, 6]
    expected = [4, 5, 6]
    assert re_order(A) == expected

def test_re_order_zeros_only_at_start():
    A = [0, 0, 7, 8]
    expected = [7, 8, 0, 0]
    assert re_order(A) == expected

def test_re_order_empty_list():
    A = []
    expected = []
    assert re_order(A) == expected

def test_re_order_boolean_values_treated_as_integers():
    A = [True, False, True, 0]
    expected = [True, True, 0, 0]
    assert re_order(A) == expected

def test_re_order_negative_and_positive_integers_including_zeros():
    A = [-1, 0, 2, 0, -3]
    expected = [-1, 2, -3, 0, 0]
    assert re_order(A) == expected
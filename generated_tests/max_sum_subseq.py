def max_sum_subseq(A):
    n = len(A)
    if n == 1:
        return A[0]
    look_up = [None] * n
    look_up[0] = A[0]
    look_up[1] = max(A[0], A[1])
    for i in range(2, n):
        look_up[i] = max(look_up[i - 1], look_up[i - 2] + A[i])
        look_up[i] = max(look_up[i], A[i])
    return look_up[n - 1]

import pytest

def test_single_element_list_returns_that_element():
    A = [5]
    expected = 5
    assert max_sum_subseq(A) == expected

def test_two_elements_list_returns_the_maximum_element():
    A = [3, 7]
    expected = 7
    assert max_sum_subseq(A) == expected

def test_three_elements_with_non_adjacent_max_sum_subsequence():
    A = [3, 2, 5]
    expected = 8
    assert max_sum_subseq(A) == expected

def test_list_with_negative_and_positive_numbers():
    A = [-1, 4, -2, 5]
    expected = 7
    assert max_sum_subseq(A) == expected

def test_list_with_all_negative_numbers():
    A = [-3, -5, -2, -8]
    expected = -2
    assert max_sum_subseq(A) == expected

def test_list_with_zeros_and_positive_numbers():
    A = [0, 0, 5, 0, 10]
    expected = 15
    assert max_sum_subseq(A) == expected

def test_list_with_alternating_positive_and_negative_numbers():
    A = [4, -1, 3, -2, 5]
    expected = 12
    assert max_sum_subseq(A) == expected
def sort_matrix(M):
    result = sorted(M, key=sum)
    return result

import pytest

def test_sort_matrix_distinct_sums():
    M = [[3, 1, 2], [1, 1, 1], [4, 4, 4]]
    expected = [[1, 1, 1], [3, 1, 2], [4, 4, 4]]
    assert sort_matrix(M) == expected

def test_sort_matrix_equal_sums():
    M = [[2, 2], [1, 3], [4, 0]]
    expected = [[2, 2], [1, 3], [4, 0]]
    assert sort_matrix(M) == expected

def test_sort_matrix_negative_and_positive():
    M = [[-1, -2], [0, 0], [1, 2]]
    expected = [[-1, -2], [0, 0], [1, 2]]
    assert sort_matrix(M) == expected

def test_sort_matrix_empty():
    M = []
    expected = []
    assert sort_matrix(M) == expected

def test_sort_matrix_single_element_rows():
    M = [[5], [3], [10], [1]]
    expected = [[1], [3], [5], [10]]
    assert sort_matrix(M) == expected
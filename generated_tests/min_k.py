def min_k(test_list, K):
  res = sorted(test_list, key = lambda x: x[1])[:K]
  return (res)

import pytest

def test_select_two_smallest_second_values():
    test_list = [(1, 5), (2, 3), (3, 4), (4, 1)]
    K = 2
    expected_output = [(4, 1), (2, 3)]
    assert min_k(test_list, K) == expected_output

def test_select_all_elements_when_K_equals_list_length():
    test_list = [(10, 10), (20, 20), (30, 30)]
    K = 3
    expected_output = [(10, 10), (20, 20), (30, 30)]
    assert min_k(test_list, K) == expected_output

def test_select_fewer_elements_with_duplicate_second_values():
    test_list = [(1, 2), (2, 2), (3, 1), (4, 3)]
    K = 2
    expected_output = [(3, 1), (1, 2)]
    assert min_k(test_list, K) == expected_output

def test_select_zero_elements_when_K_is_zero():
    test_list = [(1, 100), (2, 50)]
    K = 0
    expected_output = []
    assert min_k(test_list, K) == expected_output

def test_select_all_elements_when_K_larger_than_list_length():
    test_list = [(5, 9), (6, 7)]
    K = 5
    expected_output = [(6, 7), (5, 9)]
    assert min_k(test_list, K) == expected_output
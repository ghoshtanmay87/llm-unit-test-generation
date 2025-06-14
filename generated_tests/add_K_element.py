def add_K_element(test_list, K):
  res = [tuple(j + K for j in sub ) for sub in test_list]
  return (res)

import pytest

def test_add_K_positive_integers():
    # Add K to each element in a list of tuples with positive integers
    test_list = [(1, 2), (3, 4)]
    K = 5
    expected_output = [(6, 7), (8, 9)]
    assert add_K_element(test_list, K) == expected_output

def test_add_zero_to_each_element():
    # Add zero to each element in a list of tuples
    test_list = [(10, 20), (30, 40)]
    K = 0
    expected_output = [(10, 20), (30, 40)]
    assert add_K_element(test_list, K) == expected_output

def test_add_negative_number_to_each_element():
    # Add a negative number to each element in a list of tuples
    test_list = [(5, 10), (15, 20)]
    K = -3
    expected_output = [(2, 7), (12, 17)]
    assert add_K_element(test_list, K) == expected_output

def test_add_K_to_empty_list():
    # Add K to each element in an empty list
    test_list = []
    K = 10
    expected_output = []
    assert add_K_element(test_list, K) == expected_output

def test_add_K_mixed_positive_negative_integers():
    # Add K to each element in a list of tuples with mixed positive and negative integers
    test_list = [(-1, 0), (2, -3)]
    K = 4
    expected_output = [(3, 4), (6, 1)]
    assert add_K_element(test_list, K) == expected_output
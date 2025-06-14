def check_k_elements(test_list, K):
  res = True
  for tup in test_list:
    for ele in tup:
      if ele != K:
        res = False
  return (res)

import pytest

def test_all_elements_equal_to_k():
    # All elements in all tuples equal to K
    test_list = [(3, 3), (3, 3, 3)]
    K = 3
    expected_output = True
    assert check_k_elements(test_list, K) == expected_output

def test_at_least_one_element_not_equal_to_k():
    # At least one element in the tuples not equal to K
    test_list = [(3, 2), (3, 3, 3)]
    K = 3
    expected_output = False
    assert check_k_elements(test_list, K) == expected_output

def test_empty_list_input():
    # Empty list input
    test_list = []
    K = 5
    expected_output = True
    assert check_k_elements(test_list, K) == expected_output

def test_tuples_all_elements_different_from_k():
    # Tuples contain elements all different from K
    test_list = [(1, 2), (4, 5)]
    K = 3
    expected_output = False
    assert check_k_elements(test_list, K) == expected_output

def test_single_tuple_one_element_equal_to_k():
    # Single tuple with one element equal to K
    test_list = [(7,)]
    K = 7
    expected_output = True
    assert check_k_elements(test_list, K) == expected_output

def test_single_tuple_one_element_not_equal_to_k():
    # Single tuple with one element not equal to K
    test_list = [(8,)]
    K = 7
    expected_output = False
    assert check_k_elements(test_list, K) == expected_output

def test_multiple_tuples_last_element_not_equal_to_k():
    # Multiple tuples with mixed elements, last element not equal to K
    test_list = [(5, 5), (5, 4)]
    K = 5
    expected_output = False
    assert check_k_elements(test_list, K) == expected_output

def test_multiple_tuples_all_elements_equal_to_k_zero():
    # Multiple tuples all elements equal to K, K is zero
    test_list = [(0, 0), (0, 0, 0)]
    K = 0
    expected_output = True
    assert check_k_elements(test_list, K) == expected_output
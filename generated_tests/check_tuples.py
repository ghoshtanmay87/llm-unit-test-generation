def check_tuples(test_tuple, K):
  res = all(ele in K for ele in test_tuple)
  return (res)

import pytest

def test_all_elements_present_in_K():
    test_tuple = (1, 2, 3)
    K = [1, 2, 3, 4]
    expected_output = True
    assert check_tuples(test_tuple, K) == expected_output

def test_some_elements_not_present_in_K():
    test_tuple = (1, 5)
    K = [1, 2, 3, 4]
    expected_output = False
    assert check_tuples(test_tuple, K) == expected_output

def test_empty_test_tuple():
    test_tuple = ()
    K = [1, 2, 3]
    expected_output = True
    assert check_tuples(test_tuple, K) == expected_output

def test_repeated_elements_all_in_K():
    test_tuple = (2, 2, 3)
    K = [1, 2, 3]
    expected_output = True
    assert check_tuples(test_tuple, K) == expected_output

def test_elements_not_in_K_and_K_empty():
    test_tuple = (1,)
    K = []
    expected_output = False
    assert check_tuples(test_tuple, K) == expected_output
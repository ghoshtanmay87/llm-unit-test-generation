def check_K(test_tup, K):
  res = False
  for ele in test_tup:
    if ele == K:
      res = True
      break
  return (res)

import pytest

def test_check_K_present_in_tuple():
    # Check when K is present in the tuple
    test_tup = (1, 2, 3, 4, 5)
    K = 3
    expected_output = True
    assert check_K(test_tup, K) == expected_output

def test_check_K_not_present_in_tuple():
    # Check when K is not present in the tuple
    test_tup = (10, 20, 30)
    K = 25
    expected_output = False
    assert check_K(test_tup, K) == expected_output

def test_check_K_empty_tuple():
    # Check when tuple is empty
    test_tup = ()
    K = 1
    expected_output = False
    assert check_K(test_tup, K) == expected_output

def test_check_K_first_element():
    # Check when K is the first element in the tuple
    test_tup = (7, 8, 9)
    K = 7
    expected_output = True
    assert check_K(test_tup, K) == expected_output

def test_check_K_last_element():
    # Check when K is the last element in the tuple
    test_tup = (4, 5, 6)
    K = 6
    expected_output = True
    assert check_K(test_tup, K) == expected_output

def test_check_K_multiple_occurrences():
    # Check when tuple contains multiple occurrences of K
    test_tup = (2, 3, 2, 4, 2)
    K = 2
    expected_output = True
    assert check_K(test_tup, K) == expected_output

def test_check_K_none_present():
    # Check when K is None and present in the tuple
    test_tup = (None, 1, 2)
    K = None
    expected_output = True
    assert check_K(test_tup, K) == expected_output

def test_check_K_none_not_present():
    # Check when K is None and not present in the tuple
    test_tup = (1, 2, 3)
    K = None
    expected_output = False
    assert check_K(test_tup, K) == expected_output
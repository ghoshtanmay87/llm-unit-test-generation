def check_element(test_tup, check_list):
  res = False
  for ele in check_list:
    if ele in test_tup:
      res = True
      break
  return (res)

import pytest

def test_check_element_with_element_in_test_tup():
    # Check when test_tup contains an element from check_list
    test_tup = (1, 2, 3)
    check_list = [3, 4, 5]
    expected_output = True
    assert check_element(test_tup, check_list) == expected_output

def test_check_element_with_no_element_in_test_tup():
    # Check when test_tup does not contain any element from check_list
    test_tup = (1, 2, 3)
    check_list = [4, 5, 6]
    expected_output = False
    assert check_element(test_tup, check_list) == expected_output

def test_check_element_with_empty_check_list():
    # Check when check_list is empty
    test_tup = (1, 2, 3)
    check_list = []
    expected_output = False
    assert check_element(test_tup, check_list) == expected_output

def test_check_element_with_empty_test_tup():
    # Check when test_tup is empty
    test_tup = ()
    check_list = [1, 2, 3]
    expected_output = False
    assert check_element(test_tup, check_list) == expected_output

def test_check_element_with_both_empty():
    # Check when both test_tup and check_list are empty
    test_tup = ()
    check_list = []
    expected_output = False
    assert check_element(test_tup, check_list) == expected_output
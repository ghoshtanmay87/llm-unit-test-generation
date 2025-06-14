def check_none(test_tup):
  res = any(map(lambda ele: ele is None, test_tup))
  return (res)

import pytest

def test_input_tuple_contains_none_as_first_element():
    test_tup = [None, 1, 2]
    expected_output = True
    assert check_none(test_tup) == expected_output

def test_input_tuple_contains_none_as_last_element():
    test_tup = [1, 2, None]
    expected_output = True
    assert check_none(test_tup) == expected_output

def test_input_tuple_contains_no_none_elements():
    test_tup = [1, 2, 3]
    expected_output = False
    assert check_none(test_tup) == expected_output

def test_input_tuple_is_empty():
    test_tup = []
    expected_output = False
    assert check_none(test_tup) == expected_output

def test_input_tuple_contains_multiple_none_elements():
    test_tup = [None, None, None]
    expected_output = True
    assert check_none(test_tup) == expected_output
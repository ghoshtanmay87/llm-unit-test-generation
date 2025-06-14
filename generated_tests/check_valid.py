def check_valid(test_tup):
  res = not any(map(lambda ele: not ele, test_tup))
  return (res)

import pytest

def test_all_elements_true():
    test_tup = (True, True, True)
    expected_output = True
    assert check_valid(test_tup) == expected_output

def test_one_element_false():
    test_tup = (True, False, True)
    expected_output = False
    assert check_valid(test_tup) == expected_output

def test_all_elements_false():
    test_tup = (False, False)
    expected_output = False
    assert check_valid(test_tup) == expected_output

def test_empty_tuple_input():
    test_tup = ()
    expected_output = True
    assert check_valid(test_tup) == expected_output

def test_mixed_truthy_and_falsy_values():
    test_tup = (1, 0, True)
    expected_output = False
    assert check_valid(test_tup) == expected_output
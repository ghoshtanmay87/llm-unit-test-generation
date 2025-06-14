def check_type(test_tuple):
  res = True
  for ele in test_tuple:
    if not isinstance(ele, type(test_tuple[0])):
      res = False
      break
  return (res)

import pytest

def test_all_elements_are_integers():
    test_tuple = (1, 2, 3)
    expected_output = True
    assert check_type(test_tuple) == expected_output

def test_mixed_types_int_and_str():
    test_tuple = (1, '2', 3)
    expected_output = False
    assert check_type(test_tuple) == expected_output

def test_all_elements_are_strings():
    test_tuple = ('a', 'b', 'c')
    expected_output = True
    assert check_type(test_tuple) == expected_output

def test_empty_tuple():
    test_tuple = ()
    expected_output = True
    assert check_type(test_tuple) == expected_output

def test_all_elements_are_floats():
    test_tuple = (1.0, 2.0, 3.0)
    expected_output = True
    assert check_type(test_tuple) == expected_output

def test_first_element_int_others_floats():
    test_tuple = (1, 2.0, 3.0)
    expected_output = False
    assert check_type(test_tuple) == expected_output

def test_all_elements_are_lists():
    test_tuple = ([1], [2], [3])
    expected_output = True
    assert check_type(test_tuple) == expected_output

def test_first_element_list_second_tuple():
    test_tuple = ([1], (2,), [3])
    expected_output = False
    assert check_type(test_tuple) == expected_output
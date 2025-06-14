def maximum_value(test_list):
  res = [(key, max(lst)) for key, lst in test_list]
  return (res)

import pytest

def test_maximum_value_multiple_keys_integer_lists():
    test_list = [('a', [1, 2, 3]), ('b', [4, 5, 6])]
    expected_output = [('a', 3), ('b', 6)]
    assert maximum_value(test_list) == expected_output

def test_maximum_value_negative_and_positive_integers():
    test_list = [('x', [-1, -2, 0]), ('y', [10, 5, 7])]
    expected_output = [('x', 0), ('y', 10)]
    assert maximum_value(test_list) == expected_output

def test_maximum_value_single_element_lists():
    test_list = [('single', [42])]
    expected_output = [('single', 42)]
    assert maximum_value(test_list) == expected_output

def test_maximum_value_floating_point_numbers():
    test_list = [('floats', [1.1, 2.2, 3.3]), ('mixed', [-1.5, 0.0, 1.5])]
    expected_output = [('floats', 3.3), ('mixed', 1.5)]
    assert maximum_value(test_list) == expected_output

def test_maximum_value_empty_input_list():
    test_list = []
    expected_output = []
    assert maximum_value(test_list) == expected_output
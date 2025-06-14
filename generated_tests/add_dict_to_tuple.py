def add_dict_to_tuple(test_tup, test_dict):
  test_tup = list(test_tup)
  test_tup.append(test_dict)
  test_tup = tuple(test_tup)
  return (test_tup)

import pytest

def test_append_non_empty_dict_to_non_empty_tuple():
    test_tup = (1, 2, 3)
    test_dict = {'a': 10, 'b': 20}
    expected_output = (1, 2, 3, {'a': 10, 'b': 20})
    assert add_dict_to_tuple(test_tup, test_dict) == expected_output

def test_append_empty_dict_to_non_empty_tuple():
    test_tup = (4, 5)
    test_dict = {}
    expected_output = (4, 5, {})
    assert add_dict_to_tuple(test_tup, test_dict) == expected_output

def test_append_dict_to_empty_tuple():
    test_tup = ()
    test_dict = {'key': 'value'}
    expected_output = ({'key': 'value'},)
    assert add_dict_to_tuple(test_tup, test_dict) == expected_output

def test_append_dict_with_multiple_pairs_to_mixed_tuple():
    test_tup = (True, None, 3.14)
    test_dict = {'x': 1, 'y': 2}
    expected_output = (True, None, 3.14, {'x': 1, 'y': 2})
    assert add_dict_to_tuple(test_tup, test_dict) == expected_output

def test_append_dict_with_nested_dict_to_tuple():
    test_tup = (0,)
    test_dict = {'nested': {'a': 1}}
    expected_output = (0, {'nested': {'a': 1}})
    assert add_dict_to_tuple(test_tup, test_dict) == expected_output
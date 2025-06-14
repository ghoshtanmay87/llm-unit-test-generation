def assign_elements(test_list):
  res = dict()
  for key, val in test_list:
    res.setdefault(val, [])
    res.setdefault(key, []).append(val)
  return (res)

import pytest

def test_assign_elements_distinct_keys_and_values():
    test_list = [('a', 1), ('b', 2), ('c', 3)]
    expected_output = {'a': [1], 'b': [2], 'c': [3], 1: [], 2: [], 3: []}
    assert assign_elements(test_list) == expected_output

def test_assign_elements_repeated_keys_and_values():
    test_list = [('a', 1), ('a', 2), ('b', 1)]
    expected_output = {'a': [1, 2], 'b': [1], 1: [], 2: []}
    assert assign_elements(test_list) == expected_output

def test_assign_elements_keys_and_values_overlap():
    test_list = [('x', 'y'), ('y', 'z'), ('z', 'x')]
    expected_output = {'x': ['y'], 'y': ['z'], 'z': ['x']}
    assert assign_elements(test_list) == expected_output

def test_assign_elements_empty_input_list():
    test_list = []
    expected_output = {}
    assert assign_elements(test_list) == expected_output

def test_assign_elements_keys_equal_values():
    test_list = [('a', 'a'), ('b', 'b')]
    expected_output = {'a': ['a'], 'b': ['b']}
    assert assign_elements(test_list) == expected_output
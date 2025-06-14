def drop_empty(dict1):
  dict1 = {key:value for (key, value) in dict1.items() if value is not None}
  return dict1

import pytest

def test_remove_keys_with_none_values():
    # Remove keys with None values from a dictionary with mixed None and non-None values
    input_dict = {'a': 1, 'b': None, 'c': 3}
    expected = {'a': 1, 'c': 3}
    assert drop_empty(input_dict) == expected

def test_all_values_none_results_in_empty_dict():
    # Input dictionary with all values as None
    input_dict = {'x': None, 'y': None}
    expected = {}
    assert drop_empty(input_dict) == expected

def test_no_none_values_dictionary_unchanged():
    # Input dictionary with no None values
    input_dict = {'name': 'Alice', 'age': 30}
    expected = {'name': 'Alice', 'age': 30}
    assert drop_empty(input_dict) == expected

def test_empty_string_and_zero_values_kept():
    # Input dictionary with some values as empty strings and zeros
    input_dict = {'key1': '', 'key2': 0, 'key3': None}
    expected = {'key1': '', 'key2': 0}
    assert drop_empty(input_dict) == expected

def test_empty_input_dictionary_returns_empty():
    # Empty input dictionary
    input_dict = {}
    expected = {}
    assert drop_empty(input_dict) == expected
def access_key(ditionary,key):
  return list(ditionary)[key]

import pytest

def test_access_first_key_in_multiple_keys_dict():
    ditionary = {'a': 1, 'b': 2, 'c': 3}
    key = 0
    expected_output = 'a'
    assert access_key(ditionary, key) == expected_output

def test_access_second_key_in_multiple_keys_dict():
    ditionary = {'a': 1, 'b': 2, 'c': 3}
    key = 1
    expected_output = 'b'
    assert access_key(ditionary, key) == expected_output

def test_access_last_key_in_multiple_keys_dict():
    ditionary = {'a': 1, 'b': 2, 'c': 3}
    key = 2
    expected_output = 'c'
    assert access_key(ditionary, key) == expected_output

def test_access_key_in_single_key_dict():
    ditionary = {'only_key': 42}
    key = 0
    expected_output = 'only_key'
    assert access_key(ditionary, key) == expected_output

def test_access_key_with_negative_index():
    ditionary = {'x': 10, 'y': 20, 'z': 30}
    key = -1
    expected_output = 'z'
    assert access_key(ditionary, key) == expected_output
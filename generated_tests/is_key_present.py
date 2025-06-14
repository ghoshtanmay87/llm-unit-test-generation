def is_key_present(d,x):
  if x in d:
    return True
  else:
     return False

import pytest

def test_key_present_in_dictionary():
    d = {'a': 1, 'b': 2}
    x = 'a'
    expected = True
    assert is_key_present(d, x) == expected

def test_key_not_present_in_dictionary():
    d = {'a': 1, 'b': 2}
    x = 'c'
    expected = False
    assert is_key_present(d, x) == expected

def test_empty_dictionary_with_any_key():
    d = {}
    x = 'anykey'
    expected = False
    assert is_key_present(d, x) == expected

def test_key_present_with_none_value():
    d = {'key': None}
    x = 'key'
    expected = True
    assert is_key_present(d, x) == expected

def test_key_present_with_integer_key():
    d = {1: 'one', 2: 'two'}
    x = 2
    expected = True
    assert is_key_present(d, x) == expected

def test_key_not_present_with_integer_key():
    d = {1: 'one', 2: 'two'}
    x = 3
    expected = False
    assert is_key_present(d, x) == expected
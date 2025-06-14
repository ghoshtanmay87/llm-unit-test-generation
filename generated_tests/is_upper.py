def is_upper(string):
  return (string.upper())

import pytest

def test_is_upper_all_lowercase():
    # Input string is all lowercase letters
    input_string = 'hello'
    expected = 'HELLO'
    assert is_upper(input_string) == expected

def test_is_upper_all_uppercase():
    # Input string is all uppercase letters
    input_string = 'WORLD'
    expected = 'WORLD'
    assert is_upper(input_string) == expected

def test_is_upper_mixed_case():
    # Input string is mixed case letters
    input_string = 'PyThOn'
    expected = 'PYTHON'
    assert is_upper(input_string) == expected

def test_is_upper_letters_and_numbers():
    # Input string contains numbers and letters
    input_string = 'abc123'
    expected = 'ABC123'
    assert is_upper(input_string) == expected

def test_is_upper_special_characters():
    # Input string contains special characters
    input_string = 'hello!@#'
    expected = 'HELLO!@#'
    assert is_upper(input_string) == expected

def test_is_upper_empty_string():
    # Input string is empty
    input_string = ''
    expected = ''
    assert is_upper(input_string) == expected
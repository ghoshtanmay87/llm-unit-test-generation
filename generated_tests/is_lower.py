def is_lower(string):
  return (string.lower())

import pytest

def test_is_lower_all_uppercase():
    # Input string is all uppercase letters
    input_string = "HELLO"
    expected = "hello"
    assert is_lower(input_string) == expected

def test_is_lower_mixed_case():
    # Input string is mixed case letters
    input_string = "HeLLo WoRLd"
    expected = "hello world"
    assert is_lower(input_string) == expected

def test_is_lower_already_lowercase():
    # Input string is already all lowercase
    input_string = "python"
    expected = "python"
    assert is_lower(input_string) == expected

def test_is_lower_numbers_and_symbols():
    # Input string contains numbers and symbols
    input_string = "123 ABC!@#"
    expected = "123 abc!@#"
    assert is_lower(input_string) == expected

def test_is_lower_empty_string():
    # Input string is empty
    input_string = ""
    expected = ""
    assert is_lower(input_string) == expected
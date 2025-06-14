import re
def remove_lowercase(str1):
  remove_lower = lambda text: re.sub('[a-z]', '', text)
  result =  remove_lower(str1)
  return (result)

import pytest

def test_remove_lowercase_from_mixed_case_string():
    # Remove all lowercase letters from a mixed case string
    input_str = "HelloWorld"
    expected = "HW"
    assert remove_lowercase(input_str) == expected

def test_remove_lowercase_from_all_lowercase_string():
    # Remove all lowercase letters from a string with only lowercase letters
    input_str = "python"
    expected = ""
    assert remove_lowercase(input_str) == expected

def test_remove_lowercase_from_all_uppercase_string():
    # Remove all lowercase letters from a string with only uppercase letters
    input_str = "PYTHON"
    expected = "PYTHON"
    assert remove_lowercase(input_str) == expected

def test_remove_lowercase_from_mixed_letters_and_digits():
    # Remove all lowercase letters from a string with mixed letters and digits
    input_str = "a1B2c3D4"
    expected = "1B234"
    assert remove_lowercase(input_str) == expected

def test_remove_lowercase_from_empty_string():
    # Remove all lowercase letters from an empty string
    input_str = ""
    expected = ""
    assert remove_lowercase(input_str) == expected
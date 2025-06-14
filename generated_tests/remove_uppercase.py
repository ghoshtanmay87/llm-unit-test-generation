import re
def remove_uppercase(str1):
  remove_upper = lambda text: re.sub('[A-Z]', '', text)
  result =  remove_upper(str1)
  return (result)

import pytest

def test_remove_uppercase_mixed_case_string():
    # Remove uppercase letters from a mixed case string
    input_str = 'HelloWorld'
    expected = 'elloorld'
    assert remove_uppercase(input_str) == expected

def test_remove_uppercase_all_uppercase_letters():
    # Remove uppercase letters from a string with only uppercase letters
    input_str = 'ABCXYZ'
    expected = ''
    assert remove_uppercase(input_str) == expected

def test_remove_uppercase_no_uppercase_letters():
    # Remove uppercase letters from a string with no uppercase letters
    input_str = 'python'
    expected = 'python'
    assert remove_uppercase(input_str) == expected

def test_remove_uppercase_empty_string():
    # Remove uppercase letters from an empty string
    input_str = ''
    expected = ''
    assert remove_uppercase(input_str) == expected

def test_remove_uppercase_uppercase_and_special_characters():
    # Remove uppercase letters from a string with uppercase letters and special characters
    input_str = '123ABC!@#defGHI'
    expected = '123!@#def'
    assert remove_uppercase(input_str) == expected
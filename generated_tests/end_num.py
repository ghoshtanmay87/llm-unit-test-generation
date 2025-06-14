import re
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False

import pytest

def test_string_ends_with_digit():
    # The string 'hello123' ends with the digit '3', so the regex pattern matches, returning True.
    assert end_num("hello123") is True

def test_string_ends_with_non_digit_character():
    # The string 'hello123a' ends with 'a', not a digit, so the regex pattern does not match, returning False.
    assert end_num("hello123a") is False

def test_string_is_single_digit():
    # The string '7' is a single digit, so the regex pattern matches, returning True.
    assert end_num("7") is True

def test_empty_string_input():
    # An empty string has no characters, so it cannot end with a digit, returning False.
    assert end_num("") is False

def test_string_ends_with_space_after_digits():
    # The string 'test123 ' ends with a space, not a digit, so the regex pattern does not match, returning False.
    assert end_num("test123 ") is False

def test_string_ends_with_zero_digit():
    # The string 'number0' ends with the digit '0', so the regex pattern matches, returning True.
    assert end_num("number0") is True
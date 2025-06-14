import re
def num_position(text):
 for m in re.finditer("\d+", text):
    return m.start()

import pytest

def test_num_position_single_number():
    # Find position of first number in a string with a single number
    result = num_position("abc123def")
    assert result == 3

def test_num_position_multiple_numbers():
    # Find position of first number in a string with multiple numbers
    result = num_position("abc12def34gh56")
    assert result == 3

def test_num_position_no_numbers():
    # String with no numbers returns None
    result = num_position("abcdef")
    assert result is None

def test_num_position_number_at_start():
    # Number at the start of the string
    result = num_position("123abc")
    assert result == 0

def test_num_position_number_at_end():
    # Number at the end of the string
    result = num_position("abcxyz789")
    assert result == 6

def test_num_position_single_digit_numbers():
    # String with a single digit number
    result = num_position("a1b2c3")
    assert result == 1

def test_num_position_empty_string():
    # Empty string input
    result = num_position("")
    assert result is None
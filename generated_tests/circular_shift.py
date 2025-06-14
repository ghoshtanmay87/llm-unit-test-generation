def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]

import pytest

def test_shift_less_than_length_of_string():
    # Shift 2 less than length 5, expect last 2 chars + first 3 chars
    result = circular_shift(12345, 2)
    assert result == "45123"

def test_shift_greater_than_length_of_string():
    # Shift 6 greater than length 5, expect reversed string
    result = circular_shift(12345, 6)
    assert result == "54321"

def test_shift_zero_no_shift():
    # Shift 0, expect original string
    result = circular_shift(9876, 0)
    assert result == "9876"

def test_single_character_string_with_shift_1():
    # Single char string with shift 1 equals length, expect reversed (same) string
    result = circular_shift(7, 1)
    assert result == "7"

def test_shift_exactly_one_less_than_length():
    # Shift 5 less than length 6, expect last 5 chars + first char
    result = circular_shift(123456, 5)
    assert result == "234561"

def test_shift_equal_to_length_of_string():
    # Shift 5 equals length 5, expect original string
    result = circular_shift(12345, 5)
    assert result == "12345"
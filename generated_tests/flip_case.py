def flip_case(string: str) -> str:
    return string.swapcase()

import pytest

def test_flip_case_mixed_case_string():
    # Flip case of a mixed case string
    input_string = "Hello World"
    expected = "hELLO wORLD"
    assert flip_case(input_string) == expected

def test_flip_case_all_uppercase_string():
    # Flip case of an all uppercase string
    input_string = "PYTHON"
    expected = "python"
    assert flip_case(input_string) == expected

def test_flip_case_all_lowercase_string():
    # Flip case of an all lowercase string
    input_string = "python"
    expected = "PYTHON"
    assert flip_case(input_string) == expected

def test_flip_case_string_with_numbers_and_symbols():
    # Flip case of a string with numbers and symbols
    input_string = "1234!@#AbC"
    expected = "1234!@#aBc"
    assert flip_case(input_string) == expected

def test_flip_case_empty_string():
    # Flip case of an empty string
    input_string = ""
    expected = ""
    assert flip_case(input_string) == expected

def test_flip_case_string_with_whitespace_only():
    # Flip case of a string with whitespace only
    input_string = "   \t\n"
    expected = "   \t\n"
    assert flip_case(input_string) == expected

def test_flip_case_string_with_mixed_unicode_characters():
    # Flip case of a string with mixed unicode characters
    input_string = "ÄÖÜäöü"
    expected = "äöüÄÖÜ"
    assert flip_case(input_string) == expected
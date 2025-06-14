def toggle_string(string):
 string1 = string.swapcase()
 return string1

import pytest

def test_toggle_case_mixed_case_string():
    # Toggle case of a mixed-case string
    input_string = "Hello World"
    expected_output = "hELLO wORLD"
    assert toggle_string(input_string) == expected_output

def test_toggle_case_all_uppercase_string():
    # Toggle case of an all uppercase string
    input_string = "PYTHON"
    expected_output = "python"
    assert toggle_string(input_string) == expected_output

def test_toggle_case_all_lowercase_string():
    # Toggle case of an all lowercase string
    input_string = "python"
    expected_output = "PYTHON"
    assert toggle_string(input_string) == expected_output

def test_toggle_case_string_with_numbers_and_symbols():
    # Toggle case of a string with numbers and symbols
    input_string = "1234!@#AbC"
    expected_output = "1234!@#aBc"
    assert toggle_string(input_string) == expected_output

def test_toggle_case_empty_string():
    # Toggle case of an empty string
    input_string = ""
    expected_output = ""
    assert toggle_string(input_string) == expected_output
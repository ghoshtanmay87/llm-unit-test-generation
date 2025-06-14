def strlen(string: str) -> int:
    return len(string)

import pytest

def test_strlen_simple_lowercase_string():
    # Calculate length of a simple lowercase string
    input_string = 'hello'
    expected = 5
    assert strlen(input_string) == expected

def test_strlen_empty_string():
    # Calculate length of an empty string
    input_string = ''
    expected = 0
    assert strlen(input_string) == expected

def test_strlen_string_with_spaces():
    # Calculate length of a string with spaces
    input_string = 'a b c'
    expected = 5
    assert strlen(input_string) == expected

def test_strlen_string_with_special_characters():
    # Calculate length of a string with special characters
    input_string = '!@#$%^&*()'
    expected = 10
    assert strlen(input_string) == expected

def test_strlen_string_with_unicode_characters():
    # Calculate length of a string with unicode characters
    input_string = '你好世界'
    expected = 4
    assert strlen(input_string) == expected

def test_strlen_string_with_newline_and_tab():
    # Calculate length of a string with newline and tab characters
    input_string = 'line1\nline2\tend'
    expected = 15
    assert strlen(input_string) == expected
import re
def is_allowed_specific_char(string):
    get_char = re.compile(r'[^a-zA-Z0-9.]')
    string = get_char.search(string)
    return not bool(string)

import pytest

def test_alphanumeric_and_dots_allowed():
    # Input string contains only alphanumeric characters and dots
    input_string = 'abc123.456'
    expected = True
    assert is_allowed_specific_char(input_string) == expected

def test_string_with_space_character():
    # Input string contains a space character
    input_string = 'hello world'
    expected = False
    assert is_allowed_specific_char(input_string) == expected

def test_string_with_special_character_at():
    # Input string contains a special character '@'
    input_string = 'user@domain.com'
    expected = False
    assert is_allowed_specific_char(input_string) == expected

def test_string_with_only_letters():
    # Input string contains only letters
    input_string = 'OpenAI'
    expected = True
    assert is_allowed_specific_char(input_string) == expected

def test_string_with_underscore_character():
    # Input string contains underscore character
    input_string = 'file_name.txt'
    expected = False
    assert is_allowed_specific_char(input_string) == expected

def test_empty_string():
    # Input string is empty
    input_string = ''
    expected = True
    assert is_allowed_specific_char(input_string) == expected

def test_string_with_only_dots():
    # Input string contains only dots
    input_string = '...'
    expected = True
    assert is_allowed_specific_char(input_string) == expected

def test_string_with_newline_character():
    # Input string contains newline character
    input_string = 'line1\nline2'
    expected = False
    assert is_allowed_specific_char(input_string) == expected
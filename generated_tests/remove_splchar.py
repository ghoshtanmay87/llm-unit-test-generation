import re
def remove_splchar(text): 
 pattern = re.compile('[\W_]+')
 return (pattern.sub('', text))

import pytest

def test_remove_special_characters_and_underscores_from_mixed_string():
    # Remove special characters and underscores from a string with letters, digits, and special characters
    input_text = 'Hello, World!_123'
    expected = 'HelloWorld123'
    assert remove_splchar(input_text) == expected

def test_remove_special_characters_from_only_special_chars_and_underscores():
    # Remove special characters from a string containing only special characters and underscores
    input_text = '!@#$%^&*()_+'
    expected = ''
    assert remove_splchar(input_text) == expected

def test_remove_special_characters_from_alphanumeric_only_string():
    # Remove special characters from a string with only alphanumeric characters
    input_text = 'abcDEF123'
    expected = 'abcDEF123'
    assert remove_splchar(input_text) == expected

def test_remove_special_characters_from_string_with_spaces_and_underscores():
    # Remove special characters from a string with spaces and underscores
    input_text = 'a_b c_d e_f'
    expected = 'abcdef'
    assert remove_splchar(input_text) == expected

def test_remove_special_characters_from_empty_string():
    # Remove special characters from an empty string
    input_text = ''
    expected = ''
    assert remove_splchar(input_text) == expected
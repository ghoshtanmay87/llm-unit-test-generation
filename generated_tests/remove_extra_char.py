import re
def remove_extra_char(text1):
  pattern = re.compile('[\W_]+')
  return (pattern.sub('', text1))

import pytest

def test_remove_non_alphanumeric_and_underscores_from_special_characters():
    # Remove all non-alphanumeric characters and underscores from a string with special characters
    input_text = 'Hello, World!'
    expected = 'HelloWorld'
    assert remove_extra_char(input_text) == expected

def test_remove_underscores_and_special_characters_from_underscores_and_punctuation():
    # Remove underscores and special characters from a string with underscores and punctuation
    input_text = 'Python_is_awesome!!!'
    expected = 'Pythonisawesome'
    assert remove_extra_char(input_text) == expected

def test_remove_spaces_and_special_characters_from_spaces_and_symbols():
    # Remove spaces and special characters from a string with spaces and symbols
    input_text = ' 123 @# $%^&*() 456 '
    expected = '123456'
    assert remove_extra_char(input_text) == expected

def test_remove_special_characters_from_mixed_alphanumeric_and_symbols():
    # Remove special characters from a string with mixed alphanumeric and symbols
    input_text = 'abc_def-123'
    expected = 'abcdef123'
    assert remove_extra_char(input_text) == expected

def test_input_string_with_only_special_characters_and_underscores():
    # Input string with only special characters and underscores
    input_text = '!@#$%^&*()_+'
    expected = ''
    assert remove_extra_char(input_text) == expected

def test_input_string_with_only_alphanumeric_characters():
    # Input string with only alphanumeric characters
    input_text = 'Test123'
    expected = 'Test123'
    assert remove_extra_char(input_text) == expected
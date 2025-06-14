import re
def remove_whitespaces(text1):
  return (re.sub(r'\s+', '',text1))

import pytest

def test_remove_whitespace_spaces_only():
    # Remove all whitespace characters from a string with spaces only
    input_text = 'Hello World'
    expected = 'HelloWorld'
    assert remove_whitespaces(input_text) == expected

def test_remove_whitespace_multiple_spaces_and_tabs():
    # Remove all whitespace characters from a string with multiple spaces and tabs
    input_text = '  Hello\tWorld  '
    expected = 'HelloWorld'
    assert remove_whitespaces(input_text) == expected

def test_remove_whitespace_newlines_and_spaces():
    # Remove all whitespace characters from a string with newlines and spaces
    input_text = 'Hello\nWorld\n'
    expected = 'HelloWorld'
    assert remove_whitespaces(input_text) == expected

def test_remove_whitespace_no_whitespace():
    # Remove all whitespace characters from a string with no whitespace
    input_text = 'HelloWorld'
    expected = 'HelloWorld'
    assert remove_whitespaces(input_text) == expected

def test_remove_whitespace_empty_string():
    # Remove all whitespace characters from an empty string
    input_text = ''
    expected = ''
    assert remove_whitespaces(input_text) == expected

def test_remove_whitespace_mixed_whitespace_characters():
    # Remove all whitespace characters from a string with mixed whitespace characters
    input_text = ' \tHello \n World \r\n'
    expected = 'HelloWorld'
    assert remove_whitespaces(input_text) == expected
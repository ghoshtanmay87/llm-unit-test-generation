import re
def remove_multiple_spaces(text1):
  return (re.sub(' +',' ',text1))

import pytest

def test_remove_multiple_spaces_with_multiple_consecutive_spaces():
    # Input string with multiple consecutive spaces between words
    input_text = 'This  is   a    test'
    expected = 'This is a test'
    assert remove_multiple_spaces(input_text) == expected

def test_remove_multiple_spaces_with_single_spaces_only():
    # Input string with no multiple spaces (only single spaces)
    input_text = 'No extra spaces here'
    expected = 'No extra spaces here'
    assert remove_multiple_spaces(input_text) == expected

def test_remove_multiple_spaces_with_leading_and_trailing_spaces():
    # Input string with leading and trailing multiple spaces
    input_text = '   Leading and trailing   '
    expected = ' Leading and trailing '
    assert remove_multiple_spaces(input_text) == expected

def test_remove_multiple_spaces_with_tabs_and_newlines():
    # Input string with tabs and newlines mixed with spaces
    input_text = 'Line1\t  Line2\n   Line3'
    expected = 'Line1\t Line2\n Line3'
    assert remove_multiple_spaces(input_text) == expected

def test_remove_multiple_spaces_with_only_spaces():
    # Input string with only spaces
    input_text = '     '
    expected = ' '
    assert remove_multiple_spaces(input_text) == expected

def test_remove_multiple_spaces_with_empty_string():
    # Empty string input
    input_text = ''
    expected = ''
    assert remove_multiple_spaces(input_text) == expected
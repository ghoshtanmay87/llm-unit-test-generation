import re
def remove_all_spaces(text):
 return (re.sub(r'\s+', '',text))

import pytest

def test_remove_all_spaces_multiple_spaces_between_words():
    # Remove all spaces from a string with multiple spaces between words
    input_text = 'Hello   World'
    expected = 'HelloWorld'
    assert remove_all_spaces(input_text) == expected

def test_remove_all_spaces_tabs_and_newlines():
    # Remove all spaces from a string with tabs and newlines
    input_text = 'Line1\n\tLine2'
    expected = 'Line1Line2'
    assert remove_all_spaces(input_text) == expected

def test_remove_all_spaces_no_spaces():
    # Remove all spaces from a string with no spaces
    input_text = 'NoSpacesHere'
    expected = 'NoSpacesHere'
    assert remove_all_spaces(input_text) == expected

def test_remove_all_spaces_leading_and_trailing_spaces():
    # Remove all spaces from a string with leading and trailing spaces
    input_text = '  Leading and trailing  '
    expected = 'Leadingandtrailing'
    assert remove_all_spaces(input_text) == expected

def test_remove_all_spaces_empty_string():
    # Remove all spaces from an empty string
    input_text = ''
    expected = ''
    assert remove_all_spaces(input_text) == expected
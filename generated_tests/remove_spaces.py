import re
def remove_spaces(text):
 return (re.sub(' +',' ',text))

import pytest

def test_remove_multiple_consecutive_spaces_in_simple_sentence():
    input_text = 'This  is   a    test'
    expected = 'This is a test'
    assert remove_spaces(input_text) == expected

def test_input_with_no_extra_spaces():
    input_text = 'NoExtraSpacesHere'
    expected = 'NoExtraSpacesHere'
    assert remove_spaces(input_text) == expected

def test_input_with_single_spaces_only():
    input_text = 'Single spaced sentence'
    expected = 'Single spaced sentence'
    assert remove_spaces(input_text) == expected

def test_input_with_leading_and_trailing_spaces():
    input_text = '  Leading and trailing  '
    expected = ' Leading and trailing '
    assert remove_spaces(input_text) == expected

def test_input_with_tabs_and_newlines_mixed_with_spaces():
    input_text = 'Line1\t  Line2\n   Line3'
    expected = 'Line1\t Line2\n Line3'
    assert remove_spaces(input_text) == expected
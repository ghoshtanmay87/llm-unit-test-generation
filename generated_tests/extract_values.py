import re
def extract_values(text):
 return (re.findall(r'"(.*?)"', text))

import pytest

def test_extract_simple_quoted_substrings():
    # Extract all substrings enclosed in double quotes from a simple sentence
    text = 'He said "hello" and then "goodbye".'
    expected = ['hello', 'goodbye']
    assert extract_values(text) == expected

def test_extract_no_quotes_returns_empty_list():
    # Extract quoted substrings when there are no quotes in the text
    text = 'No quotes here'
    expected = []
    assert extract_values(text) == expected

def test_extract_empty_and_nonempty_quotes():
    # Extract quoted substrings when quotes are empty
    text = 'Empty quotes "" and "non-empty"'
    expected = ['', 'non-empty']
    assert extract_values(text) == expected

def test_extract_multiple_quoted_parts_with_spaces_and_punctuation():
    # Extract quoted substrings with multiple quoted parts including spaces and punctuation
    text = 'She said "yes", then paused, and said "no".'
    expected = ['yes', 'no']
    assert extract_values(text) == expected

def test_extract_quoted_substrings_with_escaped_characters_not_handled():
    # Extract quoted substrings when quotes contain escaped characters (but regex does not handle escapes)
    text = 'He said "She said \\"hello\\"" and left.'
    expected = ['She said \\']
    assert extract_values(text) == expected

def test_extract_multiple_quoted_substrings_with_improper_nesting():
    # Extract quoted substrings when quotes are nested improperly
    text = '"First" and then "Second" and "Third"'
    expected = ['First', 'Second', 'Third']
    assert extract_values(text) == expected
import re
def check_literals(text, patterns):
  for pattern in patterns:
    if re.search(pattern,  text):
        return ('Matched!')
    else:
        return ('Not Matched!')

import pytest

def test_single_pattern_matches_text():
    text = 'hello world'
    patterns = ['world']
    expected = 'Matched!'
    assert check_literals(text, patterns) == expected

def test_single_pattern_does_not_match_text():
    text = 'hello world'
    patterns = ['python']
    expected = 'Not Matched!'
    assert check_literals(text, patterns) == expected

def test_multiple_patterns_first_matches():
    text = 'abc123'
    patterns = ['abc', '\\d+']
    expected = 'Matched!'
    assert check_literals(text, patterns) == expected

def test_multiple_patterns_first_does_not_match():
    text = 'abc123'
    patterns = ['xyz', '\\d+']
    expected = 'Not Matched!'
    assert check_literals(text, patterns) == expected

def test_empty_patterns_list():
    text = 'anything'
    patterns = []
    expected = None
    assert check_literals(text, patterns) is expected
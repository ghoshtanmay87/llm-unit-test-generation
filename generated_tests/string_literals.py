import re
def string_literals(patterns,text):
  for pattern in patterns:
     if re.search(pattern,  text):
       return ('Matched!')
     else:
       return ('Not Matched!')

import pytest

def test_single_pattern_matches_text():
    patterns = ['hello']
    text = 'hello world'
    expected = 'Matched!'
    assert string_literals(patterns, text) == expected

def test_single_pattern_does_not_match_text():
    patterns = ['bye']
    text = 'hello world'
    expected = 'Not Matched!'
    assert string_literals(patterns, text) == expected

def test_multiple_patterns_first_matches():
    patterns = ['world', 'hello']
    text = 'hello world'
    expected = 'Matched!'
    assert string_literals(patterns, text) == expected

def test_multiple_patterns_first_does_not_match_second_does():
    patterns = ['bye', 'hello']
    text = 'hello world'
    expected = 'Not Matched!'
    assert string_literals(patterns, text) == expected

def test_empty_patterns_list():
    patterns = []
    text = 'hello world'
    expected = None
    assert string_literals(patterns, text) is expected
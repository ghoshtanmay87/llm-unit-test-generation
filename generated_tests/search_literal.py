import re
def search_literal(pattern,text):
 match = re.search(pattern, text)
 s = match.start()
 e = match.end()
 return (s, e)

import pytest

def test_search_simple_substring_present():
    pattern = 'abc'
    text = 'xyzabc123'
    expected = (3, 6)
    assert search_literal(pattern, text) == expected

def test_search_pattern_at_beginning():
    pattern = 'hello'
    text = 'hello world'
    expected = (0, 5)
    assert search_literal(pattern, text) == expected

def test_search_pattern_at_end():
    pattern = 'world'
    text = 'hello world'
    expected = (6, 11)
    assert search_literal(pattern, text) == expected

def test_search_digit_pattern():
    pattern = r'\d+'
    text = 'abc123def'
    expected = (3, 6)
    assert search_literal(pattern, text) == expected

def test_search_pattern_with_special_characters():
    pattern = r'\.'
    text = 'file.txt'
    expected = (4, 5)
    assert search_literal(pattern, text) == expected
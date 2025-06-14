import re
def occurance_substring(text,pattern):
 for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    return (text[s:e], s, e)

import pytest

def test_find_first_occurrence_simple_substring():
    text = 'hello world'
    pattern = 'world'
    expected = ('world', 6, 11)
    assert occurance_substring(text, pattern) == expected

def test_find_first_occurrence_multiple_matches():
    text = 'ababab'
    pattern = 'ab'
    expected = ('ab', 0, 2)
    assert occurance_substring(text, pattern) == expected

def test_pattern_not_found_returns_none():
    text = 'abcdef'
    pattern = 'xyz'
    expected = None
    assert occurance_substring(text, pattern) == expected

def test_pattern_matches_at_start_of_text():
    text = 'start middle end'
    pattern = 'start'
    expected = ('start', 0, 5)
    assert occurance_substring(text, pattern) == expected

def test_pattern_matches_at_end_of_text():
    text = 'beginning to end'
    pattern = 'end'
    expected = ('end', 13, 16)
    assert occurance_substring(text, pattern) == expected

def test_pattern_is_regex_dot_matching_any_character():
    text = 'abc'
    pattern = '.'
    expected = ('a', 0, 1)
    assert occurance_substring(text, pattern) == expected

def test_pattern_is_regex_character_class_matching_digits():
    text = 'abc123def'
    pattern = '\\d+'
    expected = ('123', 3, 6)
    assert occurance_substring(text, pattern) == expected

def test_empty_pattern_matches_at_start_of_text():
    text = 'abc'
    pattern = ''
    expected = ('', 0, 0)
    assert occurance_substring(text, pattern) == expected
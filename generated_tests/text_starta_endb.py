import re
def text_starta_endb(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

import pytest

def test_text_starts_with_a_and_ends_with_b_with_characters_in_between():
    # Text: 'a123b' matches pattern 'a.*?b$'
    assert text_starta_endb('a123b') == 'Found a match!'

def test_text_starts_with_a_and_ends_with_b_with_no_characters_in_between():
    # Text: 'ab' matches pattern 'a.*?b$' with zero characters in between
    assert text_starta_endb('ab') == 'Found a match!'

def test_text_contains_a_and_ends_with_b_but_does_not_start_with_a():
    # Text: 'xa123b' does not start with 'a', so no match
    assert text_starta_endb('xa123b') == 'Not matched!'

def test_text_starts_with_a_but_does_not_end_with_b():
    # Text: 'a123c' ends with 'c', not 'b', so no match
    assert text_starta_endb('a123c') == 'Not matched!'

def test_text_is_exactly_b():
    # Text: 'b' does not start with 'a', so no match
    assert text_starta_endb('b') == 'Not matched!'

def test_text_is_exactly_a():
    # Text: 'a' does not end with 'b', so no match
    assert text_starta_endb('a') == 'Not matched!'

def test_text_starts_with_a_and_ends_with_b_with_multiple_bs_at_end():
    # Text: 'a123bb' ends with 'b', matches pattern
    assert text_starta_endb('a123bb') == 'Found a match!'

def test_text_contains_multiple_as_and_ends_with_b():
    # Text: 'aaab' starts with 'a' and ends with 'b', matches pattern
    assert text_starta_endb('aaab') == 'Found a match!'

def test_text_contains_a_and_b_but_b_is_not_at_the_end():
    # Text: 'a123b456' ends with '6', not 'b', so no match
    assert text_starta_endb('a123b456') == 'Not matched!'

def test_empty_string_input():
    # Empty string does not match pattern requiring start with 'a' and end with 'b'
    assert text_starta_endb('') == 'Not matched!'
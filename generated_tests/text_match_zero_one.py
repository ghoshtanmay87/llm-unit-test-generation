import re
def text_match_zero_one(text):
        patterns = 'ab?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

import pytest

def test_text_contains_a_followed_by_zero_bs():
    # The pattern 'ab?' matches 'a' followed by zero or one 'b'.
    # The input 'a' matches because 'b?' allows zero 'b's.
    result = text_match_zero_one(text='a')
    assert result == 'Found a match!'

def test_text_contains_ab_exactly():
    # The pattern 'ab?' matches 'a' followed by zero or one 'b'.
    # The input 'ab' matches because it has one 'b' after 'a'.
    result = text_match_zero_one(text='ab')
    assert result == 'Found a match!'

def test_text_contains_b_only_no_a():
    # The pattern requires an 'a' followed by zero or one 'b'.
    # 'b' alone does not match because it lacks the initial 'a'.
    result = text_match_zero_one(text='b')
    assert result == 'Not matched!'

def test_text_contains_ac_where_c_is_not_b():
    # The pattern 'ab?' matches 'a' followed by zero or one 'b'.
    # 'ac' contains 'a' followed by 'c', but the pattern only requires 'a' optionally followed by 'b'.
    # Since 'a' alone matches, the substring 'a' in 'ac' matches the pattern.
    result = text_match_zero_one(text='ac')
    assert result == 'Found a match!'

def test_text_contains_ba_where_a_is_after_b():
    # The pattern looks for 'a' followed by zero or one 'b'.
    # The substring 'a' in 'ba' matches the pattern because 'a' alone is a valid match.
    # The pattern does not require the match to start at the beginning.
    result = text_match_zero_one(text='ba')
    assert result == 'Found a match!'

def test_text_contains_no_a_or_b():
    # The pattern requires an 'a' followed by zero or one 'b'.
    # Since there is no 'a' in 'xyz', no match is found.
    result = text_match_zero_one(text='xyz')
    assert result == 'Not matched!'

def test_empty_string_input():
    # The pattern requires at least an 'a'.
    # An empty string has no characters, so no match is found.
    result = text_match_zero_one(text='')
    assert result == 'Not matched!'
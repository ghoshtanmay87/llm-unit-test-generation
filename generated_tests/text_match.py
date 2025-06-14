import re
def text_match(text):
        patterns = 'ab*?'
        if re.search(patterns,  text):
                return ('Found a match!')
        else:
                return ('Not matched!')

import pytest

def test_text_contains_a_followed_by_zero_bs():
    # The pattern 'ab*?' matches 'a' followed by zero or more 'b's (non-greedy).
    # 'a' alone matches because 'b*?' can match zero 'b's.
    input_text = 'a'
    expected = 'Found a match!'
    assert text_match(input_text) == expected

def test_text_contains_ab_sequence():
    # 'ab*?' matches 'a' followed by zero or more 'b's non-greedily.
    # 'ab' matches because 'b*?' matches one 'b'.
    input_text = 'ab'
    expected = 'Found a match!'
    assert text_match(input_text) == expected

def test_text_contains_abb_sequence():
    # 'ab*?' matches 'a' followed by zero or more 'b's non-greedily.
    # The pattern matches starting at 'a' and the first 'b' (non-greedy).
    input_text = 'abb'
    expected = 'Found a match!'
    assert text_match(input_text) == expected

def test_text_contains_no_a_character():
    # The pattern requires an 'a' followed by zero or more 'b's.
    # Since there is no 'a' in the text, no match is found.
    input_text = 'bbb'
    expected = 'Not matched!'
    assert text_match(input_text) == expected

def test_text_contains_ba_sequence():
    # The pattern 'ab*?' looks for 'a' followed by zero or more 'b's.
    # The substring 'a' in 'ba' matches the pattern (starting at second character).
    input_text = 'ba'
    expected = 'Found a match!'
    assert text_match(input_text) == expected

def test_empty_string_input():
    # Empty string contains no characters, so no 'a' to match the pattern.
    input_text = ''
    expected = 'Not matched!'
    assert text_match(input_text) == expected

def test_text_contains_multiple_matches():
    # The pattern matches the substring 'ab' starting at index 2 ('a' followed by 'b').
    # The function returns on first match.
    input_text = 'cababbb'
    expected = 'Found a match!'
    assert text_match(input_text) == expected

def test_text_contains_a_at_the_end():
    # The pattern matches 'a' at the end of the string,
    # since 'b*?' can match zero 'b's after 'a'.
    input_text = 'bbbba'
    expected = 'Found a match!'
    assert text_match(input_text) == expected
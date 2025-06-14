import re
def text_match_three(text):
        patterns = 'ab{3}?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

import pytest

def test_text_contains_abbb_matches_pattern():
    # Text contains 'abbb' which matches the pattern 'ab{3}?'
    input_text = 'xxabbbxx'
    expected = 'Found a match!'
    assert text_match_three(input_text) == expected

def test_text_contains_abb_does_not_match_pattern():
    # Text contains 'abb' which does not match the pattern 'ab{3}?'
    input_text = 'xxabbxx'
    expected = 'Not matched!'
    assert text_match_three(input_text) == expected

def test_text_contains_abbbb_contains_abbb_substring():
    # Text contains 'abbbb' which contains 'abbb' as a substring matching the pattern
    input_text = 'abbbb'
    expected = 'Found a match!'
    assert text_match_three(input_text) == expected

def test_text_contains_no_a_followed_by_bs():
    # Text contains no 'a' followed by 'b's
    input_text = 'xyz'
    expected = 'Not matched!'
    assert text_match_three(input_text) == expected

def test_text_contains_a_followed_by_4_bs_includes_3_bs_substring():
    # Text contains 'a' followed by 4 'b's, which includes 'a' followed by 3 'b's as a substring
    input_text = 'aabbbb'
    expected = 'Found a match!'
    assert text_match_three(input_text) == expected
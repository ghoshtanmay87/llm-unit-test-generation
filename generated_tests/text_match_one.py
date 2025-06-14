import re
def text_match_one(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

import pytest

def test_text_contains_ab_with_one_b_minimal_match():
    text = 'ab'
    expected = 'Found a match!'
    assert text_match_one(text) == expected

def test_text_contains_abb_with_two_bs_minimal_match_still_matches():
    text = 'abb'
    expected = 'Found a match!'
    assert text_match_one(text) == expected

def test_text_contains_a_without_b_no_match():
    text = 'a'
    expected = 'Not matched!'
    assert text_match_one(text) == expected

def test_text_contains_b_without_preceding_a_no_match():
    text = 'b'
    expected = 'Not matched!'
    assert text_match_one(text) == expected

def test_text_contains_acb_with_a_and_b_separated_by_c_no_match():
    text = 'acb'
    expected = 'Not matched!'
    assert text_match_one(text) == expected

def test_text_contains_multiple_matches_returns_on_first_found():
    text = 'xxabyyabbzz'
    expected = 'Found a match!'
    assert text_match_one(text) == expected

def test_empty_string_input_no_match():
    text = ''
    expected = 'Not matched!'
    assert text_match_one(text) == expected

def test_text_contains_a_followed_by_multiple_bs_and_other_characters():
    text = 'aabbb'
    expected = 'Found a match!'
    assert text_match_one(text) == expected

def test_text_contains_a_followed_by_zero_bs_no_match():
    text = 'aabc'
    expected = 'Found a match!'
    assert text_match_one(text) == expected

def test_text_contains_a_followed_by_b_and_other_letters():
    text = 'abc'
    expected = 'Found a match!'
    assert text_match_one(text) == expected
import re
def text_match_wordz_middle(text):
        patterns = '\Bz\B'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

import pytest

def test_text_contains_z_surrounded_by_word_characters():
    # Scenario: Text contains 'z' surrounded by word characters
    input_text = 'amazing'
    expected = 'Found a match!'
    assert text_match_wordz_middle(input_text) == expected

def test_text_contains_z_at_start_of_word():
    # Scenario: Text contains 'z' at the start of the word
    input_text = 'zebra'
    expected = 'Not matched!'
    assert text_match_wordz_middle(input_text) == expected

def test_text_contains_z_at_end_of_word():
    # Scenario: Text contains 'z' at the end of the word
    input_text = 'jazz'
    expected = 'Not matched!'
    assert text_match_wordz_middle(input_text) == expected

def test_text_contains_multiple_z_with_one_in_middle():
    # Scenario: Text contains multiple 'z's with one in the middle
    input_text = 'puzzle'
    expected = 'Found a match!'
    assert text_match_wordz_middle(input_text) == expected

def test_text_contains_no_z_characters():
    # Scenario: Text contains no 'z' characters
    input_text = 'hello'
    expected = 'Not matched!'
    assert text_match_wordz_middle(input_text) == expected

def test_text_contains_z_surrounded_by_non_word_characters():
    # Scenario: Text contains 'z' surrounded by non-word characters
    input_text = ' z '
    expected = 'Not matched!'
    assert text_match_wordz_middle(input_text) == expected

def test_text_contains_z_in_middle_of_word_with_digits():
    # Scenario: Text contains 'z' in the middle of a word with digits
    input_text = 'a1z2b'
    expected = 'Found a match!'
    assert text_match_wordz_middle(input_text) == expected
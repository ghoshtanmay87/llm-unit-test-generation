import re
def text_match_wordz(text):
        patterns = '\w*z.\w*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

import pytest

def test_text_contains_word_with_z_followed_by_any_character_amazing():
    # Scenario: Text contains a word with 'z' followed by any character
    input_text = 'amazing'
    expected = 'Found a match!'
    assert text_match_wordz(input_text) == expected

def test_text_contains_word_with_z_followed_by_space_crazy_day():
    # Scenario: Text contains a word with 'z' followed by a space character
    input_text = 'crazy day'
    expected = 'Found a match!'
    assert text_match_wordz(input_text) == expected

def test_text_contains_word_with_z_followed_by_punctuation_buzz():
    # Scenario: Text contains a word with 'z' followed by punctuation
    input_text = 'buzz!'
    expected = 'Found a match!'
    assert text_match_wordz(input_text) == expected

def test_text_contains_no_z_character_hello_world():
    # Scenario: Text contains no 'z' character
    input_text = 'hello world'
    expected = 'Not matched!'
    assert text_match_wordz(input_text) == expected

def test_text_contains_z_at_end_of_word_no_following_character_fizz():
    # Scenario: Text contains 'z' at the end of a word with no following character
    input_text = 'fizz'
    expected = 'Not matched!'
    assert text_match_wordz(input_text) == expected
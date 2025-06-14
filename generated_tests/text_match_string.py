import re
def text_match_string(text):
        patterns = '^\w+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return 'Not matched!'

import pytest

def test_input_starts_with_word_characters():
    # Input string starts with one or more word characters
    text = "Hello world"
    expected = "Found a match!"
    assert text_match_string(text) == expected

def test_input_starts_with_non_word_character():
    # Input string starts with a non-word character
    text = "  Hello world"
    expected = "Not matched!"
    assert text_match_string(text) == expected

def test_input_is_empty_string():
    # Input string is empty
    text = ""
    expected = "Not matched!"
    assert text_match_string(text) == expected

def test_input_starts_with_digit():
    # Input string starts with a digit
    text = "123abc"
    expected = "Found a match!"
    assert text_match_string(text) == expected

def test_input_starts_with_underscore():
    # Input string starts with an underscore
    text = "_underscore"
    expected = "Found a match!"
    assert text_match_string(text) == expected

def test_input_starts_with_punctuation():
    # Input string starts with a punctuation mark
    text = "!exclamation"
    expected = "Not matched!"
    assert text_match_string(text) == expected
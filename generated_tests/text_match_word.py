import re
def text_match_word(text):
        patterns = '\w+\S*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return 'Not matched!'

import pytest

def test_text_ends_with_word_no_trailing_whitespace():
    # Text ends with a word followed by no trailing whitespace
    text = 'Hello world'
    expected = 'Found a match!'
    assert text_match_word(text) == expected

def test_text_ends_with_word_followed_by_punctuation():
    # Text ends with a word followed by punctuation
    text = 'Hello world!'
    expected = 'Found a match!'
    assert text_match_word(text) == expected

def test_text_ends_with_whitespace_character():
    # Text ends with a whitespace character
    text = 'Hello world '
    expected = 'Not matched!'
    assert text_match_word(text) == expected

def test_text_is_single_word_no_trailing_whitespace():
    # Text is a single word with no trailing whitespace
    text = 'Python3'
    expected = 'Found a match!'
    assert text_match_word(text) == expected

def test_text_is_empty_string():
    # Text is empty string
    text = ''
    expected = 'Not matched!'
    assert text_match_word(text) == expected

def test_text_ends_with_number_and_punctuation():
    # Text ends with a number and punctuation
    text = 'Version 2.0!'
    expected = 'Found a match!'
    assert text_match_word(text) == expected

def test_text_ends_with_multiple_spaces():
    # Text ends with multiple spaces
    text = 'End with spaces   '
    expected = 'Not matched!'
    assert text_match_word(text) == expected

def test_text_ends_with_word_followed_by_tab():
    # Text ends with a word followed by a tab character
    text = 'Hello\tworld\t'
    expected = 'Not matched!'
    assert text_match_word(text) == expected

def test_text_ends_with_word_followed_by_newline():
    # Text ends with a word followed by a newline character
    text = 'Hello world\n'
    expected = 'Not matched!'
    assert text_match_word(text) == expected

def test_text_ends_with_word_followed_by_non_whitespace_symbol():
    # Text ends with a word followed by a non-whitespace symbol
    text = 'Check this out!'
    expected = 'Found a match!'
    assert text_match_word(text) == expected
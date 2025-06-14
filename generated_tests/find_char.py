import re
def find_char(text):
  return (re.findall(r"\w{3,5}", text))

import pytest

def test_no_special_characters_no_backspace():
    # Input string with no special characters or backspace characters
    text = 'hello world'
    expected = []
    assert find_char(text) == expected

def test_backspace_surrounding_3_letter_word():
    # Input string with backspace characters surrounding a 3-letter word
    text = '\x08cat\x08'
    expected = ['\x08cat\x08']
    assert find_char(text) == expected

def test_backspace_surrounding_6_letter_word():
    # Input string with backspace characters surrounding a 6-letter word
    text = '\x08python\x08'
    expected = []
    assert find_char(text) == expected

def test_multiple_matches_words_between_backspace():
    # Input string with multiple matches of words between backspace characters
    text = '\x08cat\x08 and \x08doggy\x08 and \x08fish\x08'
    expected = ['\x08cat\x08', '\x08doggy\x08', '\x08fish\x08']
    assert find_char(text) == expected

def test_backspace_words_too_short_or_too_long():
    # Input string with backspace characters but words too short or too long
    text = '\x08hi\x08 \x08toolongword\x08 \x08ok\x08'
    expected = []
    assert find_char(text) == expected
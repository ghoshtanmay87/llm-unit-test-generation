import re
def find_char_long(text):
  return (re.findall(r"\w{4,}", text))

import pytest

def test_words_longer_or_equal_4_chars_surrounded_by_backspace():
    text = '\x08word\x08 \x08longer\x08 \x08no\x08 \x081234\x08'
    expected_output = ['word', 'longer', '1234']
    assert find_char_long(text) == expected_output

def test_words_shorter_than_4_chars_surrounded_by_backspace():
    text = '\x08cat\x08 \x08dog\x08 \x08hi\x08'
    expected_output = []
    assert find_char_long(text) == expected_output

def test_no_backspace_characters_in_input():
    text = 'word longer no 1234'
    expected_output = []
    assert find_char_long(text) == expected_output

def test_backspace_surrounded_words_all_shorter_than_4_chars():
    text = '\x08abc\x08 \x08def\x08 \x08ghi\x08'
    expected_output = []
    assert find_char_long(text) == expected_output

def test_multiple_backspace_surrounded_words_varying_lengths():
    text = '\x08test\x08 \x08word\x08 \x08no\x08 \x08yes\x08 \x0812345\x08'
    expected_output = ['test', 'word', '12345']
    assert find_char_long(text) == expected_output
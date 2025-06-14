def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len

import pytest

def test_no_words_longer_than_n():
    # Scenario: No words longer than n in the string
    n = 5
    s = 'hello world test'
    expected = []
    assert long_words(n, s) == expected

def test_some_words_longer_than_n():
    # Scenario: Some words longer than n in the string
    n = 3
    s = 'this is a simple test'
    expected = ['this', 'simple', 'test']
    assert long_words(n, s) == expected

def test_all_words_longer_than_n():
    # Scenario: All words longer than n in the string
    n = 1
    s = 'go to the park'
    expected = ['go', 'to', 'the', 'park']
    assert long_words(n, s) == expected

def test_empty_string_input():
    # Scenario: Empty string input
    n = 2
    s = ''
    expected = []
    assert long_words(n, s) == expected

def test_string_with_multiple_spaces_between_words():
    # Scenario: String with multiple spaces between words
    n = 2
    s = 'a  bb   ccc    dddd'
    expected = ['ccc', 'dddd']
    assert long_words(n, s) == expected

def test_words_exactly_length_n_are_excluded():
    # Scenario: Words exactly length n are excluded
    n = 4
    s = 'four five six seven'
    expected = ['seven']
    assert long_words(n, s) == expected
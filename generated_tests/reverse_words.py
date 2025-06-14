def reverse_words(s):
        return ' '.join(reversed(s.split()))

import pytest

def test_reverse_words_simple_sentence():
    s = 'hello world'
    expected = 'world hello'
    assert reverse_words(s) == expected

def test_reverse_words_multiple_words():
    s = 'the quick brown fox'
    expected = 'fox brown quick the'
    assert reverse_words(s) == expected

def test_reverse_words_single_word():
    s = 'python'
    expected = 'python'
    assert reverse_words(s) == expected

def test_reverse_words_empty_string():
    s = ''
    expected = ''
    assert reverse_words(s) == expected

def test_reverse_words_multiple_spaces():
    s = '  hello   world  '
    expected = 'world hello'
    assert reverse_words(s) == expected

def test_reverse_words_with_punctuation():
    s = 'hello, world!'
    expected = 'world! hello,'
    assert reverse_words(s) == expected
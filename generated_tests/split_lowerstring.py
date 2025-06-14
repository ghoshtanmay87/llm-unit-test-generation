import re
def split_lowerstring(text):
 return (re.findall('[a-z][^a-z]*', text))

import pytest

def test_split_mixed_lowercase_uppercase_with_punctuation():
    text = 'aBcDeF!gH'
    expected = ['aB', 'cD', 'eF!', 'gH']
    assert split_lowerstring(text) == expected

def test_split_only_lowercase_letters():
    text = 'abcdef'
    expected = ['a', 'b', 'c', 'd', 'e', 'f']
    assert split_lowerstring(text) == expected

def test_split_lowercase_followed_by_digits_and_symbols():
    text = 'a1b2c3!'
    expected = ['a1', 'b2', 'c3!']
    assert split_lowerstring(text) == expected

def test_split_no_lowercase_letters():
    text = 'ABC123!'
    expected = []
    assert split_lowerstring(text) == expected

def test_split_lowercase_letters_at_end():
    text = '123!abc'
    expected = ['a', 'b', 'c']
    assert split_lowerstring(text) == expected

def test_split_consecutive_lowercase_followed_by_uppercase():
    text = 'abCDefGH'
    expected = ['a', 'bCD', 'e', 'fGH']
    assert split_lowerstring(text) == expected

def test_split_lowercase_followed_by_spaces():
    text = 'a b c'
    expected = ['a ', 'b ', 'c']
    assert split_lowerstring(text) == expected
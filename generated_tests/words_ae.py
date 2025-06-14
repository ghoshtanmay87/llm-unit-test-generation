import re
def words_ae(text):
 list = re.findall("[ae]\w+", text)
 return list

import pytest

def test_words_starting_with_a_and_e():
    # Input text contains words starting with 'a' and 'e'
    text = 'apple eagle ant elephant bear'
    expected = ['apple', 'eagle', 'ant', 'elephant']
    assert words_ae(text) == expected

def test_words_starting_with_a_and_e_with_punctuation():
    # Input text contains words starting with 'a' and 'e' with punctuation
    text = 'An eagle, an ant, and an elephant.'
    expected = ['agle', 'ant', 'and', 'an', 'elephant']
    assert words_ae(text) == expected

def test_no_words_starting_with_a_or_e():
    # Input text with no words starting with 'a' or 'e'
    text = 'dog cat bird fish'
    expected = []
    assert words_ae(text) == expected

def test_words_starting_with_uppercase_A_or_E():
    # Input text with words starting with uppercase 'A' or 'E'
    text = 'Apple Elephant Antelope Eagle'
    expected = []
    assert words_ae(text) == expected

def test_mixed_case_words_starting_with_lowercase_a_or_e():
    # Input text with mixed case and words starting with lowercase 'a' or 'e'
    text = 'apple Apple eagle Eagle ant Ant'
    expected = ['apple', 'eagle', 'ant']
    assert words_ae(text) == expected

def test_words_starting_with_a_or_e_embedded_in_other_words():
    # Input text with words starting with 'a' or 'e' embedded in other words
    text = "The area is an example of an eagle's nest."
    expected = ['area', 'an', 'example', 'an', 'eagle']
    assert words_ae(text) == expected
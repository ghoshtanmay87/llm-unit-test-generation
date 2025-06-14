from collections import Counter
import re
def n_common_words(text,n):
  words = re.findall('\w+',text)
  n_common_words= Counter(words).most_common(n)
  return list(n_common_words)

import pytest

def test_two_most_common_words_simple_sentence():
    text = 'apple banana apple orange banana apple'
    n = 2
    expected = [('apple', 3), ('banana', 2)]
    assert n_common_words(text, n) == expected

def test_one_most_common_word_empty_string():
    text = ''
    n = 1
    expected = []
    assert n_common_words(text, n) == expected

def test_five_most_common_words_fewer_unique():
    text = 'one two two three three three'
    n = 5
    expected = [('three', 3), ('two', 2), ('one', 1)]
    assert n_common_words(text, n) == expected

def test_three_most_common_words_with_numbers_and_underscores():
    text = 'test_1 test_2 test_1 test_3 test_2 test_2'
    n = 3
    expected = [('test_2', 3), ('test_1', 2), ('test_3', 1)]
    assert n_common_words(text, n) == expected

def test_three_most_common_words_with_punctuation_and_mixed_case():
    text = 'Hello, hello! HELLO? world. World world.'
    n = 3
    expected = [('world', 2), ('Hello', 1), ('hello', 1)]
    assert n_common_words(text, n) == expected
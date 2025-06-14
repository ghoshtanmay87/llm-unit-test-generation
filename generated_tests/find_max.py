def find_max(words):
    return sorted(words, key=lambda x: (-len(set(x)), x))[0]

import pytest

def test_max_unique_chars_tie_lex_order_abc_bca_cab():
    words = ['abc', 'bca', 'cab']
    expected = 'abc'
    assert find_max(words) == expected

def test_max_unique_chars_varying_lengths_a_ab_abc_abcd():
    words = ['a', 'ab', 'abc', 'abcd']
    expected = 'abcd'
    assert find_max(words) == expected

def test_max_unique_chars_tie_lex_order_dog_god_odg():
    words = ['dog', 'god', 'odg']
    expected = 'dog'
    assert find_max(words) == expected

def test_max_unique_chars_with_empty_string_a_aa():
    words = ['', 'a', 'aa']
    expected = 'a'
    assert find_max(words) == expected

def test_max_unique_chars_distinct_words_apple_banana_cherry():
    words = ['apple', 'banana', 'cherry']
    expected = 'cherry'
    assert find_max(words) == expected
def anti_shuffle(s):
    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])

import pytest

def test_single_word_input_with_letters_in_random_order():
    s = 'dcba'
    expected = 'abcd'
    assert anti_shuffle(s) == expected

def test_multiple_words_input_with_letters_shuffled():
    s = 'cba fed'
    expected = 'abc def'
    assert anti_shuffle(s) == expected

def test_input_with_single_letter_words():
    s = 'z y x'
    expected = 'z y x'
    assert anti_shuffle(s) == expected

def test_empty_string_input():
    s = ''
    expected = ''
    assert anti_shuffle(s) == expected

def test_input_with_repeated_letters_in_words():
    s = 'bbaa cccdd'
    expected = 'aabb cccdd'
    assert anti_shuffle(s) == expected

def test_input_with_punctuation_treated_as_letters():
    s = 'd!cba e@fd'
    expected = '!abcd @def'
    assert anti_shuffle(s) == expected

def test_input_with_multiple_spaces_between_words():
    s = 'bca   edf'
    expected = 'abc   def'
    assert anti_shuffle(s) == expected
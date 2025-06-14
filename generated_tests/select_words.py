def select_words(s, n):
    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            if word[i].lower() not in ['a', 'e', 'i', 'o', 'u']:
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result

import pytest

def test_select_words_with_zero_consonants_only_vowels():
    s = 'aeiou a e i o u'
    n = 0
    expected = ['aeiou', 'a', 'e', 'i', 'o', 'u']
    assert select_words(s, n) == expected

def test_select_words_with_one_consonant_mixed_words():
    s = 'an ox is up'
    n = 1
    expected = ['an', 'ox', 'is', 'up']
    assert select_words(s, n) == expected

def test_select_words_with_three_consonants_punctuation_mixed_case():
    s = 'Hello, world! This is Python.'
    n = 3
    expected = ['This']
    assert select_words(s, n) == expected

def test_select_words_with_five_consonants_punctuation_mixed_case():
    s = 'Hello, world! This is Python.'
    n = 5
    expected = ['world!']
    assert select_words(s, n) == expected

def test_select_words_with_six_consonants_punctuation_mixed_case():
    s = 'Hello, world! This is Python.'
    n = 6
    expected = ['Python.']
    assert select_words(s, n) == expected

def test_select_words_with_one_consonant_repeated_words():
    s = 'to too two'
    n = 1
    expected = ['to', 'too']
    assert select_words(s, n) == expected

def test_select_words_with_three_consonants_simple_sentence():
    s = 'cat dog bird fish'
    n = 3
    expected = ['bird', 'fish']
    assert select_words(s, n) == expected

def test_select_words_with_two_consonants_punctuation_mixed_case():
    s = 'Hello, world! This is Python.'
    n = 2
    expected = []
    assert select_words(s, n) == expected

def test_select_words_with_four_consonants_punctuation_mixed_case():
    s = 'Hello, world! This is Python.'
    n = 4
    expected = ['Hello,']
    assert select_words(s, n) == expected

def test_select_words_with_two_consonants_repeated_words():
    s = 'to too two'
    n = 2
    expected = ['two']
    assert select_words(s, n) == expected
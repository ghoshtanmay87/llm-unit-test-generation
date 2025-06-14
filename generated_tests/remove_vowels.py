def remove_vowels(text):
    return ''.join([s for s in text if s.lower() not in ['a', 'e', 'i', 'o', 'u']])

import pytest

def test_remove_vowels_simple_lowercase_word():
    # Remove vowels from a simple lowercase word
    input_text = 'hello'
    expected = 'hll'
    assert remove_vowels(input_text) == expected

def test_remove_vowels_mixed_case_word():
    # Remove vowels from a mixed case word
    input_text = 'Apple'
    expected = 'ppl'
    assert remove_vowels(input_text) == expected

def test_remove_vowels_string_with_no_vowels():
    # Remove vowels from a string with no vowels
    input_text = 'rhythm'
    expected = 'rhythm'
    assert remove_vowels(input_text) == expected

def test_remove_vowels_empty_string():
    # Remove vowels from an empty string
    input_text = ''
    expected = ''
    assert remove_vowels(input_text) == expected

def test_remove_vowels_all_vowels_string():
    # Remove vowels from a string with all vowels
    input_text = 'aeiouAEIOU'
    expected = ''
    assert remove_vowels(input_text) == expected

def test_remove_vowels_sentence_with_spaces_and_punctuation():
    # Remove vowels from a sentence with spaces and punctuation
    input_text = 'This is a test.'
    expected = 'Ths s  tst.'
    assert remove_vowels(input_text) == expected

def test_remove_vowels_string_with_numbers_and_special_characters():
    # Remove vowels from a string with numbers and special characters
    input_text = 'Th3 qu1ck br0wn f0x!'
    expected = 'Th3 q1ck br0wn f0x!'
    assert remove_vowels(input_text) == expected
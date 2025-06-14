def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

import pytest

def test_char_frequency_simple_string_repeated_chars():
    # Calculate frequency of characters in a simple string with repeated characters
    input_str = 'hello'
    expected = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert char_frequency(input_str) == expected

def test_char_frequency_empty_string():
    # Calculate frequency of characters in an empty string
    input_str = ''
    expected = {}
    assert char_frequency(input_str) == expected

def test_char_frequency_all_unique_chars():
    # Calculate frequency of characters in a string with all unique characters
    input_str = 'abc'
    expected = {'a': 1, 'b': 1, 'c': 1}
    assert char_frequency(input_str) == expected

def test_char_frequency_multiple_repeated_chars():
    # Calculate frequency of characters in a string with multiple repeated characters
    input_str = 'banana'
    expected = {'b': 1, 'a': 3, 'n': 2}
    assert char_frequency(input_str) == expected

def test_char_frequency_spaces_and_punctuation():
    # Calculate frequency of characters in a string with spaces and punctuation
    input_str = 'hi! hi!'
    expected = {'h': 2, 'i': 2, '!': 2, ' ': 1}
    assert char_frequency(input_str) == expected
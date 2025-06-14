def reverse_vowels(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string

import pytest

def test_reverse_vowels_simple_lowercase_word():
    # Scenario: Reverse vowels in a simple lowercase word with vowels
    input_str = "hello"
    expected = "holle"
    assert reverse_vowels(input_str) == expected

def test_reverse_vowels_word_with_uppercase_vowels():
    # Scenario: Reverse vowels in a word with uppercase vowels
    input_str = "hEllO"
    expected = "hOllE"
    assert reverse_vowels(input_str) == expected

def test_reverse_vowels_string_with_no_vowels():
    # Scenario: String with no vowels remains unchanged
    input_str = "rhythm"
    expected = "rhythm"
    assert reverse_vowels(input_str) == expected

def test_reverse_vowels_string_with_all_vowels():
    # Scenario: String with all vowels reversed
    input_str = "aeiou"
    expected = "uoiea"
    assert reverse_vowels(input_str) == expected

def test_reverse_vowels_string_with_mixed_vowels_and_consonants():
    # Scenario: String with mixed vowels and consonants
    input_str = "leetcode"
    expected = "leotcede"
    assert reverse_vowels(input_str) == expected

def test_reverse_vowels_empty_string():
    # Scenario: Empty string returns empty string
    input_str = ""
    expected = ""
    assert reverse_vowels(input_str) == expected

def test_reverse_vowels_string_with_consecutive_vowels():
    # Scenario: String with consecutive vowels
    input_str = "queue"
    expected = "ueueq"
    assert reverse_vowels(input_str) == expected
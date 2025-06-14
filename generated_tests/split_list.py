import re
def split_list(text):
  return (re.findall('[A-Z][^A-Z]*', text))

import pytest

def test_split_camel_case_multiple_words():
    # Split a camel case string with multiple words
    input_text = "HelloWorldExample"
    expected = ['Hello', 'World', 'Example']
    assert split_list(input_text) == expected

def test_split_single_uppercase_letter_words():
    # Split a string with single uppercase letter words
    input_text = "AQuickBrownFox"
    expected = ['A', 'Quick', 'Brown', 'Fox']
    assert split_list(input_text) == expected

def test_split_consecutive_uppercase_letters():
    # Split a string with consecutive uppercase letters
    input_text = "NASAResearchLab"
    expected = ['N', 'A', 'S', 'A', 'Research', 'Lab']
    assert split_list(input_text) == expected

def test_split_string_starting_with_lowercase():
    # Split a string starting with lowercase letter (no match)
    input_text = "helloWorld"
    expected = ['World']
    assert split_list(input_text) == expected

def test_split_string_only_uppercase_letters():
    # Split a string with only uppercase letters
    input_text = "USA"
    expected = ['U', 'S', 'A']
    assert split_list(input_text) == expected

def test_split_empty_string():
    # Split an empty string
    input_text = ""
    expected = []
    assert split_list(input_text) == expected

def test_split_mixed_uppercase_lowercase_numbers():
    # Split a string with mixed uppercase and lowercase letters and numbers
    input_text = "Test123CaseABC"
    expected = ['Test', 'Case', 'A', 'B', 'C']
    assert split_list(input_text) == expected
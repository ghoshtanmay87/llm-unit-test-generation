import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r" ", str1)

import pytest

def test_camel_case_word_substitution():
    # Input with camelCase word to check substitution
    input_str = 'camelCase'
    expected = 'camel\x01 \x02ase'
    assert capital_words_spaces(input_str) == expected

def test_multiple_camel_case_transitions():
    # Input with multiple camelCase transitions
    input_str = 'thisIsATest'
    expected = 'this\x01 \x02s\x01 \x02\x01 \x02est'
    assert capital_words_spaces(input_str) == expected

def test_no_uppercase_following_lowercase():
    # Input with no uppercase letter following a word character
    input_str = 'lowercase'
    expected = 'lowercase'
    assert capital_words_spaces(input_str) == expected

def test_uppercase_letters_no_lowercase_before():
    # Input with uppercase letters but no lowercase before them
    input_str = 'NASA'
    expected = 'NASA'
    assert capital_words_spaces(input_str) == expected

def test_single_uppercase_letter_at_start():
    # Input with single uppercase letter at start
    input_str = 'Apple'
    expected = 'Apple'
    assert capital_words_spaces(input_str) == expected

def test_mixed_case_and_spaces():
    # Input with mixed case and spaces
    input_str = 'HelloWorld TestCase'
    expected = 'Hello\x01 \x02orld Test\x01 \x02ase'
    assert capital_words_spaces(input_str) == expected
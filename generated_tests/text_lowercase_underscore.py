import re
def text_lowercase_underscore(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

import pytest

def test_lowercase_letters_single_underscore_match():
    # Input string matches pattern with lowercase letters separated by a single underscore
    input_text = 'hello_world'
    expected = 'Found a match!'
    assert text_lowercase_underscore(input_text) == expected

def test_uppercase_letters_no_match():
    # Input string with uppercase letters does not match
    input_text = 'Hello_World'
    expected = 'Not matched!'
    assert text_lowercase_underscore(input_text) == expected

def test_multiple_underscores_no_match():
    # Input string with multiple underscores does not match
    input_text = 'hello_world_test'
    expected = 'Not matched!'
    assert text_lowercase_underscore(input_text) == expected

def test_digits_in_string_no_match():
    # Input string with digits does not match
    input_text = 'hello_world1'
    expected = 'Not matched!'
    assert text_lowercase_underscore(input_text) == expected

def test_no_underscore_no_match():
    # Input string without underscore does not match
    input_text = 'helloworld'
    expected = 'Not matched!'
    assert text_lowercase_underscore(input_text) == expected

def test_underscore_at_start_no_match():
    # Input string with underscore at start does not match
    input_text = '_helloworld'
    expected = 'Not matched!'
    assert text_lowercase_underscore(input_text) == expected

def test_underscore_at_end_no_match():
    # Input string with underscore at end does not match
    input_text = 'helloworld_'
    expected = 'Not matched!'
    assert text_lowercase_underscore(input_text) == expected

def test_special_characters_no_match():
    # Input string with special characters does not match
    input_text = 'hello_world!'
    expected = 'Not matched!'
    assert text_lowercase_underscore(input_text) == expected

def test_single_lowercase_word_no_match():
    # Input string with single lowercase word does not match
    input_text = 'hello'
    expected = 'Not matched!'
    assert text_lowercase_underscore(input_text) == expected

def test_multiple_underscores_trailing_underscore_no_match():
    # Input string with multiple underscores but only two groups separated by first underscore does not match
    input_text = 'hello_world_'
    expected = 'Not matched!'
    assert text_lowercase_underscore(input_text) == expected
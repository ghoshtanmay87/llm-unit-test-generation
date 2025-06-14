import re
def snake_to_camel(word):
  return ''.join(x.capitalize() or '_' for x in word.split('_'))

import pytest

def test_convert_simple_snake_case_to_camelcase():
    # Convert a simple snake_case word to CamelCase
    input_word = 'hello_world'
    expected = 'HelloWorld'
    assert snake_to_camel(input_word) == expected

def test_convert_single_word_no_underscores():
    # Convert a single word with no underscores
    input_word = 'python'
    expected = 'Python'
    assert snake_to_camel(input_word) == expected

def test_convert_snake_case_multiple_underscores():
    # Convert a snake_case word with multiple underscores
    input_word = 'this_is_a_test'
    expected = 'ThisIsATest'
    assert snake_to_camel(input_word) == expected

def test_convert_snake_case_consecutive_underscores():
    # Convert a snake_case word with consecutive underscores
    input_word = 'hello__world'
    expected = 'Hello_World'
    assert snake_to_camel(input_word) == expected

def test_convert_snake_case_leading_and_trailing_underscores():
    # Convert a snake_case word starting and ending with underscores
    input_word = '_leading_and_trailing_'
    expected = '_LeadingAndTrailing_'
    assert snake_to_camel(input_word) == expected

def test_convert_empty_string():
    # Convert an empty string
    input_word = ''
    expected = '_'
    assert snake_to_camel(input_word) == expected

def test_convert_snake_case_only_underscores():
    # Convert a snake_case word with only underscores
    input_word = '___'
    expected = '____'
    assert snake_to_camel(input_word) == expected
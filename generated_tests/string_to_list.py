def string_to_list(string): 
    lst = list(string.split(" ")) 
    return lst

import pytest

def test_simple_space_separated_string():
    # Convert a simple space-separated string into a list of words
    input_string = 'hello world'
    expected = ['hello', 'world']
    assert string_to_list(input_string) == expected

def test_string_with_multiple_spaces_between_words():
    # Convert a string with multiple spaces between words
    input_string = 'hello   world'
    expected = ['hello', '', '', 'world']
    assert string_to_list(input_string) == expected

def test_string_with_leading_and_trailing_spaces():
    # Convert a string with leading and trailing spaces
    input_string = '  hello world  '
    expected = ['', '', 'hello', 'world', '', '']
    assert string_to_list(input_string) == expected

def test_single_word_string():
    # Convert a single word string
    input_string = 'hello'
    expected = ['hello']
    assert string_to_list(input_string) == expected

def test_empty_string():
    # Convert an empty string
    input_string = ''
    expected = ['']
    assert string_to_list(input_string) == expected

def test_multiple_words_separated_by_single_spaces():
    # Convert a string with multiple words separated by single spaces
    input_string = 'one two three four'
    expected = ['one', 'two', 'three', 'four']
    assert string_to_list(input_string) == expected
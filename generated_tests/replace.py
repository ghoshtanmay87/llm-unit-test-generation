import re 
def replace(string, char): 
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string) 
    return string

import pytest

def test_replace_multiple_consecutive_occurrences_start():
    # Replace multiple consecutive occurrences of a character with a single occurrence
    input_string = 'aaabbbaaa'
    input_char = 'a'
    expected = 'abbaaa'
    assert replace(input_string, input_char) == expected

def test_replace_multiple_consecutive_occurrences_middle():
    # Replace multiple consecutive occurrences of a character in the middle of the string
    input_string = 'hellooooo world'
    input_char = 'o'
    expected = 'helo world'
    assert replace(input_string, input_char) == expected

def test_no_replacement_single_occurrence():
    # No replacement when character does not appear consecutively
    input_string = 'abcde'
    input_char = 'b'
    expected = 'abcde'
    assert replace(input_string, input_char) == expected

def test_replace_multiple_consecutive_spaces():
    # Replace multiple consecutive spaces with a single space
    input_string = 'This  is   a    test'
    input_char = ' '
    expected = 'This is a test'
    assert replace(input_string, input_char) == expected

def test_replace_multiple_consecutive_special_characters():
    # Replace multiple consecutive special characters
    input_string = "Wow!!! That's amazing!!!"
    input_char = '!'
    expected = "Wow! That's amazing!"
    assert replace(input_string, input_char) == expected

def test_replace_multiple_consecutive_digits():
    # Replace multiple consecutive digits
    input_string = 'My number is 1112223333'
    input_char = '3'
    expected = 'My number is 1112223'
    assert replace(input_string, input_char) == expected

def test_replace_entire_string_repeated_char():
    # Replace multiple consecutive characters when entire string is repeated char
    input_string = 'aaaaaa'
    input_char = 'a'
    expected = 'a'
    assert replace(input_string, input_char) == expected

def test_no_replacement_char_not_in_string():
    # No replacement when character does not appear in string
    input_string = 'hello world'
    input_char = 'x'
    expected = 'hello world'
    assert replace(input_string, input_char) == expected
import re
def find_character(string):
  uppercase_characters = re.findall(r"[A-Z]", string) 
  lowercase_characters = re.findall(r"[a-z]", string) 
  numerical_characters = re.findall(r"[0-9]", string) 
  special_characters = re.findall(r"[, .!?]", string) 
  return uppercase_characters, lowercase_characters, numerical_characters, special_characters

import pytest

def test_mixed_characters_including_upper_lower_digits_special():
    input_string = 'Hello, World! 123'
    expected = (['H', 'W'], ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd'], ['1', '2', '3'], [',', '!'])
    assert find_character(input_string) == expected

def test_only_uppercase_letters():
    input_string = 'ABCXYZ'
    expected = (['A', 'B', 'C', 'X', 'Y', 'Z'], [], [], [])
    assert find_character(input_string) == expected

def test_only_lowercase_letters():
    input_string = 'abcdef'
    expected = ([], ['a', 'b', 'c', 'd', 'e', 'f'], [], [])
    assert find_character(input_string) == expected

def test_only_digits():
    input_string = '9876543210'
    expected = ([], [], ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0'], [])
    assert find_character(input_string) == expected

def test_only_special_characters():
    input_string = ',.!?'
    expected = ([], [], [], [',', '.', '!', '?'])
    assert find_character(input_string) == expected

def test_characters_not_matching_any_category():
    input_string = '@#$%^&*()'
    expected = ([], [], [], [])
    assert find_character(input_string) == expected

def test_empty_string_input():
    input_string = ''
    expected = ([], [], [], [])
    assert find_character(input_string) == expected

def test_spaces_and_special_characters():
    input_string = 'Hi! How are you?'
    expected = (['H', 'H'], ['i', 'o', 'w', 'a', 'r', 'e', 'y', 'o', 'u'], [], ['!', '?'])
    assert find_character(input_string) == expected
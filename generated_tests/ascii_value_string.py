def ascii_value_string(str1):
  for i in range(len(str1)):
   return ord(str1[i])

import pytest

def test_ascii_value_single_character():
    # Return ASCII value of the first character in a single-character string
    result = ascii_value_string('A')
    assert result == 65

def test_ascii_value_multi_character_string():
    # Return ASCII value of the first character in a multi-character string
    result = ascii_value_string('Hello')
    assert result == 72

def test_ascii_value_string_starting_with_space():
    # Return ASCII value of the first character when string starts with a space
    result = ascii_value_string(' world')
    assert result == 32

def test_ascii_value_string_starting_with_digit():
    # Return ASCII value of the first character when string starts with a digit
    result = ascii_value_string('9 lives')
    assert result == 57

def test_ascii_value_string_starting_with_special_character():
    # Return ASCII value of the first character when string starts with a special character
    result = ascii_value_string('#hashtag')
    assert result == 35
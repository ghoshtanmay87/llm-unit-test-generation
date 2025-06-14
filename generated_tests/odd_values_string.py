def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

import pytest

def test_extract_characters_at_even_indices_from_simple_string():
    input_str = "abcdef"
    expected = "ace"
    assert odd_values_string(input_str) == expected

def test_handle_empty_string_input():
    input_str = ""
    expected = ""
    assert odd_values_string(input_str) == expected

def test_single_character_string_returns_the_character():
    input_str = "x"
    expected = "x"
    assert odd_values_string(input_str) == expected

def test_string_with_spaces_and_punctuation():
    input_str = "a b!c?d"
    expected = "abcd"
    assert odd_values_string(input_str) == expected

def test_string_with_numbers_and_letters():
    input_str = "1a2b3c4d"
    expected = "1234"
    assert odd_values_string(input_str) == expected

def test_string_with_all_identical_characters():
    input_str = "zzzzzz"
    expected = "zzz"
    assert odd_values_string(input_str) == expected
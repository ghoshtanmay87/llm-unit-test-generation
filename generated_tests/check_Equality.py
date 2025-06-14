def check_Equality(str):
  if (str[0] == str[-1]):  
    return ("Equal") 
  else:  
    return ("Not Equal")

import pytest

def test_string_with_identical_first_and_last_characters():
    # The first character 'r' and the last character 'r' are the same
    result = check_Equality("radar")
    assert result == "Equal"

def test_string_with_different_first_and_last_characters():
    # The first character 'h' and the last character 'o' are different
    result = check_Equality("hello")
    assert result == "Not Equal"

def test_single_character_string():
    # Single character string, first and last character are the same
    result = check_Equality("a")
    assert result == "Equal"

def test_string_with_spaces_as_first_and_last_characters():
    # The first and last characters are spaces, so they are equal
    result = check_Equality(" a ")
    assert result == "Equal"
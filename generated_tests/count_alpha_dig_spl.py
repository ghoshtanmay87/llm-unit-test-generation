def count_alpha_dig_spl(string):
  alphabets=digits = special = 0
  for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
  return (alphabets,digits,special)

import pytest

def test_count_alpha_dig_spl_alphabets_only():
    # Count characters in a string with alphabets only
    result = count_alpha_dig_spl("HelloWorld")
    assert result == (10, 0, 0)

def test_count_alpha_dig_spl_digits_only():
    # Count characters in a string with digits only
    result = count_alpha_dig_spl("1234567890")
    assert result == (0, 10, 0)

def test_count_alpha_dig_spl_special_characters_only():
    # Count characters in a string with special characters only
    result = count_alpha_dig_spl("!@#$%^&*()")
    assert result == (0, 0, 10)

def test_count_alpha_dig_spl_mixed_characters():
    # Count characters in a mixed string with alphabets, digits, and special characters
    result = count_alpha_dig_spl("abc123!@#")
    assert result == (3, 3, 3)

def test_count_alpha_dig_spl_empty_string():
    # Count characters in an empty string
    result = count_alpha_dig_spl("")
    assert result == (0, 0, 0)

def test_count_alpha_dig_spl_spaces_and_tabs():
    # Count characters in a string with spaces and tabs as special characters
    result = count_alpha_dig_spl("a1 \t!")
    assert result == (1, 1, 3)

def test_count_alpha_dig_spl_unicode_alphabets_and_digits():
    # Count characters in a string with unicode alphabets and digits
    result = count_alpha_dig_spl("ñ5ß")
    assert result == (2, 1, 0)

def test_count_alpha_dig_spl_newline_and_carriage_return():
    # Count characters in a string with newline and carriage return as special characters
    result = count_alpha_dig_spl("A1\n\r")
    assert result == (1, 1, 2)
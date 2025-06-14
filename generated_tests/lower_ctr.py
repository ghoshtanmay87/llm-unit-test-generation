def lower_ctr(str):
      lower_ctr= 0
      for i in range(len(str)):
          if str[i] >= 'a' and str[i] <= 'z': lower_ctr += 1     
      return  lower_ctr

import pytest

def test_count_lowercase_letters_in_mixed_case_string():
    # The string 'HelloWorld' has 8 lowercase letters: 'e', 'l', 'l', 'o', 'o', 'r', 'l', 'd'.
    result = lower_ctr('HelloWorld')
    assert result == 8

def test_count_lowercase_letters_in_all_uppercase_string():
    # The string 'HELLO' contains no lowercase letters, so the count is zero.
    result = lower_ctr('HELLO')
    assert result == 0

def test_count_lowercase_letters_in_all_lowercase_string():
    # All characters in 'python' are lowercase letters, so the count is 6.
    result = lower_ctr('python')
    assert result == 6

def test_count_lowercase_letters_in_string_with_digits_and_symbols():
    # Only 'a', 'b', and 'c' are lowercase letters; digits and symbols are ignored.
    result = lower_ctr('abc123!@#XYZ')
    assert result == 3

def test_count_lowercase_letters_in_empty_string():
    # An empty string contains no characters, so the count is zero.
    result = lower_ctr('')
    assert result == 0
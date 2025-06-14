def number_ctr(str):
      number_ctr= 0
      for i in range(len(str)):
          if str[i] >= '0' and str[i] <= '9': number_ctr += 1     
      return  number_ctr

import pytest

def test_count_digits_in_mixed_characters():
    # Scenario: Count digits in a string with mixed characters
    input_str = 'abc123xyz'
    expected = 3
    assert number_ctr(input_str) == expected

def test_count_digits_in_string_with_no_digits():
    # Scenario: Count digits in a string with no digits
    input_str = 'hello world!'
    expected = 0
    assert number_ctr(input_str) == expected

def test_count_digits_in_string_with_only_digits():
    # Scenario: Count digits in a string with only digits
    input_str = '9876543210'
    expected = 10
    assert number_ctr(input_str) == expected

def test_count_digits_in_empty_string():
    # Scenario: Count digits in an empty string
    input_str = ''
    expected = 0
    assert number_ctr(input_str) == expected

def test_count_digits_in_string_with_digits_and_special_characters():
    # Scenario: Count digits in a string with digits and special characters
    input_str = 'a1!b2@c3#'
    expected = 3
    assert number_ctr(input_str) == expected
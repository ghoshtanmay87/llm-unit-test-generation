def move_num(test_str):
  res = ''
  dig = ''
  for ele in test_str:
    if ele.isdigit():
      dig += ele
    else:
      res += ele
  res += dig
  return (res)

import pytest

def test_string_with_digits_at_the_end():
    # All digits are already at the end, so the function returns the string unchanged.
    input_str = 'abc123'
    expected = 'abc123'
    assert move_num(input_str) == expected

def test_string_with_digits_at_the_beginning():
    # Digits '123' are collected and moved to the end, non-digit characters 'abc' remain at the front.
    input_str = '123abc'
    expected = 'abc123'
    assert move_num(input_str) == expected

def test_string_with_digits_interspersed():
    # Digits '1', '2', '3' are extracted and appended at the end, letters 'a', 'b', 'c' remain in original order.
    input_str = 'a1b2c3'
    expected = 'abc123'
    assert move_num(input_str) == expected

def test_string_with_no_digits():
    # No digits to move, so the string is returned unchanged.
    input_str = 'abcdef'
    expected = 'abcdef'
    assert move_num(input_str) == expected

def test_string_with_only_digits():
    # All characters are digits, so they are collected and appended at the end, resulting in the same string.
    input_str = '987654'
    expected = '987654'
    assert move_num(input_str) == expected

def test_empty_string_input():
    # Empty input returns empty output as there are no characters to process.
    input_str = ''
    expected = ''
    assert move_num(input_str) == expected

def test_string_with_special_characters_and_digits():
    # Digits '2', '3', '4' are moved to the end; special characters and letters remain in original order.
    input_str = 'a!2b@3c#4'
    expected = 'a!b@c#234'
    assert move_num(input_str) == expected

def test_string_with_spaces_and_digits():
    # Digits '1', '2', '3' are moved to the end; spaces and letters remain in original order, so spaces before 'abc' remain.
    input_str = '1 2 3 abc'
    expected = '   abc123'
    assert move_num(input_str) == expected
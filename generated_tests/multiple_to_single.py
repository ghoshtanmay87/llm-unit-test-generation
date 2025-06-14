def multiple_to_single(L):
  x = int("".join(map(str, L)))
  return x

import pytest

def test_convert_list_of_single_digit_integers_to_single_integer():
    # Scenario: Convert a list of single-digit integers to a single integer
    input_data = [1, 2, 3]
    expected = 123
    assert multiple_to_single(input_data) == expected

def test_convert_list_with_single_integer_element():
    # Scenario: Convert a list with a single integer element
    input_data = [7]
    expected = 7
    assert multiple_to_single(input_data) == expected

def test_convert_list_of_multiple_digits_including_zero():
    # Scenario: Convert a list of multiple digits including zero
    input_data = [0, 4, 5]
    expected = 45
    assert multiple_to_single(input_data) == expected

def test_convert_list_of_multiple_digits_including_multiple_zeros():
    # Scenario: Convert a list of multiple digits including multiple zeros
    input_data = [0, 0, 1]
    expected = 1
    assert multiple_to_single(input_data) == expected

def test_convert_list_of_digits_forming_large_number():
    # Scenario: Convert a list of digits forming a large number
    input_data = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    expected = 9876543210
    assert multiple_to_single(input_data) == expected
def float_to_tuple(test_str):
  res = tuple(map(float, test_str.split(', ')))
  return (res)

import pytest

def test_convert_two_floats_separated_by_comma_and_space():
    # Convert a string of two floats separated by comma and space
    input_str = '1.0, 2.0'
    expected = (1.0, 2.0)
    assert float_to_tuple(input_str) == expected

def test_convert_three_floats_separated_by_comma_and_space():
    # Convert a string of three floats separated by comma and space
    input_str = '3.5, 4.5, 5.5'
    expected = (3.5, 4.5, 5.5)
    assert float_to_tuple(input_str) == expected

def test_convert_negative_and_positive_floats():
    # Convert a string with negative and positive floats
    input_str = '-1.1, 0.0, 2.2'
    expected = (-1.1, 0.0, 2.2)
    assert float_to_tuple(input_str) == expected

def test_convert_single_float_string():
    # Convert a string with a single float
    input_str = '42.42'
    expected = (42.42,)
    assert float_to_tuple(input_str) == expected

def test_convert_floats_with_no_decimal_part():
    # Convert a string with floats having no decimal part
    input_str = '10, 20, 30'
    expected = (10.0, 20.0, 30.0)
    assert float_to_tuple(input_str) == expected
def str_to_tuple(test_str):
  res = tuple(map(int, test_str.split(', ')))
  return (res)

import pytest

def test_str_to_tuple_two_element_string():
    # Convert a simple two-element string of integers separated by comma and space
    input_str = '1, 2'
    expected = (1, 2)
    assert str_to_tuple(input_str) == expected

def test_str_to_tuple_multiple_integers():
    # Convert a string with multiple integers separated by comma and space
    input_str = '10, 20, 30, 40'
    expected = (10, 20, 30, 40)
    assert str_to_tuple(input_str) == expected

def test_str_to_tuple_negative_integers():
    # Convert a string with negative integers separated by comma and space
    input_str = '-1, -2, -3'
    expected = (-1, -2, -3)
    assert str_to_tuple(input_str) == expected

def test_str_to_tuple_single_integer():
    # Convert a string with a single integer
    input_str = '42'
    expected = (42,)
    assert str_to_tuple(input_str) == expected

def test_str_to_tuple_zero_and_positive_integers():
    # Convert a string with zero and positive integers
    input_str = '0, 5, 10'
    expected = (0, 5, 10)
    assert str_to_tuple(input_str) == expected
def tuple_str_int(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split(', '))
  return (res)

import pytest

def test_convert_tuple_like_string_two_integers():
    # Convert a tuple-like string with two integers
    input_str = '(1, 2)'
    expected = (1, 2)
    assert tuple_str_int(input_str) == expected

def test_convert_tuple_like_string_three_integers():
    # Convert a tuple-like string with three integers
    input_str = '(10, 20, 30)'
    expected = (10, 20, 30)
    assert tuple_str_int(input_str) == expected

def test_convert_tuple_like_string_negative_integers():
    # Convert a tuple-like string with negative integers
    input_str = '(-5, -10, 0)'
    expected = (-5, -10, 0)
    assert tuple_str_int(input_str) == expected

def test_convert_tuple_like_string_single_integer():
    # Convert a tuple-like string with single integer
    input_str = '(42)'
    expected = (42,)
    assert tuple_str_int(input_str) == expected

def test_convert_tuple_like_string_extra_spaces():
    # Convert a tuple-like string with extra spaces
    input_str = '( 7, 8, 9 )'
    expected = (7, 8, 9)
    assert tuple_str_int(input_str) == expected
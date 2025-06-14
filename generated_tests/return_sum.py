def return_sum(dict):
  sum = 0
  for i in dict.values():
    sum = sum + i
  return sum

import pytest

def test_sum_multiple_positive_integers():
    input_dict = {'a': 1, 'b': 2, 'c': 3}
    expected = 6
    assert return_sum(input_dict) == expected

def test_sum_empty_dictionary():
    input_dict = {}
    expected = 0
    assert return_sum(input_dict) == expected

def test_sum_negative_and_positive_integers():
    input_dict = {'x': -1, 'y': 5, 'z': -3}
    expected = 1
    assert return_sum(input_dict) == expected

def test_sum_float_values():
    input_dict = {'a': 1.5, 'b': 2.5, 'c': 3.0}
    expected = 7.0
    assert return_sum(input_dict) == expected

def test_sum_single_key_value_pair():
    input_dict = {'only': 42}
    expected = 42
    assert return_sum(input_dict) == expected
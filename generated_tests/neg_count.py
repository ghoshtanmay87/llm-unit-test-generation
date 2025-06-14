def neg_count(list):
  neg_count= 0
  for num in list: 
    if num <= 0: 
      neg_count += 1
  return neg_count

import pytest

def test_count_negatives_and_zeros_mixed_values():
    # Count negatives and zeros in a list with positive, negative, and zero values
    input_list = [1, -1, 0, 2, -3]
    expected = 3
    assert neg_count(input_list) == expected

def test_count_negatives_and_zeros_all_positive():
    # Count negatives and zeros in a list with all positive numbers
    input_list = [5, 10, 3]
    expected = 0
    assert neg_count(input_list) == expected

def test_count_negatives_and_zeros_all_negative():
    # Count negatives and zeros in a list with all negative numbers
    input_list = [-5, -10, -3]
    expected = 3
    assert neg_count(input_list) == expected

def test_count_negatives_and_zeros_zeros_only():
    # Count negatives and zeros in a list with zeros only
    input_list = [0, 0, 0]
    expected = 3
    assert neg_count(input_list) == expected

def test_count_negatives_and_zeros_empty_list():
    # Count negatives and zeros in an empty list
    input_list = []
    expected = 0
    assert neg_count(input_list) == expected
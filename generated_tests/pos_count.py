def pos_count(list):
  pos_count= 0
  for num in list: 
    if num >= 0: 
      pos_count += 1
  return pos_count

import pytest

def test_count_positive_and_zero_mixed_values():
    # Count positive numbers including zero in a list with mixed positive, negative, and zero values
    input_list = [1, -2, 3, 0, -5]
    expected = 3
    assert pos_count(input_list) == expected

def test_count_positive_all_negative_values():
    # Count positive numbers in a list with all negative values
    input_list = [-1, -2, -3]
    expected = 0
    assert pos_count(input_list) == expected

def test_count_positive_all_zeros():
    # Count positive numbers in a list with all zeros
    input_list = [0, 0, 0]
    expected = 3
    assert pos_count(input_list) == expected

def test_count_positive_empty_list():
    # Count positive numbers in an empty list
    input_list = []
    expected = 0
    assert pos_count(input_list) == expected

def test_count_positive_all_positive_values():
    # Count positive numbers in a list with only positive numbers
    input_list = [5, 10, 15]
    expected = 3
    assert pos_count(input_list) == expected
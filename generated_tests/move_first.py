def move_first(test_list):
  test_list = test_list[-1:] + test_list[:-1]  
  return test_list

import pytest

def test_move_last_element_to_front_integers():
    # Move last element to front in a list of integers
    input_list = [1, 2, 3, 4, 5]
    expected = [5, 1, 2, 3, 4]
    assert move_first(input_list) == expected

def test_move_last_element_to_front_strings():
    # Move last element to front in a list of strings
    input_list = ['a', 'b', 'c', 'd']
    expected = ['d', 'a', 'b', 'c']
    assert move_first(input_list) == expected

def test_move_last_element_to_front_single_element():
    # Move last element to front in a single-element list
    input_list = [42]
    expected = [42]
    assert move_first(input_list) == expected

def test_move_last_element_to_front_empty_list():
    # Move last element to front in an empty list
    input_list = []
    expected = []
    assert move_first(input_list) == expected

def test_move_last_element_to_front_mixed_types():
    # Move last element to front in a list with mixed types
    input_list = [True, None, 3.14, 'end']
    expected = ['end', True, None, 3.14]
    assert move_first(input_list) == expected
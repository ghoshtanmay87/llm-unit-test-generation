def neg_nos(list1):
  for num in list1: 
    if num < 0: 
       return num

import pytest

def test_single_negative_number():
    # List contains a single negative number
    input_list = [-5]
    expected = -5
    assert neg_nos(input_list) == expected

def test_first_negative_number_at_start():
    # List contains multiple numbers with the first negative number at the start
    input_list = [-3, 2, -1]
    expected = -3
    assert neg_nos(input_list) == expected

def test_first_negative_number_in_middle():
    # List contains multiple numbers with the first negative number in the middle
    input_list = [4, -2, -7]
    expected = -2
    assert neg_nos(input_list) == expected

def test_no_negative_numbers():
    # List contains no negative numbers
    input_list = [1, 2, 3]
    expected = None
    assert neg_nos(input_list) == expected

def test_empty_list():
    # Empty list input
    input_list = []
    expected = None
    assert neg_nos(input_list) == expected
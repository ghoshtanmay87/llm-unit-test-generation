def pos_nos(list1):
  for num in list1: 
    if num >= 0: 
       return num

import pytest

def test_first_positive_number_at_start():
    # The first element 5 is >= 0, so it returns 5 immediately.
    assert pos_nos([5, -3, 2, 0]) == 5

def test_first_positive_number_in_middle():
    # Skips -1 and -2, then finds 3 which is >= 0 and returns it.
    assert pos_nos([-1, -2, 3, 4]) == 3

def test_first_non_negative_number_is_zero():
    # Skips -5 and -1, then finds 0 which is >= 0 and returns it.
    assert pos_nos([-5, -1, 0, 2]) == 0

def test_all_numbers_negative():
    # Finds no number >= 0, so returns None.
    assert pos_nos([-3, -2, -1]) is None

def test_empty_list_input():
    # No elements to iterate over, so returns None.
    assert pos_nos([]) is None

def test_first_element_is_zero():
    # The first element 0 is >= 0, so returns 0 immediately.
    assert pos_nos([0, 1, 2]) == 0

def test_list_with_positive_numbers_only():
    # The first element 10 is >= 0, so returns 10 immediately.
    assert pos_nos([10, 20, 30]) == 10
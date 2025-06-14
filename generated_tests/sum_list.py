def sum_list(lst1,lst2):
  res_list = [lst1[i] + lst2[i] for i in range(len(lst1))] 
  return res_list

import pytest

def test_sum_two_lists_of_positive_integers():
    # Sum two lists of equal length with positive integers
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    expected = [5, 7, 9]
    assert sum_list(lst1, lst2) == expected

def test_sum_two_lists_with_negative_and_positive_integers():
    # Sum two lists of equal length with negative and positive integers
    lst1 = [-1, 0, 3]
    lst2 = [1, -2, 4]
    expected = [0, -2, 7]
    assert sum_list(lst1, lst2) == expected

def test_sum_two_lists_of_zeros():
    # Sum two lists of equal length with zeros
    lst1 = [0, 0, 0]
    lst2 = [0, 0, 0]
    expected = [0, 0, 0]
    assert sum_list(lst1, lst2) == expected

def test_sum_two_lists_of_floats():
    # Sum two lists of equal length with floats
    lst1 = [1.5, 2.5, 3.5]
    lst2 = [4.5, 5.5, 6.5]
    expected = [6.0, 8.0, 10.0]
    assert sum_list(lst1, lst2) == expected

def test_sum_two_empty_lists():
    # Sum two empty lists
    lst1 = []
    lst2 = []
    expected = []
    assert sum_list(lst1, lst2) == expected
def last(n):
   return n[-1]
def sort_list_last(tuples):
  return sorted(tuples, key=last)

import pytest

def test_sort_list_last_ascending_order():
    # Sorting a list of tuples by their last element in ascending order
    tuples = [(1, 3), (3, 2), (2, 1)]
    expected = [(2, 1), (3, 2), (1, 3)]
    assert sort_list_last(tuples) == expected

def test_sort_list_last_negative_and_positive():
    # Sorting a list of tuples with negative and positive last elements
    tuples = [(4, -1), (2, 0), (3, -5)]
    expected = [(3, -5), (4, -1), (2, 0)]
    assert sort_list_last(tuples) == expected

def test_sort_list_last_all_equal_last_elements():
    # Sorting a list of tuples where all last elements are equal
    tuples = [(1, 2), (3, 2), (2, 2)]
    expected = [(1, 2), (3, 2), (2, 2)]
    assert sort_list_last(tuples) == expected

def test_sort_list_last_single_element_tuples():
    # Sorting a list of tuples with single-element tuples
    tuples = [(5,), (3,), (4,)]
    expected = [(3,), (4,), (5,)]
    assert sort_list_last(tuples) == expected

def test_sort_list_last_empty_list():
    # Sorting an empty list of tuples
    tuples = []
    expected = []
    assert sort_list_last(tuples) == expected
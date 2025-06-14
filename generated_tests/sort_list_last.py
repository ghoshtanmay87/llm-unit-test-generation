def last(n):
   return n[-1]
def sort_list_last(tuples):
  return sorted(tuples, key=last)

import pytest

def test_sort_list_of_tuples_by_last_element_ascending():
    tuples = [(1, 3), (3, 2), (2, 1)]
    expected = [(2, 1), (3, 2), (1, 3)]
    assert sort_list_last(tuples) == expected

def test_sort_list_of_tuples_with_varying_last_elements_including_duplicates():
    tuples = [(2, 5), (1, 2), (4, 2), (3, 7)]
    expected = [(1, 2), (4, 2), (2, 5), (3, 7)]
    assert sort_list_last(tuples) == expected

def test_sort_list_of_single_element_tuples():
    tuples = [(3,), (1,), (2,)]
    expected = [(1,), (2,), (3,)]
    assert sort_list_last(tuples) == expected

def test_sort_empty_list_of_tuples():
    tuples = []
    expected = []
    assert sort_list_last(tuples) == expected

def test_sort_list_of_tuples_with_negative_and_positive_last_elements():
    tuples = [(1, -1), (2, 0), (3, -2), (4, 2)]
    expected = [(3, -2), (1, -1), (2, 0), (4, 2)]
    assert sort_list_last(tuples) == expected
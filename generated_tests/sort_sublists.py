def sort_sublists(list1):
      list1.sort()  
      list1.sort(key=len)
      return  list1

import pytest

def test_sort_sublists_by_length_then_lexicographically():
    input_list = [[3, 2], [1], [2, 1], [1, 2, 3]]
    expected = [[1], [2, 1], [3, 2], [1, 2, 3]]
    assert sort_sublists(input_list) == expected

def test_sort_sublists_varying_lengths_and_values():
    input_list = [[5, 4, 3], [1, 2], [3], [2, 2], [1]]
    expected = [[1], [3], [1, 2], [2, 2], [5, 4, 3]]
    assert sort_sublists(input_list) == expected

def test_sort_sublists_all_same_length():
    input_list = [[3, 1], [2, 2], [1, 3]]
    expected = [[1, 3], [2, 2], [3, 1]]
    assert sort_sublists(input_list) == expected

def test_sort_sublists_with_empty_sublists():
    input_list = [[], [1], [2, 2], []]
    expected = [[], [], [1], [2, 2]]
    assert sort_sublists(input_list) == expected

def test_sort_sublists_single_element_sublists_only():
    input_list = [[3], [1], [2]]
    expected = [[1], [2], [3]]
    assert sort_sublists(input_list) == expected
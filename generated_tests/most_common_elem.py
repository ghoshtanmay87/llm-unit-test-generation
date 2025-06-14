from collections import Counter 
def most_common_elem(s,a):
  most_common_elem=Counter(s).most_common(a)
  return most_common_elem

import pytest

def test_single_most_common_element_distinct():
    s = [1, 2, 3, 4, 5]
    a = 1
    expected = [(1, 1)]
    assert most_common_elem(s, a) == expected

def test_top_two_most_common_repeated_elements():
    s = [1, 2, 2, 3, 3, 3, 4]
    a = 2
    expected = [(3, 3), (2, 2)]
    assert most_common_elem(s, a) == expected

def test_top_three_with_ties_in_frequency():
    s = ['a', 'b', 'b', 'c', 'c', 'd']
    a = 3
    expected = [('b', 2), ('c', 2), ('a', 1)]
    assert most_common_elem(s, a) == expected

def test_request_more_than_unique_elements():
    s = [10, 20, 20, 30]
    a = 5
    expected = [(20, 2), (10, 1), (30, 1)]
    assert most_common_elem(s, a) == expected

def test_empty_list_returns_empty():
    s = []
    a = 3
    expected = []
    assert most_common_elem(s, a) == expected

def test_all_elements_same_frequency_return_top_two():
    s = [5, 6, 7, 8]
    a = 2
    expected = [(5, 1), (6, 1)]
    assert most_common_elem(s, a) == expected
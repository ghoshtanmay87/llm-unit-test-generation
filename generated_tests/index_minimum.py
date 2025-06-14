from operator import itemgetter 
def index_minimum(test_list):
  res = min(test_list, key = itemgetter(1))[0]
  return (res)

import pytest

def test_index_minimum_distinct_values():
    test_list = [[0, 10], [1, 5], [2, 7]]
    expected = 1
    assert index_minimum(test_list) == expected

def test_index_minimum_min_at_first_position():
    test_list = [[0, 3], [1, 4], [2, 5]]
    expected = 0
    assert index_minimum(test_list) == expected

def test_index_minimum_multiple_min_values():
    test_list = [[0, 2], [1, 2], [2, 3]]
    expected = 0
    assert index_minimum(test_list) == expected

def test_index_minimum_with_negative_values():
    test_list = [[0, -1], [1, -5], [2, 0]]
    expected = 1
    assert index_minimum(test_list) == expected

def test_index_minimum_single_element():
    test_list = [[42, 100]]
    expected = 42
    assert index_minimum(test_list) == expected
from itertools import groupby 
def group_element(test_list):
  res = dict()
  for key, val in groupby(sorted(test_list, key = lambda ele: ele[1]), key = lambda ele: ele[1]):
    res[key] = [ele[0] for ele in val] 
  return (res)

import pytest

def test_group_elements_by_second_value_with_distinct_groups():
    test_list = [[1, 2], [3, 1], [4, 2], [5, 3]]
    expected_output = {1: [3], 2: [1, 4], 3: [5]}
    assert group_element(test_list) == expected_output

def test_group_elements_when_all_second_values_are_the_same():
    test_list = [[10, 5], [20, 5], [30, 5]]
    expected_output = {5: [10, 20, 30]}
    assert group_element(test_list) == expected_output

def test_group_elements_with_multiple_groups_and_unordered_input():
    test_list = [[7, 3], [2, 1], [9, 3], [4, 1], [5, 2]]
    expected_output = {1: [2, 4], 2: [5], 3: [7, 9]}
    assert group_element(test_list) == expected_output

def test_empty_input_list_returns_empty_dictionary():
    test_list = []
    expected_output = {}
    assert group_element(test_list) == expected_output

def test_group_elements_with_negative_and_zero_second_values():
    test_list = [[1, 0], [2, -1], [3, 0], [4, -1], [5, 1]]
    expected_output = {-1: [2, 4], 0: [1, 3], 1: [5]}
    assert group_element(test_list) == expected_output
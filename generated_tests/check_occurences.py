from collections import Counter 
def check_occurences(test_list):
  res = dict(Counter(tuple(ele) for ele in map(sorted, test_list)))
  return  (res)

import pytest

def test_count_occurrences_sorted_tuples_with_duplicates():
    test_list = [[1, 2], [2, 1], [1, 2], [3, 4]]
    expected_output = {(1, 2): 3, (3, 4): 1}
    assert check_occurences(test_list) == expected_output

def test_count_occurrences_empty_input_list():
    test_list = []
    expected_output = {}
    assert check_occurences(test_list) == expected_output

def test_count_occurrences_single_element_lists():
    test_list = [[5], [5], [5]]
    expected_output = {(5,): 3}
    assert check_occurences(test_list) == expected_output

def test_count_occurrences_different_length_sublists():
    test_list = [[1, 2], [2, 1, 3], [3, 2, 1], [1, 2]]
    expected_output = {(1, 2): 2, (1, 2, 3): 2}
    assert check_occurences(test_list) == expected_output

def test_count_occurrences_sublists_with_repeated_elements():
    test_list = [[1, 1, 2], [2, 1, 1], [1, 2, 2]]
    expected_output = {(1, 1, 2): 2, (1, 2, 2): 1}
    assert check_occurences(test_list) == expected_output
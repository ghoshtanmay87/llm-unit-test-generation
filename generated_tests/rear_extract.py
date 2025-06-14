def rear_extract(test_list):
  res = [lis[-1] for lis in test_list]
  return (res)

import pytest

def test_rear_extract_with_integer_lists():
    # Extract last elements from a list of integer lists
    input_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [3, 6, 9]
    assert rear_extract(input_data) == expected

def test_rear_extract_with_string_lists():
    # Extract last elements from a list of string lists
    input_data = [['apple', 'banana'], ['cat', 'dog'], ['egg', 'fish']]
    expected = ['banana', 'dog', 'fish']
    assert rear_extract(input_data) == expected

def test_rear_extract_with_single_element_lists():
    # Extract last elements from a list of single-element lists
    input_data = [[10], [20], [30]]
    expected = [10, 20, 30]
    assert rear_extract(input_data) == expected

def test_rear_extract_with_mixed_type_lists():
    # Extract last elements from a list of mixed-type lists
    input_data = [[1, 'a', 3.5], [True, False], ['x', 'y', 'z']]
    expected = [3.5, False, 'z']
    assert rear_extract(input_data) == expected

def test_rear_extract_with_empty_list():
    # Extract last elements from an empty list
    input_data = []
    expected = []
    assert rear_extract(input_data) == expected
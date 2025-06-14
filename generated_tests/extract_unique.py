def extract_unique(test_dict):
  res = list(sorted({ele for val in test_dict.values() for ele in val}))
  return res

import pytest

def test_extract_unique_with_overlapping_integers():
    test_dict = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [4, 5]}
    expected_output = [1, 2, 3, 4, 5]
    assert extract_unique(test_dict) == expected_output

def test_extract_unique_with_empty_lists():
    test_dict = {'x': [], 'y': [], 'z': []}
    expected_output = []
    assert extract_unique(test_dict) == expected_output

def test_extract_unique_with_single_element_lists():
    test_dict = {'one': [10], 'two': [20], 'three': [10]}
    expected_output = [10, 20]
    assert extract_unique(test_dict) == expected_output

def test_extract_unique_with_string_elements():
    test_dict = {'first': ['apple', 'banana'], 'second': ['banana', 'cherry'], 'third': ['date']}
    expected_output = ['apple', 'banana', 'cherry', 'date']
    assert extract_unique(test_dict) == expected_output

def test_extract_unique_with_mixed_int_and_float():
    test_dict = {'nums1': [1, 2.0, 3], 'nums2': [2, 3.0, 4]}
    expected_output = [1, 2, 3, 4]
    assert extract_unique(test_dict) == expected_output
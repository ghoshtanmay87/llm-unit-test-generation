def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;

import pytest

def test_all_elements_unique():
    data = [1, 2, 3, 4, 5]
    expected_output = True
    assert test_distinct(data) == expected_output

def test_list_contains_duplicates():
    data = [1, 2, 2, 3, 4]
    expected_output = False
    assert test_distinct(data) == expected_output

def test_empty_list():
    data = []
    expected_output = True
    assert test_distinct(data) == expected_output

def test_single_element_list():
    data = [42]
    expected_output = True
    assert test_distinct(data) == expected_output

def test_multiple_identical_elements():
    data = [7, 7, 7, 7]
    expected_output = False
    assert test_distinct(data) == expected_output

def test_different_data_types_with_duplicates():
    data = [1, '1', 1.0, (1,)]
    expected_output = False
    assert test_distinct(data) == expected_output

def test_all_unique_string_elements():
    data = ['apple', 'banana', 'cherry']
    expected_output = True
    assert test_distinct(data) == expected_output
def extract_rear(test_tuple):
  res = list(sub[len(sub) - 1] for sub in test_tuple)
  return (res)

import pytest

def test_extract_last_elements_from_tuples_of_integers():
    test_tuple = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected_output = [3, 6, 9]
    assert extract_rear(test_tuple) == expected_output

def test_extract_last_elements_from_tuples_of_mixed_types():
    test_tuple = [(10, 'a'), (20, 'b'), (30, 'c')]
    expected_output = ['a', 'b', 'c']
    assert extract_rear(test_tuple) == expected_output

def test_extract_last_elements_from_single_element_tuples():
    test_tuple = [(100,), (200,), (300,)]
    expected_output = [100, 200, 300]
    assert extract_rear(test_tuple) == expected_output

def test_extract_last_elements_from_tuples_with_nested_tuples():
    test_tuple = [(1, (2, 3)), (4, (5, 6)), (7, (8, 9))]
    expected_output = [(2, 3), (5, 6), (8, 9)]
    assert extract_rear(test_tuple) == expected_output

def test_extract_last_elements_from_empty_list():
    test_tuple = []
    expected_output = []
    assert extract_rear(test_tuple) == expected_output
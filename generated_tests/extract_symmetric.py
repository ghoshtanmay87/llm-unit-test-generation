def extract_symmetric(test_list):
  temp = set(test_list) & {(b, a) for a, b in test_list}
  res = {(a, b) for a, b in temp if a < b}
  return (res)

import pytest

def test_extract_symmetric_one_symmetric_pair():
    test_list = [(1, 2), (2, 1), (3, 4)]
    expected_output = {(1, 2)}
    assert extract_symmetric(test_list) == expected_output

def test_extract_symmetric_no_symmetric_pairs():
    test_list = [(1, 2), (3, 4), (5, 6)]
    expected_output = set()
    assert extract_symmetric(test_list) == expected_output

def test_extract_symmetric_multiple_symmetric_pairs_with_duplicates():
    test_list = [(1, 2), (2, 1), (3, 4), (4, 3), (1, 2)]
    expected_output = {(1, 2), (3, 4)}
    assert extract_symmetric(test_list) == expected_output

def test_extract_symmetric_symmetric_pairs_with_equal_elements():
    test_list = [(1, 1), (2, 2), (3, 3)]
    expected_output = set()
    assert extract_symmetric(test_list) == expected_output

def test_extract_symmetric_empty_input_list():
    test_list = []
    expected_output = set()
    assert extract_symmetric(test_list) == expected_output

def test_extract_symmetric_symmetric_pairs_with_negative_and_positive_integers():
    test_list = [(-1, 2), (2, -1), (3, -3), (-3, 3), (0, 0)]
    expected_output = {(-3, 3), (-1, 2)}
    assert extract_symmetric(test_list) == expected_output
def extract_min_max(test_tup, K):
  res = []
  test_tup = list(test_tup)
  temp = sorted(test_tup)
  for idx, val in enumerate(temp):
    if idx < K or idx >= len(temp) - K:
      res.append(val)
  res = tuple(res)
  return (res)

import pytest

def test_extract_min_max_k_1_distinct_integers():
    # Extract min and max elements when K is 1 from a tuple of distinct integers
    test_tup = (5, 1, 9, 3, 7)
    K = 1
    expected_output = (1, 9)
    assert extract_min_max(test_tup, K) == expected_output

def test_extract_min_max_k_2_distinct_integers():
    # Extract min and max elements when K is 2 from a tuple of distinct integers
    test_tup = (5, 1, 9, 3, 7)
    K = 2
    expected_output = (1, 3, 7, 9)
    assert extract_min_max(test_tup, K) == expected_output

def test_extract_min_max_k_0_edge_case():
    # Extract min and max elements when K is 0 (edge case)
    test_tup = (5, 1, 9, 3, 7)
    K = 0
    expected_output = ()
    assert extract_min_max(test_tup, K) == expected_output

def test_extract_min_max_k_larger_than_half_length():
    # Extract min and max elements when K is larger than half the tuple length
    test_tup = (10, 20, 30, 40, 50)
    K = 3
    expected_output = (10, 20, 30, 40, 50)
    assert extract_min_max(test_tup, K) == expected_output

def test_extract_min_max_duplicates_k_2_corrected():
    # Extract min and max elements from a tuple with duplicate values (corrected)
    test_tup = (4, 2, 2, 8, 6, 6)
    K = 2
    expected_output = (2, 2, 6, 8)
    assert extract_min_max(test_tup, K) == expected_output

def test_extract_min_max_empty_tuple():
    # Extract min and max elements when input tuple is empty
    test_tup = ()
    K = 1
    expected_output = ()
    assert extract_min_max(test_tup, K) == expected_output

def test_extract_min_max_k_equals_tuple_length():
    # Extract min and max elements when K equals tuple length
    test_tup = (3, 1, 4)
    K = 3
    expected_output = (1, 3, 4)
    assert extract_min_max(test_tup, K) == expected_output
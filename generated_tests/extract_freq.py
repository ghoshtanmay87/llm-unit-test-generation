def extract_freq(test_list):
  res = len(list(set(tuple(sorted(sub)) for sub in test_list)))
  return (res)

import pytest

def test_extract_freq_unique_sorted_sublists():
    test_list = [[1, 2], [2, 1], [3, 4]]
    expected_output = 2
    assert extract_freq(test_list) == expected_output

def test_extract_freq_identical_sublists():
    test_list = [[5, 5], [5, 5], [5, 5]]
    expected_output = 1
    assert extract_freq(test_list) == expected_output

def test_extract_freq_varying_length_sublists():
    test_list = [[1], [1, 2], [2, 1], [1, 2, 3]]
    expected_output = 3
    assert extract_freq(test_list) == expected_output

def test_extract_freq_empty_list():
    test_list = []
    expected_output = 0
    assert extract_freq(test_list) == expected_output

def test_extract_freq_sublists_with_internal_duplicates():
    test_list = [[1, 1, 2], [2, 1, 1], [1, 2, 2]]
    expected_output = 2
    assert extract_freq(test_list) == expected_output
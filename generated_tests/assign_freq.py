from collections import Counter 
def assign_freq(test_list):
  res = [(*key, val) for key, val in Counter(test_list).items()]
  return (str(res))

import pytest

def test_assign_freq_multiple_repeated_tuples():
    test_list = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (3, 4)]
    expected_output = "[(1, 2, 2), (3, 4, 3), (5, 6, 1)]"
    assert assign_freq(test_list) == expected_output

def test_assign_freq_unique_tuples_only():
    test_list = [(7, 8), (9, 10), (11, 12)]
    expected_output = "[(7, 8, 1), (9, 10, 1), (11, 12, 1)]"
    assert assign_freq(test_list) == expected_output

def test_assign_freq_empty_list():
    test_list = []
    expected_output = "[]"
    assert assign_freq(test_list) == expected_output

def test_assign_freq_one_tuple_repeated_multiple_times():
    test_list = [(0, 0), (0, 0), (0, 0), (0, 0)]
    expected_output = "[(0, 0, 4)]"
    assert assign_freq(test_list) == expected_output

def test_assign_freq_tuples_of_varying_lengths():
    test_list = [(1,), (1,), (2, 3), (2, 3), (2, 3), (4, 5, 6)]
    expected_output = "[(1, 2), (2, 3, 3), (4, 5, 6, 1)]"
    assert assign_freq(test_list) == expected_output
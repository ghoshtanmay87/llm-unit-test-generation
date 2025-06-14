def trim_tuple(test_list, K):
  res = []
  for ele in test_list:
    N = len(ele)
    res.append(tuple(list(ele)[K: N - K]))
  return (str(res))

import pytest

def test_trim_1_element_from_start_and_end_of_length_5():
    test_list = [(1, 2, 3, 4, 5)]
    K = 1
    expected_output = "[(2, 3, 4)]"
    assert trim_tuple(test_list, K) == expected_output

def test_trim_2_elements_from_start_and_end_of_length_6():
    test_list = [(10, 20, 30, 40, 50, 60)]
    K = 2
    expected_output = "[(30, 40)]"
    assert trim_tuple(test_list, K) == expected_output

def test_trim_0_elements_returns_original_tuples():
    test_list = [(7, 8, 9)]
    K = 0
    expected_output = "[(7, 8, 9)]"
    assert trim_tuple(test_list, K) == expected_output

def test_trim_more_than_half_length_results_in_empty_tuples():
    test_list = [(1, 2, 3, 4)]
    K = 3
    expected_output = "[()]"
    assert trim_tuple(test_list, K) == expected_output

def test_multiple_tuples_different_lengths_trimmed_by_1():
    test_list = [(1, 2, 3), (4, 5, 6, 7), (8, 9)]
    K = 1
    expected_output = "[(2,), (5, 6), ()]"
    assert trim_tuple(test_list, K) == expected_output
def find_equal_tuple(Input, k):
  flag = 1
  for tuple in Input:
    if len(tuple) != k:
      flag = 0
      break
  return flag
def get_equal(Input, k):
  if find_equal_tuple(Input, k) == 1:
    return ("All tuples have same length")
  else:
    return ("All tuples do not have same length")

import pytest

def test_all_tuples_have_length_equal_to_k():
    Input = [(1, 2), (3, 4), (5, 6)]
    k = 2
    expected_output = "All tuples have same length"
    assert get_equal(Input, k) == expected_output

def test_at_least_one_tuple_does_not_have_length_equal_to_k():
    Input = [(1, 2), (3, 4, 5), (6, 7)]
    k = 2
    expected_output = "All tuples do not have same length"
    assert get_equal(Input, k) == expected_output

def test_empty_input_list():
    Input = []
    k = 3
    expected_output = "All tuples have same length"
    assert get_equal(Input, k) == expected_output

def test_all_tuples_have_length_1_k_is_1():
    Input = [(1,), (2,), (3,)]
    k = 1
    expected_output = "All tuples have same length"
    assert get_equal(Input, k) == expected_output

def test_mixed_tuple_lengths_none_match_k():
    Input = [(1,), (2, 3), (4, 5, 6)]
    k = 4
    expected_output = "All tuples do not have same length"
    assert get_equal(Input, k) == expected_output
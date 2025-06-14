def join_tuples(test_list):
  res = []
  for sub in test_list:
    if res and res[-1][0] == sub[0]:
      res[-1].extend(sub[1:])
    else:
      res.append([ele for ele in sub])
  res = list(map(tuple, res))
  return (res)

import pytest

def test_join_tuples_matching_first_elements():
    test_list = [(1, 2), (1, 3), (2, 4)]
    expected_output = [(1, 2, 3), (2, 4)]
    assert join_tuples(test_list) == expected_output

def test_join_tuples_no_matching_first_elements():
    test_list = [(1, 2), (3, 4), (5, 6)]
    expected_output = [(1, 2), (3, 4), (5, 6)]
    assert join_tuples(test_list) == expected_output

def test_join_tuples_multiple_consecutive_same_first_element():
    test_list = [(1, 2), (1, 3), (1, 4), (2, 5)]
    expected_output = [(1, 2, 3, 4), (2, 5)]
    assert join_tuples(test_list) == expected_output

def test_join_tuples_empty_input_list():
    test_list = []
    expected_output = []
    assert join_tuples(test_list) == expected_output

def test_join_tuples_single_tuple_in_list():
    test_list = [(7, 8, 9)]
    expected_output = [(7, 8, 9)]
    assert join_tuples(test_list) == expected_output

def test_join_tuples_tuples_with_single_elements():
    test_list = [(1,), (1,), (2,), (2,), (2,)]
    expected_output = [(1,), (1,), (2,), (2,), (2,)]
    assert join_tuples(test_list) == expected_output

def test_join_tuples_non_consecutive_same_first_element():
    test_list = [(1, 2), (2, 3), (1, 4)]
    expected_output = [(1, 2), (2, 3), (1, 4)]
    assert join_tuples(test_list) == expected_output
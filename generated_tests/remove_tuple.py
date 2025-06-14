def remove_tuple(test_list):
  res = [sub for sub in test_list if not all(ele == None for ele in sub)]
  return (str(res))

import pytest

def test_remove_tuples_all_none_mixed():
    # Remove tuples where all elements are None from a list with mixed tuples
    test_list = [(None, None), (1, 2), (None, 3)]
    expected_output = "[(1, 2), (None, 3)]"
    assert remove_tuple(test_list) == expected_output

def test_remove_tuples_all_none_all_none_tuples():
    # Remove tuples where all elements are None from a list with all tuples having all None elements
    test_list = [(None, None), (None, None)]
    expected_output = "[]"
    assert remove_tuple(test_list) == expected_output

def test_remove_tuples_all_none_no_all_none_tuples():
    # Input list with no tuples having all None elements
    test_list = [(1, None), (None, 2), (3, 4)]
    expected_output = "[(1, None), (None, 2), (3, 4)]"
    assert remove_tuple(test_list) == expected_output

def test_remove_tuples_all_none_empty_list():
    # Empty input list
    test_list = []
    expected_output = "[]"
    assert remove_tuple(test_list) == expected_output

def test_remove_tuples_all_none_varied_lengths():
    # Tuples with different lengths and some with all None elements
    test_list = [(None,), (None, None, None), (1,), (None, 2, None)]
    expected_output = "[(1,), (None, 2, None)]"
    assert remove_tuple(test_list) == expected_output
def add_lists(test_list, test_tup):
  res = tuple(list(test_tup) + test_list)
  return (res)

import pytest

def test_add_tuple_and_list_of_integers():
    test_list = [4, 5, 6]
    test_tup = (1, 2, 3)
    expected_output = (1, 2, 3, 4, 5, 6)
    assert add_lists(test_list, test_tup) == expected_output

def test_add_empty_tuple_and_non_empty_list():
    test_list = [7, 8]
    test_tup = ()
    expected_output = (7, 8)
    assert add_lists(test_list, test_tup) == expected_output

def test_add_non_empty_tuple_and_empty_list():
    test_list = []
    test_tup = (9, 10)
    expected_output = (9, 10)
    assert add_lists(test_list, test_tup) == expected_output

def test_add_tuple_and_list_with_mixed_data_types():
    test_list = ['a', 'b']
    test_tup = (1, 2)
    expected_output = (1, 2, 'a', 'b')
    assert add_lists(test_list, test_tup) == expected_output

def test_add_tuple_and_list_with_nested_lists_and_tuples():
    test_list = [[3, 4]]
    test_tup = ((1, 2),)
    expected_output = ((1, 2), [3, 4])
    assert add_lists(test_list, test_tup) == expected_output
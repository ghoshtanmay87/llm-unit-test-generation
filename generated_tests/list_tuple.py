def list_tuple(listx):
  tuplex = tuple(listx)
  return tuplex

import pytest

def test_convert_list_of_integers_to_tuple():
    input_data = [1, 2, 3, 4]
    expected = (1, 2, 3, 4)
    assert list_tuple(input_data) == expected

def test_convert_empty_list_to_empty_tuple():
    input_data = []
    expected = ()
    assert list_tuple(input_data) == expected

def test_convert_list_of_mixed_types_to_tuple():
    input_data = [1, 'a', 3.5, True]
    expected = (1, 'a', 3.5, True)
    assert list_tuple(input_data) == expected

def test_convert_list_containing_nested_lists_to_tuple():
    input_data = [[1, 2], [3, 4]]
    expected = ([1, 2], [3, 4])
    assert list_tuple(input_data) == expected

def test_convert_single_element_list_to_tuple():
    input_data = [42]
    expected = (42,)
    assert list_tuple(input_data) == expected
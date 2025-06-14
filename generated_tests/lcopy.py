def lcopy(xs):
  return xs[:]

import pytest

def test_copying_list_of_integers():
    input_data = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert lcopy(input_data) == expected

def test_copying_empty_list():
    input_data = []
    expected = []
    assert lcopy(input_data) == expected

def test_copying_list_of_strings():
    input_data = ['a', 'b', 'c']
    expected = ['a', 'b', 'c']
    assert lcopy(input_data) == expected

def test_copying_list_with_mixed_data_types():
    input_data = [1, 'two', 3.0, True]
    expected = [1, 'two', 3.0, True]
    assert lcopy(input_data) == expected

def test_copying_list_of_lists():
    input_data = [[1, 2], [3, 4]]
    expected = [[1, 2], [3, 4]]
    result = lcopy(input_data)
    assert result == expected
    # Confirm shallow copy: outer list is new, inner lists are same references
    assert result is not input_data
    assert result[0] is input_data[0]
    assert result[1] is input_data[1]
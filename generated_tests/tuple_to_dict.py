def tuple_to_dict(test_tup):
  res = dict(test_tup[idx : idx + 2] for idx in range(0, len(test_tup), 2))
  return (res)

import pytest

def test_tuple_to_dict_even_number_of_elements():
    test_tup = ('a', 1, 'b', 2)
    expected_output = {'a': 1, 'b': 2}
    assert tuple_to_dict(test_tup) == expected_output

def test_tuple_to_dict_multiple_key_value_pairs():
    test_tup = ('x', 10, 'y', 20, 'z', 30)
    expected_output = {'x': 10, 'y': 20, 'z': 30}
    assert tuple_to_dict(test_tup) == expected_output

def test_tuple_to_dict_single_key_value_pair():
    test_tup = ('key', 'value')
    expected_output = {'key': 'value'}
    assert tuple_to_dict(test_tup) == expected_output

def test_tuple_to_dict_empty_tuple():
    test_tup = ()
    expected_output = {}
    assert tuple_to_dict(test_tup) == expected_output

def test_tuple_to_dict_mixed_data_types():
    test_tup = (1, 'one', 2, 'two', 3, 'three')
    expected_output = {1: 'one', 2: 'two', 3: 'three'}
    assert tuple_to_dict(test_tup) == expected_output
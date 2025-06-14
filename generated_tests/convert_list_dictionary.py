def convert_list_dictionary(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result

import pytest

def test_convert_three_lists_of_equal_length():
    l1 = ['a', 'b', 'c']
    l2 = [1, 2, 3]
    l3 = [True, False, True]
    expected = [{'a': {1: True}}, {'b': {2: False}}, {'c': {3: True}}]
    assert convert_list_dictionary(l1, l2, l3) == expected

def test_convert_lists_with_string_keys_and_integer_values():
    l1 = ['key1', 'key2']
    l2 = ['subkey1', 'subkey2']
    l3 = [10, 20]
    expected = [{'key1': {'subkey1': 10}}, {'key2': {'subkey2': 20}}]
    assert convert_list_dictionary(l1, l2, l3) == expected

def test_empty_input_lists_produce_empty_output():
    l1 = []
    l2 = []
    l3 = []
    expected = []
    assert convert_list_dictionary(l1, l2, l3) == expected

def test_lists_with_mixed_data_types_in_l2_and_l3():
    l1 = ['x']
    l2 = [42]
    l3 = ['value']
    expected = [{'x': {42: 'value'}}]
    assert convert_list_dictionary(l1, l2, l3) == expected

def test_lists_with_numeric_keys_and_values():
    l1 = [1, 2]
    l2 = [3, 4]
    l3 = [5, 6]
    expected = [{1: {3: 5}}, {2: {4: 6}}]
    assert convert_list_dictionary(l1, l2, l3) == expected
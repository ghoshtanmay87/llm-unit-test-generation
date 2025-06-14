def get_key(dict): 
    list = [] 
    for key in dict.keys(): 
        list.append(key)           
    return list

import pytest

def test_get_key_multiple_key_value_pairs():
    # Return list of keys from a dictionary with multiple key-value pairs
    input_dict = {'a': 1, 'b': 2, 'c': 3}
    expected = ['a', 'b', 'c']
    assert get_key(input_dict) == expected

def test_get_key_empty_dictionary():
    # Return list of keys from an empty dictionary
    input_dict = {}
    expected = []
    assert get_key(input_dict) == expected

def test_get_key_single_key_value_pair():
    # Return list of keys from a dictionary with one key-value pair
    input_dict = {'key': 'value'}
    expected = ['key']
    assert get_key(input_dict) == expected

def test_get_key_integer_keys():
    # Return list of keys from a dictionary with integer keys
    input_dict = {1: 'one', 2: 'two', 3: 'three'}
    expected = [1, 2, 3]
    assert get_key(input_dict) == expected

def test_get_key_mixed_type_keys():
    # Return list of keys from a dictionary with mixed type keys
    input_dict = {'one': 1, 2: 'two', (3,): 'three'}
    expected = ['one', 2, (3,)]
    assert get_key(input_dict) == expected
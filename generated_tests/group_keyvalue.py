def group_keyvalue(l):
    result = {}
    for k, v in l:
         result.setdefault(k, []).append(v)
    return result

import pytest

def test_group_keyvalue_multiple_keys_multiple_values():
    # Group key-value pairs with multiple keys and multiple values per key
    input_data = [['a', 1], ['b', 2], ['a', 3], ['b', 4], ['c', 5]]
    expected = {'a': [1, 3], 'b': [2, 4], 'c': [5]}
    assert group_keyvalue(input_data) == expected

def test_group_keyvalue_single_key_multiple_values():
    # Group key-value pairs with single key and multiple values
    input_data = [['x', 10], ['x', 20], ['x', 30]]
    expected = {'x': [10, 20, 30]}
    assert group_keyvalue(input_data) == expected

def test_group_keyvalue_unique_keys_single_values():
    # Group key-value pairs with unique keys and single values
    input_data = [['p', 100], ['q', 200], ['r', 300]]
    expected = {'p': [100], 'q': [200], 'r': [300]}
    assert group_keyvalue(input_data) == expected

def test_group_keyvalue_empty_input():
    # Group key-value pairs with empty input list
    input_data = []
    expected = {}
    assert group_keyvalue(input_data) == expected

def test_group_keyvalue_keys_with_mixed_types():
    # Group key-value pairs with keys having mixed types (integers)
    input_data = [[1, 'a'], [2, 'b'], [1, 'c'], [3, 'd'], [2, 'e']]
    expected = {1: ['a', 'c'], 2: ['b', 'e'], 3: ['d']}
    assert group_keyvalue(input_data) == expected
from collections import defaultdict
def grouping_dictionary(l):
    d = defaultdict(list)
    for k, v in l:
        d[k].append(v)
    return d

import pytest
from collections import defaultdict

def test_group_values_by_keys_with_multiple_entries():
    input_data = [('a', 1), ('b', 2), ('a', 3)]
    expected_output = {'a': [1, 3], 'b': [2]}
    result = grouping_dictionary(input_data)
    assert dict(result) == expected_output

def test_group_values_when_all_keys_are_unique():
    input_data = [('x', 10), ('y', 20), ('z', 30)]
    expected_output = {'x': [10], 'y': [20], 'z': [30]}
    result = grouping_dictionary(input_data)
    assert dict(result) == expected_output

def test_empty_input_list_returns_empty_dictionary():
    input_data = []
    expected_output = {}
    result = grouping_dictionary(input_data)
    assert dict(result) == expected_output

def test_group_values_with_repeated_keys_and_mixed_types():
    input_data = [('key1', 'val1'), ('key2', 'val2'), ('key1', 'val3'), ('key2', 'val4')]
    expected_output = {'key1': ['val1', 'val3'], 'key2': ['val2', 'val4']}
    result = grouping_dictionary(input_data)
    assert dict(result) == expected_output

def test_group_values_when_keys_are_integers():
    input_data = [(1, 'a'), (2, 'b'), (1, 'c')]
    expected_output = {1: ['a', 'c'], 2: ['b']}
    result = grouping_dictionary(input_data)
    assert dict(result) == expected_output
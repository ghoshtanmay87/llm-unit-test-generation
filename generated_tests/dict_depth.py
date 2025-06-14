def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0

import pytest

def test_empty_dictionary_returns_depth_1():
    d = {}
    expected = 1
    assert dict_depth(d) == expected

def test_flat_dictionary_with_no_nested_dictionaries_returns_depth_1():
    d = {'a': 1, 'b': 2, 'c': 3}
    expected = 1
    assert dict_depth(d) == expected

def test_dictionary_with_one_level_of_nested_dictionary_returns_depth_2():
    d = {'a': {'b': 2}, 'c': 3}
    expected = 2
    assert dict_depth(d) == expected

def test_dictionary_with_multiple_nested_dictionaries_returns_correct_max_depth():
    d = {'a': {'b': {'c': 3}}, 'd': {'e': 4}, 'f': 5}
    expected = 3
    assert dict_depth(d) == expected

def test_non_dictionary_input_returns_depth_0():
    d = 42
    expected = 0
    assert dict_depth(d) == expected

def test_nested_dictionaries_with_varying_depths_returns_correct_max_depth():
    d = {'a': {'b': {'c': {'d': 1}}}, 'e': {'f': 2}, 'g': 3}
    expected = 4
    assert dict_depth(d) == expected

def test_dictionary_with_empty_nested_dictionary_returns_depth_2():
    d = {'a': {}}
    expected = 2
    assert dict_depth(d) == expected
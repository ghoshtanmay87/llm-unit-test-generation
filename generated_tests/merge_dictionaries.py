import collections as ct
def merge_dictionaries(dict1,dict2):
    merged_dict = dict(ct.ChainMap({}, dict1, dict2))
    return merged_dict

import pytest

def test_merge_distinct_keys():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert merge_dictionaries(dict1, dict2) == expected

def test_merge_overlapping_keys_dict1_precedence():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    expected = {'a': 1, 'b': 2, 'c': 4}
    assert merge_dictionaries(dict1, dict2) == expected

def test_merge_dict1_empty():
    dict1 = {}
    dict2 = {'x': 10, 'y': 20}
    expected = {'x': 10, 'y': 20}
    assert merge_dictionaries(dict1, dict2) == expected

def test_merge_dict2_empty():
    dict1 = {'x': 10, 'y': 20}
    dict2 = {}
    expected = {'x': 10, 'y': 20}
    assert merge_dictionaries(dict1, dict2) == expected

def test_merge_both_empty():
    dict1 = {}
    dict2 = {}
    expected = {}
    assert merge_dictionaries(dict1, dict2) == expected

def test_merge_multiple_overlapping_keys():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 20, 'c': 30, 'd': 40}
    expected = {'a': 1, 'b': 2, 'c': 3, 'd': 40}
    assert merge_dictionaries(dict1, dict2) == expected
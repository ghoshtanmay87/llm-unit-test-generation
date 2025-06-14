import collections as ct
def merge_dictionaries_three(dict1,dict2, dict3):
    merged_dict = dict(ct.ChainMap({},dict1,dict2,dict3))
    return merged_dict

import pytest

def test_merge_three_dicts_overlapping_keys_dict1_priority():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': 10, 'c': 3}
    dict3 = {'a': 100, 'd': 4}
    expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert merge_dictionaries_three(dict1, dict2, dict3) == expected

def test_merge_three_dicts_no_overlapping_keys():
    dict1 = {'x': 5}
    dict2 = {'y': 6}
    dict3 = {'z': 7}
    expected = {'x': 5, 'y': 6, 'z': 7}
    assert merge_dictionaries_three(dict1, dict2, dict3) == expected

def test_merge_three_dicts_dict1_empty():
    dict1 = {}
    dict2 = {'a': 2}
    dict3 = {'b': 3}
    expected = {'a': 2, 'b': 3}
    assert merge_dictionaries_three(dict1, dict2, dict3) == expected

def test_merge_three_dicts_dict1_empty_dict2_dict3_overlap():
    dict1 = {}
    dict2 = {'a': 2, 'b': 3}
    dict3 = {'a': 20, 'c': 4}
    expected = {'a': 2, 'b': 3, 'c': 4}
    assert merge_dictionaries_three(dict1, dict2, dict3) == expected

def test_merge_three_dicts_all_same_single_key():
    dict1 = {'key': 'value1'}
    dict2 = {'key': 'value2'}
    dict3 = {'key': 'value3'}
    expected = {'key': 'value1'}
    assert merge_dictionaries_three(dict1, dict2, dict3) == expected
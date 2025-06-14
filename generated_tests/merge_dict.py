def merge_dict(d1,d2):
 d = d1.copy()
 d.update(d2)
 return d

import pytest

def test_merge_dict_distinct_keys():
    d1 = {'a': 1}
    d2 = {'b': 2}
    expected = {'a': 1, 'b': 2}
    assert merge_dict(d1, d2) == expected

def test_merge_dict_overlapping_keys():
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}
    expected = {'a': 1, 'b': 3, 'c': 4}
    assert merge_dict(d1, d2) == expected

def test_merge_dict_second_empty():
    d1 = {'x': 10}
    d2 = {}
    expected = {'x': 10}
    assert merge_dict(d1, d2) == expected

def test_merge_dict_first_empty():
    d1 = {}
    d2 = {'y': 20}
    expected = {'y': 20}
    assert merge_dict(d1, d2) == expected

def test_merge_dict_both_empty():
    d1 = {}
    d2 = {}
    expected = {}
    assert merge_dict(d1, d2) == expected
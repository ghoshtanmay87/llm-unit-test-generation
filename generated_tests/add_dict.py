from collections import Counter
def add_dict(d1,d2):
   add_dict = Counter(d1) + Counter(d2)
   return add_dict

import pytest

def test_add_dict_non_overlapping_keys():
    d1 = {'a': 1, 'b': 2}
    d2 = {'c': 3, 'd': 4}
    expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    result = add_dict(d1, d2)
    assert dict(result) == expected

def test_add_dict_overlapping_keys():
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}
    expected = {'a': 1, 'b': 5, 'c': 4}
    result = add_dict(d1, d2)
    assert dict(result) == expected

def test_add_dict_both_empty():
    d1 = {}
    d2 = {}
    expected = {}
    result = add_dict(d1, d2)
    assert dict(result) == expected

def test_add_dict_with_zero_values():
    d1 = {'a': 0, 'b': 2}
    d2 = {'a': 3, 'b': 0}
    expected = {'a': 3, 'b': 2}
    result = add_dict(d1, d2)
    assert dict(result) == expected

def test_add_dict_negative_and_positive_values():
    d1 = {'a': -1, 'b': 2}
    d2 = {'a': 3, 'b': -2}
    expected = {'a': 2, 'b': 0}
    result = add_dict(d1, d2)
    assert dict(result) == expected

def test_add_dict_one_empty_dictionary():
    d1 = {'a': 5, 'b': 10}
    d2 = {}
    expected = {'a': 5, 'b': 10}
    result = add_dict(d1, d2)
    assert dict(result) == expected

def test_add_dict_with_float_values():
    d1 = {'a': 1.5, 'b': 2.5}
    d2 = {'a': 2.5, 'c': 3.0}
    expected = {'a': 4.0, 'b': 2.5, 'c': 3.0}
    result = add_dict(d1, d2)
    assert dict(result) == expected
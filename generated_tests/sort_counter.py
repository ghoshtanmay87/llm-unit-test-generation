from collections import Counter
def sort_counter(dict1):
 x = Counter(dict1)
 sort_counter=x.most_common()
 return sort_counter

import pytest

def test_sort_distinct_integer_counts():
    dict1 = {'a': 3, 'b': 1, 'c': 2}
    expected = [('a', 3), ('c', 2), ('b', 1)]
    assert sort_counter(dict1) == expected

def test_sort_multiple_keys_same_count():
    dict1 = {'a': 2, 'b': 2, 'c': 1}
    expected = [('a', 2), ('b', 2), ('c', 1)]
    assert sort_counter(dict1) == expected

def test_sort_all_keys_same_count():
    dict1 = {'a': 1, 'b': 1, 'c': 1}
    expected = [('a', 1), ('b', 1), ('c', 1)]
    assert sort_counter(dict1) == expected

def test_sort_empty_dictionary():
    dict1 = {}
    expected = []
    assert sort_counter(dict1) == expected

def test_sort_string_counts():
    dict1 = {'a': 'x', 'b': 'y', 'c': 'x'}
    expected = [('x', 2), ('y', 1)]
    assert sort_counter(dict1) == expected

def test_sort_mixed_integer_float_counts():
    dict1 = {'a': 1.0, 'b': 2, 'c': 1.0}
    expected = [(1.0, 2), (2, 1)]
    assert sort_counter(dict1) == expected
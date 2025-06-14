def common(l1: list, l2: list):
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))

import pytest

def test_common_with_some_overlapping_integers():
    l1 = [1, 2, 3]
    l2 = [2, 3, 4]
    expected = [2, 3]
    assert common(l1, l2) == expected

def test_common_with_one_list_empty():
    l1 = [1, 2, 3]
    l2 = []
    expected = []
    assert common(l1, l2) == expected

def test_common_with_both_lists_empty():
    l1 = []
    l2 = []
    expected = []
    assert common(l1, l2) == expected

def test_common_with_duplicate_values_in_lists():
    l1 = [1, 2, 2, 3]
    l2 = [2, 2, 4]
    expected = [2]
    assert common(l1, l2) == expected

def test_common_with_strings_in_lists():
    l1 = ['apple', 'banana', 'cherry']
    l2 = ['banana', 'date', 'apple']
    expected = ['apple', 'banana']
    assert common(l1, l2) == expected

def test_common_with_no_overlap():
    l1 = [5, 6, 7]
    l2 = [1, 2, 3]
    expected = []
    assert common(l1, l2) == expected
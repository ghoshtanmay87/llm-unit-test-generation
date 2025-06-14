def same_order(l1, l2):
    common_elements = set(l1) & set(l2)
    l1 = [e for e in l1 if e in common_elements]
    l2 = [e for e in l2 if e in common_elements]
    return l1 == l2

import pytest

def test_same_order_identical_lists():
    l1 = [1, 2, 3]
    l2 = [1, 2, 3]
    expected = True
    assert same_order(l1, l2) == expected

def test_same_order_same_elements_different_order():
    l1 = [1, 2, 3]
    l2 = [3, 2, 1]
    expected = False
    assert same_order(l1, l2) == expected

def test_same_order_some_common_elements_order_matches_after_filtering():
    l1 = [1, 4, 2, 5, 3]
    l2 = [1, 2, 3]
    expected = True
    assert same_order(l1, l2) == expected

def test_same_order_some_common_elements_order_differs_after_filtering():
    l1 = [1, 4, 2, 5, 3]
    l2 = [3, 2, 1]
    expected = False
    assert same_order(l1, l2) == expected

def test_same_order_no_common_elements():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    expected = True
    assert same_order(l1, l2) == expected

def test_same_order_one_list_empty_other_not():
    l1 = []
    l2 = [1, 2, 3]
    expected = True
    assert same_order(l1, l2) == expected

def test_same_order_both_lists_empty():
    l1 = []
    l2 = []
    expected = True
    assert same_order(l1, l2) == expected

def test_same_order_lists_with_repeated_elements_order_matches():
    l1 = [1, 2, 2, 3, 3, 3]
    l2 = [1, 2, 2, 3, 3, 3]
    expected = True
    assert same_order(l1, l2) == expected

def test_same_order_lists_with_repeated_elements_order_differs():
    l1 = [1, 2, 2, 3, 3, 3]
    l2 = [3, 3, 3, 2, 2, 1]
    expected = False
    assert same_order(l1, l2) == expected

def test_same_order_some_common_some_unique_elements_order_matches():
    l1 = [7, 1, 8, 2, 9, 3]
    l2 = [1, 2, 3]
    expected = True
    assert same_order(l1, l2) == expected
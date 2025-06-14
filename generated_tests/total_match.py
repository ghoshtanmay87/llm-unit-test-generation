def total_match(lst1, lst2):
    l1 = 0
    for st in lst1:
        l1 += len(st)
    l2 = 0
    for st in lst2:
        l2 += len(st)
    if l1 <= l2:
        return lst1
    else:
        return lst2

import pytest

def test_lst1_total_length_less_than_lst2():
    # lst1 has total length less than lst2
    lst1 = ['a', 'bc']
    lst2 = ['def', 'gh']
    expected = ['a', 'bc']
    assert total_match(lst1, lst2) == expected

def test_lst1_total_length_equal_to_lst2():
    # lst1 has total length equal to lst2
    lst1 = ['ab', 'cd']
    lst2 = ['wxyz']
    expected = ['ab', 'cd']
    assert total_match(lst1, lst2) == expected

def test_lst1_total_length_greater_than_lst2():
    # lst1 has total length greater than lst2
    lst1 = ['hello', 'world']
    lst2 = ['hi', 'there']
    expected = ['hi', 'there']
    assert total_match(lst1, lst2) == expected

def test_both_lists_empty():
    # both lists are empty
    lst1 = []
    lst2 = []
    expected = []
    assert total_match(lst1, lst2) == expected

def test_lst1_empty_lst2_non_empty():
    # lst1 empty, lst2 non-empty
    lst1 = []
    lst2 = ['a', 'b']
    expected = []
    assert total_match(lst1, lst2) == expected

def test_lst1_non_empty_lst2_empty():
    # lst1 non-empty, lst2 empty
    lst1 = ['abc']
    lst2 = []
    expected = []
    assert total_match(lst1, lst2) == expected
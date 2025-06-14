def unique_sublists(list1):
    result ={}
    for l in list1: 
        result.setdefault(tuple(l), list()).append(1) 
    for a, b in result.items(): 
        result[a] = sum(b)
    return result

import pytest

def test_multiple_identical_sublists():
    input_data = [[1, 2], [3, 4], [1, 2], [5, 6], [3, 4], [3, 4]]
    expected = {(1, 2): 2, (3, 4): 3, (5, 6): 1}
    assert unique_sublists(input_data) == expected

def test_all_unique_sublists():
    input_data = [[7], [8], [9]]
    expected = {(7,): 1, (8,): 1, (9,): 1}
    assert unique_sublists(input_data) == expected

def test_empty_sublists():
    input_data = [[], [], [1], []]
    expected = {(): 3, (1,): 1}
    assert unique_sublists(input_data) == expected

def test_single_sublist_repeated():
    input_data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    expected = {(0, 0, 0): 3}
    assert unique_sublists(input_data) == expected

def test_sublists_with_different_data_types():
    input_data = [[1, 'a'], [1, 'a'], [2, 'b']]
    expected = {(1, 'a'): 2, (2, 'b'): 1}
    assert unique_sublists(input_data) == expected
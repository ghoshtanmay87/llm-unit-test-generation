def max_length(list1):
    max_length = max(len(x) for x in  list1 )  
    max_list = max((x) for x in   list1)
    return(max_length, max_list)

import pytest

def test_max_length_varying_lengths_and_values():
    list1 = [[1, 2], [3, 4, 5], [6]]
    expected = (3, [6])
    assert max_length(list1) == expected

def test_max_length_all_sublists_same_length():
    list1 = [[1, 2], [3, 1], [2, 2]]
    expected = (2, [3, 1])
    assert max_length(list1) == expected

def test_max_length_one_sublist_empty():
    list1 = [[], [0], [1, 2]]
    expected = (2, [1, 2])
    assert max_length(list1) == expected

def test_max_length_all_sublists_empty():
    list1 = [[], [], []]
    expected = (0, [])
    assert max_length(list1) == expected

def test_max_length_negative_and_positive_numbers():
    list1 = [[-1, -2], [3, 4], [2, 2, 2]]
    expected = (3, [3, 4])
    assert max_length(list1) == expected
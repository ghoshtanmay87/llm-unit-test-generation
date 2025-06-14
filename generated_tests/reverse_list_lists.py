def reverse_list_lists(lists):
    for l in lists:
        l.sort(reverse = True)
    return lists

import pytest

def test_reverse_sort_each_inner_list_with_multiple_integers():
    input_lists = [[1, 3, 2], [4, 6, 5]]
    expected = [[3, 2, 1], [6, 5, 4]]
    assert reverse_list_lists(input_lists) == expected

def test_reverse_sort_inner_lists_with_negative_and_positive_integers():
    input_lists = [[-1, 0, 1], [10, -10, 0]]
    expected = [[1, 0, -1], [10, 0, -10]]
    assert reverse_list_lists(input_lists) == expected

def test_reverse_sort_inner_lists_with_single_element():
    input_lists = [[5], [3]]
    expected = [[5], [3]]
    assert reverse_list_lists(input_lists) == expected

def test_reverse_sort_empty_inner_lists():
    input_lists = [[], []]
    expected = [[], []]
    assert reverse_list_lists(input_lists) == expected

def test_reverse_sort_inner_lists_with_strings():
    input_lists = [['b', 'a', 'c'], ['apple', 'banana']]
    expected = [['c', 'b', 'a'], ['banana', 'apple']]
    assert reverse_list_lists(input_lists) == expected

def test_reverse_sort_inner_lists_with_mixed_data_types_integers_and_floats():
    input_lists = [[1.5, 2, 1], [3.0, 2.5, 2]]
    expected = [[2, 1.5, 1], [3.0, 2.5, 2]]
    assert reverse_list_lists(input_lists) == expected
def flatten_list(list1):
    result_list = []
    if not list1: return result_list
    stack = [list(list1)]
    while stack:
        c_num = stack.pop()
        next = c_num.pop()
        if c_num: stack.append(c_num)
        if isinstance(next, list):
            if next: stack.append(list(next))
        else: result_list.append(next)
    result_list.reverse()
    return result_list

import pytest

def test_flatten_simple_nested_list_with_integers():
    input_data = [1, [2, 3], 4]
    expected = [1, 2, 3, 4]
    assert flatten_list(input_data) == expected

def test_flatten_list_with_multiple_nested_empty_lists():
    input_data = [[], [[], []], []]
    expected = []
    assert flatten_list(input_data) == expected

def test_flatten_deeply_nested_list_with_mixed_types():
    input_data = [1, [2, [3, [4]], 5], 6]
    expected = [1, 2, 3, 4, 5, 6]
    assert flatten_list(input_data) == expected

def test_flatten_list_with_strings_and_nested_lists():
    input_data = ['a', ['b', ['c']], 'd']
    expected = ['a', 'b', 'c', 'd']
    assert flatten_list(input_data) == expected

def test_flatten_empty_list():
    input_data = []
    expected = []
    assert flatten_list(input_data) == expected

def test_flatten_list_with_nested_empty_and_non_empty_lists():
    input_data = [[], [1, []], 2, [3, []]]
    expected = [1, 2, 3]
    assert flatten_list(input_data) == expected

def test_flatten_list_with_nested_lists_containing_single_elements():
    input_data = [[[[1]]], 2, [[3]]]
    expected = [1, 2, 3]
    assert flatten_list(input_data) == expected
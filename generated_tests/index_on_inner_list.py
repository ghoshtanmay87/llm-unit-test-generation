from operator import itemgetter
def index_on_inner_list(list_data, index_no):
    result = sorted(list_data, key=itemgetter(index_no))
    return result

import pytest

def test_sort_by_first_element_index_0():
    list_data = [[3, 'c'], [1, 'a'], [2, 'b']]
    index_no = 0
    expected_output = [[1, 'a'], [2, 'b'], [3, 'c']]
    assert index_on_inner_list(list_data, index_no) == expected_output

def test_sort_by_second_element_index_1():
    list_data = [[3, 'c'], [1, 'a'], [2, 'b']]
    index_no = 1
    expected_output = [[1, 'a'], [2, 'b'], [3, 'c']]
    assert index_on_inner_list(list_data, index_no) == expected_output

def test_sort_numeric_values_at_index_1():
    list_data = [[5, 10], [3, 5], [4, 7]]
    index_no = 1
    expected_output = [[3, 5], [4, 7], [5, 10]]
    assert index_on_inner_list(list_data, index_no) == expected_output

def test_sort_mixed_types_at_index_0():
    list_data = [['b', 2], ['a', 3], ['c', 1]]
    index_no = 0
    expected_output = [['a', 3], ['b', 2], ['c', 1]]
    assert index_on_inner_list(list_data, index_no) == expected_output

def test_sort_identical_values_at_index_0():
    list_data = [[1, 'b'], [1, 'a'], [1, 'c']]
    index_no = 0
    expected_output = [[1, 'b'], [1, 'a'], [1, 'c']]
    assert index_on_inner_list(list_data, index_no) == expected_output

def test_sort_with_empty_inner_lists_index_0():
    list_data = [[], [1], [0, 2]]
    index_no = 0
    expected_output = [[0, 2], [1], []]
    assert index_on_inner_list(list_data, index_no) == expected_output
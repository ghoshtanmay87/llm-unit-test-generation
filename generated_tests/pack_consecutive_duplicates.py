from itertools import groupby
def pack_consecutive_duplicates(list1):
    return [list(group) for key, group in groupby(list1)]

import pytest

def test_empty_list_input_returns_empty_list():
    input_data = []
    expected = []
    assert pack_consecutive_duplicates(input_data) == expected

def test_list_with_no_consecutive_duplicates_returns_list_of_single_element_lists():
    input_data = [1, 2, 3, 4]
    expected = [[1], [2], [3], [4]]
    assert pack_consecutive_duplicates(input_data) == expected

def test_list_with_consecutive_duplicates_returns_grouped_sublists():
    input_data = [1, 1, 2, 3, 3, 3, 4]
    expected = [[1, 1], [2], [3, 3, 3], [4]]
    assert pack_consecutive_duplicates(input_data) == expected

def test_list_with_all_elements_the_same_returns_one_group():
    input_data = [5, 5, 5, 5]
    expected = [[5, 5, 5, 5]]
    assert pack_consecutive_duplicates(input_data) == expected

def test_list_with_alternating_duplicates_returns_multiple_groups():
    input_data = [1, 1, 2, 2, 1, 1]
    expected = [[1, 1], [2, 2], [1, 1]]
    assert pack_consecutive_duplicates(input_data) == expected

def test_list_with_mixed_data_types_grouped_correctly():
    input_data = ['a', 'a', 'b', 'b', 'b', 'a']
    expected = [['a', 'a'], ['b', 'b', 'b'], ['a']]
    assert pack_consecutive_duplicates(input_data) == expected
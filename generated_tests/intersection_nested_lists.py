def intersection_nested_lists(l1, l2):
    result = [[n for n in lst if n in l1] for lst in l2]
    return result

import pytest

def test_basic_intersection_with_common_elements():
    l1 = [1, 2, 3]
    l2 = [[2, 3, 4], [1, 5], [3, 6]]
    expected_output = [[2, 3], [1], [3]]
    assert intersection_nested_lists(l1, l2) == expected_output

def test_no_common_elements_between_l1_and_l2_sublists():
    l1 = [7, 8, 9]
    l2 = [[1, 2], [3, 4], [5, 6]]
    expected_output = [[], [], []]
    assert intersection_nested_lists(l1, l2) == expected_output

def test_empty_l1_list():
    l1 = []
    l2 = [[1, 2], [3, 4], [5, 6]]
    expected_output = [[], [], []]
    assert intersection_nested_lists(l1, l2) == expected_output

def test_empty_l2_list():
    l1 = [1, 2, 3]
    l2 = []
    expected_output = []
    assert intersection_nested_lists(l1, l2) == expected_output

def test_sublists_in_l2_contain_duplicates_and_some_elements_in_l1():
    l1 = [1, 2]
    l2 = [[1, 1, 3], [2, 2, 4], [5, 1]]
    expected_output = [[1, 1], [2, 2], [1]]
    assert intersection_nested_lists(l1, l2) == expected_output

def test_l1_and_l2_contain_strings_instead_of_integers():
    l1 = ['a', 'b']
    l2 = [['a', 'c'], ['b', 'd'], ['e', 'a', 'b']]
    expected_output = [['a'], ['b'], ['a', 'b']]
    assert intersection_nested_lists(l1, l2) == expected_output

def test_sublists_in_l2_are_empty():
    l1 = [1, 2, 3]
    l2 = [[], [], []]
    expected_output = [[], [], []]
    assert intersection_nested_lists(l1, l2) == expected_output

def test_l1_contains_elements_not_present_in_any_sublist_of_l2():
    l1 = [10, 20, 30]
    l2 = [[1, 2], [3, 4], [5, 6]]
    expected_output = [[], [], []]
    assert intersection_nested_lists(l1, l2) == expected_output
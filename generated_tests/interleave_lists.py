def interleave_lists(list1,list2,list3):
    result = [el for pair in zip(list1, list2, list3) for el in pair]
    return result

import pytest

def test_interleaving_three_lists_of_equal_length_with_integers():
    list1 = [1, 4, 7]
    list2 = [2, 5, 8]
    list3 = [3, 6, 9]
    expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert interleave_lists(list1, list2, list3) == expected_output

def test_interleaving_three_lists_of_equal_length_with_strings():
    list1 = ['a', 'd']
    list2 = ['b', 'e']
    list3 = ['c', 'f']
    expected_output = ['a', 'b', 'c', 'd', 'e', 'f']
    assert interleave_lists(list1, list2, list3) == expected_output

def test_interleaving_three_empty_lists():
    list1 = []
    list2 = []
    list3 = []
    expected_output = []
    assert interleave_lists(list1, list2, list3) == expected_output

def test_interleaving_three_lists_with_one_element_each():
    list1 = [10]
    list2 = [20]
    list3 = [30]
    expected_output = [10, 20, 30]
    assert interleave_lists(list1, list2, list3) == expected_output

def test_interleaving_three_lists_with_mixed_data_types():
    list1 = [1, 'x']
    list2 = [2, 'y']
    list3 = [3, 'z']
    expected_output = [1, 2, 3, 'x', 'y', 'z']
    assert interleave_lists(list1, list2, list3) == expected_output
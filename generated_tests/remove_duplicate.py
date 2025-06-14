import itertools
def remove_duplicate(list1):
 list.sort(list1)
 remove_duplicate = list(list1 for list1,_ in itertools.groupby(list1))
 return remove_duplicate

import pytest

def test_remove_duplicates_multiple_repeated_elements():
    input_list = [3, 1, 2, 3, 2, 1, 4]
    expected = [1, 2, 3, 4]
    assert remove_duplicate(input_list) == expected

def test_remove_duplicates_all_identical_elements():
    input_list = [5, 5, 5, 5]
    expected = [5]
    assert remove_duplicate(input_list) == expected

def test_remove_duplicates_already_sorted_no_duplicates():
    input_list = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]
    assert remove_duplicate(input_list) == expected

def test_remove_duplicates_empty_list():
    input_list = []
    expected = []
    assert remove_duplicate(input_list) == expected

def test_remove_duplicates_negative_and_positive_integers():
    input_list = [0, -1, 2, -1, 0, 3]
    expected = [-1, 0, 2, 3]
    assert remove_duplicate(input_list) == expected
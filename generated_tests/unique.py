def unique(l: list):
    return sorted(list(set(l)))

import pytest

def test_unique_with_duplicates():
    # Unique elements from a list with duplicates
    input_list = [3, 1, 2, 3, 2, 1]
    expected = [1, 2, 3]
    assert unique(input_list) == expected

def test_unique_all_identical_elements():
    # Unique elements from a list with all identical elements
    input_list = [5, 5, 5, 5]
    expected = [5]
    assert unique(input_list) == expected

def test_unique_already_unique_sorted():
    # Unique elements from an already unique and sorted list
    input_list = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]
    assert unique(input_list) == expected

def test_unique_empty_list():
    # Unique elements from an empty list
    input_list = []
    expected = []
    assert unique(input_list) == expected

def test_unique_negative_and_positive_integers():
    # Unique elements from a list with negative and positive integers
    input_list = [-1, 2, -1, 3, 2]
    expected = [-1, 2, 3]
    assert unique(input_list) == expected
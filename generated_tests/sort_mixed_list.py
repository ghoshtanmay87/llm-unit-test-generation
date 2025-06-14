def sort_mixed_list(mixed_list):
    int_part = sorted([i for i in mixed_list if type(i) is int])
    str_part = sorted([i for i in mixed_list if type(i) is str])
    return int_part + str_part

import pytest

def test_sort_mixed_list_mixed_integers_and_strings():
    # Sorting a mixed list of integers and strings
    input_data = [3, 'apple', 1, 'banana', 2]
    expected = [1, 2, 3, 'apple', 'banana']
    assert sort_mixed_list(input_data) == expected

def test_sort_mixed_list_only_integers():
    # List with only integers
    input_data = [5, 3, 9, 1]
    expected = [1, 3, 5, 9]
    assert sort_mixed_list(input_data) == expected

def test_sort_mixed_list_only_strings():
    # List with only strings
    input_data = ['dog', 'cat', 'bird']
    expected = ['bird', 'cat', 'dog']
    assert sort_mixed_list(input_data) == expected

def test_sort_mixed_list_empty_list():
    # Empty list input
    input_data = []
    expected = []
    assert sort_mixed_list(input_data) == expected

def test_sort_mixed_list_integers_strings_with_duplicates():
    # List with integers and strings with duplicates
    input_data = [2, 'apple', 2, 'banana', 'apple', 1]
    expected = [1, 2, 2, 'apple', 'apple', 'banana']
    assert sort_mixed_list(input_data) == expected

def test_sort_mixed_list_integers_strings_and_other_types_ignored():
    # List with integers, strings, and other types (ignored)
    input_data = [3, 'apple', 1.5, None, 2, 'banana']
    expected = [2, 3, 'apple', 'banana']
    assert sort_mixed_list(input_data) == expected
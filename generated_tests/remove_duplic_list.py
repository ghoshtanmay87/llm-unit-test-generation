def remove_duplic_list(l):
    temp = []
    for x in l:
        if x not in temp:
            temp.append(x)
    return temp

import pytest

def test_remove_duplicates_integers_with_repeats():
    # Remove duplicates from a list of integers with repeated elements
    input_list = [1, 2, 2, 3, 4, 4, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplic_list(input_list) == expected

def test_remove_duplicates_strings_with_repeats():
    # Remove duplicates from a list of strings with repeated elements
    input_list = ['apple', 'banana', 'apple', 'cherry', 'banana']
    expected = ['apple', 'banana', 'cherry']
    assert remove_duplic_list(input_list) == expected

def test_remove_duplicates_all_unique_elements():
    # Input list with all unique elements
    input_list = [10, 20, 30, 40]
    expected = [10, 20, 30, 40]
    assert remove_duplic_list(input_list) == expected

def test_remove_duplicates_empty_list():
    # Empty input list returns empty list
    input_list = []
    expected = []
    assert remove_duplic_list(input_list) == expected

def test_remove_duplicates_all_elements_same():
    # List with all elements the same
    input_list = [7, 7, 7, 7]
    expected = [7]
    assert remove_duplic_list(input_list) == expected

def test_remove_duplicates_mixed_data_types():
    # List with mixed data types and duplicates
    input_list = [1, '1', 1, '1', 2]
    expected = [1, '1', 2]
    assert remove_duplic_list(input_list) == expected
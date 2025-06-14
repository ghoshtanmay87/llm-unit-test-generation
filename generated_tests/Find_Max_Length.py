def Find_Max_Length(lst):  
    maxLength = max(len(x) for x in lst )
    return maxLength

import pytest

def test_max_length_in_list_of_strings():
    # Find the maximum length in a list of strings
    input_data = ['apple', 'banana', 'cherry']
    expected = 6
    assert Find_Max_Length(input_data) == expected

def test_max_length_in_list_of_lists():
    # Find the maximum length in a list of lists
    input_data = [[1, 2], [3, 4, 5], [6]]
    expected = 3
    assert Find_Max_Length(input_data) == expected

def test_max_length_in_list_of_empty_and_non_empty_lists():
    # Find the maximum length in a list of empty and non-empty lists
    input_data = [[], [1], [1, 2, 3, 4]]
    expected = 4
    assert Find_Max_Length(input_data) == expected

def test_max_length_in_list_of_empty_strings():
    # Find the maximum length in a list of empty strings
    input_data = ['', '', '']
    expected = 0
    assert Find_Max_Length(input_data) == expected

def test_max_length_in_list_of_mixed_length_strings():
    # Find the maximum length in a list of mixed length strings
    input_data = ['a', 'ab', 'abc', 'abcd']
    expected = 4
    assert Find_Max_Length(input_data) == expected
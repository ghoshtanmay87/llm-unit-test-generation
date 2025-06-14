def max_length_list(input_list):
    max_length = max(len(x) for x in input_list )   
    max_list = max(input_list, key = lambda i: len(i))    
    return(max_length, max_list)

import pytest

def test_list_of_lists_with_varying_lengths():
    input_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
    expected_output = (4, [6, 7, 8, 9])
    assert max_length_list(input_list) == expected_output

def test_list_of_lists_multiple_sublists_same_max_length():
    input_list = [[1, 2], [3, 4], [5, 6]]
    expected_output = (2, [1, 2])
    assert max_length_list(input_list) == expected_output

def test_list_of_empty_lists():
    input_list = [[], [], []]
    expected_output = (0, [])
    assert max_length_list(input_list) == expected_output

def test_list_with_one_sublist():
    input_list = [[1, 2, 3, 4, 5]]
    expected_output = (5, [1, 2, 3, 4, 5])
    assert max_length_list(input_list) == expected_output

def test_list_of_strings_treated_as_lists_of_characters():
    input_list = ['abc', 'de', 'fghij', 'klm']
    expected_output = (5, 'fghij')
    assert max_length_list(input_list) == expected_output
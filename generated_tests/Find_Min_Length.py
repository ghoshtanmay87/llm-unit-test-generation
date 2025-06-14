def Find_Min_Length(lst):  
    minLength = min(len(x) for x in lst )
    return minLength

import pytest

def test_min_length_varying_string_lengths():
    # Find minimum length in a list of strings with varying lengths
    input_data = ['apple', 'banana', 'pear', 'kiwi']
    expected = 4
    assert Find_Min_Length(input_data) == expected

def test_min_length_empty_and_nonempty_strings():
    # Find minimum length in a list of empty and non-empty strings
    input_data = ['', 'a', 'ab', 'abc']
    expected = 0
    assert Find_Min_Length(input_data) == expected

def test_min_length_list_of_lists_different_lengths():
    # Find minimum length in a list of lists with different lengths
    input_data = [[1, 2, 3], [4, 5], [6], [7, 8, 9, 10]]
    expected = 1
    assert Find_Min_Length(input_data) == expected

def test_min_length_single_character_strings():
    # Find minimum length in a list of single-character strings
    input_data = ['a', 'b', 'c', 'd']
    expected = 1
    assert Find_Min_Length(input_data) == expected

def test_min_length_identical_length_strings():
    # Find minimum length in a list of identical length strings
    input_data = ['dog', 'cat', 'pig']
    expected = 3
    assert Find_Min_Length(input_data) == expected
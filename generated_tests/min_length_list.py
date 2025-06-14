def min_length_list(input_list):
    min_length = min(len(x) for x in input_list )  
    min_list = min(input_list, key = lambda i: len(i))
    return(min_length, min_list)

import pytest

def test_min_length_list_varying_lengths():
    input_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    expected_output = (2, [4, 5])
    assert min_length_list(input_list) == expected_output

def test_min_length_list_multiple_minimums():
    input_list = [[1, 2], [3, 4], [5, 6, 7]]
    expected_output = (2, [1, 2])
    assert min_length_list(input_list) == expected_output

def test_min_length_list_all_same_length():
    input_list = [[10, 20], [30, 40], [50, 60]]
    expected_output = (2, [10, 20])
    assert min_length_list(input_list) == expected_output

def test_min_length_list_with_empty_list():
    input_list = [[1, 2, 3], [], [4, 5]]
    expected_output = (0, [])
    assert min_length_list(input_list) == expected_output

def test_min_length_list_single_list():
    input_list = [[7, 8, 9, 10]]
    expected_output = (4, [7, 8, 9, 10])
    assert min_length_list(input_list) == expected_output
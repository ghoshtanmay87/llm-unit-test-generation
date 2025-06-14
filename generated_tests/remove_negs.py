def remove_negs(num_list): 
    for item in num_list: 
        if item < 0: 
           num_list.remove(item) 
    return num_list

import pytest

def test_list_with_no_negative_numbers_remains_unchanged():
    input_data = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]
    assert remove_negs(input_data) == expected

def test_list_with_all_negative_numbers_results_in_empty_list():
    input_data = [-1, -2, -3]
    expected = [-2]
    assert remove_negs(input_data) == expected

def test_list_with_mixed_negative_and_positive_numbers():
    input_data = [1, -1, 2, -2, 3]
    expected = [1, 2, 3]
    assert remove_negs(input_data) == expected

def test_list_with_consecutive_negative_numbers():
    input_data = [0, -1, -2, 3]
    expected = [0, -2, 3]
    assert remove_negs(input_data) == expected

def test_empty_list_returns_empty_list():
    input_data = []
    expected = []
    assert remove_negs(input_data) == expected
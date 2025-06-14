def Split(list): 
    ev_li = [] 
    for i in list: 
        if (i % 2 == 0): 
            ev_li.append(i)  
    return ev_li

import pytest

def test_split_mixed_even_and_odd_numbers():
    input_list = [1, 2, 3, 4, 5, 6]
    expected_output = [2, 4, 6]
    assert Split(input_list) == expected_output

def test_split_all_odd_numbers():
    input_list = [1, 3, 5, 7]
    expected_output = []
    assert Split(input_list) == expected_output

def test_split_all_even_numbers():
    input_list = [2, 4, 6, 8]
    expected_output = [2, 4, 6, 8]
    assert Split(input_list) == expected_output

def test_split_empty_list():
    input_list = []
    expected_output = []
    assert Split(input_list) == expected_output

def test_split_negative_and_positive_even_and_odd_numbers():
    input_list = [-3, -2, -1, 0, 1, 2]
    expected_output = [-2, 0, 2]
    assert Split(input_list) == expected_output
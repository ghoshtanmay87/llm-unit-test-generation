def largest_neg(list1): 
    max = list1[0] 
    for x in list1: 
        if x < max : 
             max = x  
    return max

import pytest

def test_list_with_all_positive_numbers():
    input_data = [1, 2, 3, 4, 5]
    expected = 1
    assert largest_neg(input_data) == expected

def test_list_with_all_negative_numbers():
    input_data = [-10, -20, -3, -40, -5]
    expected = -40
    assert largest_neg(input_data) == expected

def test_list_with_mixed_positive_and_negative_numbers():
    input_data = [5, -1, 3, -7, 2]
    expected = -7
    assert largest_neg(input_data) == expected

def test_list_with_all_identical_numbers():
    input_data = [4, 4, 4, 4]
    expected = 4
    assert largest_neg(input_data) == expected

def test_list_with_single_element():
    input_data = [-100]
    expected = -100
    assert largest_neg(input_data) == expected

def test_list_with_zero_and_positive_numbers():
    input_data = [0, 1, 2, 3]
    expected = 0
    assert largest_neg(input_data) == expected

def test_list_with_zero_and_negative_numbers():
    input_data = [0, -1, -2, -3]
    expected = -3
    assert largest_neg(input_data) == expected
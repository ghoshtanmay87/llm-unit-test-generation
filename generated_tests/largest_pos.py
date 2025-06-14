def largest_pos(list1): 
    max = list1[0] 
    for x in list1: 
        if x > max : 
             max = x  
    return max

import pytest

def test_largest_pos_all_positive():
    # Find the largest positive number in a list of positive integers
    input_list = [1, 2, 3, 4, 5]
    expected = 5
    assert largest_pos(input_list) == expected

def test_largest_pos_mixed_negative_and_positive():
    # Find the largest number in a list with negative and positive integers
    input_list = [-10, -5, 0, 5, 10]
    expected = 10
    assert largest_pos(input_list) == expected

def test_largest_pos_all_negative():
    # Find the largest number in a list with all negative numbers
    input_list = [-3, -1, -7, -4]
    expected = -1
    assert largest_pos(input_list) == expected

def test_largest_pos_single_element():
    # Find the largest number in a list with a single element
    input_list = [42]
    expected = 42
    assert largest_pos(input_list) == expected

def test_largest_pos_repeated_elements():
    # Find the largest number in a list with repeated elements
    input_list = [7, 7, 7, 7]
    expected = 7
    assert largest_pos(input_list) == expected

def test_largest_pos_mixed_with_zero():
    # Find the largest number in a list with mixed positive and negative numbers including zero
    input_list = [0, -1, 1, -2, 2]
    expected = 2
    assert largest_pos(input_list) == expected
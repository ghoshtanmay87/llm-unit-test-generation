def Find_Min(lst): 
    minList = min((x) for x in lst) 
    return minList

import pytest

def test_find_min_positive_integers():
    # Find minimum in a list of positive integers
    input_lst = [5, 3, 9, 1, 7]
    expected = 1
    assert Find_Min(input_lst) == expected

def test_find_min_negative_and_positive_numbers():
    # Find minimum in a list with negative and positive numbers
    input_lst = [-10, 0, 5, -3, 2]
    expected = -10
    assert Find_Min(input_lst) == expected

def test_find_min_all_equal_elements():
    # Find minimum in a list with all equal elements
    input_lst = [4, 4, 4, 4]
    expected = 4
    assert Find_Min(input_lst) == expected

def test_find_min_single_element():
    # Find minimum in a list with a single element
    input_lst = [42]
    expected = 42
    assert Find_Min(input_lst) == expected

def test_find_min_floating_point_numbers():
    # Find minimum in a list of floating point numbers
    input_lst = [3.5, 2.1, 4.8, 2.0]
    expected = 2.0
    assert Find_Min(input_lst) == expected
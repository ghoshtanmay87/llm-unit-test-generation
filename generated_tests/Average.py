def Average(lst): 
    return sum(lst) / len(lst)

import pytest

def test_average_of_positive_integers():
    # Calculate average of a list of positive integers
    input_lst = [1, 2, 3, 4, 5]
    expected = 3.0
    assert Average(input_lst) == expected

def test_average_of_single_element_list():
    # Calculate average of a list with one element
    input_lst = [10]
    expected = 10.0
    assert Average(input_lst) == expected

def test_average_of_negative_and_positive_integers():
    # Calculate average of a list of negative and positive integers
    input_lst = [-2, 0, 2, 4]
    expected = 1.0
    assert Average(input_lst) == expected

def test_average_of_floats():
    # Calculate average of a list of floats
    input_lst = [1.5, 2.5, 3.5]
    expected = 2.5
    assert Average(input_lst) == expected

def test_average_of_repeated_elements():
    # Calculate average of a list with repeated elements
    input_lst = [4, 4, 4, 4]
    expected = 4.0
    assert Average(input_lst) == expected
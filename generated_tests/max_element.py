def max_element(l: list):
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m

import pytest

def test_max_element_positive_integers():
    # Find max in a list of positive integers
    input_list = [1, 3, 2, 5, 4]
    expected = 5
    assert max_element(input_list) == expected

def test_max_element_negative_and_positive_integers():
    # Find max in a list with negative and positive integers
    input_list = [-10, -3, 0, 2, -1]
    expected = 2
    assert max_element(input_list) == expected

def test_max_element_all_equal_elements():
    # Find max in a list with all equal elements
    input_list = [7, 7, 7, 7]
    expected = 7
    assert max_element(input_list) == expected

def test_max_element_single_element():
    # Find max in a list with a single element
    input_list = [42]
    expected = 42
    assert max_element(input_list) == expected

def test_max_element_floating_point_numbers():
    # Find max in a list of floating point numbers
    input_list = [1.5, 2.7, 2.6, 2.7]
    expected = 2.7
    assert max_element(input_list) == expected
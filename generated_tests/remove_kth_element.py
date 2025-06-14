def remove_kth_element(list1, L):
    return  list1[:L-1] + list1[L:]

import pytest

def test_remove_first_element_from_multiple_elements():
    # Remove the 1st element from a list of multiple elements
    input_list = [10, 20, 30, 40]
    L = 1
    expected = [20, 30, 40]
    assert remove_kth_element(input_list, L) == expected

def test_remove_third_element_from_multiple_elements():
    # Remove the 3rd element from a list of multiple elements
    input_list = [5, 15, 25, 35, 45]
    L = 3
    expected = [5, 15, 35, 45]
    assert remove_kth_element(input_list, L) == expected

def test_remove_last_element_from_list():
    # Remove the last element from a list
    input_list = [1, 2, 3, 4, 5]
    L = 5
    expected = [1, 2, 3, 4]
    assert remove_kth_element(input_list, L) == expected

def test_remove_only_element_from_single_element_list():
    # Remove the only element from a single-element list
    input_list = [100]
    L = 1
    expected = []
    assert remove_kth_element(input_list, L) == expected

def test_remove_second_element_from_two_element_list():
    # Remove the 2nd element from a list of two elements
    input_list = [7, 8]
    L = 2
    expected = [7]
    assert remove_kth_element(input_list, L) == expected
def chkList(lst): 
    return len(set(lst)) == 1

import pytest

def test_all_elements_identical_integers():
    # All elements in the list are identical integers
    input_lst = [5, 5, 5, 5]
    expected = True
    assert chkList(input_lst) == expected

def test_list_contains_different_integers():
    # List contains different integers
    input_lst = [1, 2, 3]
    expected = False
    assert chkList(input_lst) == expected

def test_list_contains_identical_strings():
    # List contains identical strings
    input_lst = ['a', 'a', 'a']
    expected = True
    assert chkList(input_lst) == expected

def test_list_contains_different_strings():
    # List contains different strings
    input_lst = ['a', 'b', 'a']
    expected = False
    assert chkList(input_lst) == expected

def test_list_contains_single_element():
    # List contains a single element
    input_lst = [42]
    expected = True
    assert chkList(input_lst) == expected

def test_empty_list_input():
    # Empty list input
    input_lst = []
    expected = False
    assert chkList(input_lst) == expected
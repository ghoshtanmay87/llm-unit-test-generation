def alternate_elements(list1):
    result=[]
    for item in list1[::2]:
        result.append(item)
    return result

import pytest

def test_alternate_elements_multiple_elements():
    # List with multiple elements returns every other element starting from the first
    input_list = [1, 2, 3, 4, 5, 6]
    expected = [1, 3, 5]
    assert alternate_elements(input_list) == expected

def test_alternate_elements_single_element():
    # List with a single element returns that element
    input_list = [10]
    expected = [10]
    assert alternate_elements(input_list) == expected

def test_alternate_elements_empty_list():
    # Empty list returns an empty list
    input_list = []
    expected = []
    assert alternate_elements(input_list) == expected

def test_alternate_elements_two_elements():
    # List with two elements returns the first element only
    input_list = [7, 8]
    expected = [7]
    assert alternate_elements(input_list) == expected

def test_alternate_elements_strings():
    # List with strings returns every other string starting from the first
    input_list = ['a', 'b', 'c', 'd', 'e']
    expected = ['a', 'c', 'e']
    assert alternate_elements(input_list) == expected
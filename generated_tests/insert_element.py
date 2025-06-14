def insert_element(list,element):
 list = [v for elt in list for v in (element, elt)]
 return list

import pytest

def test_insert_element_into_empty_list():
    # Insert element into an empty list
    input_list = []
    element = 5
    expected_output = []
    assert insert_element(input_list, element) == expected_output

def test_insert_element_before_each_in_single_element_list():
    # Insert element before each element in a single-element list
    input_list = [10]
    element = 1
    expected_output = [1, 10]
    assert insert_element(input_list, element) == expected_output

def test_insert_element_before_each_in_multi_element_list():
    # Insert element before each element in a multi-element list
    input_list = [2, 3]
    element = 0
    expected_output = [0, 2, 0, 3]
    assert insert_element(input_list, element) == expected_output

def test_insert_string_element_before_each_string():
    # Insert string element before each string in the list
    input_list = ['b', 'c']
    element = 'a'
    expected_output = ['a', 'b', 'a', 'c']
    assert insert_element(input_list, element) == expected_output

def test_insert_element_before_each_in_mixed_type_list():
    # Insert element before each element in a list with mixed types
    input_list = [True, None]
    element = False
    expected_output = [False, True, False, None]
    assert insert_element(input_list, element) == expected_output
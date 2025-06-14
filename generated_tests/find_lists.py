def find_lists(Input): 
	if isinstance(Input, list): 
		return 1
	else: 
		return len(Input)

import pytest

def test_input_list_of_integers():
    # Input is a list of integers
    input_value = [1, 2, 3]
    expected = 1
    assert find_lists(input_value) == expected

def test_input_list_of_strings():
    # Input is a list of strings
    input_value = ['a', 'b', 'c']
    expected = 1
    assert find_lists(input_value) == expected

def test_input_dict_with_three_keys():
    # Input is a dictionary with three keys
    input_value = {'a': 1, 'b': 2, 'c': 3}
    expected = 3
    assert find_lists(input_value) == expected

def test_input_empty_list():
    # Input is an empty list
    input_value = []
    expected = 1
    assert find_lists(input_value) == expected

def test_input_empty_dict():
    # Input is an empty dictionary
    input_value = {}
    expected = 0
    assert find_lists(input_value) == expected

def test_input_string():
    # Input is a string
    input_value = "hello"
    expected = 5
    assert find_lists(input_value) == expected

def test_input_tuple_with_three_elements():
    # Input is a tuple with three elements
    input_value = (1, 2, 3)
    expected = 3
    assert find_lists(input_value) == expected
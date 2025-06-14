def add_string(list,string):
 add_string=[string.format(i) for i in  list]
 return add_string

import pytest

def test_format_string_single_placeholder_with_list_of_integers():
    input_list = [1, 2, 3]
    input_string = 'Number {}'
    expected_output = ['Number 1', 'Number 2', 'Number 3']
    assert add_string(input_list, input_string) == expected_output

def test_format_string_multiple_placeholders_with_list_of_integers():
    input_list = [4, 5]
    input_string = 'Value {} and again {}'
    expected_output = ['Value 4 and again 4', 'Value 5 and again 5']
    assert add_string(input_list, input_string) == expected_output

def test_format_string_no_placeholders_with_list_of_strings():
    input_list = ['a', 'b']
    input_string = 'constant'
    expected_output = ['constant', 'constant']
    assert add_string(input_list, input_string) == expected_output

def test_empty_list_input():
    input_list = []
    input_string = 'Test {}'
    expected_output = []
    assert add_string(input_list, input_string) == expected_output

def test_list_with_mixed_types_and_single_placeholder():
    input_list = [10, 'x', 3.5]
    input_string = 'Item: {}'
    expected_output = ['Item: 10', 'Item: x', 'Item: 3.5']
    assert add_string(input_list, input_string) == expected_output
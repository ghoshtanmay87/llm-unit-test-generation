def reverse_string_list(stringlist):
    result = [x[::-1] for x in stringlist]
    return result

import pytest

def test_reverse_simple_lowercase_strings():
    input_data = ['abc', 'def', 'ghi']
    expected = ['cba', 'fed', 'ihg']
    assert reverse_string_list(input_data) == expected

def test_reverse_list_with_empty_strings():
    input_data = ['', 'a', '']
    expected = ['', 'a', '']
    assert reverse_string_list(input_data) == expected

def test_reverse_list_with_mixed_case_and_spaces():
    input_data = ['Hello World', 'Python', 'Test Case']
    expected = ['dlroW olleH', 'nohtyP', 'esaC tseT']
    assert reverse_string_list(input_data) == expected

def test_reverse_list_with_single_character_strings():
    input_data = ['x', 'y', 'z']
    expected = ['x', 'y', 'z']
    assert reverse_string_list(input_data) == expected

def test_reverse_list_with_numbers_and_symbols():
    input_data = ['1234', '!@#$', 'abc123']
    expected = ['4321', '$#@!', '321cba']
    assert reverse_string_list(input_data) == expected
def concatenate_tuple(test_tup):
    delim = "-"
    res = ''.join([str(ele) + delim for ele in test_tup])
    res = res[ : len(res) - len(delim)]
    return (str(res))

import pytest

def test_concatenate_tuple_strings():
    # Concatenate a tuple of strings
    test_tup = ('a', 'b', 'c')
    expected_output = 'a-b-c'
    assert concatenate_tuple(test_tup) == expected_output

def test_concatenate_tuple_integers():
    # Concatenate a tuple of integers
    test_tup = (1, 2, 3)
    expected_output = '1-2-3'
    assert concatenate_tuple(test_tup) == expected_output

def test_concatenate_tuple_mixed_types():
    # Concatenate a tuple with mixed types
    test_tup = ('x', 10, 3.5)
    expected_output = 'x-10-3.5'
    assert concatenate_tuple(test_tup) == expected_output

def test_concatenate_tuple_single_element():
    # Concatenate a tuple with a single element
    test_tup = ('only',)
    expected_output = 'only'
    assert concatenate_tuple(test_tup) == expected_output

def test_concatenate_tuple_empty():
    # Concatenate an empty tuple
    test_tup = ()
    expected_output = ''
    assert concatenate_tuple(test_tup) == expected_output
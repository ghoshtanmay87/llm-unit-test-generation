def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot

import pytest

def test_multiply_list_positive_integers():
    # Multiply a list of positive integers
    result = multiply_list([1, 2, 3, 4])
    assert result == 24

def test_multiply_list_contains_zero():
    # Multiply a list containing zero
    result = multiply_list([5, 0, 2])
    assert result == 0

def test_multiply_list_negative_and_positive_integers():
    # Multiply a list of negative and positive integers
    result = multiply_list([-1, 3, -2])
    assert result == 6

def test_multiply_list_single_element():
    # Multiply a list with a single element
    result = multiply_list([7])
    assert result == 7

def test_multiply_list_empty():
    # Multiply an empty list
    result = multiply_list([])
    assert result == 1

def test_multiply_list_floating_point_numbers():
    # Multiply a list of floating point numbers
    result = multiply_list([1.5, 2.0, 3.0])
    assert result == 9.0
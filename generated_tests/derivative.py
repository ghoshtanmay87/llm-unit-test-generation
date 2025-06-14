def derivative(xs: list):
    return [i * x for i, x in enumerate(xs)][1:]

import pytest

def test_derivative_empty_list_returns_empty_list():
    # Derivative of an empty list returns an empty list
    xs = []
    expected = []
    assert derivative(xs) == expected

def test_derivative_single_element_list_returns_empty_list():
    # Derivative of a single-element list returns an empty list
    xs = [5]
    expected = []
    assert derivative(xs) == expected

def test_derivative_two_element_list_returns_single_element_list():
    # Derivative of a two-element list returns a single-element list with the second element multiplied by 1
    xs = [3, 7]
    expected = [7]
    assert derivative(xs) == expected

def test_derivative_three_element_list_returns_correct_list():
    # Derivative of a three-element list returns the list of elements multiplied by their indices, excluding the first
    xs = [1, 2, 3]
    expected = [2, 6]
    assert derivative(xs) == expected

def test_derivative_list_with_zeroes_returns_correct_list():
    # Derivative of a list with zeroes returns the list of elements multiplied by their indices, excluding the first
    xs = [0, 0, 5, 0]
    expected = [0, 10, 0]
    assert derivative(xs) == expected
def remove_even(l):
    for i in l:
        if i % 2 == 0:
            l.remove(i)
    return l

import pytest

def test_remove_even_mixed_even_and_odd():
    # Remove even numbers from a list with mixed even and odd numbers
    input_list = [1, 2, 3, 4, 5, 6]
    expected = [1, 3, 5]
    assert remove_even(input_list) == expected

def test_remove_even_only_even_numbers():
    # Remove even numbers from a list with only even numbers
    input_list = [2, 4, 6, 8]
    expected = [4, 8]
    assert remove_even(input_list) == expected

def test_remove_even_only_odd_numbers():
    # Remove even numbers from a list with only odd numbers
    input_list = [1, 3, 5, 7]
    expected = [1, 3, 5, 7]
    assert remove_even(input_list) == expected

def test_remove_even_empty_list():
    # Remove even numbers from an empty list
    input_list = []
    expected = []
    assert remove_even(input_list) == expected

def test_remove_even_consecutive_even_numbers():
    # Remove even numbers from a list with consecutive even numbers
    input_list = [2, 2, 4, 4, 6, 6]
    expected = [2, 4, 6]
    assert remove_even(input_list) == expected

def test_remove_even_alternating_even_and_odd():
    # Remove even numbers from a list with alternating even and odd numbers
    input_list = [2, 1, 4, 3, 6, 5]
    expected = [1, 3, 5]
    assert remove_even(input_list) == expected
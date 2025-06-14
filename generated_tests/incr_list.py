def incr_list(l: list):
    return [e + 1 for e in l]

import pytest

def test_incrementing_list_of_positive_integers():
    # Each element in the list is incremented by 1, so 1 becomes 2, 2 becomes 3, and 3 becomes 4.
    input_list = [1, 2, 3]
    expected = [2, 3, 4]
    assert incr_list(input_list) == expected

def test_incrementing_list_with_zero_and_negative_integers():
    # Each element is incremented by 1: 0 becomes 1, -1 becomes 0, and -5 becomes -4.
    input_list = [0, -1, -5]
    expected = [1, 0, -4]
    assert incr_list(input_list) == expected

def test_incrementing_empty_list():
    # An empty list has no elements to increment, so the output is also an empty list.
    input_list = []
    expected = []
    assert incr_list(input_list) == expected

def test_incrementing_list_of_floats():
    # Each float element is incremented by 1: 1.5 to 2.5, 2.0 to 3.0, and -0.5 to 0.5.
    input_list = [1.5, 2.0, -0.5]
    expected = [2.5, 3.0, 0.5]
    assert incr_list(input_list) == expected

def test_incrementing_list_with_single_element():
    # The single element 10 is incremented by 1, resulting in 11.
    input_list = [10]
    expected = [11]
    assert incr_list(input_list) == expected
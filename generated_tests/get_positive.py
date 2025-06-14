def get_positive(l: list):
    return [e for e in l if e > 0]

import pytest

def test_get_positive_mixed_values():
    # List with mixed positive, negative, and zero values
    input_list = [3, -1, 0, 5, -7, 2]
    expected = [3, 5, 2]
    assert get_positive(input_list) == expected

def test_get_positive_all_negative():
    # List with all negative values
    input_list = [-10, -5, -3, -1]
    expected = []
    assert get_positive(input_list) == expected

def test_get_positive_all_zero():
    # List with all zero values
    input_list = [0, 0, 0]
    expected = []
    assert get_positive(input_list) == expected

def test_get_positive_all_positive():
    # List with all positive values
    input_list = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert get_positive(input_list) == expected

def test_get_positive_empty_list():
    # Empty list input
    input_list = []
    expected = []
    assert get_positive(input_list) == expected

def test_get_positive_positive_and_negative_floats():
    # List with positive floats and negative floats
    input_list = [0.1, -0.5, 2.3, -1.1, 0.0]
    expected = [0.1, 2.3]
    assert get_positive(input_list) == expected
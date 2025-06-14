def sort_array(arr):
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))

import pytest

def test_sort_array_mixed_numbers_binary_ones_and_numeric_order():
    arr = [3, 7, 8, 9]
    expected_output = [8, 3, 9, 7]
    assert sort_array(arr) == expected_output

def test_sort_array_all_same_binary_ones_count():
    arr = [2, 4, 8]
    expected_output = [2, 4, 8]
    assert sort_array(arr) == expected_output

def test_sort_array_with_zeros_and_ones():
    arr = [0, 1, 3, 2]
    expected_output = [0, 1, 2, 3]
    assert sort_array(arr) == expected_output

def test_sort_array_with_repeated_elements():
    arr = [5, 3, 5, 7]
    expected_output = [3, 5, 5, 7]
    assert sort_array(arr) == expected_output

def test_sort_array_empty():
    arr = []
    expected_output = []
    assert sort_array(arr) == expected_output
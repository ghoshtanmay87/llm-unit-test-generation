def median(l: list):
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0

import pytest

def test_median_odd_number_of_elements():
    # Median of a list with an odd number of elements
    input_list = [3, 1, 2]
    expected = 2
    assert median(input_list) == expected

def test_median_even_number_of_elements():
    # Median of a list with an even number of elements
    input_list = [4, 1, 2, 3]
    expected = 2.5
    assert median(input_list) == expected

def test_median_single_element():
    # Median of a list with one element
    input_list = [10]
    expected = 10
    assert median(input_list) == expected

def test_median_negative_and_positive_numbers():
    # Median of a list with negative and positive numbers
    input_list = [-5, -1, 0, 1, 5]
    expected = 0
    assert median(input_list) == expected

def test_median_even_number_of_negative_numbers():
    # Median of a list with even number of negative numbers
    input_list = [-3, -1, -2, -4]
    expected = -2.5
    assert median(input_list) == expected

def test_median_repeated_elements():
    # Median of a list with repeated elements
    input_list = [2, 2, 2, 2]
    expected = 2.0
    assert median(input_list) == expected

def test_median_floats_odd():
    # Median of a list with floats
    input_list = [1.5, 3.5, 2.5]
    expected = 2.5
    assert median(input_list) == expected

def test_median_floats_even():
    # Median of a list with even number of floats
    input_list = [1.0, 2.0, 3.0, 4.0]
    expected = 2.5
    assert median(input_list) == expected
def sum_num(numbers):
    total = 0
    for x in numbers:
        total += x
    return total/len(numbers)

import pytest

def test_average_of_positive_integers():
    numbers = [1, 2, 3, 4, 5]
    expected_output = 3.0
    assert sum_num(numbers) == expected_output

def test_average_of_negative_and_positive_integers():
    numbers = [-2, 0, 2, 4]
    expected_output = 1.0
    assert sum_num(numbers) == expected_output

def test_average_of_single_element_list():
    numbers = [10]
    expected_output = 10.0
    assert sum_num(numbers) == expected_output

def test_average_of_floating_point_numbers():
    numbers = [1.5, 2.5, 3.5]
    expected_output = 2.5
    assert sum_num(numbers) == expected_output

def test_average_of_zeros():
    numbers = [0, 0, 0, 0]
    expected_output = 0.0
    assert sum_num(numbers) == expected_output
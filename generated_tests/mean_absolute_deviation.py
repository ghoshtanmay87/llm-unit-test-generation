from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    return sum((abs(x - mean) for x in numbers)) / len(numbers)

import pytest

def test_mean_absolute_deviation_positive_integers():
    numbers = [1, 2, 3, 4, 5]
    expected_output = 1.2
    assert mean_absolute_deviation(numbers) == expected_output

def test_mean_absolute_deviation_identical_elements():
    numbers = [4, 4, 4, 4]
    expected_output = 0.0
    assert mean_absolute_deviation(numbers) == expected_output

def test_mean_absolute_deviation_negative_and_positive_numbers():
    numbers = [-2, 0, 2, 4]
    expected_output = 2.0
    assert mean_absolute_deviation(numbers) == expected_output

def test_mean_absolute_deviation_single_element():
    numbers = [10]
    expected_output = 0.0
    assert mean_absolute_deviation(numbers) == expected_output

def test_mean_absolute_deviation_floats():
    numbers = [1.5, 2.5, 3.5]
    expected_output = 0.6666666666666666
    assert mean_absolute_deviation(numbers) == expected_output
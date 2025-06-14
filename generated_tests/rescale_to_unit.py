from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]

import pytest

def test_rescale_positive_numbers_to_unit_interval():
    """Test rescaling a list of positive numbers to the unit interval [0, 1]."""
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit(numbers) == expected_output

def test_rescale_negative_numbers_to_unit_interval():
    """Test rescaling a list with negative numbers to the unit interval [0, 1]."""
    numbers = [-2.0, -1.0, 0.0, 1.0, 2.0]
    expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit(numbers) == expected_output

def test_rescale_all_same_numbers():
    """Test rescaling a list where all numbers are the same."""
    numbers = [7.0, 7.0, 7.0, 7.0]
    expected_output = [0.0, 0.0, 0.0, 0.0]
    assert rescale_to_unit(numbers) == expected_output

def test_rescale_single_element_list():
    """Test rescaling a single-element list."""
    numbers = [10.0]
    expected_output = [0.0]
    assert rescale_to_unit(numbers) == expected_output

def test_rescale_floating_point_numbers():
    """Test rescaling a list with floating-point numbers."""
    numbers = [1.5, 2.5, 3.5, 4.5]
    expected_output = [0.0, 0.3333333333333333, 0.6666666666666666, 1.0]
    assert rescale_to_unit(numbers) == expected_output
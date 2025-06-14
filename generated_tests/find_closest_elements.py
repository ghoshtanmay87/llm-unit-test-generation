from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair = None
    distance = None
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))
    return closest_pair

import pytest

def test_find_closest_pair_with_duplicates():
    numbers = [5.0, 5.0, 10.0]
    expected_output = (5.0, 5.0)
    assert find_closest_elements(numbers) == expected_output

def test_find_closest_pair_two_elements():
    numbers = [100.0, 101.0]
    expected_output = (100.0, 101.0)
    assert find_closest_elements(numbers) == expected_output

def test_find_closest_pair_multiple_same_smallest_difference():
    numbers = [1.0, 2.0, 3.0, 4.0]
    expected_output = (1.0, 2.0)
    assert find_closest_elements(numbers) == expected_output

def test_find_closest_pair_distinct_positive_floats():
    numbers = [1.0, 3.0, 4.5, 2.1]
    expected_output = (2.1, 3.0)
    assert find_closest_elements(numbers) == expected_output

def test_find_closest_pair_negative_and_positive_floats():
    numbers = [-1.5, 0.0, 2.0, 1.9]
    expected_output = (1.9, 2.0)
    assert find_closest_elements(numbers) == expected_output
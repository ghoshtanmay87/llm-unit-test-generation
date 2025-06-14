from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    running_max = None
    result = []
    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)
        result.append(running_max)
    return result

import pytest

def test_empty_input_list_returns_empty_output_list():
    numbers = []
    expected = []
    assert rolling_max(numbers) == expected

def test_single_element_list_returns_list_with_same_single_element():
    numbers = [5]
    expected = [5]
    assert rolling_max(numbers) == expected

def test_strictly_increasing_list_returns_the_same_list():
    numbers = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert rolling_max(numbers) == expected

def test_strictly_decreasing_list_returns_list_of_first_element_repeated():
    numbers = [5, 4, 3, 2, 1]
    expected = [5, 5, 5, 5, 5]
    assert rolling_max(numbers) == expected

def test_list_with_mixed_values_returns_rolling_maximums():
    numbers = [2, 1, 3, 2, 5, 4]
    expected = [2, 2, 3, 3, 5, 5]
    assert rolling_max(numbers) == expected

def test_list_with_all_equal_elements_returns_list_of_same_repeated_element():
    numbers = [7, 7, 7, 7]
    expected = [7, 7, 7, 7]
    assert rolling_max(numbers) == expected

def test_list_with_negative_and_positive_numbers_returns_correct_rolling_max():
    numbers = [-1, -3, 0, 2, -2]
    expected = [-1, -1, 0, 2, 2]
    assert rolling_max(numbers) == expected
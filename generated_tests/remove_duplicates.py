from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]

import pytest

def test_list_with_no_duplicates_returns_same_list():
    numbers = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]
    assert remove_duplicates(numbers) == expected_output

def test_list_with_some_duplicates_removes_all_occurrences_of_duplicated_numbers():
    numbers = [1, 2, 2, 3, 4, 4, 5]
    expected_output = [1, 3, 5]
    assert remove_duplicates(numbers) == expected_output

def test_list_with_all_elements_duplicated_returns_empty_list():
    numbers = [7, 7, 7, 7]
    expected_output = []
    assert remove_duplicates(numbers) == expected_output

def test_empty_list_returns_empty_list():
    numbers = []
    expected_output = []
    assert remove_duplicates(numbers) == expected_output

def test_list_with_multiple_duplicates_and_unique_numbers():
    numbers = [10, 20, 10, 30, 40, 40, 50, 60, 60]
    expected_output = [20, 30, 50]
    assert remove_duplicates(numbers) == expected_output
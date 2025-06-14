def pluck(arr):
    if len(arr) == 0:
        return []
    evens = list(filter(lambda x: x % 2 == 0, arr))
    if evens == []:
        return []
    return [min(evens), arr.index(min(evens))]

import pytest

def test_empty_input_list_returns_empty_list():
    assert pluck([]) == []

def test_input_list_with_no_even_numbers_returns_empty_list():
    assert pluck([1, 3, 5, 7]) == []

def test_input_list_with_one_even_number_returns_that_number_and_its_index():
    assert pluck([1, 2, 3, 5]) == [2, 1]

def test_input_list_with_multiple_even_numbers_returns_smallest_even_and_its_first_index():
    assert pluck([4, 2, 6, 2, 8]) == [2, 1]

def test_input_list_with_all_even_numbers_returns_smallest_even_and_its_index():
    assert pluck([10, 8, 6, 4, 2]) == [2, 4]

def test_input_list_with_negative_even_numbers_returns_smallest_even_and_its_index():
    assert pluck([-4, -2, -6, -8]) == [-8, 3]

def test_input_list_with_zero_included_returns_zero_and_its_index():
    assert pluck([1, 0, 2, 4]) == [0, 1]
def filter_evennumbers(nums):
 even_nums = list(filter(lambda x: x%2 == 0, nums))
 return even_nums

import pytest

def test_filter_evennumbers_mixed_even_odd():
    # Filter even numbers from a list with mixed even and odd integers
    nums = [1, 2, 3, 4, 5, 6]
    expected_output = [2, 4, 6]
    assert filter_evennumbers(nums) == expected_output

def test_filter_evennumbers_all_odd():
    # Filter even numbers from a list with all odd integers
    nums = [1, 3, 5, 7]
    expected_output = []
    assert filter_evennumbers(nums) == expected_output

def test_filter_evennumbers_all_even():
    # Filter even numbers from a list with all even integers
    nums = [2, 4, 6, 8]
    expected_output = [2, 4, 6, 8]
    assert filter_evennumbers(nums) == expected_output

def test_filter_evennumbers_empty_list():
    # Filter even numbers from an empty list
    nums = []
    expected_output = []
    assert filter_evennumbers(nums) == expected_output

def test_filter_evennumbers_negative_and_positive():
    # Filter even numbers from a list with negative and positive integers
    nums = [-3, -2, -1, 0, 1, 2]
    expected_output = [-2, 0, 2]
    assert filter_evennumbers(nums) == expected_output
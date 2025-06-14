def filter_oddnumbers(nums):
 odd_nums = list(filter(lambda x: x%2 != 0, nums))
 return odd_nums

import pytest

def test_filter_odd_numbers_mixed_integers():
    # Filter odd numbers from a list of mixed integers
    nums = [1, 2, 3, 4, 5]
    expected_output = [1, 3, 5]
    assert filter_oddnumbers(nums) == expected_output

def test_filter_odd_numbers_all_even():
    # Filter odd numbers from a list of all even integers
    nums = [2, 4, 6, 8]
    expected_output = []
    assert filter_oddnumbers(nums) == expected_output

def test_filter_odd_numbers_all_odd():
    # Filter odd numbers from a list of all odd integers
    nums = [1, 3, 5, 7]
    expected_output = [1, 3, 5, 7]
    assert filter_oddnumbers(nums) == expected_output

def test_filter_odd_numbers_empty_list():
    # Filter odd numbers from an empty list
    nums = []
    expected_output = []
    assert filter_oddnumbers(nums) == expected_output

def test_filter_odd_numbers_negative_and_positive():
    # Filter odd numbers from a list with negative and positive integers
    nums = [-3, -2, -1, 0, 1, 2, 3]
    expected_output = [-3, -1, 1, 3]
    assert filter_oddnumbers(nums) == expected_output
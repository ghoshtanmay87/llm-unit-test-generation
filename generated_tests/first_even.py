def first_even(nums):
    first_even = next((el for el in nums if el%2==0),-1)
    return first_even

import pytest

def test_list_with_multiple_even_numbers():
    nums = [1, 3, 4, 6, 8]
    expected = 4
    assert first_even(nums) == expected

def test_list_with_no_even_numbers():
    nums = [1, 3, 5, 7]
    expected = -1
    assert first_even(nums) == expected

def test_list_with_first_element_even():
    nums = [2, 3, 5, 7]
    expected = 2
    assert first_even(nums) == expected

def test_empty_list():
    nums = []
    expected = -1
    assert first_even(nums) == expected

def test_list_with_negative_even_numbers():
    nums = [-3, -2, -1, 0]
    expected = -2
    assert first_even(nums) == expected

def test_list_with_zero_as_first_element():
    nums = [0, 1, 3, 5]
    expected = 0
    assert first_even(nums) == expected
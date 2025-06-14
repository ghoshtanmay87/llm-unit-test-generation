def first_odd(nums):
  first_odd = next((el for el in nums if el%2!=0),-1)
  return first_odd

import pytest

def test_list_with_multiple_odd_and_even_numbers():
    nums = [2, 4, 6, 7, 8, 9]
    expected = 7
    assert first_odd(nums) == expected

def test_list_with_all_even_numbers():
    nums = [2, 4, 6, 8, 10]
    expected = -1
    assert first_odd(nums) == expected

def test_list_with_first_element_odd():
    nums = [3, 4, 5, 6]
    expected = 3
    assert first_odd(nums) == expected

def test_empty_list_input():
    nums = []
    expected = -1
    assert first_odd(nums) == expected

def test_list_with_negative_odd_and_even_numbers():
    nums = [-4, -3, -2, -1, 0]
    expected = -3
    assert first_odd(nums) == expected

def test_list_with_single_odd_number():
    nums = [10, 12, 14, 15]
    expected = 15
    assert first_odd(nums) == expected

def test_list_with_single_even_number():
    nums = [8]
    expected = -1
    assert first_odd(nums) == expected

def test_list_with_zero_included():
    nums = [0, 2, 4, 5]
    expected = 5
    assert first_odd(nums) == expected
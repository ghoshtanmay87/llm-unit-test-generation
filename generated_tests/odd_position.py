def odd_position(nums):
	return all(nums[i]%2==i%2 for i in range(len(nums)))

import pytest

def test_all_elements_satisfy_parity_condition_at_their_indices():
    nums = [0, 1, 2, 3, 4, 5]
    expected = True
    assert odd_position(nums) == expected

def test_single_element_list_with_even_number_at_index_0():
    nums = [2]
    expected = True
    assert odd_position(nums) == expected

def test_single_element_list_with_odd_number_at_index_0():
    nums = [3]
    expected = False
    assert odd_position(nums) == expected

def test_list_with_mismatch_at_odd_index():
    nums = [0, 2, 4, 3]
    expected = False
    assert odd_position(nums) == expected

def test_empty_list_returns_true_by_definition():
    nums = []
    expected = True
    assert odd_position(nums) == expected

def test_list_with_negative_numbers_matching_parity():
    nums = [-2, -3, -4, -5]
    expected = True
    assert odd_position(nums) == expected

def test_list_with_zero_at_odd_index():
    nums = [1, 0, 3, 2]
    expected = False
    assert odd_position(nums) == expected

def test_list_with_all_even_numbers_at_even_indices_and_odd_numbers_at_odd_indices():
    nums = [10, 11, 12, 13, 14, 15]
    expected = True
    assert odd_position(nums) == expected
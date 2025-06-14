def even_position(nums):
	return all(nums[i]%2==i%2 for i in range(len(nums)))

import pytest

def test_all_elements_satisfy_parity_condition_even_odd_indices():
    nums = [0, 1, 2, 3]
    expected = True
    assert even_position(nums) == expected

def test_element_at_odd_index_does_not_satisfy_parity_condition():
    nums = [0, 2, 2, 3]
    expected = False
    assert even_position(nums) == expected

def test_empty_list_returns_true_by_definition():
    nums = []
    expected = True
    assert even_position(nums) == expected

def test_single_element_even_index_even_value():
    nums = [4]
    expected = True
    assert even_position(nums) == expected

def test_single_element_even_index_odd_value():
    nums = [5]
    expected = False
    assert even_position(nums) == expected

def test_mixed_list_one_even_index_has_odd_value():
    nums = [2, 1, 3, 4]
    expected = False
    assert even_position(nums) == expected

def test_all_odd_indices_odd_values_even_indices_even_values():
    nums = [10, 11, 12, 13, 14, 15]
    expected = True
    assert even_position(nums) == expected
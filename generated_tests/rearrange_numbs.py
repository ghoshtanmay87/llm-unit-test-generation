def rearrange_numbs(array_nums):
  result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
  return result

import pytest

def test_rearrange_with_positive_negative_and_zero_values_case1():
    # Scenario: Rearranging a list with positive, negative, and zero values
    input_data = [3, 0, -2, 1]
    expected = [0, 3, 1, -2]
    assert rearrange_numbs(input_data) == expected

def test_rearrange_with_positive_negative_and_zero_values_case2():
    # Scenario: Rearranging a list with positive, negative, and zero values
    input_data = [3, 0, -2, 1]
    expected = [1, 3, 0, -2]
    assert rearrange_numbs(input_data) == expected

def test_rearrange_with_only_zeros():
    # Scenario: Rearranging a list with only zeros
    input_data = [0, 0, 0]
    expected = [0, 0, 0]
    assert rearrange_numbs(input_data) == expected

def test_rearrange_with_only_positive_numbers():
    # Scenario: Rearranging a list with only positive numbers
    input_data = [4, 2, 1]
    expected = [1, 2, 4]
    assert rearrange_numbs(input_data) == expected

def test_rearrange_with_only_negative_numbers_case1():
    # Scenario: Rearranging a list with only negative numbers
    input_data = [-1, -3, -2]
    expected = [-1, -2, -3]
    assert rearrange_numbs(input_data) == expected

def test_rearrange_with_only_negative_numbers_case2():
    # Scenario: Rearranging a list with only negative numbers
    input_data = [-1, -3, -2]
    expected = [-3, -2, -1]
    assert rearrange_numbs(input_data) == expected

def test_rearrange_with_mixed_positive_negative_and_zero_values_case1():
    # Scenario: Rearranging a list with mixed positive, negative, and zero values
    input_data = [0, 5, -1, 2]
    expected = [5, 2, 0, -1]
    assert rearrange_numbs(input_data) == expected

def test_rearrange_with_mixed_positive_negative_and_zero_values_case2():
    # Scenario: Rearranging a list with mixed positive, negative, and zero values
    input_data = [0, 5, -1, 2]
    expected = [2, 5, 0, -1]
    assert rearrange_numbs(input_data) == expected
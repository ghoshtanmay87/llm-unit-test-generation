def square_nums(nums):
 square_nums = list(map(lambda x: x ** 2, nums))
 return square_nums

import pytest

def test_square_list_of_positive_integers():
    # Scenario: Square a list of positive integers
    nums = [1, 2, 3, 4]
    expected_output = [1, 4, 9, 16]
    assert square_nums(nums) == expected_output

def test_square_list_with_zero_and_negative_integers():
    # Scenario: Square a list containing zero and negative integers
    nums = [0, -1, -2, 3]
    expected_output = [0, 1, 4, 9]
    assert square_nums(nums) == expected_output

def test_square_empty_list():
    # Scenario: Square an empty list
    nums = []
    expected_output = []
    assert square_nums(nums) == expected_output

def test_square_list_of_floats():
    # Scenario: Square a list of floating point numbers
    nums = [1.5, -2.0, 0.0]
    expected_output = [2.25, 4.0, 0.0]
    assert square_nums(nums) == expected_output

def test_square_list_with_single_element():
    # Scenario: Square a list with a single element
    nums = [10]
    expected_output = [100]
    assert square_nums(nums) == expected_output
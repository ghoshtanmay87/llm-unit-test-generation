def cube_nums(nums):
 cube_nums = list(map(lambda x: x ** 3, nums))
 return cube_nums

import pytest

def test_cubing_list_of_positive_integers():
    nums = [1, 2, 3]
    expected_output = [1, 8, 27]
    assert cube_nums(nums) == expected_output

def test_cubing_list_with_zero_and_negative_integers():
    nums = [0, -1, -2]
    expected_output = [0, -1, -8]
    assert cube_nums(nums) == expected_output

def test_cubing_empty_list():
    nums = []
    expected_output = []
    assert cube_nums(nums) == expected_output

def test_cubing_list_of_floating_point_numbers():
    nums = [1.5, -2.0, 0.0]
    expected_output = [3.375, -8.0, 0.0]
    assert cube_nums(nums) == expected_output

def test_cubing_list_with_single_element():
    nums = [4]
    expected_output = [64]
    assert cube_nums(nums) == expected_output
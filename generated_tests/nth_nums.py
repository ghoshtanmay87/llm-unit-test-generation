def nth_nums(nums,n):
 nth_nums = list(map(lambda x: x ** n, nums))
 return nth_nums

import pytest

def test_calculate_squares_of_positive_integers():
    nums = [1, 2, 3, 4]
    n = 2
    expected = [1, 4, 9, 16]
    assert nth_nums(nums, n) == expected

def test_calculate_cubes_of_positive_integers():
    nums = [1, 2, 3]
    n = 3
    expected = [1, 8, 27]
    assert nth_nums(nums, n) == expected

def test_calculate_first_power_identity_including_zero():
    nums = [0, 5, 10]
    n = 1
    expected = [0, 5, 10]
    assert nth_nums(nums, n) == expected

def test_calculate_zero_power_of_positive_integers():
    nums = [2, 3, 4]
    n = 0
    expected = [1, 1, 1]
    assert nth_nums(nums, n) == expected

def test_calculate_powers_with_negative_exponent():
    nums = [1, 2, 4]
    n = -1
    expected = [1.0, 0.5, 0.25]
    assert nth_nums(nums, n) == expected

def test_calculate_powers_of_empty_list():
    nums = []
    n = 3
    expected = []
    assert nth_nums(nums, n) == expected

def test_calculate_powers_of_negative_numbers():
    nums = [-1, -2, -3]
    n = 2
    expected = [1, 4, 9]
    assert nth_nums(nums, n) == expected

def test_calculate_powers_of_negative_numbers_with_odd_exponent():
    nums = [-1, -2, -3]
    n = 3
    expected = [-1, -8, -27]
    assert nth_nums(nums, n) == expected
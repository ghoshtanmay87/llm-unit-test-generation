def order_by_points(nums):

    def digits_sum(n):
        neg = 1
        if n < 0:
            n, neg = (-1 * n, -1)
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)

import pytest

def test_order_by_points_with_zero_and_negative_numbers():
    nums = [0, -10, 10, -1]
    expected_output = [-10, -1, 0, 10]
    assert order_by_points(nums) == expected_output

def test_order_by_points_with_single_digit_negative_and_positive_numbers():
    nums = [-5, 3, -2, 1]
    expected_output = [-5, -2, 1, 3]
    assert order_by_points(nums) == expected_output

def test_order_by_points_with_positive_integers_same_digit_sum():
    nums = [13, 22, 4, 31]
    expected_output = [13, 22, 4, 31]
    assert order_by_points(nums) == expected_output

def test_order_by_points_with_multi_digit_negative_numbers_with_zeros():
    nums = [-101, -110, 11, 101]
    expected_output = [-101, -110, 11, 101]
    assert order_by_points(nums) == expected_output
def average_tuple(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    return result

import pytest

def test_average_two_tuples_equal_length():
    # Calculate average of corresponding elements in two tuples of equal length
    nums = [(1, 2), (3, 4)]
    expected = [2.0, 3.0]
    assert average_tuple(nums) == expected

def test_average_three_tuples():
    # Calculate average of corresponding elements in three tuples
    nums = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected = [4.0, 5.0, 6.0]
    assert average_tuple(nums) == expected

def test_average_with_negative_and_positive_numbers():
    # Calculate average with negative and positive numbers
    nums = [(-1, 0), (1, 2)]
    expected = [0.0, 1.0]
    assert average_tuple(nums) == expected

def test_average_single_tuple_input():
    # Calculate average with single tuple input
    nums = [(10, 20, 30)]
    expected = [10.0, 20.0, 30.0]
    assert average_tuple(nums) == expected

def test_average_with_floating_point_numbers():
    # Calculate average with floating point numbers
    nums = [(1.5, 2.5), (3.5, 4.5)]
    expected = [2.5, 3.5]
    assert average_tuple(nums) == expected
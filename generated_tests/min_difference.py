def min_difference(test_list):
  temp = [abs(b - a) for a, b in test_list]
  res = min(temp)
  return (res)

import pytest

def test_min_difference_positive_integers():
    # Calculate minimum absolute difference for pairs with positive integers
    test_list = [[1, 5], [3, 8], [10, 15]]
    expected_output = 4
    assert min_difference(test_list) == expected_output

def test_min_difference_negative_and_positive_integers():
    # Calculate minimum absolute difference for pairs with negative and positive integers
    test_list = [[-2, 3], [4, -1], [0, 0]]
    expected_output = 0
    assert min_difference(test_list) == expected_output

def test_min_difference_all_same_difference():
    # Calculate minimum absolute difference when all pairs have the same difference
    test_list = [[2, 4], [5, 7], [10, 12]]
    expected_output = 2
    assert min_difference(test_list) == expected_output

def test_min_difference_with_zero_difference():
    # Calculate minimum absolute difference with zero difference in one pair
    test_list = [[7, 7], [10, 20], [30, 40]]
    expected_output = 0
    assert min_difference(test_list) == expected_output

def test_min_difference_floating_point_numbers():
    # Calculate minimum absolute difference with floating point numbers
    test_list = [[1.5, 3.5], [2.0, 2.1], [5.5, 6.0]]
    expected_output = 0.10000000000000009
    assert min_difference(test_list) == expected_output
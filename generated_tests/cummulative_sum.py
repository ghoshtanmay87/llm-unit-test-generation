def cummulative_sum(test_list):
  res = sum(map(sum, test_list))
  return (res)

import pytest

def test_cummulative_sum_with_positive_integers():
    # Calculate cumulative sum of a list of lists with positive integers
    test_list = [[1, 2, 3], [4, 5], [6]]
    expected_output = 21
    assert cummulative_sum(test_list) == expected_output

def test_cummulative_sum_with_negative_and_positive_integers():
    # Calculate cumulative sum of a list of lists with negative and positive integers
    test_list = [[-1, -2], [3, 4], [0]]
    expected_output = 4
    assert cummulative_sum(test_list) == expected_output

def test_cummulative_sum_with_empty_list():
    # Calculate cumulative sum of an empty list
    test_list = []
    expected_output = 0
    assert cummulative_sum(test_list) == expected_output

def test_cummulative_sum_with_empty_inner_lists():
    # Calculate cumulative sum of a list containing empty lists
    test_list = [[], [], []]
    expected_output = 0
    assert cummulative_sum(test_list) == expected_output

def test_cummulative_sum_with_floats():
    # Calculate cumulative sum of a list of lists with floats
    test_list = [[1.5, 2.5], [3.0], [4.5, 0.5]]
    expected_output = 12.0
    assert cummulative_sum(test_list) == expected_output
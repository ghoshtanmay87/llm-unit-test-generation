def find_tuples(test_list, K):
  res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]
  return (str(res))

import pytest

def test_all_sublists_divisible_by_K():
    test_list = [[2, 4], [6, 8], [10, 12]]
    K = 2
    expected_output = '[[2, 4], [6, 8], [10, 12]]'
    assert find_tuples(test_list, K) == expected_output

def test_some_sublists_divisible_by_K_others_not():
    test_list = [[3, 6], [4, 5], [9, 12]]
    K = 3
    expected_output = '[[3, 6], [9, 12]]'
    assert find_tuples(test_list, K) == expected_output

def test_no_sublists_divisible_by_K():
    test_list = [[1, 2], [3, 5], [7, 11]]
    K = 4
    expected_output = '[]'
    assert find_tuples(test_list, K) == expected_output

def test_empty_test_list():
    test_list = []
    K = 5
    expected_output = '[]'
    assert find_tuples(test_list, K) == expected_output

def test_sublists_with_zero_elements_divisible_by_K():
    test_list = [[0, 0], [0, 5], [10, 0]]
    K = 5
    expected_output = '[[0, 0], [0, 5], [10, 0]]'
    assert find_tuples(test_list, K) == expected_output

def test_sublists_with_negative_numbers_divisible_by_K():
    test_list = [[-6, -12], [-3, 9], [-4, -8]]
    K = 3
    expected_output = '[[-6, -12], [-3, 9]]'
    assert find_tuples(test_list, K) == expected_output
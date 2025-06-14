def remove_tuples(test_list, K):
  res = [ele for ele in test_list if len(ele) != K]
  return (res)

import pytest

def test_remove_tuples_length_2():
    test_list = [(1, 2), (3, 4, 5), (6,), (7, 8)]
    K = 2
    expected_output = [(3, 4, 5), (6,)]
    assert remove_tuples(test_list, K) == expected_output

def test_remove_tuples_length_3_all_removed():
    test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    K = 3
    expected_output = []
    assert remove_tuples(test_list, K) == expected_output

def test_remove_tuples_length_1():
    test_list = [(1,), (2, 3), (4, 5, 6), (7,)]
    K = 1
    expected_output = [(2, 3), (4, 5, 6)]
    assert remove_tuples(test_list, K) == expected_output

def test_remove_tuples_length_0_empty_tuples():
    test_list = [(), (1,), (2, 3), ()]
    K = 0
    expected_output = [(1,), (2, 3)]
    assert remove_tuples(test_list, K) == expected_output

def test_remove_tuples_length_4_no_removal():
    test_list = [(1, 2), (3,), (4, 5, 6)]
    K = 4
    expected_output = [(1, 2), (3,), (4, 5, 6)]
    assert remove_tuples(test_list, K) == expected_output
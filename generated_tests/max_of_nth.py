def max_of_nth(test_list, N):
  res = max([sub[N] for sub in test_list])
  return (res)

import pytest

def test_max_of_nth_index_1_in_sublists():
    test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    N = 1
    expected_output = 8
    assert max_of_nth(test_list, N) == expected_output

def test_max_of_nth_index_0_with_negative_numbers():
    test_list = [[-1, 0], [-5, 10], [-3, 7]]
    N = 0
    expected_output = -1
    assert max_of_nth(test_list, N) == expected_output

def test_max_of_nth_index_2_with_mixed_values():
    test_list = [[10, 20, 30], [5, 15, 25], [7, 17, 27]]
    N = 2
    expected_output = 30
    assert max_of_nth(test_list, N) == expected_output

def test_max_of_nth_index_0_single_element_sublists():
    test_list = [[100], [200], [50]]
    N = 0
    expected_output = 200
    assert max_of_nth(test_list, N) == expected_output

def test_max_of_nth_index_1_identical_values():
    test_list = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
    N = 1
    expected_output = 3
    assert max_of_nth(test_list, N) == expected_output
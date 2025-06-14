def count_bidirectional(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return (str(res))

import pytest

def test_count_bidirectional_one_matching_pair():
    test_list = [[1, 2], [2, 1]]
    expected_output = '1'
    assert count_bidirectional(test_list) == expected_output

def test_count_bidirectional_no_matching_pairs():
    test_list = [[1, 2], [3, 4]]
    expected_output = '0'
    assert count_bidirectional(test_list) == expected_output

def test_count_bidirectional_multiple_pairs_with_duplicates():
    test_list = [[1, 2], [2, 1], [3, 4], [4, 3], [1, 2]]
    expected_output = '2'
    assert count_bidirectional(test_list) == expected_output

def test_count_bidirectional_empty_list():
    test_list = []
    expected_output = '0'
    assert count_bidirectional(test_list) == expected_output

def test_count_bidirectional_single_element():
    test_list = [[1, 2]]
    expected_output = '0'
    assert count_bidirectional(test_list) == expected_output
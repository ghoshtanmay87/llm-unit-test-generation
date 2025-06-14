def tuple_intersection(test_list1, test_list2):
  res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])
  return (res)

import pytest

def test_intersection_identical_tuples_different_orders():
    test_list1 = [[1, 2], [3, 4]]
    test_list2 = [[2, 1], [4, 3]]
    expected_output = {(1, 2), (3, 4)}
    assert tuple_intersection(test_list1, test_list2) == expected_output

def test_intersection_no_common_tuples():
    test_list1 = [[1, 2], [3, 4]]
    test_list2 = [[5, 6], [7, 8]]
    expected_output = set()
    assert tuple_intersection(test_list1, test_list2) == expected_output

def test_intersection_some_common_some_different():
    test_list1 = [[1, 2], [3, 4], [5, 6]]
    test_list2 = [[2, 1], [6, 5], [7, 8]]
    expected_output = {(1, 2), (5, 6)}
    assert tuple_intersection(test_list1, test_list2) == expected_output

def test_intersection_with_duplicate_tuples():
    test_list1 = [[1, 2], [2, 1], [3, 4]]
    test_list2 = [[2, 1], [4, 3], [4, 3]]
    expected_output = {(1, 2), (3, 4)}
    assert tuple_intersection(test_list1, test_list2) == expected_output

def test_intersection_one_list_empty():
    test_list1 = []
    test_list2 = [[1, 2], [3, 4]]
    expected_output = set()
    assert tuple_intersection(test_list1, test_list2) == expected_output

def test_intersection_both_lists_empty():
    test_list1 = []
    test_list2 = []
    expected_output = set()
    assert tuple_intersection(test_list1, test_list2) == expected_output

def test_intersection_tuples_different_lengths():
    test_list1 = [[1, 2, 3], [4, 5]]
    test_list2 = [[3, 2, 1], [5, 4], [6]]
    expected_output = {(4, 5), (1, 2, 3)}
    assert tuple_intersection(test_list1, test_list2) == expected_output
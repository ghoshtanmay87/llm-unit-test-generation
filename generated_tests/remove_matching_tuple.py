def remove_matching_tuple(test_list1, test_list2):
  res = [sub for sub in test_list1 if sub not in test_list2]
  return (res)

import pytest

def test_remove_tuples_present_in_second_list():
    test_list1 = [(1, 2), (3, 4), (5, 6)]
    test_list2 = [(3, 4)]
    expected_output = [(1, 2), (5, 6)]
    assert remove_matching_tuple(test_list1, test_list2) == expected_output

def test_no_tuples_removed_when_second_list_empty():
    test_list1 = [(1, 2), (3, 4)]
    test_list2 = []
    expected_output = [(1, 2), (3, 4)]
    assert remove_matching_tuple(test_list1, test_list2) == expected_output

def test_all_tuples_removed_when_all_present_in_second_list():
    test_list1 = [(1, 2), (3, 4)]
    test_list2 = [(1, 2), (3, 4)]
    expected_output = []
    assert remove_matching_tuple(test_list1, test_list2) == expected_output

def test_partial_removal_with_multiple_duplicates_in_second_list():
    test_list1 = [(1, 2), (3, 4), (5, 6), (7, 8)]
    test_list2 = [(3, 4), (3, 4), (7, 8)]
    expected_output = [(1, 2), (5, 6)]
    assert remove_matching_tuple(test_list1, test_list2) == expected_output

def test_no_removal_when_no_tuples_match():
    test_list1 = [(1, 2), (3, 4)]
    test_list2 = [(5, 6), (7, 8)]
    expected_output = [(1, 2), (3, 4)]
    assert remove_matching_tuple(test_list1, test_list2) == expected_output
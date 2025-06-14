def extract_singly(test_list):
  res = []
  temp = set()
  for inner in test_list:
    for ele in inner:
      if not ele in temp:
        temp.add(ele)
        res.append(ele)
  return (res)

import pytest

def test_extract_unique_no_duplicates_across_inner_lists():
    test_list = [[1, 2], [3, 4]]
    expected_output = [1, 2, 3, 4]
    assert extract_singly(test_list) == expected_output

def test_extract_unique_with_duplicates_within_and_across_inner_lists():
    test_list = [[1, 2, 2], [2, 3, 1]]
    expected_output = [1, 2, 3]
    assert extract_singly(test_list) == expected_output

def test_extract_unique_from_empty_inner_lists():
    test_list = [[], [], []]
    expected_output = []
    assert extract_singly(test_list) == expected_output

def test_extract_unique_from_single_inner_list_with_repeats():
    test_list = [[5, 5, 5, 5]]
    expected_output = [5]
    assert extract_singly(test_list) == expected_output

def test_extract_unique_from_multiple_inner_lists_with_overlapping_elements():
    test_list = [[10, 20], [20, 30], [10, 40]]
    expected_output = [10, 20, 30, 40]
    assert extract_singly(test_list) == expected_output
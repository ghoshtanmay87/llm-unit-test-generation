import heapq
def merge_sorted_list(num1,num2,num3):
  num1=sorted(num1)
  num2=sorted(num2)
  num3=sorted(num3)
  result = heapq.merge(num1,num2,num3)
  return list(result)

import pytest

def test_merge_three_sorted_lists_with_distinct_elements():
    num1 = [1, 4, 7]
    num2 = [2, 5, 8]
    num3 = [3, 6, 9]
    expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge_sorted_list(num1, num2, num3) == expected_output

def test_merge_three_unsorted_lists_with_overlapping_values():
    num1 = [5, 1, 3]
    num2 = [2, 4, 6]
    num3 = [3, 7, 0]
    expected_output = [0, 1, 2, 3, 3, 4, 5, 6, 7]
    assert merge_sorted_list(num1, num2, num3) == expected_output

def test_merge_when_one_list_is_empty():
    num1 = []
    num2 = [1, 3, 5]
    num3 = [2, 4, 6]
    expected_output = [1, 2, 3, 4, 5, 6]
    assert merge_sorted_list(num1, num2, num3) == expected_output

def test_merge_three_empty_lists():
    num1 = []
    num2 = []
    num3 = []
    expected_output = []
    assert merge_sorted_list(num1, num2, num3) == expected_output

def test_merge_lists_with_duplicate_elements_across_lists():
    num1 = [1, 2, 2]
    num2 = [2, 3, 4]
    num3 = [2, 2, 5]
    expected_output = [1, 2, 2, 2, 2, 2, 3, 4, 5]
    assert merge_sorted_list(num1, num2, num3) == expected_output

def test_merge_lists_with_negative_and_positive_numbers():
    num1 = [-3, -1, 2]
    num2 = [-2, 0, 3]
    num3 = [-5, 1, 4]
    expected_output = [-5, -3, -2, -1, 0, 1, 2, 3, 4]
    assert merge_sorted_list(num1, num2, num3) == expected_output
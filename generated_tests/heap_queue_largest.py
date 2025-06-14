import heapq as hq
def heap_queue_largest(nums,n):
  largest_nums = hq.nlargest(n, nums)
  return largest_nums

import pytest

def test_find_three_largest_distinct_positive_integers():
    nums = [1, 3, 5, 7, 9]
    n = 3
    expected_output = [9, 7, 5]
    assert heap_queue_largest(nums, n) == expected_output

def test_find_two_largest_with_duplicates():
    nums = [4, 1, 4, 2, 4]
    n = 2
    expected_output = [4, 4]
    assert heap_queue_largest(nums, n) == expected_output

def test_find_largest_when_n_is_one():
    nums = [10, 20, 30, 40]
    n = 1
    expected_output = [40]
    assert heap_queue_largest(nums, n) == expected_output

def test_find_largest_when_n_equals_list_length():
    nums = [3, 1, 4, 1, 5]
    n = 5
    expected_output = [5, 4, 3, 1, 1]
    assert heap_queue_largest(nums, n) == expected_output

def test_find_largest_when_n_is_zero():
    nums = [1, 2, 3]
    n = 0
    expected_output = []
    assert heap_queue_largest(nums, n) == expected_output

def test_find_largest_with_negative_and_positive_numbers():
    nums = [-10, 0, 10, 5, -5]
    n = 2
    expected_output = [10, 5]
    assert heap_queue_largest(nums, n) == expected_output

def test_find_largest_when_n_greater_than_list_length():
    nums = [2, 4, 6]
    n = 5
    expected_output = [6, 4, 2]
    assert heap_queue_largest(nums, n) == expected_output

def test_find_largest_in_empty_list():
    nums = []
    n = 3
    expected_output = []
    assert heap_queue_largest(nums, n) == expected_output
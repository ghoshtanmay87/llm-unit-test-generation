import heapq as hq
def heap_queue_smallest(nums,n):
  smallest_nums = hq.nsmallest(n, nums)
  return smallest_nums

import pytest

def test_find_3_smallest_numbers_in_positive_integers():
    nums = [5, 1, 3, 2, 4]
    n = 3
    expected = [1, 2, 3]
    assert heap_queue_smallest(nums, n) == expected

def test_find_2_smallest_numbers_with_duplicates():
    nums = [4, 2, 2, 3, 1]
    n = 2
    expected = [1, 2]
    assert heap_queue_smallest(nums, n) == expected

def test_find_5_smallest_numbers_when_n_equals_list_length():
    nums = [10, 9, 8, 7, 6]
    n = 5
    expected = [6, 7, 8, 9, 10]
    assert heap_queue_smallest(nums, n) == expected

def test_find_0_smallest_numbers_edge_case():
    nums = [1, 2, 3]
    n = 0
    expected = []
    assert heap_queue_smallest(nums, n) == expected

def test_find_3_smallest_numbers_with_negative_and_positive():
    nums = [-1, -3, 2, 0, 5]
    n = 3
    expected = [-3, -1, 0]
    assert heap_queue_smallest(nums, n) == expected

def test_find_4_smallest_numbers_when_n_larger_than_list_length():
    nums = [7, 3]
    n = 4
    expected = [3, 7]
    assert heap_queue_smallest(nums, n) == expected

def test_find_1_smallest_number_in_single_element_list():
    nums = [42]
    n = 1
    expected = [42]
    assert heap_queue_smallest(nums, n) == expected
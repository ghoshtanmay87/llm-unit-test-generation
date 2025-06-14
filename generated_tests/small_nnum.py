import heapq
def small_nnum(list1,n):
  smallest=heapq.nsmallest(n,list1)
  return smallest

import pytest

def test_find_3_smallest_positive_integers():
    list1 = [5, 1, 9, 3, 7]
    n = 3
    expected = [1, 3, 5]
    assert small_nnum(list1, n) == expected

def test_find_2_smallest_with_negatives_and_positives():
    list1 = [-2, 4, 0, -5, 3]
    n = 2
    expected = [-5, -2]
    assert small_nnum(list1, n) == expected

def test_find_4_smallest_when_n_equals_list_length():
    list1 = [10, 20, 30, 40]
    n = 4
    expected = [10, 20, 30, 40]
    assert small_nnum(list1, n) == expected

def test_find_1_smallest_with_duplicates():
    list1 = [2, 2, 1, 3, 1]
    n = 1
    expected = [1]
    assert small_nnum(list1, n) == expected

def test_find_0_smallest_numbers_edge_case():
    list1 = [4, 5, 6]
    n = 0
    expected = []
    assert small_nnum(list1, n) == expected

def test_find_5_smallest_when_n_larger_than_list_length():
    list1 = [7, 3, 5]
    n = 5
    expected = [3, 5, 7]
    assert small_nnum(list1, n) == expected
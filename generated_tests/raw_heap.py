import heapq as hq
def raw_heap(rawheap):
  hq.heapify(rawheap)
  return rawheap

import pytest

def test_heapify_unsorted_list_of_integers():
    rawheap = [5, 3, 8, 1, 2]
    expected_output = [1, 2, 8, 5, 3]
    assert raw_heap(rawheap) == expected_output

def test_heapify_already_heapified_list():
    rawheap = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]
    assert raw_heap(rawheap) == expected_output

def test_heapify_list_with_duplicate_elements():
    rawheap = [4, 4, 4, 4]
    expected_output = [4, 4, 4, 4]
    assert raw_heap(rawheap) == expected_output

def test_heapify_empty_list():
    rawheap = []
    expected_output = []
    assert raw_heap(rawheap) == expected_output

def test_heapify_list_with_negative_and_positive_integers():
    rawheap = [0, -1, 5, -10, 3]
    expected_output = [-10, -1, 5, 0, 3]
    assert raw_heap(rawheap) == expected_output
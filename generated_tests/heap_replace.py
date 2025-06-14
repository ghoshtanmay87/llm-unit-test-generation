import heapq as hq
def heap_replace(heap,a):
  hq.heapify(heap)
  hq.heapreplace(heap, a)
  return heap

import pytest

def test_replace_root_with_larger_element():
    heap = [1, 3, 5, 7, 9]
    a = 4
    expected = [3, 4, 5, 7, 9]
    result = heap_replace(heap, a)
    assert result == expected

def test_replace_root_with_smaller_element():
    heap = [2, 4, 6, 8, 10]
    a = 1
    expected = [1, 4, 6, 8, 10]
    result = heap_replace(heap, a)
    assert result == expected

def test_replace_root_in_single_element_heap():
    heap = [10]
    a = 5
    expected = [5]
    result = heap_replace(heap, a)
    assert result == expected

def test_replace_root_in_unsorted_list():
    heap = [9, 7, 5, 3, 1]
    a = 4
    expected = [3, 4, 5, 9, 7]
    result = heap_replace(heap, a)
    assert result == expected

def test_replace_root_with_same_value():
    heap = [2, 3, 4, 5, 6]
    a = 2
    expected = [2, 3, 4, 5, 6]
    result = heap_replace(heap, a)
    assert result == expected
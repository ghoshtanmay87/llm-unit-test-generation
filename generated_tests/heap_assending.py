import heapq as hq
def heap_assending(nums):
  hq.heapify(nums)
  s_result = [hq.heappop(nums) for i in range(len(nums))]
  return s_result

import pytest

def test_sort_positive_integers_ascending():
    nums = [3, 1, 4, 1, 5, 9, 2]
    expected = [1, 1, 2, 3, 4, 5, 9]
    assert heap_assending(nums) == expected

def test_sort_negative_and_positive_integers():
    nums = [-2, 0, 5, -1, 3]
    expected = [-2, -1, 0, 3, 5]
    assert heap_assending(nums) == expected

def test_sort_already_sorted_list():
    nums = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert heap_assending(nums) == expected

def test_sort_list_with_duplicates():
    nums = [4, 4, 4, 4]
    expected = [4, 4, 4, 4]
    assert heap_assending(nums) == expected

def test_sort_empty_list():
    nums = []
    expected = []
    assert heap_assending(nums) == expected
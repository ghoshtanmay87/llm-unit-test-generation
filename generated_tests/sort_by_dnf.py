def sort_by_dnf(arr, n):
  low=0
  mid=0
  high=n-1
  while mid <= high:
    if arr[mid] == 0:
      arr[low], arr[mid] = arr[mid], arr[low]
      low = low + 1
      mid = mid + 1
    elif arr[mid] == 1:
      mid = mid + 1
    else:
      arr[mid], arr[high] = arr[high], arr[mid]
      high = high - 1
  return arr

import pytest

def test_sort_mixed_0s_1s_2s():
    arr = [2, 0, 2, 1, 1, 0]
    n = 6
    expected = [0, 0, 1, 1, 2, 2]
    assert sort_by_dnf(arr, n) == expected

def test_sort_all_zeros():
    arr = [0, 0, 0, 0]
    n = 4
    expected = [0, 0, 0, 0]
    assert sort_by_dnf(arr, n) == expected

def test_sort_all_ones():
    arr = [1, 1, 1, 1]
    n = 4
    expected = [1, 1, 1, 1]
    assert sort_by_dnf(arr, n) == expected

def test_sort_all_twos():
    arr = [2, 2, 2, 2]
    n = 4
    expected = [2, 2, 2, 2]
    assert sort_by_dnf(arr, n) == expected

def test_sort_zeros_and_ones_only():
    arr = [1, 0, 1, 0, 0, 1]
    n = 6
    expected = [0, 0, 0, 1, 1, 1]
    assert sort_by_dnf(arr, n) == expected

def test_sort_ones_and_twos_only():
    arr = [2, 1, 2, 1, 1, 2]
    n = 6
    expected = [1, 1, 1, 2, 2, 2]
    assert sort_by_dnf(arr, n) == expected

def test_sort_zeros_and_twos_only():
    arr = [2, 0, 2, 0, 0, 2]
    n = 6
    expected = [0, 0, 0, 2, 2, 2]
    assert sort_by_dnf(arr, n) == expected

def test_sort_empty_array():
    arr = []
    n = 0
    expected = []
    assert sort_by_dnf(arr, n) == expected

def test_sort_single_element_zero():
    arr = [0]
    n = 1
    expected = [0]
    assert sort_by_dnf(arr, n) == expected

def test_sort_single_element_one():
    arr = [1]
    n = 1
    expected = [1]
    assert sort_by_dnf(arr, n) == expected

def test_sort_single_element_two():
    arr = [2]
    n = 1
    expected = [2]
    assert sort_by_dnf(arr, n) == expected
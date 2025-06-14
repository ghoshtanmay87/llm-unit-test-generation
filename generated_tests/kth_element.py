def kth_element(arr, n, k):
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]

import pytest

def test_kth_element_small_unsorted_list():
    arr = [3, 1, 2]
    n = 3
    k = 2
    expected = 1
    assert kth_element(arr, n, k) == expected

def test_kth_element_sorted_list():
    arr = [1, 2, 3, 4, 5]
    n = 5
    k = 3
    expected = 3
    assert kth_element(arr, n, k) == expected

def test_kth_element_reverse_sorted_list():
    arr = [5, 4, 3, 2, 1]
    n = 5
    k = 1
    expected = 5
    assert kth_element(arr, n, k) == expected

def test_kth_element_k_equals_n():
    arr = [10, 20, 30, 40]
    n = 4
    k = 4
    expected = 40
    assert kth_element(arr, n, k) == expected

def test_kth_element_list_with_duplicates():
    arr = [2, 3, 2, 1, 3]
    n = 5
    k = 3
    expected = 2
    assert kth_element(arr, n, k) == expected
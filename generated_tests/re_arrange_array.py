def re_arrange_array(arr, n):
  j=0
  for i in range(0, n):
    if (arr[i] < 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = j + 1
  return arr

import pytest

def test_all_positive_numbers():
    arr = [1, 2, 3, 4, 5]
    n = 5
    expected = [1, 2, 3, 4, 5]
    assert re_arrange_array(arr, n) == expected

def test_all_negative_numbers():
    arr = [-1, -2, -3, -4, -5]
    n = 5
    expected = [-1, -2, -3, -4, -5]
    assert re_arrange_array(arr, n) == expected

def test_negatives_at_start():
    arr = [-1, -2, 3, 4, 5]
    n = 5
    expected = [-1, -2, 3, 4, 5]
    assert re_arrange_array(arr, n) == expected

def test_negatives_at_end():
    arr = [1, 2, 3, -4, -5]
    n = 5
    expected = [-4, -5, 3, 1, 2]
    assert re_arrange_array(arr, n) == expected

def test_negatives_and_positives_interleaved():
    arr = [1, -2, 3, -4, 5]
    n = 5
    expected = [-2, -4, 3, 1, 5]
    assert re_arrange_array(arr, n) == expected

def test_empty_array():
    arr = []
    n = 0
    expected = []
    assert re_arrange_array(arr, n) == expected

def test_single_negative_element():
    arr = [-10]
    n = 1
    expected = [-10]
    assert re_arrange_array(arr, n) == expected

def test_single_positive_element():
    arr = [10]
    n = 1
    expected = [10]
    assert re_arrange_array(arr, n) == expected

def test_negatives_and_positives_with_zeros():
    arr = [0, -1, 2, -3, 0]
    n = 5
    expected = [-1, -3, 2, 0, 0]
    assert re_arrange_array(arr, n) == expected
def equilibrium_index(arr):
  total_sum = sum(arr)
  left_sum=0
  for i, num in enumerate(arr):
    total_sum -= num
    if left_sum == total_sum:
      return i
    left_sum += num
  return -1

import pytest

def test_equilibrium_index_single_equilibrium_point():
    arr = [1, 3, 5, 2, 2]
    expected = 2
    assert equilibrium_index(arr) == expected

def test_equilibrium_index_no_equilibrium_index():
    arr = [1, 2, 3]
    expected = -1
    assert equilibrium_index(arr) == expected

def test_equilibrium_index_at_start_of_array():
    arr = [0, -1, 1]
    expected = 0
    assert equilibrium_index(arr) == expected

def test_equilibrium_index_at_end_of_array():
    arr = [1, -1, 0]
    expected = 2
    assert equilibrium_index(arr) == expected

def test_equilibrium_index_empty_array():
    arr = []
    expected = -1
    assert equilibrium_index(arr) == expected

def test_equilibrium_index_all_zeros():
    arr = [0, 0, 0, 0]
    expected = 0
    assert equilibrium_index(arr) == expected

def test_equilibrium_index_multiple_equilibrium_indices():
    arr = [-7, 1, 5, 2, -4, 3, 0]
    expected = 3
    assert equilibrium_index(arr) == expected
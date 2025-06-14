def get_median(arr1, arr2, n):
  i = 0
  j = 0
  m1 = -1
  m2 = -1
  count = 0
  while count < n + 1:
    count += 1
    if i == n:
      m1 = m2
      m2 = arr2[0]
      break
    elif j == n:
      m1 = m2
      m2 = arr1[0]
      break
    if arr1[i] <= arr2[j]:
      m1 = m2
      m2 = arr1[i]
      i += 1
    else:
      m1 = m2
      m2 = arr2[j]
      j += 1
  return (m1 + m2)/2

import pytest

def test_median_two_sorted_arrays_size_1_each():
    arr1 = [1]
    arr2 = [2]
    n = 1
    expected = 1.5
    assert get_median(arr1, arr2, n) == expected

def test_median_two_sorted_arrays_size_2_each_distinct_elements():
    arr1 = [1, 3]
    arr2 = [2, 4]
    n = 2
    expected = 2.5
    assert get_median(arr1, arr2, n) == expected

def test_median_all_elements_arr1_smaller_than_arr2():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    n = 3
    expected = 3.5
    assert get_median(arr1, arr2, n) == expected

def test_median_arrays_with_overlapping_elements():
    arr1 = [1, 4, 7]
    arr2 = [2, 5, 8]
    n = 3
    expected = 4.5
    assert get_median(arr1, arr2, n) == expected

def test_median_arrays_with_identical_elements():
    arr1 = [1, 1, 1]
    arr2 = [1, 1, 1]
    n = 3
    expected = 1.0
    assert get_median(arr1, arr2, n) == expected

def test_median_one_array_all_smaller_other_all_larger():
    arr1 = [1, 2, 3]
    arr2 = [10, 11, 12]
    n = 3
    expected = 6.5
    assert get_median(arr1, arr2, n) == expected

def test_median_arrays_with_interleaved_elements():
    arr1 = [1, 5, 9]
    arr2 = [2, 6, 10]
    n = 3
    expected = 5.5
    assert get_median(arr1, arr2, n) == expected

def test_median_arrays_with_negative_and_positive_numbers():
    arr1 = [-3, -1, 4]
    arr2 = [-2, 0, 5]
    n = 3
    expected = -0.5
    assert get_median(arr1, arr2, n) == expected
def get_odd_occurence(arr, arr_size):
  for i in range(0, arr_size):
    count = 0
    for j in range(0, arr_size):
      if arr[i] == arr[j]:
        count += 1
    if (count % 2 != 0):
      return arr[i]
  return -1

import pytest

def test_single_element_array_returns_that_element():
    arr = [7]
    arr_size = 1
    expected = 7
    assert get_odd_occurence(arr, arr_size) == expected

def test_array_with_one_element_occurring_odd_times_returns_that_element():
    arr = [1, 2, 3, 2, 3, 1, 3]
    arr_size = 7
    expected = 3
    assert get_odd_occurence(arr, arr_size) == expected

def test_array_with_all_elements_occurring_even_times_returns_minus_one():
    arr = [4, 4, 6, 6, 8, 8]
    arr_size = 6
    expected = -1
    assert get_odd_occurence(arr, arr_size) == expected

def test_array_with_multiple_odd_occurrences_returns_first_odd_occurrence_element():
    arr = [10, 10, 20, 20, 20, 30, 30, 30, 30, 40]
    arr_size = 10
    expected = 20
    assert get_odd_occurence(arr, arr_size) == expected

def test_array_with_one_element_occurring_once_among_others_even_times():
    arr = [5, 5, 7, 7, 9]
    arr_size = 5
    expected = 9
    assert get_odd_occurence(arr, arr_size) == expected

def test_empty_array_returns_minus_one():
    arr = []
    arr_size = 0
    expected = -1
    assert get_odd_occurence(arr, arr_size) == expected

def test_array_with_negative_numbers_and_odd_occurrence():
    arr = [-1, -1, -2, -2, -2]
    arr_size = 5
    expected = -2
    assert get_odd_occurence(arr, arr_size) == expected
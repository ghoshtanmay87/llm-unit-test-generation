def check_greater(arr, number):
  arr.sort()
  if number > arr[-1]:
    return ('Yes, the entered number is greater than those in the array')
  else:
    return ('No, entered number is less than those in the array')

import pytest

def test_number_greater_than_all_elements():
    arr = [1, 3, 5, 7]
    number = 10
    expected = 'Yes, the entered number is greater than those in the array'
    assert check_greater(arr, number) == expected

def test_number_equal_to_largest_element():
    arr = [2, 4, 6, 8]
    number = 8
    expected = 'No, entered number is less than those in the array'
    assert check_greater(arr, number) == expected

def test_number_less_than_largest_element():
    arr = [10, 20, 30, 40]
    number = 25
    expected = 'No, entered number is less than those in the array'
    assert check_greater(arr, number) == expected

def test_number_less_than_all_elements():
    arr = [5, 10, 15]
    number = 1
    expected = 'No, entered number is less than those in the array'
    assert check_greater(arr, number) == expected

def test_single_element_array_number_greater():
    arr = [100]
    number = 150
    expected = 'Yes, the entered number is greater than those in the array'
    assert check_greater(arr, number) == expected

def test_single_element_array_number_equal():
    arr = [50]
    number = 50
    expected = 'No, entered number is less than those in the array'
    assert check_greater(arr, number) == expected
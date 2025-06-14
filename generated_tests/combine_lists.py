from heapq import merge
def combine_lists(num1,num2):
  combine_lists=list(merge(num1, num2))
  return combine_lists

import pytest

def test_combine_two_sorted_integer_lists():
    num1 = [1, 3, 5]
    num2 = [2, 4, 6]
    expected_output = [1, 2, 3, 4, 5, 6]
    assert combine_lists(num1, num2) == expected_output

def test_combine_two_empty_lists():
    num1 = []
    num2 = []
    expected_output = []
    assert combine_lists(num1, num2) == expected_output

def test_combine_empty_list_with_non_empty_sorted_list():
    num1 = []
    num2 = [1, 2, 3]
    expected_output = [1, 2, 3]
    assert combine_lists(num1, num2) == expected_output

def test_combine_sorted_lists_with_duplicates():
    num1 = [1, 2, 2, 3]
    num2 = [2, 3, 4]
    expected_output = [1, 2, 2, 2, 3, 3, 4]
    assert combine_lists(num1, num2) == expected_output

def test_combine_two_sorted_float_lists():
    num1 = [1.1, 2.2, 3.3]
    num2 = [2.0, 4.4]
    expected_output = [1.1, 2.0, 2.2, 3.3, 4.4]
    assert combine_lists(num1, num2) == expected_output

def test_combine_sorted_lists_one_all_smaller():
    num1 = [1, 2, 3]
    num2 = [10, 20, 30]
    expected_output = [1, 2, 3, 10, 20, 30]
    assert combine_lists(num1, num2) == expected_output

def test_combine_sorted_lists_with_negative_and_positive_integers():
    num1 = [-3, -1, 0]
    num2 = [-2, 1, 2]
    expected_output = [-3, -2, -1, 0, 1, 2]
    assert combine_lists(num1, num2) == expected_output
def count_even(array_nums):
   count_even = len(list(filter(lambda x: (x%2 == 0) , array_nums)))
   return count_even

import pytest

def test_count_even_mixed_even_and_odd():
    # Count even numbers in a list with mixed even and odd integers
    input_data = [1, 2, 3, 4, 5, 6]
    expected = 3
    assert count_even(input_data) == expected

def test_count_even_all_odd():
    # Count even numbers in a list with all odd integers
    input_data = [1, 3, 5, 7]
    expected = 0
    assert count_even(input_data) == expected

def test_count_even_all_even():
    # Count even numbers in a list with all even integers
    input_data = [2, 4, 6, 8]
    expected = 4
    assert count_even(input_data) == expected

def test_count_even_empty_list():
    # Count even numbers in an empty list
    input_data = []
    expected = 0
    assert count_even(input_data) == expected

def test_count_even_negative_and_positive():
    # Count even numbers in a list with negative and positive integers
    input_data = [-2, -1, 0, 1, 2]
    expected = 3
    assert count_even(input_data) == expected
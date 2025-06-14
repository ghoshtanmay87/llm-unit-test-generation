def sum_even_odd(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even+first_odd)

import pytest

def test_sum_even_odd_with_even_and_odd_numbers():
    # List with both even and odd numbers
    input_list = [2, 3, 4, 5]
    expected = 5
    assert sum_even_odd(input_list) == expected

def test_sum_even_odd_with_only_even_numbers():
    # List with only even numbers
    input_list = [4, 6, 8]
    expected = 3
    assert sum_even_odd(input_list) == expected

def test_sum_even_odd_with_only_odd_numbers():
    # List with only odd numbers
    input_list = [1, 3, 5]
    expected = 0
    assert sum_even_odd(input_list) == expected

def test_sum_even_odd_with_empty_list():
    # Empty list
    input_list = []
    expected = -2
    assert sum_even_odd(input_list) == expected

def test_sum_even_odd_with_negative_even_and_odd_numbers():
    # List with negative even and odd numbers
    input_list = [-4, -3, -2, -1]
    expected = -7
    assert sum_even_odd(input_list) == expected

def test_sum_even_odd_with_zero_and_odd_numbers():
    # List with zero and odd numbers
    input_list = [0, 7, 8]
    expected = 7
    assert sum_even_odd(input_list) == expected

def test_sum_even_odd_with_zero_only():
    # List with zero only
    input_list = [0]
    expected = -1
    assert sum_even_odd(input_list) == expected

def test_sum_even_odd_with_one_odd_number_only():
    # List with one odd number only
    input_list = [9]
    expected = 8
    assert sum_even_odd(input_list) == expected
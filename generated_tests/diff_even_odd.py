def diff_even_odd(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even-first_odd)

import pytest

def test_diff_even_odd_even_before_odd():
    # List contains both even and odd numbers, even appears before odd
    result = diff_even_odd([2, 3, 4, 5])
    assert result == -1

def test_diff_even_odd_odd_before_even():
    # List contains both even and odd numbers, odd appears before even
    result = diff_even_odd([7, 8, 10])
    assert result == 1

def test_diff_even_odd_only_even_numbers():
    # List contains only even numbers
    result = diff_even_odd([4, 6, 8])
    assert result == 5

def test_diff_even_odd_only_odd_numbers():
    # List contains only odd numbers
    result = diff_even_odd([1, 3, 5])
    assert result == -2

def test_diff_even_odd_empty_list():
    # List is empty
    result = diff_even_odd([])
    assert result == 0

def test_diff_even_odd_one_even_number_only():
    # List contains one even number only
    result = diff_even_odd([10])
    assert result == 11

def test_diff_even_odd_one_odd_number_only():
    # List contains one odd number only
    result = diff_even_odd([9])
    assert result == -10

def test_diff_even_odd_contains_zero_even():
    # List contains zero which is even
    result = diff_even_odd([0, 1, 2])
    assert result == -1
def is_equal_to_sum_even(n):
    return n % 2 == 0 and n >= 8

import pytest

def test_even_number_greater_or_equal_8():
    # Input is an even number greater than or equal to 8
    n = 10
    expected = True
    assert is_equal_to_sum_even(n) == expected

def test_even_number_less_than_8():
    # Input is an even number less than 8
    n = 6
    expected = False
    assert is_equal_to_sum_even(n) == expected

def test_odd_number_greater_than_8():
    # Input is an odd number greater than 8
    n = 9
    expected = False
    assert is_equal_to_sum_even(n) == expected

def test_odd_number_less_than_8():
    # Input is an odd number less than 8
    n = 3
    expected = False
    assert is_equal_to_sum_even(n) == expected

def test_input_exactly_8():
    # Input is exactly 8, which is even and equal to 8
    n = 8
    expected = True
    assert is_equal_to_sum_even(n) == expected

def test_input_zero():
    # Input is zero, which is even but less than 8
    n = 0
    expected = False
    assert is_equal_to_sum_even(n) == expected

def test_negative_even_less_than_8():
    # Input is a negative even number less than 8
    n = -2
    expected = False
    assert is_equal_to_sum_even(n) == expected

def test_negative_odd_less_than_8():
    # Input is a negative odd number less than 8
    n = -3
    expected = False
    assert is_equal_to_sum_even(n) == expected
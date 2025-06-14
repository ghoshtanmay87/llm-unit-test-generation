def swap_numbers(a,b):
 temp = a
 a = b
 b = temp
 return (a,b)

import pytest

def test_swap_two_positive_integers():
    # Swapping two positive integers: a=5, b=10
    result = swap_numbers(5, 10)
    assert result == (10, 5)

def test_swap_positive_and_negative_integer():
    # Swapping a positive and a negative integer: a=-3, b=7
    result = swap_numbers(-3, 7)
    assert result == (7, -3)

def test_swap_two_equal_numbers():
    # Swapping two equal numbers: a=4, b=4
    result = swap_numbers(4, 4)
    assert result == (4, 4)

def test_swap_zero_and_positive_number():
    # Swapping zero and a positive number: a=0, b=9
    result = swap_numbers(0, 9)
    assert result == (9, 0)

def test_swap_two_floating_point_numbers():
    # Swapping two floating point numbers: a=1.5, b=2.5
    result = swap_numbers(1.5, 2.5)
    assert result == (2.5, 1.5)
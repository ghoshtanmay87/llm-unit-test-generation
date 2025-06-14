def first_Digit(n) :  
    while n >= 10:  
        n = n / 10; 
    return int(n)

import pytest

def test_first_digit_single_digit_integer():
    # Input is a single-digit integer
    n = 7
    expected = 7
    assert first_Digit(n) == expected

def test_first_digit_two_digit_integer():
    # Input is a two-digit integer
    n = 42
    expected = 4
    assert first_Digit(n) == expected

def test_first_digit_three_digit_integer():
    # Input is a three-digit integer
    n = 365
    expected = 3
    assert first_Digit(n) == expected

def test_first_digit_large_integer():
    # Input is a large integer
    n = 987654321
    expected = 9
    assert first_Digit(n) == expected

def test_first_digit_exactly_ten():
    # Input is exactly 10
    n = 10
    expected = 1
    assert first_Digit(n) == expected

def test_first_digit_float_greater_than_ten():
    # Input is a floating point number greater than 10
    n = 123.45
    expected = 1
    assert first_Digit(n) == expected

def test_first_digit_float_less_than_ten():
    # Input is a floating point number less than 10
    n = 7.89
    expected = 7
    assert first_Digit(n) == expected
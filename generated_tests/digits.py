def digits(n):
    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        if int_digit % 2 == 1:
            product = product * int_digit
            odd_count += 1
    if odd_count == 0:
        return 0
    else:
        return product

import pytest

def test_digits_multiple_odd_digits():
    # Digits are 1, 3, 5, 7, 9; all are odd. Product = 1*3*5*7*9 = 945.
    assert digits(13579) == 945

def test_digits_no_odd_digits():
    # Digits are 2, 4, 6, 8; none are odd, so odd_count is 0 and function returns 0.
    assert digits(2468) == 0

def test_digits_some_odd_some_even_digits():
    # Digits are 1, 2, 3, 4; odd digits are 1 and 3. Product = 1*3 = 3.
    assert digits(1234) == 3

def test_digits_single_odd_digit():
    # Only one digit 7 which is odd, so product is 7.
    assert digits(7) == 7

def test_digits_single_even_digit():
    # Only one digit 8 which is even, so odd_count is 0 and function returns 0.
    assert digits(8) == 0

def test_digits_zero_digits_included():
    # Digits are 9, 0, 7, 0; odd digits are 9 and 7. Product = 9*7 = 63.
    assert digits(9070) == 63

def test_digits_repeated_odd_digits():
    # Digits are 1, 1, 1; all odd. Product = 1*1*1 = 1.
    assert digits(111) == 1
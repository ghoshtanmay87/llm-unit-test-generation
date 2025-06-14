def count_Digit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

import pytest

def test_count_digits_positive_multiple_digits():
    # Count digits of a positive integer with multiple digits
    n = 12345
    expected = 5
    assert count_Digit(n) == expected

def test_count_digits_single_digit_positive():
    # Count digits of a single-digit positive integer
    n = 7
    expected = 1
    assert count_Digit(n) == expected

def test_count_digits_zero():
    # Count digits of zero
    n = 0
    expected = 0
    assert count_Digit(n) == expected

def test_count_digits_large_positive():
    # Count digits of a large positive integer
    n = 1000000
    expected = 7
    assert count_Digit(n) == expected

def test_count_digits_negative_integer():
    # Count digits of a negative integer
    n = -123
    expected = 0
    assert count_Digit(n) == expected
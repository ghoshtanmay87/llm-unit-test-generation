def sum_digits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sum_digits(int(n / 10))

import pytest

def test_sum_digits_single_digit_positive():
    # Scenario: Sum digits of a single-digit positive number
    n = 7
    expected = 7
    assert sum_digits(n) == expected

def test_sum_digits_two_digit_positive():
    # Scenario: Sum digits of a two-digit positive number
    n = 42
    expected = 6
    assert sum_digits(n) == expected

def test_sum_digits_three_digit_positive():
    # Scenario: Sum digits of a three-digit positive number
    n = 123
    expected = 6
    assert sum_digits(n) == expected

def test_sum_digits_zero():
    # Scenario: Sum digits of zero
    n = 0
    expected = 0
    assert sum_digits(n) == expected

def test_sum_digits_trailing_zeros():
    # Scenario: Sum digits of a number with trailing zeros
    n = 1000
    expected = 1
    assert sum_digits(n) == expected

def test_sum_digits_large_number():
    # Scenario: Sum digits of a large number
    n = 987654321
    expected = 45
    assert sum_digits(n) == expected
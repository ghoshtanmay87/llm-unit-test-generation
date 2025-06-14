def multiply(a, b):
    return abs(a % 10) * abs(b % 10)

import pytest

def test_multiply_last_digits_two_positive_single_digit_numbers():
    # scenario: Multiply last digits of two positive single-digit numbers
    a = 3
    b = 7
    expected = 21
    assert multiply(a, b) == expected

def test_multiply_last_digits_one_negative_single_digit():
    # scenario: Multiply last digits when one number is negative single-digit
    a = -4
    b = 6
    expected = 36
    assert multiply(a, b) == expected

def test_multiply_last_digits_one_number_ends_with_zero():
    # scenario: Multiply last digits when one number ends with zero
    a = 20
    b = 3
    expected = 0
    assert multiply(a, b) == expected

def test_multiply_last_digits_both_numbers_end_with_zero():
    # scenario: Multiply last digits when both numbers end with zero
    a = 100
    b = 50
    expected = 0
    assert multiply(a, b) == expected

def test_multiply_last_digits_numbers_are_zero():
    # scenario: Multiply last digits when numbers are zero
    a = 0
    b = 0
    expected = 0
    assert multiply(a, b) == expected

def test_multiply_last_digits_large_negative_integers():
    # scenario: Multiply last digits when numbers are large negative integers
    a = -123456789
    b = -987654321
    expected = 9
    assert multiply(a, b) == expected

def test_multiply_last_digits_both_numbers_negative():
    # scenario: Multiply last digits when both numbers are negative
    a = -12
    b = -25
    expected = 40
    assert multiply(a, b) == expected

def test_multiply_last_digits_large_positive_integers():
    # scenario: Multiply last digits when numbers are large positive integers
    a = 123456789
    b = 987654321
    expected = 9
    assert multiply(a, b) == expected
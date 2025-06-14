def recur_gcd(a, b):
	low = min(a, b)
	high = max(a, b)
	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return recur_gcd(low, high%low)

import pytest

def test_gcd_one_number_zero():
    # Calculate GCD when one number is zero
    result = recur_gcd(0, 5)
    assert result == 5

def test_gcd_both_numbers_equal():
    # Calculate GCD when both numbers are equal
    result = recur_gcd(7, 7)
    assert result == 7

def test_gcd_two_positive_integers_gcd_one():
    # Calculate GCD of two positive integers where GCD is 1
    result = recur_gcd(8, 15)
    assert result == 1

def test_gcd_two_positive_integers_gcd_greater_than_one():
    # Calculate GCD of two positive integers where GCD is greater than 1
    result = recur_gcd(12, 18)
    assert result == 6

def test_gcd_one_number_is_one():
    # Calculate GCD when one number is 1
    result = recur_gcd(1, 999)
    assert result == 1

def test_gcd_two_large_numbers_common_divisor():
    # Calculate GCD of two large numbers with common divisor
    result = recur_gcd(100, 250)
    assert result == 50

def test_gcd_both_numbers_zero():
    # Calculate GCD when both inputs are zero
    result = recur_gcd(0, 0)
    assert result == 0
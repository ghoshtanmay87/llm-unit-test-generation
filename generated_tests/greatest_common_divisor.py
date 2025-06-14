def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = (b, a % b)
    return a

import pytest

def test_gcd_multiple_of_other():
    # Calculate GCD of two positive integers where one is a multiple of the other
    a = 20
    b = 5
    expected = 5
    assert greatest_common_divisor(a, b) == expected

def test_gcd_no_common_factors_other_than_one():
    # Calculate GCD of two positive integers with no common factors other than 1
    a = 17
    b = 13
    expected = 1
    assert greatest_common_divisor(a, b) == expected

def test_gcd_one_number_zero():
    # Calculate GCD when one number is zero
    a = 0
    b = 7
    expected = 7
    assert greatest_common_divisor(a, b) == expected

def test_gcd_both_numbers_equal():
    # Calculate GCD when both numbers are equal
    a = 9
    b = 9
    expected = 9
    assert greatest_common_divisor(a, b) == expected

def test_gcd_large_numbers_with_common_factors():
    # Calculate GCD of two large numbers with common factors
    a = 48
    b = 18
    expected = 6
    assert greatest_common_divisor(a, b) == expected
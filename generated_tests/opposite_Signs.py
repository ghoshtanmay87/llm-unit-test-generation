def opposite_Signs(x,y): 
    return ((x ^ y) < 0);

import pytest

def test_both_positive_numbers():
    # Both 5 and 10 are positive, so their sign bits are the same.
    # XOR of two positive numbers is non-negative, so (x ^ y) < 0 is False.
    assert opposite_Signs(5, 10) is False

def test_both_negative_numbers():
    # Both -3 and -7 are negative, so their sign bits are the same.
    # XOR of two negative numbers is non-negative, so (x ^ y) < 0 is False.
    assert opposite_Signs(-3, -7) is False

def test_one_positive_one_negative_number():
    # 4 is positive and -2 is negative, so their sign bits differ.
    # XOR of numbers with opposite signs has the sign bit set, so (x ^ y) < 0 is True.
    assert opposite_Signs(4, -2) is True

def test_zero_and_positive_number():
    # 0 is non-negative and 7 is positive, both have sign bit 0.
    # XOR is non-negative, so (x ^ y) < 0 is False.
    assert opposite_Signs(0, 7) is False

def test_zero_and_negative_number():
    # 0 is non-negative (sign bit 0) and -1 is negative (sign bit 1).
    # XOR has sign bit set, so (x ^ y) < 0 is True.
    assert opposite_Signs(0, -1) is True

def test_positive_and_negative_large_numbers():
    # 123456 is positive and -654321 is negative, so their sign bits differ.
    # XOR is negative, so (x ^ y) < 0 is True.
    assert opposite_Signs(123456, -654321) is True

def test_same_number_positive():
    # Both numbers are identical and positive, so XOR is zero (0), which is not less than zero.
    assert opposite_Signs(42, 42) is False

def test_same_number_negative():
    # Both numbers are identical and negative, XOR is zero (0), which is not less than zero.
    assert opposite_Signs(-42, -42) is False
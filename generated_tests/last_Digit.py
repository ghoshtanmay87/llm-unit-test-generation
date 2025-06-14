def last_Digit(n) :
    return (n % 10)

import pytest

def test_last_digit_positive_integer_ending_with_7():
    # Input is a positive integer ending with 7
    n = 27
    expected = 7
    assert last_Digit(n) == expected

def test_last_digit_zero():
    # Input is zero
    n = 0
    expected = 0
    assert last_Digit(n) == expected

def test_last_digit_positive_integer_ending_with_0():
    # Input is a positive integer ending with 0
    n = 100
    expected = 0
    assert last_Digit(n) == expected

def test_last_digit_positive_integer_ending_with_9():
    # Input is a positive integer ending with 9
    n = 999
    expected = 9
    assert last_Digit(n) == expected

def test_last_digit_negative_integer_ending_with_3():
    # Input is a negative integer ending with 3
    n = -13
    expected = 7
    assert last_Digit(n) == expected

def test_last_digit_negative_integer_ending_with_0():
    # Input is a negative integer ending with 0
    n = -20
    expected = 0
    assert last_Digit(n) == expected

def test_last_digit_large_positive_integer():
    # Input is a large positive integer
    n = 1234567890
    expected = 0
    assert last_Digit(n) == expected

def test_last_digit_large_negative_integer():
    # Input is a large negative integer
    n = -987654321
    expected = 9
    assert last_Digit(n) == expected
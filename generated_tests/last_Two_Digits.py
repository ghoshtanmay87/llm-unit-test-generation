def last_Two_Digits(N): 
    if (N >= 10): 
        return
    fac = 1
    for i in range(1,N + 1): 
        fac = (fac * i) % 100
    return (fac)

import pytest

def test_input_less_than_10_factorial_mod_100():
    # Input less than 10, compute factorial modulo 100
    result = last_Two_Digits(5)
    assert result == 20

def test_input_equal_to_10_returns_none():
    # Input equal to 10, function returns None
    result = last_Two_Digits(10)
    assert result is None

def test_input_greater_than_10_returns_none():
    # Input greater than 10, function returns None
    result = last_Two_Digits(12)
    assert result is None

def test_input_zero_factorial_mod_100():
    # Input is 0, factorial of 0 is 1 modulo 100
    result = last_Two_Digits(0)
    assert result == 1

def test_input_one_factorial_mod_100():
    # Input is 1, factorial of 1 is 1 modulo 100
    result = last_Two_Digits(1)
    assert result == 1

def test_input_nine_factorial_mod_100():
    # Input is 9, factorial modulo 100
    result = last_Two_Digits(9)
    assert result == 80
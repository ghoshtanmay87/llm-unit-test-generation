import math 
def find_Digits(n): 
    if (n < 0): 
        return 0;
    if (n <= 1): 
        return 1; 
    x = ((n * math.log10(n / math.e) + math.log10(2 * math.pi * n) /2.0)); 
    return math.floor(x) + 1;

import pytest

def test_find_digits_zero():
    # Calculate number of digits for n = 0
    result = find_Digits(0)
    assert result == 1

def test_find_digits_one():
    # Calculate number of digits for n = 1
    result = find_Digits(1)
    assert result == 1

def test_find_digits_negative():
    # Calculate number of digits for a negative number n = -5
    result = find_Digits(-5)
    assert result == 0

def test_find_digits_five():
    # Calculate number of digits for n = 5
    result = find_Digits(5)
    assert result == 3

def test_find_digits_ten():
    # Calculate number of digits for n = 10
    result = find_Digits(10)
    assert result == 7

def test_find_digits_hundred():
    # Calculate number of digits for n = 100
    result = find_Digits(100)
    assert result == 158
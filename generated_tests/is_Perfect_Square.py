def is_Perfect_Square(n) :
    i = 1
    while (i * i<= n):
        if ((n % i == 0) and (n / i == i)):
            return True     
        i = i + 1
    return False

import pytest

def test_is_Perfect_Square_with_16():
    # Check if 16 is a perfect square
    n = 16
    expected = True
    assert is_Perfect_Square(n) == expected

def test_is_Perfect_Square_with_14():
    # Check if 14 is a perfect square
    n = 14
    expected = False
    assert is_Perfect_Square(n) == expected

def test_is_Perfect_Square_with_1():
    # Check if 1 is a perfect square
    n = 1
    expected = True
    assert is_Perfect_Square(n) == expected

def test_is_Perfect_Square_with_0():
    # Check if 0 is a perfect square
    n = 0
    expected = False
    assert is_Perfect_Square(n) == expected

def test_is_Perfect_Square_with_25():
    # Check if 25 is a perfect square
    n = 25
    expected = True
    assert is_Perfect_Square(n) == expected

def test_is_Perfect_Square_with_26():
    # Check if 26 is a perfect square
    n = 26
    expected = False
    assert is_Perfect_Square(n) == expected

def test_is_Perfect_Square_with_100():
    # Check if 100 is a perfect square
    n = 100
    expected = True
    assert is_Perfect_Square(n) == expected

def test_is_Perfect_Square_with_99():
    # Check if 99 is a perfect square
    n = 99
    expected = False
    assert is_Perfect_Square(n) == expected
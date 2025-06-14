def is_prime(n):
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True

import pytest

def test_is_prime_with_1_returns_false():
    # Check if 1 is prime (less than 2)
    n = 1
    expected = False
    assert is_prime(n) == expected

def test_is_prime_with_2_returns_true():
    # Check if 2 is prime (smallest prime number)
    n = 2
    expected = True
    assert is_prime(n) == expected

def test_is_prime_with_3_returns_true():
    # Check if 3 is prime
    n = 3
    expected = True
    assert is_prime(n) == expected

def test_is_prime_with_4_returns_false():
    # Check if 4 is prime (composite number)
    n = 4
    expected = False
    assert is_prime(n) == expected

def test_is_prime_with_5_returns_true():
    # Check if 5 is prime
    n = 5
    expected = True
    assert is_prime(n) == expected

def test_is_prime_with_9_returns_false():
    # Check if 9 is prime (composite number)
    n = 9
    expected = False
    assert is_prime(n) == expected

def test_is_prime_with_11_returns_true():
    # Check if 11 is prime
    n = 11
    expected = True
    assert is_prime(n) == expected

def test_is_prime_with_15_returns_false():
    # Check if 15 is prime (composite number)
    n = 15
    expected = False
    assert is_prime(n) == expected

def test_is_prime_with_17_returns_true():
    # Check if 17 is prime
    n = 17
    expected = True
    assert is_prime(n) == expected

def test_is_prime_with_20_returns_false():
    # Check if 20 is prime (composite number)
    n = 20
    expected = False
    assert is_prime(n) == expected
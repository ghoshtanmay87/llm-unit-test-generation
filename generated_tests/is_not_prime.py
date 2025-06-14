import math
def is_not_prime(n):
    result = False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            result = True
    return result

import pytest

def test_is_not_prime_with_1():
    # Check if 1 is not prime
    n = 1
    expected = False
    assert is_not_prime(n) == expected

def test_is_not_prime_with_2():
    # Check if 2 is not prime
    n = 2
    expected = False
    assert is_not_prime(n) == expected

def test_is_not_prime_with_3():
    # Check if 3 is not prime
    n = 3
    expected = False
    assert is_not_prime(n) == expected

def test_is_not_prime_with_4():
    # Check if 4 is not prime
    n = 4
    expected = True
    assert is_not_prime(n) == expected

def test_is_not_prime_with_9():
    # Check if 9 is not prime
    n = 9
    expected = True
    assert is_not_prime(n) == expected

def test_is_not_prime_with_11():
    # Check if 11 is not prime
    n = 11
    expected = False
    assert is_not_prime(n) == expected

def test_is_not_prime_with_25():
    # Check if 25 is not prime
    n = 25
    expected = True
    assert is_not_prime(n) == expected

def test_is_not_prime_with_29():
    # Check if 29 is not prime
    n = 29
    expected = False
    assert is_not_prime(n) == expected

def test_is_not_prime_with_1000000():
    # Check if 1000000 is not prime
    n = 1000000
    expected = True
    assert is_not_prime(n) == expected
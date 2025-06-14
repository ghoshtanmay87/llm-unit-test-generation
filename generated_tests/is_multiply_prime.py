def is_multiply_prime(a):

    def is_prime(n):
        for j in range(2, n):
            if n % j == 0:
                return False
        return True
    for i in range(2, 101):
        if not is_prime(i):
            continue
        for j in range(2, 101):
            if not is_prime(j):
                continue
            for k in range(2, 101):
                if not is_prime(k):
                    continue
                if i * j * k == a:
                    return True
    return False

import pytest

def test_is_multiply_prime_30():
    # Check if 30 can be expressed as a product of three primes between 2 and 100
    a = 30
    expected = True
    assert is_multiply_prime(a) == expected

def test_is_multiply_prime_60():
    # Check if 60 can be expressed as a product of three primes between 2 and 100
    a = 60
    expected = False
    assert is_multiply_prime(a) == expected

def test_is_multiply_prime_125():
    # Check if 125 can be expressed as a product of three primes between 2 and 100
    a = 125
    expected = True
    assert is_multiply_prime(a) == expected

def test_is_multiply_prime_1():
    # Check if 1 can be expressed as a product of three primes between 2 and 100
    a = 1
    expected = False
    assert is_multiply_prime(a) == expected

def test_is_multiply_prime_8():
    # Check if 8 can be expressed as a product of three primes between 2 and 100
    a = 8
    expected = True
    assert is_multiply_prime(a) == expected

def test_is_multiply_prime_210():
    # Check if 210 can be expressed as a product of three primes between 2 and 100
    a = 210
    expected = False
    assert is_multiply_prime(a) == expected

def test_is_multiply_prime_343():
    # Check if 343 can be expressed as a product of three primes between 2 and 100
    a = 343
    expected = True
    assert is_multiply_prime(a) == expected

def test_is_multiply_prime_1000():
    # Check if 1000 can be expressed as a product of three primes between 2 and 100
    a = 1000
    expected = False
    assert is_multiply_prime(a) == expected
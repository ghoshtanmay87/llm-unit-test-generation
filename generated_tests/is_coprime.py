def gcd(p,q):
    while q != 0:
        p, q = q,p%q
    return p
def is_coprime(x,y):
    return gcd(x,y) == 1

import pytest

def test_coprime_14_and_15():
    # The gcd of 14 and 15 is 1, so they are coprime.
    assert is_coprime(14, 15) is True

def test_not_coprime_12_and_18():
    # The gcd of 12 and 18 is 6, which is greater than 1, so they are not coprime.
    assert is_coprime(12, 18) is False

def test_coprime_17_and_19():
    # The gcd of 17 and 19 is 1, so they are coprime.
    assert is_coprime(17, 19) is True

def test_not_coprime_21_and_28():
    # The gcd of 21 and 28 is 7, which is greater than 1, so they are not coprime.
    assert is_coprime(21, 28) is False

def test_coprime_1_and_100():
    # The gcd of 1 and any number is 1, so they are coprime.
    assert is_coprime(1, 100) is True

def test_not_coprime_0_and_5():
    # The gcd of 0 and 5 is 5, not 1, so they are not coprime.
    assert is_coprime(0, 5) is False

def test_not_coprime_13_and_0():
    # The gcd of 13 and 0 is 13, not 1, so they are not coprime.
    assert is_coprime(13, 0) is False

def test_not_coprime_0_and_0():
    # The gcd of 0 and 0 is 0, not 1, so they are not coprime.
    assert is_coprime(0, 0) is False
def gcd(x, y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break  
    return gcd

import pytest

def test_gcd_divisible_returns_y():
    # When x is divisible by y, gcd should be y
    x = 20
    y = 5
    expected = 5
    assert gcd(x, y) == expected

def test_gcd_not_divisible_finds_greatest_divisor():
    # When x is not divisible by y, find the greatest divisor of both starting from y//2
    x = 12
    y = 8
    expected = 4
    assert gcd(x, y) == expected

def test_gcd_coprime_returns_1():
    # When x and y are coprime, gcd should be 1
    x = 17
    y = 4
    expected = 1
    assert gcd(x, y) == expected

def test_gcd_x_equals_y_returns_y():
    # When x equals y, gcd should be y
    x = 7
    y = 7
    expected = 7
    assert gcd(x, y) == expected

def test_gcd_y_is_1_returns_1():
    # When y is 1, gcd should be 1
    x = 100
    y = 1
    expected = 1
    assert gcd(x, y) == expected

def test_gcd_x_smaller_than_y_not_divisible_returns_1():
    # When x is smaller than y and not divisible, gcd is found by checking divisors
    x = 5
    y = 12
    expected = 1
    assert gcd(x, y) == expected

def test_gcd_both_even_not_divisible_returns_largest_even_divisor():
    # When both numbers are even and not divisible, gcd is the largest even divisor
    x = 14
    y = 8
    expected = 2
    assert gcd(x, y) == expected
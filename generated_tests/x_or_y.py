def x_or_y(n, x, y):
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x

import pytest

def test_n_is_1_should_return_y_immediately():
    # Since n == 1, the function returns y immediately without further checks.
    result = x_or_y(n=1, x=10, y=20)
    assert result == 20

def test_n_is_prime_should_return_x():
    # n=7 is prime, so the for loop finds no divisor between 2 and 6, thus the else clause executes returning x.
    result = x_or_y(n=7, x=100, y=200)
    assert result == 100

def test_n_is_composite_should_return_y():
    # n=8 is composite, divisible by 2, so the function returns y inside the loop.
    result = x_or_y(n=8, x=5, y=15)
    assert result == 15

def test_n_is_2_prime_should_return_x():
    # For n=2, the for loop range(2,2) is empty, so the else clause executes returning x.
    result = x_or_y(n=2, x=7, y=9)
    assert result == 7

def test_n_is_large_prime_should_return_x():
    # n=13 is prime, no divisors found in the loop, so else clause returns x.
    result = x_or_y(n=13, x=50, y=100)
    assert result == 50

def test_n_is_large_composite_should_return_y():
    # n=15 is composite, divisible by 3, so function returns y inside the loop.
    result = x_or_y(n=15, x=1, y=2)
    assert result == 2
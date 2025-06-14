def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

import pytest

def test_fib_base_case_zero():
    # Calculate fib(0), the base case for zero
    result = fib(0)
    assert result == 0

def test_fib_base_case_one():
    # Calculate fib(1), the base case for one
    result = fib(1)
    assert result == 1

def test_fib_two():
    # Calculate fib(2), sum of fib(1) and fib(0)
    result = fib(2)
    assert result == 1

def test_fib_three():
    # Calculate fib(3), sum of fib(2) and fib(1)
    result = fib(3)
    assert result == 2

def test_fib_four():
    # Calculate fib(4), sum of fib(3) and fib(2)
    result = fib(4)
    assert result == 3

def test_fib_five():
    # Calculate fib(5), sum of fib(4) and fib(3)
    result = fib(5)
    assert result == 5

def test_fib_six():
    # Calculate fib(6), sum of fib(5) and fib(4)
    result = fib(6)
    assert result == 8

def test_fib_seven():
    # Calculate fib(7), sum of fib(6) and fib(5)
    result = fib(7)
    assert result == 13
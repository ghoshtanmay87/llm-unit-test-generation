def prime_fib(n: int):
    import math

    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            if p % k == 0:
                return False
        return True
    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]

import pytest

def test_find_1st_prime_fibonacci_number():
    # The first prime Fibonacci number is 2
    result = prime_fib(1)
    assert result == 2

def test_find_2nd_prime_fibonacci_number():
    # The second prime Fibonacci number is 3
    result = prime_fib(2)
    assert result == 3

def test_find_3rd_prime_fibonacci_number():
    # The third prime Fibonacci number is 5
    result = prime_fib(3)
    assert result == 5

def test_find_5th_prime_fibonacci_number():
    # The fifth prime Fibonacci number is 89
    result = prime_fib(5)
    assert result == 89

def test_find_6th_prime_fibonacci_number():
    # The sixth prime Fibonacci number is 233
    result = prime_fib(6)
    assert result == 233

def test_find_7th_prime_fibonacci_number():
    # The seventh prime Fibonacci number is 1597
    result = prime_fib(7)
    assert result == 1597
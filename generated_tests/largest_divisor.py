def largest_divisor(n: int) -> int:
    for i in reversed(range(n)):
        if n % i == 0:
            return i

import pytest

def test_largest_divisor_of_10():
    # Find largest divisor of 10 excluding itself
    result = largest_divisor(10)
    assert result == 5

def test_largest_divisor_of_15():
    # Find largest divisor of 15 excluding itself
    result = largest_divisor(15)
    assert result == 5

def test_largest_divisor_of_prime_13():
    # Find largest divisor of 13 (a prime number) excluding itself
    result = largest_divisor(13)
    assert result == 1

def test_largest_divisor_of_2():
    # Find largest divisor of 2 excluding itself
    result = largest_divisor(2)
    assert result == 1

def test_largest_divisor_of_100():
    # Find largest divisor of 100 excluding itself
    result = largest_divisor(100)
    assert result == 50
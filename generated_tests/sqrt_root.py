import math
def sqrt_root(num):
 sqrt_root = math.pow(num, 0.5)
 return sqrt_root

import pytest

def test_sqrt_root_perfect_square():
    # Calculate square root of a perfect square
    result = sqrt_root(16)
    assert result == 4.0

def test_sqrt_root_non_perfect_square():
    # Calculate square root of a non-perfect square
    result = sqrt_root(20)
    assert result == 4.47213595499958

def test_sqrt_root_zero():
    # Calculate square root of zero
    result = sqrt_root(0)
    assert result == 0.0

def test_sqrt_root_one():
    # Calculate square root of one
    result = sqrt_root(1)
    assert result == 1.0

def test_sqrt_root_large_number():
    # Calculate square root of a large number
    result = sqrt_root(1000000)
    assert result == 1000.0
import math  
def next_Perfect_Square(N): 
    nextN = math.floor(math.sqrt(N)) + 1
    return nextN * nextN

import pytest

def test_next_perfect_square_perfect_square_16():
    # Input is a perfect square number 16
    result = next_Perfect_Square(16)
    assert result == 25

def test_next_perfect_square_non_perfect_square_20():
    # Input is a non-perfect square number 20
    result = next_Perfect_Square(20)
    assert result == 25

def test_next_perfect_square_zero():
    # Input is 0, the smallest perfect square
    result = next_Perfect_Square(0)
    assert result == 1

def test_next_perfect_square_one():
    # Input is 1, the smallest positive perfect square
    result = next_Perfect_Square(1)
    assert result == 4

def test_next_perfect_square_large_perfect_square_10000():
    # Input is a large perfect square 10000
    result = next_Perfect_Square(10000)
    assert result == 10201

def test_next_perfect_square_large_non_perfect_square_9999():
    # Input is a large non-perfect square 9999
    result = next_Perfect_Square(9999)
    assert result == 10000

def test_next_perfect_square_small_non_perfect_square_2():
    # Input is 2, a small non-perfect square
    result = next_Perfect_Square(2)
    assert result == 4
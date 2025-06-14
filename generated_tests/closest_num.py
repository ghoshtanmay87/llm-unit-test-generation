def closest_num(N):
  return (N - 1)

import pytest

def test_closest_num_positive_integer():
    # Input is a positive integer
    result = closest_num(10)
    assert result == 9

def test_closest_num_zero():
    # Input is zero
    result = closest_num(0)
    assert result == -1

def test_closest_num_negative_integer():
    # Input is a negative integer
    result = closest_num(-5)
    assert result == -6

def test_closest_num_positive_float():
    # Input is a positive float
    result = closest_num(3.5)
    assert result == 2.5

def test_closest_num_one():
    # Input is one
    result = closest_num(1)
    assert result == 0
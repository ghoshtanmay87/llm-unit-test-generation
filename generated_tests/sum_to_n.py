def sum_to_n(n: int):
    return sum(range(n + 1))

import pytest

def test_sum_to_n_zero():
    # Sum of numbers from 0 to 0
    result = sum_to_n(0)
    assert result == 0

def test_sum_to_n_one():
    # Sum of numbers from 0 to 1
    result = sum_to_n(1)
    assert result == 1

def test_sum_to_n_five():
    # Sum of numbers from 0 to 5
    result = sum_to_n(5)
    assert result == 15

def test_sum_to_n_ten():
    # Sum of numbers from 0 to 10
    result = sum_to_n(10)
    assert result == 55

def test_sum_to_n_hundred():
    # Sum of numbers from 0 to 100
    result = sum_to_n(100)
    assert result == 5050
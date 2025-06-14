def sum_difference(n):
    sumofsquares = 0
    squareofsum = 0
    for num in range(1, n+1):
        sumofsquares += num * num
        squareofsum += num
    squareofsum = squareofsum ** 2
    return squareofsum - sumofsquares

import pytest

def test_sum_difference_n_1():
    # For n=1, difference should be 0
    result = sum_difference(1)
    assert result == 0

def test_sum_difference_n_2():
    # For n=2, difference should be 4
    result = sum_difference(2)
    assert result == 4

def test_sum_difference_n_3():
    # For n=3, difference should be 22
    result = sum_difference(3)
    assert result == 22

def test_sum_difference_n_5():
    # For n=5, difference should be 170
    result = sum_difference(5)
    assert result == 170

def test_sum_difference_n_10():
    # For n=10, difference should be 2640
    result = sum_difference(10)
    assert result == 2640
def square_Sum(n):  
    return int(2*n*(n+1)*(2*n+1)/3)

import pytest

def test_square_sum_n_1():
    # Calculate square sum for n=1
    result = square_Sum(1)
    assert result == 4

def test_square_sum_n_2():
    # Calculate square sum for n=2
    result = square_Sum(2)
    assert result == 20

def test_square_sum_n_3():
    # Calculate square sum for n=3
    result = square_Sum(3)
    assert result == 56

def test_square_sum_n_0():
    # Calculate square sum for n=0
    result = square_Sum(0)
    assert result == 0

def test_square_sum_n_5():
    # Calculate square sum for n=5
    result = square_Sum(5)
    assert result == 220
def hexagonal_num(n): 
	return n*(2*n - 1)

import pytest

def test_hexagonal_num_n_1():
    assert hexagonal_num(1) == 1

def test_hexagonal_num_n_2():
    assert hexagonal_num(2) == 6

def test_hexagonal_num_n_3():
    assert hexagonal_num(3) == 15

def test_hexagonal_num_n_4():
    assert hexagonal_num(4) == 28

def test_hexagonal_num_n_5():
    assert hexagonal_num(5) == 45

def test_hexagonal_num_n_10():
    assert hexagonal_num(10) == 190

def test_hexagonal_num_n_0():
    assert hexagonal_num(0) == 0

def test_hexagonal_num_n_100():
    assert hexagonal_num(100) == 19900
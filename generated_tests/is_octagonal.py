def is_octagonal(n): 
	return 3 * n * n - 2 * n

import pytest

def test_is_octagonal_n_0():
    # Check output for n=0
    assert is_octagonal(0) == 0

def test_is_octagonal_n_1():
    # Check output for n=1
    assert is_octagonal(1) == 1

def test_is_octagonal_n_2():
    # Check output for n=2
    assert is_octagonal(2) == 8

def test_is_octagonal_n_3():
    # Check output for n=3
    assert is_octagonal(3) == 21

def test_is_octagonal_n_4():
    # Check output for n=4
    assert is_octagonal(4) == 40

def test_is_octagonal_n_5():
    # Check output for n=5
    assert is_octagonal(5) == 65

def test_is_octagonal_n_10():
    # Check output for n=10
    assert is_octagonal(10) == 280

def test_is_octagonal_n_100():
    # Check output for n=100
    assert is_octagonal(100) == 29800
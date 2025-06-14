def is_num_decagonal(n): 
	return 4 * n * n - 3 * n

import pytest

def test_is_num_decagonal_n_0():
    # Check the output for n=0
    result = is_num_decagonal(0)
    assert result == 0

def test_is_num_decagonal_n_1():
    # Check the output for n=1
    result = is_num_decagonal(1)
    assert result == 1

def test_is_num_decagonal_n_2():
    # Check the output for n=2
    result = is_num_decagonal(2)
    assert result == 10

def test_is_num_decagonal_n_3():
    # Check the output for n=3
    result = is_num_decagonal(3)
    assert result == 27

def test_is_num_decagonal_n_4():
    # Check the output for n=4
    result = is_num_decagonal(4)
    assert result == 52

def test_is_num_decagonal_n_5():
    # Check the output for n=5
    result = is_num_decagonal(5)
    assert result == 85
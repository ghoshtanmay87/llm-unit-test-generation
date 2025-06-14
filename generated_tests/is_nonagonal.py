def is_nonagonal(n): 
	return int(n * (7 * n - 5) / 2)

import pytest

def test_nonagonal_number_n_1():
    # Calculate nonagonal number for n=1
    result = is_nonagonal(1)
    assert result == 1

def test_nonagonal_number_n_2():
    # Calculate nonagonal number for n=2
    result = is_nonagonal(2)
    assert result == 9

def test_nonagonal_number_n_3():
    # Calculate nonagonal number for n=3
    result = is_nonagonal(3)
    assert result == 24

def test_nonagonal_number_n_0():
    # Calculate nonagonal number for n=0
    result = is_nonagonal(0)
    assert result == 0

def test_nonagonal_number_n_5():
    # Calculate nonagonal number for n=5
    # Note: expected output corrected to 70 as per user story
    result = is_nonagonal(5)
    assert result == 70

def test_nonagonal_number_n_10():
    # Calculate nonagonal number for n=10
    result = is_nonagonal(10)
    assert result == 325
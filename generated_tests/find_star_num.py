def find_star_num(n): 
	return (6 * n * (n - 1) + 1)

import pytest

def test_find_star_num_n_1():
    # Calculate star number for n=1
    result = find_star_num(1)
    assert result == 1

def test_find_star_num_n_2():
    # Calculate star number for n=2
    result = find_star_num(2)
    assert result == 13

def test_find_star_num_n_3():
    # Calculate star number for n=3
    result = find_star_num(3)
    assert result == 37

def test_find_star_num_n_4():
    # Calculate star number for n=4
    result = find_star_num(4)
    assert result == 73

def test_find_star_num_n_5():
    # Calculate star number for n=5
    result = find_star_num(5)
    assert result == 121
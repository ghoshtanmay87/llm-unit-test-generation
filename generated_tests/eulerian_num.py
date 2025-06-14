def eulerian_num(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))

import pytest

def test_base_case_n_zero():
    # Base case when n is 0
    result = eulerian_num(0, 0)
    assert result == 0

def test_case_m_greater_equal_n():
    # Case when m >= n
    result = eulerian_num(3, 3)
    assert result == 0

def test_case_m_zero_n_positive():
    # Case when m is 0 and n > 0
    result = eulerian_num(4, 0)
    assert result == 1

def test_calculate_eulerian_num_31():
    # Calculate eulerian_num(3,1)
    result = eulerian_num(3, 1)
    assert result == 4

def test_calculate_eulerian_num_42():
    # Calculate eulerian_num(4,2)
    result = eulerian_num(4, 2)
    assert result == 11

def test_calculate_eulerian_num_52():
    # Calculate eulerian_num(5,2)
    result = eulerian_num(5, 2)
    assert result == 66
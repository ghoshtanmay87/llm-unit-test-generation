def jacobsthal_num(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]

import pytest

def test_jacobsthal_num_n_0():
    # Calculate Jacobsthal number for n=0
    result = jacobsthal_num(0)
    assert result == 0

def test_jacobsthal_num_n_1():
    # Calculate Jacobsthal number for n=1
    result = jacobsthal_num(1)
    assert result == 1

def test_jacobsthal_num_n_2():
    # Calculate Jacobsthal number for n=2
    result = jacobsthal_num(2)
    assert result == 1

def test_jacobsthal_num_n_3():
    # Calculate Jacobsthal number for n=3
    result = jacobsthal_num(3)
    assert result == 3

def test_jacobsthal_num_n_4():
    # Calculate Jacobsthal number for n=4
    result = jacobsthal_num(4)
    assert result == 5

def test_jacobsthal_num_n_5():
    # Calculate Jacobsthal number for n=5
    result = jacobsthal_num(5)
    assert result == 11

def test_jacobsthal_num_n_6():
    # Calculate Jacobsthal number for n=6
    result = jacobsthal_num(6)
    assert result == 21

def test_jacobsthal_num_n_7():
    # Calculate Jacobsthal number for n=7
    result = jacobsthal_num(7)
    assert result == 43
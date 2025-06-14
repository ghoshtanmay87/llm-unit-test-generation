def jacobsthal_lucas(n): 
	dp=[0] * (n + 1) 
	dp[0] = 2
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2]; 
	return dp[n]

import pytest

def test_jacobsthal_lucas_base_case_n_0():
    # Calculate jacobsthal_lucas for n=0 (base case)
    result = jacobsthal_lucas(0)
    assert result == 2

def test_jacobsthal_lucas_base_case_n_1():
    # Calculate jacobsthal_lucas for n=1 (base case)
    result = jacobsthal_lucas(1)
    assert result == 1

def test_jacobsthal_lucas_n_2():
    # Calculate jacobsthal_lucas for n=2
    result = jacobsthal_lucas(2)
    assert result == 5

def test_jacobsthal_lucas_n_3():
    # Calculate jacobsthal_lucas for n=3
    result = jacobsthal_lucas(3)
    assert result == 7

def test_jacobsthal_lucas_n_4():
    # Calculate jacobsthal_lucas for n=4
    result = jacobsthal_lucas(4)
    assert result == 17

def test_jacobsthal_lucas_n_5():
    # Calculate jacobsthal_lucas for n=5
    result = jacobsthal_lucas(5)
    assert result == 31
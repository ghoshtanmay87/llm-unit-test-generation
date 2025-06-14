MAX = 1000000
def breakSum(n): 
	dp = [0]*(n+1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = max(dp[int(i/2)] + dp[int(i/3)] + dp[int(i/4)], i); 
	return dp[n]

import pytest

def test_breakSum_base_case_1():
    # Input is 1, base case
    n = 1
    expected = 1
    assert breakSum(n) == expected

def test_breakSum_small_number_2():
    # Input is 2, small number where breaking is not beneficial
    n = 2
    expected = 2
    assert breakSum(n) == expected

def test_breakSum_breaking_beneficial_12():
    # Input is 12, where breaking is beneficial
    n = 12
    expected = 13
    assert breakSum(n) == expected

def test_breakSum_larger_number_24():
    # Input is 24, larger number to test recursion
    n = 24
    expected = 27
    assert breakSum(n) == expected

def test_breakSum_larger_input_100():
    # Input is 100, to test larger input
    n = 100
    expected = 120
    assert breakSum(n) == expected
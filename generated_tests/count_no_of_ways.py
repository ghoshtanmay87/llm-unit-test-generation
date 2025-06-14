def count_no_of_ways(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]

import pytest

def test_count_no_of_ways_n1_k3():
    # Calculate number of ways for n=1, k=3
    n = 1
    k = 3
    expected_output = 3
    assert count_no_of_ways(n, k) == expected_output

def test_count_no_of_ways_n2_k3():
    # Calculate number of ways for n=2, k=3
    n = 2
    k = 3
    expected_output = 9
    assert count_no_of_ways(n, k) == expected_output

def test_count_no_of_ways_n3_k3():
    # Calculate number of ways for n=3, k=3
    n = 3
    k = 3
    expected_output = 24
    assert count_no_of_ways(n, k) == expected_output

def test_count_no_of_ways_n4_k2():
    # Calculate number of ways for n=4, k=2
    n = 4
    k = 2
    expected_output = 10
    assert count_no_of_ways(n, k) == expected_output

def test_count_no_of_ways_n5_k1():
    # Calculate number of ways for n=5, k=1
    n = 5
    k = 1
    expected_output = 0
    assert count_no_of_ways(n, k) == expected_output

def test_count_no_of_ways_n3_k4():
    # Calculate number of ways for n=3, k=4
    n = 3
    k = 4
    expected_output = 60
    assert count_no_of_ways(n, k) == expected_output
def nCr(n, r): 
	if (r > n / 2): 
		r = n - r 
	answer = 1 
	for i in range(1, r + 1): 
		answer *= (n - r + i) 
		answer /= i 
	return answer 
def binomial_probability(n, k, p): 
	return (nCr(n, k) * pow(p, k) *	pow(1 - p, n - k))

import pytest

def test_binomial_probability_n5_k2_p05():
    # Calculate binomial probability for n=5, k=2, p=0.5
    result = binomial_probability(n=5, k=2, p=0.5)
    assert result == 0.3125

def test_binomial_probability_n10_k0_p01():
    # Calculate binomial probability for n=10, k=0, p=0.1
    result = binomial_probability(n=10, k=0, p=0.1)
    assert result == 0.3486784401

def test_binomial_probability_n4_k4_p07():
    # Calculate binomial probability for n=4, k=4, p=0.7
    result = binomial_probability(n=4, k=4, p=0.7)
    assert result == 0.2401

def test_binomial_probability_n6_k3_p02():
    # Calculate binomial probability for n=6, k=3, p=0.2
    result = binomial_probability(n=6, k=3, p=0.2)
    assert result == 0.098304

def test_binomial_probability_n8_k5_p03():
    # Calculate binomial probability for n=8, k=5, p=0.3
    result = binomial_probability(n=8, k=5, p=0.3)
    assert result == 0.086871168
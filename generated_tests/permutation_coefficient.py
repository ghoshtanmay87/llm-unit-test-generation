def permutation_coefficient(n, k): 
	P = [[0 for i in range(k + 1)] 
			for j in range(n + 1)] 
	for i in range(n + 1): 
		for j in range(min(i, k) + 1): 
			if (j == 0): 
				P[i][j] = 1
			else: 
				P[i][j] = P[i - 1][j] + ( 
						j * P[i - 1][j - 1]) 
			if (j < k): 
				P[i][j + 1] = 0
	return P[n][k]

import pytest

def test_permutation_coefficient_n5_k3():
    # Calculate permutation coefficient for n=5, k=3
    result = permutation_coefficient(5, 3)
    assert result == 60

def test_permutation_coefficient_n4_k2():
    # Calculate permutation coefficient for n=4, k=2
    result = permutation_coefficient(4, 2)
    assert result == 12

def test_permutation_coefficient_n3_k3():
    # Calculate permutation coefficient for n=3, k=3
    result = permutation_coefficient(3, 3)
    assert result == 6

def test_permutation_coefficient_n6_k0():
    # Calculate permutation coefficient for n=6, k=0
    result = permutation_coefficient(6, 0)
    assert result == 1

def test_permutation_coefficient_n0_k0():
    # Calculate permutation coefficient for n=0, k=0
    result = permutation_coefficient(0, 0)
    assert result == 1

def test_permutation_coefficient_n7_k1():
    # Calculate permutation coefficient for n=7, k=1
    result = permutation_coefficient(7, 1)
    assert result == 7
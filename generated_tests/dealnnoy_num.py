def dealnnoy_num(n, m): 
	if (m == 0 or n == 0) : 
		return 1
	return dealnnoy_num(m - 1, n) + dealnnoy_num(m - 1, n - 1) + dealnnoy_num(m, n - 1)

import pytest

def test_base_case_both_zero():
    # Base case when both n and m are zero
    n = 0
    m = 0
    expected = 1
    assert dealnnoy_num(n, m) == expected

def test_base_case_n_zero_m_positive():
    # Base case when n is zero and m is positive
    n = 0
    m = 3
    expected = 1
    assert dealnnoy_num(n, m) == expected

def test_base_case_m_zero_n_positive():
    # Base case when m is zero and n is positive
    n = 4
    m = 0
    expected = 1
    assert dealnnoy_num(n, m) == expected

def test_small_values_n1_m1():
    # Small values n=1, m=1
    n = 1
    m = 1
    expected = 3
    assert dealnnoy_num(n, m) == expected

def test_small_values_n2_m1():
    # Small values n=2, m=1
    n = 2
    m = 1
    expected = 5
    assert dealnnoy_num(n, m) == expected

def test_small_values_n1_m2():
    # Small values n=1, m=2
    n = 1
    m = 2
    expected = 5
    assert dealnnoy_num(n, m) == expected

def test_values_n2_m2():
    # Values n=2, m=2
    n = 2
    m = 2
    expected = 13
    assert dealnnoy_num(n, m) == expected

def test_values_n3_m2():
    # Values n=3, m=2
    n = 3
    m = 2
    expected = 25
    assert dealnnoy_num(n, m) == expected

def test_values_n3_m3():
    # Values n=3, m=3
    n = 3
    m = 3
    expected = 63
    assert dealnnoy_num(n, m) == expected
def binomial_coeffi(n, k): 
	if (k == 0 or k == n): 
		return 1
	return (binomial_coeffi(n - 1, k - 1) 
		+ binomial_coeffi(n - 1, k)) 
def rencontres_number(n, m): 
	if (n == 0 and m == 0): 
		return 1
	if (n == 1 and m == 0): 
		return 0
	if (m == 0): 
		return ((n - 1) * (rencontres_number(n - 1, 0)+ rencontres_number(n - 2, 0))) 
	return (binomial_coeffi(n, m) * rencontres_number(n - m, 0))

import pytest

def test_rencontres_number_base_case_0_0():
    # The function returns 1 directly when n and m are both 0 as per the first if condition.
    assert rencontres_number(0, 0) == 1

def test_rencontres_number_base_case_1_0():
    # The function returns 0 directly when n is 1 and m is 0 as per the second if condition.
    assert rencontres_number(1, 0) == 0

def test_rencontres_number_recursion_2_0():
    # For n=2, m=0, the function returns (n-1)*(rencontres_number(10)+rencontres_number(00)) = 1*(0+1) = 1.
    assert rencontres_number(2, 0) == 1

def test_rencontres_number_recursion_3_0():
    # For n=3, m=0, the function returns (3-1)*(rencontres_number(20)+rencontres_number(10)) = 2*(1+0) = 2.
    assert rencontres_number(3, 0) == 2

def test_rencontres_number_recursion_4_0():
    # For n=4, m=0, the function returns (4-1)*(rencontres_number(30)+rencontres_number(20)) = 3*(2+1) = 9.
    assert rencontres_number(4, 0) == 9

def test_rencontres_number_binomial_4_1():
    # For m>0, the function returns binomial_coeffi(4,1)*rencontres_number(3,0).
    # binomial_coeffi(4,1) = 4, rencontres_number(3,0) = 2, so 4*2=8.
    assert rencontres_number(4, 1) == 8

def test_rencontres_number_binomial_5_2():
    # For m>0, the function returns binomial_coeffi(5,2)*rencontres_number(3,0).
    # binomial_coeffi(5,2) = 10, rencontres_number(3,0) = 2, so 10*2=20.
    assert rencontres_number(5, 2) == 20
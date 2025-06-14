def binomial_Coeff(n,k): 
    if k > n : 
       return 0
    if k==0 or k ==n : 
        return 1 
    return binomial_Coeff(n-1,k-1) + binomial_Coeff(n-1,k)

import pytest

def test_binomial_coeff_k_greater_than_n():
    # Since k (5) is greater than n (3), the function returns 0 immediately as per the first condition.
    assert binomial_Coeff(3, 5) == 0

def test_binomial_coeff_k_equals_zero():
    # When k is 0, the function returns 1 as per the second condition, representing the number of ways to choose 0 items.
    assert binomial_Coeff(4, 0) == 1

def test_binomial_coeff_k_equals_n():
    # When k equals n, the function returns 1 as per the second condition, representing the number of ways to choose all items.
    assert binomial_Coeff(5, 5) == 1

def test_binomial_coeff_n_5_k_2():
    # Using the recursive formula: C(5,2) = C(4,1) + C(4,2). C(4,1)=4 and C(4,2)=6, so total is 10.
    assert binomial_Coeff(5, 2) == 10

def test_binomial_coeff_n_6_k_3():
    # Using the recursive formula: C(6,3) = C(5,2) + C(5,3). From previous calculation, C(5,2)=10 and C(5,3)=10, total is 20.
    assert binomial_Coeff(6, 3) == 20

def test_binomial_coeff_n_0_k_0():
    # When n and k are both zero, the function returns 1 as per the second condition, representing the base case.
    assert binomial_Coeff(0, 0) == 1
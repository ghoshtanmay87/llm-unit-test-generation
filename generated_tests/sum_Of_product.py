def binomial_Coeff(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def sum_Of_product(n): 
    return binomial_Coeff(2 * n,n - 1);

import pytest

def test_sum_Of_product_n_1():
    # Scenario: Calculate sum_Of_product for n=1
    # Expected output: 1
    result = sum_Of_product(1)
    assert result == 1

def test_sum_Of_product_n_2():
    # Scenario: Calculate sum_Of_product for n=2
    # Expected output: 4
    result = sum_Of_product(2)
    assert result == 4

def test_sum_Of_product_n_3():
    # Scenario: Calculate sum_Of_product for n=3
    # Expected output: 15
    result = sum_Of_product(3)
    assert result == 15

def test_sum_Of_product_n_4():
    # Scenario: Calculate sum_Of_product for n=4
    # Expected output: 56
    result = sum_Of_product(4)
    assert result == 56

def test_sum_Of_product_n_5():
    # Scenario: Calculate sum_Of_product for n=5
    # Expected output: 210
    result = sum_Of_product(5)
    assert result == 210
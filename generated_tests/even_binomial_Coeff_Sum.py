import math  
def even_binomial_Coeff_Sum( n): 
    return (1 << (n - 1))

import pytest

def test_sum_binomial_coefficients_even_indices_n_1():
    # For n=1, expected output is 1
    assert even_binomial_Coeff_Sum(1) == 1

def test_sum_binomial_coefficients_even_indices_n_2():
    # For n=2, expected output is 2
    assert even_binomial_Coeff_Sum(2) == 2

def test_sum_binomial_coefficients_even_indices_n_3():
    # For n=3, expected output is 4
    assert even_binomial_Coeff_Sum(3) == 4

def test_sum_binomial_coefficients_even_indices_n_4():
    # For n=4, expected output is 8
    assert even_binomial_Coeff_Sum(4) == 8

def test_sum_binomial_coefficients_even_indices_n_5():
    # For n=5, expected output is 16
    assert even_binomial_Coeff_Sum(5) == 16
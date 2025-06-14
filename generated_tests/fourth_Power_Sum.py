import math  
def fourth_Power_Sum(n): 
    sum = 0
    for i in range(1,n+1) : 
        sum = sum + (i*i*i*i) 
    return sum

import pytest

def test_sum_fourth_powers_n_1():
    # Calculate the sum of fourth powers from 1 to 1
    result = fourth_Power_Sum(1)
    assert result == 1

def test_sum_fourth_powers_n_2():
    # Calculate the sum of fourth powers from 1 to 2
    result = fourth_Power_Sum(2)
    assert result == 17

def test_sum_fourth_powers_n_3():
    # Calculate the sum of fourth powers from 1 to 3
    result = fourth_Power_Sum(3)
    assert result == 98

def test_sum_fourth_powers_n_4():
    # Calculate the sum of fourth powers from 1 to 4
    result = fourth_Power_Sum(4)
    assert result == 354

def test_sum_fourth_powers_n_5():
    # Calculate the sum of fourth powers from 1 to 5
    result = fourth_Power_Sum(5)
    assert result == 979

def test_sum_fourth_powers_n_0_edge_case():
    # Calculate the sum of fourth powers from 1 to 0 (edge case)
    result = fourth_Power_Sum(0)
    assert result == 0
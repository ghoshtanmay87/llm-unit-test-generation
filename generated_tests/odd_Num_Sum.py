def odd_Num_Sum(n) : 
    j = 0
    sm = 0
    for i in range(1,n + 1) : 
        j = (2*i-1) 
        sm = sm + (j*j*j*j)   
    return sm

import pytest

def test_sum_of_fourth_powers_first_1_odd_number():
    # For n=1, the first odd number is 1. 1^4 = 1, so the sum is 1.
    assert odd_Num_Sum(1) == 1

def test_sum_of_fourth_powers_first_2_odd_numbers():
    # For n=2, odd numbers are 1 and 3. 1^4=1, 3^4=81, sum=1+81=82.
    assert odd_Num_Sum(2) == 82

def test_sum_of_fourth_powers_first_3_odd_numbers_corrected():
    # For n=3, odd numbers are 1, 3, 5. Their fourth powers are 1, 81, and 625 respectively.
    # Sum is 1+81+625=707.
    assert odd_Num_Sum(3) == 707

def test_sum_of_fourth_powers_first_4_odd_numbers_corrected():
    # For n=4, odd numbers are 1, 3, 5, 7. Their fourth powers are 1, 81, 625, and 2401 respectively.
    # Sum is 1+81+625+2401=3108.
    assert odd_Num_Sum(4) == 3108

def test_sum_of_fourth_powers_first_0_odd_numbers_edge_case():
    # For n=0, no odd numbers are considered, so sum is 0.
    assert odd_Num_Sum(0) == 0
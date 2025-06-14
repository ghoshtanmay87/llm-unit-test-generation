def Sum_of_Inverse_Divisors(N,Sum): 
    ans = float(Sum)*1.0 /float(N);  
    return round(ans,2);

import pytest

def test_sum_of_inverse_divisors_N_10_Sum_5():
    # Calculate sum of inverse divisors for N=10 and Sum=5
    result = Sum_of_Inverse_Divisors(10, 5)
    assert result == 0.5

def test_sum_of_inverse_divisors_N_3_Sum_1():
    # Calculate sum of inverse divisors for N=3 and Sum=1
    result = Sum_of_Inverse_Divisors(3, 1)
    assert result == 0.33

def test_sum_of_inverse_divisors_N_7_Sum_14():
    # Calculate sum of inverse divisors for N=7 and Sum=14
    result = Sum_of_Inverse_Divisors(7, 14)
    assert result == 2.0

def test_sum_of_inverse_divisors_N_1_Sum_1():
    # Calculate sum of inverse divisors for N=1 and Sum=1
    result = Sum_of_Inverse_Divisors(1, 1)
    assert result == 1.0

def test_sum_of_inverse_divisors_N_4_Sum_7():
    # Calculate sum of inverse divisors for N=4 and Sum=7
    result = Sum_of_Inverse_Divisors(4, 7)
    assert result == 1.75
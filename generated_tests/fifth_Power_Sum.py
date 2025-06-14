def fifth_Power_Sum(n) : 
    sm = 0 
    for i in range(1,n+1) : 
        sm = sm + (i*i*i*i*i) 
    return sm

import pytest

def test_sum_of_fifth_powers_from_1_to_1():
    # The function sums i^5 for i from 1 to n. For n=1, sum = 1^5 = 1.
    assert fifth_Power_Sum(1) == 1

def test_sum_of_fifth_powers_from_1_to_2():
    # Sum = 1^5 + 2^5 = 1 + 32 = 33.
    assert fifth_Power_Sum(2) == 33

def test_sum_of_fifth_powers_from_1_to_3():
    # Sum = 1^5 + 2^5 + 3^5 = 1 + 32 + 243 = 276.
    assert fifth_Power_Sum(3) == 276

def test_sum_of_fifth_powers_from_1_to_4():
    # Sum = 1^5 + 2^5 + 3^5 + 4^5 = 1 + 32 + 243 + 1024 = 1300.
    assert fifth_Power_Sum(4) == 1300

def test_sum_of_fifth_powers_from_1_to_5():
    # Sum = 1^5 + 2^5 + 3^5 + 4^5 + 5^5 = 1 + 32 + 243 + 1024 + 3125 = 3413.
    assert fifth_Power_Sum(5) == 3413

def test_sum_of_fifth_powers_from_1_to_0_edge_case():
    # For n=0, the loop does not run, so sum is 0.
    assert fifth_Power_Sum(0) == 0
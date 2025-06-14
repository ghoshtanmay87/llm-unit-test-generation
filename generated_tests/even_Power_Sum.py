def even_Power_Sum(n): 
    sum = 0; 
    for i in range(1,n+1): 
        j = 2*i; 
        sum = sum + (j*j*j*j*j); 
    return sum;

import pytest

def test_sum_of_fifth_powers_first_1_even_number():
    # For n=1, only i=1 is considered. j=2*1=2. 2^5=32. Sum=32.
    assert even_Power_Sum(1) == 32

def test_sum_of_fifth_powers_first_2_even_numbers():
    # For n=2, i=1: j=2, 2^5=32; i=2: j=4, 4^5=1024; sum=32+1024=1056.
    assert even_Power_Sum(2) == 1056

def test_sum_of_fifth_powers_first_3_even_numbers():
    # For n=3, i=1: 2^5=32; i=2: 4^5=1024; i=3: 6^5=7776; sum=32+1024+7776=8832.
    assert even_Power_Sum(3) == 8832

def test_sum_of_fifth_powers_first_4_even_numbers():
    # For n=4, i=1: 2^5=32; i=2: 4^5=1024; i=3: 6^5=7776; i=4: 8^5=32768; sum=32+1024+7776+32768=41600.
    assert even_Power_Sum(4) == 130048

def test_sum_of_fifth_powers_first_0_even_numbers_edge_case():
    # For n=0, the loop does not run, so sum remains 0.
    assert even_Power_Sum(0) == 0
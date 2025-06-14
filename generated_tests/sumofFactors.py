import math 
def sumofFactors(n) : 
    if (n % 2 != 0) : 
        return 0
    res = 1
    for i in range(2, (int)(math.sqrt(n)) + 1) :    
        count = 0
        curr_sum = 1
        curr_term = 1
        while (n % i == 0) : 
            count= count + 1
            n = n // i 
            if (i == 2 and count == 1) : 
                curr_sum = 0
            curr_term = curr_term * i 
            curr_sum = curr_sum + curr_term 
        res = res * curr_sum  
    if (n >= 2) : 
        res = res * (1 + n) 
    return res

import pytest

def test_sumofFactors_odd_number_returns_zero():
    # Input is an odd number, should return 0 immediately
    n = 15
    expected = 0
    assert sumofFactors(n) == expected

def test_sumofFactors_input_6_product_of_2_and_3():
    # Input is 6, a product of 2 and 3
    n = 6
    expected = 8
    assert sumofFactors(n) == expected

def test_sumofFactors_input_1_odd_and_less_than_2():
    # Input is 1, which is odd and less than 2
    n = 1
    expected = 0
    assert sumofFactors(n) == expected

def test_sumofFactors_input_4_power_of_2():
    # Input is 4, a power of 2
    n = 4
    expected = 6
    assert sumofFactors(n) == expected

def test_sumofFactors_input_12_multiple_prime_factors():
    # Input is 12, multiple prime factors including 2 with exponent > 1
    n = 12
    expected = 24
    assert sumofFactors(n) == expected

def test_sumofFactors_input_8_power_of_2_exponent_3():
    # Input is 8, power of 2 with exponent 3
    n = 8
    expected = 14
    assert sumofFactors(n) == expected

def test_sumofFactors_input_2_smallest_even_prime():
    # Input is 2, the smallest even prime number
    n = 2
    expected = 3
    assert sumofFactors(n) == expected
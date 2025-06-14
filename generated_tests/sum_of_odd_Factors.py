import math
def sum_of_odd_Factors(n): 
    res = 1
    while n % 2 == 0: 
        n = n // 2 
    for i in range(3,int(math.sqrt(n) + 1)): 
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0: 
            count+=1 
            n = n // i 
            curr_term *= i 
            curr_sum += curr_term    
        res *= curr_sum  
    if n >= 2: 
        res *= (1 + n) 
    return res

import pytest

def test_sum_of_odd_factors_n_1():
    # 1 has only one factor which is 1 itself, and it is odd. The function returns 1.
    assert sum_of_odd_Factors(1) == 1

def test_sum_of_odd_factors_n_2_even_prime():
    # 2 is even, the function removes factors of 2, leaving n=1. Sum of odd factors of 1 is 1.
    assert sum_of_odd_Factors(2) == 1

def test_sum_of_odd_factors_n_3_odd_prime():
    # 3 is odd prime, factors are 1 and 3. Sum is 1+3=4.
    assert sum_of_odd_Factors(3) == 4

def test_sum_of_odd_factors_n_12():
    # Remove factors of 2: 12 -> 3. Odd factors of 3 are 1 and 3, sum=4.
    assert sum_of_odd_Factors(12) == 4

def test_sum_of_odd_factors_n_15():
    # 15 is odd, factors are 1,3,5,15. Sum=1+3+5+15=24.
    assert sum_of_odd_Factors(15) == 24

def test_sum_of_odd_factors_n_36():
    # Remove factors of 2: 36 -> 9. Odd factors of 9 (3^2) are 1,3,9 sum=13.
    assert sum_of_odd_Factors(36) == 13

def test_sum_of_odd_factors_n_45():
    # 45 is odd. Factors: 1,3,5,9,15,45. Sum=78.
    assert sum_of_odd_Factors(45) == 78

def test_sum_of_odd_factors_n_100():
    # Remove factors of 2: 100 -> 25. Odd factors of 25 (5^2) are 1,5,25 sum=31.
    assert sum_of_odd_Factors(100) == 31

def test_sum_of_odd_factors_n_1000():
    # Remove factors of 2: 1000 -> 125. Odd factors of 125 (5^3) are 1,5,25,125 sum=156.
    assert sum_of_odd_Factors(1000) == 156

def test_sum_of_odd_factors_n_81():
    # 81 is odd, factors are 1,3,9,27,81 sum=121.
    assert sum_of_odd_Factors(81) == 121
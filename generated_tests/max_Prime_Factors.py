import math 
def max_Prime_Factors (n): 
    maxPrime = -1 
    while n%2 == 0: 
        maxPrime = 2
        n >>= 1    
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 
    if n > 2: 
        maxPrime = n  
    return int(maxPrime)

import pytest

def test_input_is_1_no_prime_factors():
    # Input is 1, which has no prime factors
    result = max_Prime_Factors(1)
    assert result == -1

def test_input_is_2_smallest_prime():
    # Input is 2, the smallest prime number
    result = max_Prime_Factors(2)
    assert result == 2

def test_input_is_3_prime_greater_than_2():
    # Input is 3, a prime number greater than 2
    result = max_Prime_Factors(3)
    assert result == 3

def test_input_is_6_factors_2_and_3():
    # Input is 6, which factors into 2 and 3
    result = max_Prime_Factors(6)
    assert result == 3

def test_input_is_100_factors_2_squared_and_5_squared():
    # Input is 100, which factors into 2^2 and 5^2
    result = max_Prime_Factors(100)
    assert result == 5

def test_input_is_37_prime_number():
    # Input is 37, a prime number
    result = max_Prime_Factors(37)
    assert result == 37

def test_input_is_84_factors_2_squared_3_and_7():
    # Input is 84, which factors into 2^2 * 3 * 7
    result = max_Prime_Factors(84)
    assert result == 7

def test_input_is_1000_factors_2_cubed_and_5_cubed():
    # Input is 1000, which factors into 2^3 * 5^3
    result = max_Prime_Factors(1000)
    assert result == 5

def test_input_is_49_seven_squared():
    # Input is 49, which is 7^2
    result = max_Prime_Factors(49)
    assert result == 7

def test_input_is_97_prime_number():
    # Input is 97, a prime number
    result = max_Prime_Factors(97)
    assert result == 97
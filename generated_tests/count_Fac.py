def count_Fac(n):  
    m = n 
    count = 0
    i = 2
    while((i * i) <= m): 
        total = 0
        while (n % i == 0): 
            n /= i 
            total += 1 
        temp = 0
        j = 1
        while((temp + j) <= total): 
            temp += j 
            count += 1
            j += 1 
        i += 1
    if (n != 1): 
        count += 1 
    return count

import pytest

def test_input_is_1_no_prime_factors():
    # Input is 1, which has no prime factors
    result = count_Fac(n=1)
    assert result == 0

def test_input_is_prime_number_2():
    # Input is a prime number 2
    result = count_Fac(n=2)
    assert result == 1

def test_input_is_4_two_squared():
    # Input is 4 (2^2)
    result = count_Fac(n=4)
    assert result == 3

def test_input_is_12_two_squared_times_three():
    # Input is 12 (2^2 * 3^1)
    result = count_Fac(n=12)
    assert result == 4

def test_input_is_18_two_times_three_squared():
    # Input is 18 (2^1 * 3^2)
    result = count_Fac(n=18)
    assert result == 4

def test_input_is_30_product_of_three_primes():
    # Input is 30 (2^1 * 3^1 * 5^1)
    result = count_Fac(n=30)
    assert result == 3

def test_input_is_100_two_squared_times_five_squared():
    # Input is 100 (2^2 * 5^2)
    result = count_Fac(n=100)
    assert result == 6

def test_input_is_1000_two_cubed_times_five_cubed():
    # Input is 1000 (2^3 * 5^3)
    result = count_Fac(n=1000)
    assert result == 12

def test_input_is_7_prime_number():
    # Input is 7 (prime number)
    result = count_Fac(n=7)
    assert result == 1

def test_input_is_36_two_squared_times_three_squared():
    # Input is 36 (2^2 * 3^2)
    result = count_Fac(n=36)
    assert result == 6
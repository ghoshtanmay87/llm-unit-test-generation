def Sum(N): 
    SumOfPrimeDivisors = [0]*(N + 1)   
    for i in range(2,N + 1) : 
        if (SumOfPrimeDivisors[i] == 0) : 
            for j in range(i,N + 1,i) : 
                SumOfPrimeDivisors[j] += i           
    return SumOfPrimeDivisors[N]

import pytest

def test_sum_prime_divisors_N_1():
    # Since 1 has no prime divisors, the sum is 0.
    assert Sum(1) == 0

def test_sum_prime_divisors_N_2():
    # 2 is prime, so its only prime divisor is 2 itself, sum is 2.
    assert Sum(2) == 2

def test_sum_prime_divisors_N_13():
    # 13 is prime, so the sum of its prime divisors is 13.
    assert Sum(13) == 13

def test_sum_prime_divisors_N_6():
    # 6 has prime divisors 2 and 3, sum is 2 + 3 = 5.
    assert Sum(6) == 5

def test_sum_prime_divisors_N_12():
    # 12 has prime divisors 2 and 3, sum is 2 + 3 = 5.
    assert Sum(12) == 5

def test_sum_prime_divisors_N_28():
    # 28 has prime divisors 2 and 7, sum is 2 + 7 = 9.
    assert Sum(28) == 9

def test_sum_prime_divisors_N_30():
    # 30 has prime divisors 2, 3, and 5, sum is 2 + 3 + 5 = 10.
    assert Sum(30) == 10

def test_sum_prime_divisors_N_17():
    # 17 is prime, so the sum of its prime divisors is 17.
    assert Sum(17) == 17

def test_sum_prime_divisors_N_100():
    # 100 has prime divisors 2 and 5, sum is 2 + 5 = 7.
    assert Sum(100) == 7
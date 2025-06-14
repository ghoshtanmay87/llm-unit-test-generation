def sum_Of_Primes(n): 
    prime = [True] * (n + 1)  
    p = 2
    while p * p <= n: 
        if prime[p] == True:  
            i = p * 2
            while i <= n: 
                prime[i] = False
                i += p 
        p += 1    
    sum = 0
    for i in range (2,n + 1): 
        if(prime[i]): 
            sum += i 
    return sum

import pytest

def test_sum_of_primes_up_to_10():
    # Primes up to 10 are 2, 3, 5, 7. Their sum is 17.
    assert sum_Of_Primes(10) == 17

def test_sum_of_primes_up_to_1_no_primes():
    # No primes less than or equal to 1, sum is 0.
    assert sum_Of_Primes(1) == 0

def test_sum_of_primes_up_to_2_smallest_prime():
    # 2 is the only prime <= 2, sum is 2.
    assert sum_Of_Primes(2) == 2

def test_sum_of_primes_up_to_20():
    # Primes up to 20 sum to 77.
    assert sum_Of_Primes(20) == 77

def test_sum_of_primes_up_to_0_edge_case():
    # No primes <= 0, sum is 0.
    assert sum_Of_Primes(0) == 0

def test_sum_of_primes_up_to_30():
    # Primes up to 30 sum to 129.
    assert sum_Of_Primes(30) == 129
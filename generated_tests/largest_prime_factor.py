def largest_prime_factor(n: int):

    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True
    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest

import pytest

def test_largest_prime_factor_of_prime_number_13():
    # 13 is prime, so its only prime factor is itself.
    assert largest_prime_factor(13) == 13

def test_largest_prime_factor_of_composite_number_28():
    # 28 factors: 1,2,4,7,14,28. Prime factors are 2 and 7. Largest is 7.
    assert largest_prime_factor(28) == 7

def test_largest_prime_factor_of_number_with_repeated_prime_factors_100():
    # 100 factors include 2 and 5 as prime factors. Largest prime factor is 5.
    assert largest_prime_factor(100) == 5

def test_largest_prime_factor_of_1_edge_case():
    # 1 has no prime factors. Function returns 1.
    assert largest_prime_factor(1) == 1

def test_largest_prime_factor_of_prime_squared_49():
    # 49 = 7 * 7, 7 is prime, so largest prime factor is 7.
    assert largest_prime_factor(49) == 7

def test_largest_prime_factor_of_number_with_small_prime_factors_30():
    # 30 factors: 2,3,5 are prime factors. Largest is 5.
    assert largest_prime_factor(30) == 5
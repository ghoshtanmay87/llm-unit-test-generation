from typing import List

def factorize(n: int) -> List[int]:
    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        fact.append(n)
    return fact

import pytest

def test_factorize_prime_number_13():
    # Factorize a prime number
    n = 13
    expected = [13]
    assert factorize(n) == expected

def test_factorize_composite_number_12():
    # Factorize a composite number with multiple prime factors
    n = 12
    expected = [2, 2, 3]
    assert factorize(n) == expected

def test_factorize_perfect_square_36():
    # Factorize a perfect square
    n = 36
    expected = [2, 2, 3, 3]
    assert factorize(n) == expected

def test_factorize_large_prime_factor_29():
    # Factorize a number with a large prime factor
    n = 29
    expected = [29]
    assert factorize(n) == expected

def test_factorize_multiple_distinct_prime_factors_30():
    # Factorize a number with multiple distinct prime factors
    n = 30
    expected = [2, 3, 5]
    assert factorize(n) == expected

def test_factorize_repeated_prime_factors_and_prime_leftover_1001():
    # Factorize a number with repeated prime factors and a prime leftover
    n = 1001
    expected = [7, 11, 13]
    assert factorize(n) == expected

def test_factorize_power_of_two_64():
    # Factorize a number that is a power of two
    n = 64
    expected = [2, 2, 2, 2, 2, 2]
    assert factorize(n) == expected

def test_factorize_smallest_composite_number_4():
    # Factorize the smallest composite number
    n = 4
    expected = [2, 2]
    assert factorize(n) == expected

def test_factorize_large_prime_factor_near_sqrt_221():
    # Factorize a number with a large prime factor near sqrt
    n = 221
    expected = [13, 17]
    assert factorize(n) == expected

def test_factorize_prime_just_above_perfect_square_101():
    # Factorize a prime number just above a perfect square
    n = 101
    expected = [101]
    assert factorize(n) == expected
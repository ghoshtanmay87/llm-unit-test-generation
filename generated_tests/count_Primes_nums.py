def count_Primes_nums(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr

import pytest

def test_count_primes_less_than_0_no_primes():
    # Range is empty, so no numbers to check, result is 0.
    assert count_Primes_nums(0) == 0

def test_count_primes_less_than_1_no_primes():
    # Only number 0 is checked and skipped (<=1), so no primes counted.
    assert count_Primes_nums(1) == 0

def test_count_primes_less_than_2_no_primes():
    # Numbers checked: 0 and 1 skipped; 2 not included since range is up to n-1=1, so no primes.
    assert count_Primes_nums(2) == 0

def test_count_primes_less_than_3_only_prime_2():
    # Numbers checked: 0 and 1 skipped; 2 is prime, so count is 1.
    assert count_Primes_nums(3) == 1

def test_count_primes_less_than_10_primes_2357():
    # Primes less than 10 are 2,3,5,7 total 4.
    assert count_Primes_nums(10) == 4

def test_count_primes_less_than_20_primes_235711131719():
    # Primes less than 20 are 2,3,5,7,11,13,17,19 total 8.
    assert count_Primes_nums(20) == 8

def test_count_primes_less_than_30_primes_2357111317192329():
    # Primes less than 30 are 2,3,5,7,11,13,17,19,23,29 total 10.
    assert count_Primes_nums(30) == 10
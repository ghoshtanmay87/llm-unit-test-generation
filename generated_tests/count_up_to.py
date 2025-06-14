def count_up_to(n):
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

import pytest

def test_count_up_to_primes_less_than_10():
    # Counting primes less than 10
    result = count_up_to(10)
    expected = [2, 3, 5, 7]
    assert result == expected

def test_count_up_to_primes_less_than_2_edge_case():
    # Counting primes less than 2 (edge case)
    result = count_up_to(2)
    expected = []
    assert result == expected

def test_count_up_to_primes_less_than_3():
    # Counting primes less than 3
    result = count_up_to(3)
    expected = [2]
    assert result == expected

def test_count_up_to_primes_less_than_20():
    # Counting primes less than 20
    result = count_up_to(20)
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    assert result == expected

def test_count_up_to_primes_less_than_1_no_primes():
    # Counting primes less than 1 (no primes)
    result = count_up_to(1)
    expected = []
    assert result == expected
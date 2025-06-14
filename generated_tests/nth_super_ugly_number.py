import heapq
def nth_super_ugly_number(n, primes):
    uglies = [1]
    def gen(prime):
        for ugly in uglies:
            yield ugly * prime
    merged = heapq.merge(*map(gen, primes))
    while len(uglies) < n:
        ugly = next(merged)
        if ugly != uglies[-1]:
            uglies.append(ugly)
    return uglies[-1]

import pytest

def test_first_super_ugly_number_with_primes_2_3_5():
    n = 1
    primes = [2, 3, 5]
    expected = 1
    assert nth_super_ugly_number(n, primes) == expected

def test_tenth_super_ugly_number_with_primes_2_3_5():
    n = 10
    primes = [2, 3, 5]
    expected = 12
    assert nth_super_ugly_number(n, primes) == expected

def test_twelfth_super_ugly_number_with_primes_2_7_13_19():
    n = 12
    primes = [2, 7, 13, 19]
    expected = 32
    assert nth_super_ugly_number(n, primes) == expected

def test_fifteenth_super_ugly_number_with_primes_3_5_7():
    n = 15
    primes = [3, 5, 7]
    expected = 45
    assert nth_super_ugly_number(n, primes) == expected

def test_fifth_super_ugly_number_with_prime_2():
    n = 5
    primes = [2]
    expected = 16
    assert nth_super_ugly_number(n, primes) == expected
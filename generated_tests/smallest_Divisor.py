def smallest_Divisor(n): 
    if (n % 2 == 0): 
        return 2; 
    i = 3;  
    while (i*i <= n): 
        if (n % i == 0): 
            return i; 
        i += 2; 
    return n;

import pytest

def test_smallest_divisor_even_number():
    # Find smallest divisor of an even number
    n = 10
    expected = 2
    assert smallest_Divisor(n) == expected

def test_smallest_divisor_odd_composite_number():
    # Find smallest divisor of an odd composite number
    n = 15
    expected = 3
    assert smallest_Divisor(n) == expected

def test_smallest_divisor_prime_number():
    # Find smallest divisor of a prime number
    n = 17
    expected = 17
    assert smallest_Divisor(n) == expected

def test_smallest_divisor_of_one():
    # Find smallest divisor of 1
    n = 1
    expected = 1
    assert smallest_Divisor(n) == expected

def test_smallest_divisor_large_even_number():
    # Find smallest divisor of a large even number
    n = 1000000
    expected = 2
    assert smallest_Divisor(n) == expected

def test_smallest_divisor_odd_with_divisor_greater_than_three():
    # Find smallest divisor of an odd number with smallest divisor greater than 3
    n = 49
    expected = 7
    assert smallest_Divisor(n) == expected

def test_smallest_divisor_prime_just_above_perfect_square():
    # Find smallest divisor of a prime number just above a perfect square
    n = 101
    expected = 101
    assert smallest_Divisor(n) == expected
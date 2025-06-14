def divisor(n):
  for i in range(n):
    x = len([i for i in range(1,n+1) if not n % i])
  return x

import pytest

def test_divisor_with_n_1_smallest_positive_integer():
    # Test with n=1, smallest positive integer
    n = 1
    expected_output = 1
    assert divisor(n) == expected_output

def test_divisor_with_n_2_small_prime_number():
    # Test with n=2, a small prime number
    n = 2
    expected_output = 2
    assert divisor(n) == expected_output

def test_divisor_with_n_3_small_prime_number():
    # Test with n=3, a small prime number
    n = 3
    expected_output = 2
    assert divisor(n) == expected_output

def test_divisor_with_n_4_small_composite_number():
    # Test with n=4, a small composite number
    n = 4
    expected_output = 3
    assert divisor(n) == expected_output

def test_divisor_with_n_5_small_prime_number():
    # Test with n=5, a small prime number
    n = 5
    expected_output = 2
    assert divisor(n) == expected_output

def test_divisor_with_n_6_small_composite_number():
    # Test with n=6, a small composite number
    n = 6
    expected_output = 4
    assert divisor(n) == expected_output
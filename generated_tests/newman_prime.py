def newman_prime(n): 
	if n == 0 or n == 1: 
		return 1
	return 2 * newman_prime(n - 1) + newman_prime(n - 2)

import pytest

def test_newman_prime_base_case_zero():
    # Input is 0, base case returns 1
    assert newman_prime(0) == 1

def test_newman_prime_base_case_one():
    # Input is 1, base case returns 1
    assert newman_prime(1) == 1

def test_newman_prime_input_two():
    # Input is 2, computed from base cases
    assert newman_prime(2) == 3

def test_newman_prime_input_three():
    # Input is 3, recursive calculation
    assert newman_prime(3) == 7

def test_newman_prime_input_four():
    # Input is 4, recursive calculation
    assert newman_prime(4) == 17

def test_newman_prime_input_five():
    # Input is 5, recursive calculation
    assert newman_prime(5) == 41

def test_newman_prime_input_six():
    # Input is 6, recursive calculation
    assert newman_prime(6) == 99
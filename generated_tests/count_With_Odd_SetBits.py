def count_With_Odd_SetBits(n): 
    if (n % 2 != 0): 
        return (n + 1) / 2
    count = bin(n).count('1') 
    ans = n / 2
    if (count % 2 != 0): 
        ans += 1
    return ans

import pytest

def test_input_is_odd_number():
    # Scenario: Input is an odd number
    n = 5
    expected = 3.0
    assert count_With_Odd_SetBits(n) == expected

def test_input_is_even_number_with_odd_set_bits():
    # Scenario: Input is a large even number with odd set bits
    n = 14
    expected = 8.0
    assert count_With_Odd_SetBits(n) == expected

def test_input_is_even_number_with_even_set_bits():
    # Scenario: Input is zero
    n = 0
    expected = 0.0
    assert count_With_Odd_SetBits(n) == expected

def test_input_is_one():
    # Scenario: Input is one
    n = 1
    expected = 1.0
    assert count_With_Odd_SetBits(n) == expected

def test_input_is_large_odd_number():
    # Scenario: Input is a large odd number
    n = 101
    expected = 51.0
    assert count_With_Odd_SetBits(n) == expected
def count_Set_Bits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count

import pytest

def test_count_set_bits_in_zero():
    # Scenario: Count set bits in zero
    n = 0
    expected = 0
    assert count_Set_Bits(n) == expected

def test_count_set_bits_in_small_number_with_one_set_bit():
    # Scenario: Count set bits in a small number with one set bit
    n = 1
    expected = 1
    assert count_Set_Bits(n) == expected

def test_count_set_bits_in_number_with_multiple_set_bits():
    # Scenario: Count set bits in a number with multiple set bits
    n = 7
    expected = 3
    assert count_Set_Bits(n) == expected

def test_count_set_bits_in_number_with_alternating_bits():
    # Scenario: Count set bits in a number with alternating bits
    n = 10
    expected = 2
    assert count_Set_Bits(n) == expected

def test_count_set_bits_in_larger_number():
    # Scenario: Count set bits in a larger number
    n = 1023
    expected = 10
    assert count_Set_Bits(n) == expected
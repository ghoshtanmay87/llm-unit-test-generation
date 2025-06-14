def find_Parity(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return ("Odd Parity"); 
    return ("Even Parity");

import pytest

def test_find_Parity_zero_input():
    # Check parity for zero input
    x = 0
    expected = "Even Parity"
    assert find_Parity(x) == expected

def test_find_Parity_one_set_bit():
    # Check parity for input with one set bit
    x = 1
    expected = "Odd Parity"
    assert find_Parity(x) == expected

def test_find_Parity_two_set_bits():
    # Check parity for input with two set bits
    x = 3
    expected = "Even Parity"
    assert find_Parity(x) == expected

def test_find_Parity_three_set_bits():
    # Check parity for input with three set bits
    x = 7
    expected = "Odd Parity"
    assert find_Parity(x) == expected

def test_find_Parity_four_set_bits():
    # Check parity for input with four set bits
    x = 15
    expected = "Even Parity"
    assert find_Parity(x) == expected

def test_find_Parity_large_number_odd_set_bits():
    # Check parity for a large number with odd number of set bits
    x = 85
    expected = "Odd Parity"
    assert find_Parity(x) == expected

def test_find_Parity_large_number_even_set_bits():
    # Check parity for a large number with even number of set bits
    x = 170
    expected = "Even Parity"
    assert find_Parity(x) == expected

def test_find_Parity_single_high_bit_set():
    # Check parity for a number with a single high bit set
    x = 2147483648
    expected = "Odd Parity"
    assert find_Parity(x) == expected
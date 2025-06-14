def take_L_and_F_set_bits(n) : 
    n = n | n >> 1
    n = n | n >> 2
    n = n | n >> 4
    n = n | n >> 8
    n = n | n >> 16 
    return ((n + 1) >> 1) + 1      
def toggle_F_and_L_bits(n) :  
    if (n == 1) : 
        return 0 
    return n ^ take_L_and_F_set_bits(n)

import pytest

def test_toggle_bits_smallest_positive_integer():
    # Toggle bits for input 1, the smallest positive integer
    n = 1
    expected_output = 0
    assert toggle_F_and_L_bits(n) == expected_output

def test_toggle_bits_small_power_of_two():
    # Toggle bits for input 2, a small power of two
    n = 2
    expected_output = 1
    assert toggle_F_and_L_bits(n) == expected_output

def test_toggle_bits_all_bits_set_2bit():
    # Toggle bits for input 3, all bits set in 2-bit number
    n = 3
    expected_output = 0
    assert toggle_F_and_L_bits(n) == expected_output

def test_toggle_bits_4bit_number():
    # Toggle bits for input 10, a 4-bit number
    n = 10
    expected_output = 5
    assert toggle_F_and_L_bits(n) == expected_output

def test_toggle_bits_5bit_mixed_bits():
    # Toggle bits for input 21, a 5-bit number with mixed bits
    n = 21
    expected_output = 10
    assert toggle_F_and_L_bits(n) == expected_output

def test_toggle_bits_power_of_two_single_bit_set():
    # Toggle bits for input 32, a power of two with a single bit set
    n = 32
    expected_output = 31
    assert toggle_F_and_L_bits(n) == expected_output

def test_toggle_bits_all_bits_set_6bit():
    # Toggle bits for input 63, all bits set in 6-bit number
    n = 63
    expected_output = 0
    assert toggle_F_and_L_bits(n) == expected_output

def test_toggle_bits_7bit_number():
    # Toggle bits for input 100, a 7-bit number
    n = 100
    expected_output = 27
    assert toggle_F_and_L_bits(n) == expected_output
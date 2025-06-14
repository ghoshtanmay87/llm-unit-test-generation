def check_Even_Parity(x): 
    parity = 0
    while (x != 0): 
        x = x & (x - 1) 
        parity += 1
    if (parity % 2 == 0): 
        return True
    else: 
        return False

import pytest

def test_check_parity_zero_input():
    # Check parity for zero input
    x = 0
    expected = True
    assert check_Even_Parity(x) == expected

def test_check_parity_one_set_bit():
    # Check parity for input with one set bit
    x = 1
    expected = False
    assert check_Even_Parity(x) == expected

def test_check_parity_two_set_bits():
    # Check parity for input with two set bits
    x = 3
    expected = True
    assert check_Even_Parity(x) == expected

def test_check_parity_three_set_bits():
    # Check parity for input with three set bits
    x = 7
    expected = False
    assert check_Even_Parity(x) == expected

def test_check_parity_four_set_bits():
    # Check parity for input with four set bits
    x = 15
    expected = True
    assert check_Even_Parity(x) == expected

def test_check_parity_mixed_bits_101010_corrected():
    # Check parity for input with mixed bits (binary 101010 corrected)
    x = 42
    expected = False
    assert check_Even_Parity(x) == expected

def test_check_parity_all_bits_set_byte():
    # Check parity for input with all bits set in a byte
    x = 255
    expected = True
    assert check_Even_Parity(x) == expected

def test_check_parity_one_bit_high_position():
    # Check parity for input with one bit set at high position
    x = 1024
    expected = False
    assert check_Even_Parity(x) == expected
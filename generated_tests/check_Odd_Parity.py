def check_Odd_Parity(x): 
    parity = 0
    while (x != 0): 
        x = x & (x - 1) 
        parity += 1
    if (parity % 2 == 1): 
        return True
    else: 
        return False

import pytest

def test_check_odd_parity_zero_input():
    # Check odd parity for zero input
    x = 0
    expected = False
    assert check_Odd_Parity(x) == expected

def test_check_odd_parity_one_set_bit():
    # Check odd parity for input with one set bit
    x = 1
    expected = True
    assert check_Odd_Parity(x) == expected

def test_check_odd_parity_two_set_bits():
    # Check odd parity for input with two set bits
    x = 3
    expected = False
    assert check_Odd_Parity(x) == expected

def test_check_odd_parity_three_set_bits():
    # Check odd parity for input with three set bits
    x = 7
    expected = True
    assert check_Odd_Parity(x) == expected

def test_check_odd_parity_four_set_bits():
    # Check odd parity for input with four set bits
    x = 15
    expected = False
    assert check_Odd_Parity(x) == expected

def test_check_odd_parity_five_set_bits():
    # Check odd parity for input with five set bits
    x = 31
    expected = True
    assert check_Odd_Parity(x) == expected

def test_check_odd_parity_mixed_bits_42_false():
    # Check odd parity for input with mixed bits set (binary 101010)
    # This test corresponds to the first story with expected_output False (which was corrected)
    # We include it to reflect the original story but mark as expected False
    x = 42
    expected = False
    assert check_Odd_Parity(x) == expected

def test_check_odd_parity_mixed_bits_42_true():
    # Check odd parity for input with mixed bits set (binary 101010)
    x = 42
    expected = True
    assert check_Odd_Parity(x) == expected

def test_check_odd_parity_high_bit_set_only():
    # Check odd parity for input with high bit set only
    x = 1024
    expected = True
    assert check_Odd_Parity(x) == expected

def test_check_odd_parity_all_bits_set_byte():
    # Check odd parity for input with all bits set in a byte
    x = 255
    expected = False
    assert check_Odd_Parity(x) == expected
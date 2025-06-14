def set_middle_bits(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def toggle_middle_bits(n): 
    if (n == 1): 
        return 1
    return n ^ set_middle_bits(n)

import pytest

def test_toggle_middle_bits_input_1_edge_case():
    # For n=1, the function immediately returns 1 as per the if condition.
    assert toggle_middle_bits(1) == 1

def test_toggle_middle_bits_input_2_binary_10():
    # For n=2 (binary 10), set_middle_bits(2) returns 1 (binary 01).
    # XOR 2 ^ 1 = 3 (binary 11).
    assert toggle_middle_bits(2) == 3

def test_toggle_middle_bits_input_3_binary_11():
    # For n=3 (binary 11), set_middle_bits(3) returns 1 (binary 01).
    # XOR 3 ^ 1 = 2 (binary 10).
    assert toggle_middle_bits(3) == 2

def test_toggle_middle_bits_input_4_binary_100():
    # For n=4 (binary 100), set_middle_bits(4) returns 2 (binary 010).
    # XOR 4 ^ 2 = 6 (binary 110).
    assert toggle_middle_bits(4) == 6

def test_toggle_middle_bits_input_7_binary_111():
    # For n=7 (binary 111), set_middle_bits(7) returns 7 (binary 111).
    # XOR 7 ^ 7 = 0.
    assert toggle_middle_bits(7) == 0

def test_toggle_middle_bits_input_8_binary_1000():
    # For n=8 (binary 1000), set_middle_bits(8) returns 4 (binary 0100).
    # XOR 8 ^ 4 = 12 (binary 1100).
    assert toggle_middle_bits(8) == 12

def test_toggle_middle_bits_input_15_binary_1111():
    # For n=15 (binary 1111), set_middle_bits(15) returns 15 (binary 1111).
    # XOR 15 ^ 15 = 0.
    assert toggle_middle_bits(15) == 0

def test_toggle_middle_bits_input_16_binary_10000():
    # For n=16 (binary 10000), set_middle_bits(16) returns 8 (binary 01000).
    # XOR 16 ^ 8 = 24 (binary 11000).
    assert toggle_middle_bits(16) == 24

def test_toggle_middle_bits_input_31_binary_11111():
    # For n=31 (binary 11111), set_middle_bits(31) returns 31 (binary 11111).
    # XOR 31 ^ 31 = 0.
    assert toggle_middle_bits(31) == 0
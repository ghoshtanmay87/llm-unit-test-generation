import math 
def get_Pos_Of_Right_most_Set_Bit(n): 
    return int(math.log2(n&-n)+1)   
def set_Right_most_Unset_Bit(n): 
    if (n == 0): 
        return 1
    if ((n & (n + 1)) == 0):     
        return n 
    pos = get_Pos_Of_Right_most_Set_Bit(~n)      
    return ((1 << (pos - 1)) | n)

import pytest

def test_zero_input_sets_least_significant_bit():
    # Input is zero, so the rightmost unset bit is the least significant bit
    n = 0
    expected = 1
    assert set_Right_most_Unset_Bit(n) == expected

def test_input_one_sets_bit_one():
    # Input is 1 (binary 1), rightmost unset bit is bit 1 (0-based), so set bit 1
    n = 1
    expected = 3
    assert set_Right_most_Unset_Bit(n) == expected

def test_input_two_sets_bit_zero():
    # Input is 2 (binary 10), rightmost unset bit is bit 0, so set bit 0
    n = 2
    expected = 3
    assert set_Right_most_Unset_Bit(n) == expected

def test_input_three_all_lower_bits_set_returns_n():
    # Input is 3 (binary 11), all lower bits set, so function returns n as is
    n = 3
    expected = 3
    assert set_Right_most_Unset_Bit(n) == expected

def test_input_four_sets_bit_zero():
    # Input is 4 (binary 100), rightmost unset bit is bit 0, so set bit 0
    n = 4
    expected = 5
    assert set_Right_most_Unset_Bit(n) == expected

def test_input_six_sets_bit_zero():
    # Input is 6 (binary 110), rightmost unset bit is bit 0, so set bit 0
    n = 6
    expected = 7
    assert set_Right_most_Unset_Bit(n) == expected

def test_input_seven_all_lower_bits_set_returns_n():
    # Input is 7 (binary 111), all lower bits set, so function returns n as is
    n = 7
    expected = 7
    assert set_Right_most_Unset_Bit(n) == expected

def test_input_eight_sets_bit_zero():
    # Input is 8 (binary 1000), rightmost unset bit is bit 0, so set bit 0
    n = 8
    expected = 9
    assert set_Right_most_Unset_Bit(n) == expected

def test_input_ten_sets_bit_one():
    # Input is 10 (binary 1010), rightmost unset bit is bit 1, so set bit 1
    n = 10
    expected = 14
    assert set_Right_most_Unset_Bit(n) == expected

def test_input_fifteen_all_lower_bits_set_returns_n():
    # Input is 15 (binary 1111), all lower bits set, so function returns n as is
    n = 15
    expected = 15
    assert set_Right_most_Unset_Bit(n) == expected
def all_Bits_Set_In_The_Given_Range(n,l,r): 
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1) 
    new_num = n & num 
    if (num == new_num): 
        return True
    return False

import pytest

def test_all_bits_set_in_range_1_to_3_in_7():
    # Check if all bits from position 1 to 3 are set in number 7
    n = 7
    l = 1
    r = 3
    expected = True
    assert all_Bits_Set_In_The_Given_Range(n, l, r) == expected

def test_all_bits_set_in_range_2_to_4_in_14():
    # Check if all bits from position 2 to 4 are set in number 14
    n = 14
    l = 2
    r = 4
    expected = True
    assert all_Bits_Set_In_The_Given_Range(n, l, r) == expected

def test_all_bits_set_in_range_1_to_3_in_6():
    # Check if all bits from position 1 to 3 are set in number 6
    n = 6
    l = 1
    r = 3
    expected = False
    assert all_Bits_Set_In_The_Given_Range(n, l, r) == expected

def test_all_bits_set_in_range_3_to_5_in_56():
    # Check if all bits from position 3 to 5 are set in number 56
    n = 56
    l = 3
    r = 5
    expected = True
    assert all_Bits_Set_In_The_Given_Range(n, l, r) == expected

def test_all_bits_set_in_range_4_to_6_in_48():
    # Check if all bits from position 4 to 6 are set in number 48
    n = 48
    l = 4
    r = 6
    expected = False
    assert all_Bits_Set_In_The_Given_Range(n, l, r) == expected

def test_all_bits_set_in_range_1_to_1_in_1():
    # Check if all bits from position 1 to 1 are set in number 1
    n = 1
    l = 1
    r = 1
    expected = True
    assert all_Bits_Set_In_The_Given_Range(n, l, r) == expected

def test_all_bits_set_in_range_1_to_1_in_0():
    # Check if all bits from position 1 to 1 are set in number 0
    n = 0
    l = 1
    r = 1
    expected = False
    assert all_Bits_Set_In_The_Given_Range(n, l, r) == expected

def test_all_bits_set_in_range_5_to_8_in_240():
    # Check if all bits from position 5 to 8 are set in number 240
    n = 240
    l = 5
    r = 8
    expected = True
    assert all_Bits_Set_In_The_Given_Range(n, l, r) == expected

def test_all_bits_set_in_range_5_to_8_in_224():
    # Check if all bits from position 5 to 8 are set in number 224
    n = 224
    l = 5
    r = 8
    expected = False
    assert all_Bits_Set_In_The_Given_Range(n, l, r) == expected

def test_all_bits_set_in_range_10_to_12_in_7168():
    # Check if all bits from position 10 to 12 are set in number 7168
    n = 7168
    l = 10
    r = 12
    expected = True
    assert all_Bits_Set_In_The_Given_Range(n, l, r) == expected
def is_Power_Of_Two (x): 
    return x and (not(x & (x - 1))) 
def differ_At_One_Bit_Pos(a,b): 
    return is_Power_Of_Two(a ^ b)

import pytest

def test_differ_at_one_bit_pos_1_and_3():
    # Two numbers differ at exactly one bit position (1 and 3)
    a = 1
    b = 3
    expected_output = True
    assert differ_At_One_Bit_Pos(a, b) == expected_output

def test_differ_at_one_bit_pos_1_and_7():
    # Two numbers differ at more than one bit position (1 and 7)
    a = 1
    b = 7
    expected_output = False
    assert differ_At_One_Bit_Pos(a, b) == expected_output

def test_differ_at_one_bit_pos_4_and_4():
    # Two identical numbers (4 and 4)
    a = 4
    b = 4
    expected_output = False
    assert differ_At_One_Bit_Pos(a, b) == expected_output

def test_differ_at_one_bit_pos_8_and_0():
    # Two numbers differ at exactly one bit position (8 and 0)
    a = 8
    b = 0
    expected_output = True
    assert differ_At_One_Bit_Pos(a, b) == expected_output

def test_differ_at_one_bit_pos_15_and_14():
    # Two numbers differ at exactly one bit position (15 and 14)
    a = 15
    b = 14
    expected_output = True
    assert differ_At_One_Bit_Pos(a, b) == expected_output

def test_differ_at_one_bit_pos_10_and_5():
    # Two numbers differ at more than one bit position (10 and 5)
    a = 10
    b = 5
    expected_output = False
    assert differ_At_One_Bit_Pos(a, b) == expected_output
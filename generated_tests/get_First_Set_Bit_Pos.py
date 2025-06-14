import math
def get_First_Set_Bit_Pos(n):
     return math.log2(n&-n)+1

import pytest

def test_first_set_bit_position_least_significant_bit_set():
    # For n=1 (binary 1), expected output is 1.0
    assert get_First_Set_Bit_Pos(1) == 1.0

def test_first_set_bit_position_second_least_significant_bit_set():
    # For n=2 (binary 10), expected output is 2.0
    assert get_First_Set_Bit_Pos(2) == 2.0

def test_first_set_bit_position_multiple_bits_set_first_at_position_1():
    # For n=3 (binary 11), expected output is 1.0
    assert get_First_Set_Bit_Pos(3) == 1.0

def test_first_set_bit_position_first_set_bit_at_position_3():
    # For n=12 (binary 1100), expected output is 3.0
    assert get_First_Set_Bit_Pos(12) == 3.0

def test_first_set_bit_position_first_set_bit_at_position_5():
    # For n=18 (binary 10010), expected output is 2.0
    assert get_First_Set_Bit_Pos(18) == 2.0

def test_first_set_bit_position_first_set_bit_at_position_4():
    # For n=8 (binary 1000), expected output is 4.0
    assert get_First_Set_Bit_Pos(8) == 4.0
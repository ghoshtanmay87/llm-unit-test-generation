def set_Bit_Number(n): 
    if (n == 0): 
        return 0; 
    msb = 0; 
    n = int(n / 2); 
    while (n > 0): 
        n = int(n / 2); 
        msb += 1; 
    return (1 << msb)

import pytest

def test_input_zero_should_return_zero():
    assert set_Bit_Number(0) == 0

def test_input_one_smallest_positive_integer():
    assert set_Bit_Number(1) == 1

def test_input_two_power_of_two():
    assert set_Bit_Number(2) == 1

def test_input_three_just_above_power_of_two():
    assert set_Bit_Number(3) == 2

def test_input_four_power_of_two():
    assert set_Bit_Number(4) == 4

def test_input_five_just_above_power_of_two():
    assert set_Bit_Number(5) == 4

def test_input_fifteen_just_below_next_power_of_two():
    assert set_Bit_Number(15) == 8

def test_input_sixteen_exact_power_of_two():
    assert set_Bit_Number(16) == 16

def test_input_thirty_one_just_below_next_power_of_two():
    assert set_Bit_Number(31) == 16

def test_input_thirty_two_exact_power_of_two():
    assert set_Bit_Number(32) == 32
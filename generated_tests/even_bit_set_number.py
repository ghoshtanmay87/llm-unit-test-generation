def even_bit_set_number(n): 
    count = 0;res = 0;temp = n 
    while(temp > 0): 
        if (count % 2 == 1): 
            res |= (1 << count)
        count+=1
        temp >>= 1
    return (n | res)

import pytest

def test_input_zero_no_bits_set():
    # Input is zero, no bits set
    n = 0
    expected = 0
    assert even_bit_set_number(n) == expected

def test_input_bit_0_set_1():
    # Input with only bit 0 set (1)
    n = 1
    expected = 1
    assert even_bit_set_number(n) == expected

def test_input_bit_1_set_2():
    # Input with bit 1 set (2)
    n = 2
    expected = 2
    assert even_bit_set_number(n) == expected

def test_input_bits_0_and_1_set_3():
    # Input with bits 0 and 1 set (3)
    n = 3
    expected = 3
    assert even_bit_set_number(n) == expected

def test_input_bit_2_set_4():
    # Input with bit 2 set (4)
    n = 4
    expected = 6
    assert even_bit_set_number(n) == expected

def test_input_bits_0_2_4_set_21():
    # Input with bits 0, 2, 4 set (21)
    n = 21
    expected = 31
    assert even_bit_set_number(n) == expected

def test_input_all_bits_set_first_4_bits_15():
    # Input with all bits set in first 4 bits (15)
    n = 15
    expected = 15
    assert even_bit_set_number(n) == expected

def test_input_bit_5_set_32():
    # Input with bit 5 set (32)
    n = 32
    expected = 42
    assert even_bit_set_number(n) == expected
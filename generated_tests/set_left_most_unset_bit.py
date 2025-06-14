def set_left_most_unset_bit(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 << (pos)))

import pytest

def test_input_zero_all_bits_unset():
    # Input is zero, all bits are unset, so left-most unset bit is bit 0
    n = 0
    expected = 1
    result = set_left_most_unset_bit(n)
    assert result == expected

def test_input_seven_all_lower_bits_set():
    # Input is 7 (binary 111), all lower bits set, no unset bits below highest set bit
    n = 7
    expected = 7
    result = set_left_most_unset_bit(n)
    assert result == expected

def test_input_eleven_left_most_unset_bit_bit2():
    # Input is 11 (binary 1011), left-most unset bit is bit 2
    n = 11
    expected = 15
    result = set_left_most_unset_bit(n)
    assert result == expected

def test_input_twentyone_left_most_unset_bit_bit3():
    # Input is 21 (binary 10101), left-most unset bit is bit 3
    n = 21
    expected = 29
    result = set_left_most_unset_bit(n)
    assert result == expected

def test_input_thirtyone_all_bits_set():
    # Input is 31 (binary 11111), all bits set, no unset bits below highest set bit
    n = 31
    expected = 31
    result = set_left_most_unset_bit(n)
    assert result == expected

def test_input_eighteen_left_most_unset_bit_bit3():
    # Input is 18 (binary 10010), left-most unset bit is bit 3
    n = 18
    expected = 26
    result = set_left_most_unset_bit(n)
    assert result == expected
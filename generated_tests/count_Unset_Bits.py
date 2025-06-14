def count_Unset_Bits(n) :  
    cnt = 0;  
    for i in range(1,n + 1) : 
        temp = i;  
        while (temp) :  
            if (temp % 2 == 0) : 
                cnt += 1;  
            temp = temp // 2;  
    return cnt;

import pytest

def test_count_unset_bits_n_1():
    # Count unset bits for n=1
    # Number 1 in binary is '1' which has no zero bits, so total count is 0.
    assert count_Unset_Bits(1) == 0

def test_count_unset_bits_n_2():
    # Count unset bits for n=2
    # Numbers 1 ('1') and 2 ('10') have a total of 1 zero bit (in '10').
    assert count_Unset_Bits(2) == 1

def test_count_unset_bits_n_3():
    # Count unset bits for n=3
    # Numbers 1 ('1'), 2 ('10'), and 3 ('11') have a total of 1 zero bit (in '10').
    assert count_Unset_Bits(3) == 1

def test_count_unset_bits_n_4():
    # Count unset bits for n=4
    # Numbers 1 ('1'), 2 ('10'), 3 ('11'), and 4 ('100') have a total of 3 zero bits (1 in '10' and 2 in '100').
    assert count_Unset_Bits(4) == 3

def test_count_unset_bits_n_5():
    # Count unset bits for n=5
    # Numbers 1 ('1'), 2 ('10'), 3 ('11'), 4 ('100'), and 5 ('101') have a total of 4 zero bits (1 in '10', 2 in '100', and 1 in '101').
    assert count_Unset_Bits(5) == 4
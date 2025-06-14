def count_Hexadecimal(L,R) :  
    count = 0;  
    for i in range(L,R + 1) : 
        if (i >= 10 and i <= 15) : 
            count += 1;  
        elif (i > 15) : 
            k = i;  
            while (k != 0) :  
                if (k % 16 >= 10) : 
                    count += 1;  
                k = k // 16;  
    return count;

import pytest

def test_count_hex_digits_10_to_15():
    # Count hexadecimal digits between 10 and 15 inclusive
    result = count_Hexadecimal(10, 15)
    assert result == 6

def test_count_hex_digits_0_to_9():
    # Count hexadecimal digits from 0 to 9 (no digits >= 10)
    result = count_Hexadecimal(0, 9)
    assert result == 0

def test_count_hex_digits_0_to_16():
    # Count hexadecimal digits from 0 to 16
    result = count_Hexadecimal(0, 16)
    assert result == 7

def test_count_hex_digits_15_to_17():
    # Count hexadecimal digits from 15 to 17
    result = count_Hexadecimal(15, 17)
    assert result == 2

def test_count_hex_digits_255_to_260():
    # Count hexadecimal digits from 255 to 260
    result = count_Hexadecimal(255, 260)
    assert result == 7

def test_count_hex_digits_10_to_20():
    # Count hexadecimal digits from 10 to 20
    result = count_Hexadecimal(10, 20)
    assert result == 7
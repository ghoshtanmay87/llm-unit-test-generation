def get_Char(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)

import pytest

def test_sum_divisible_by_26_single_z():
    # Sum of character positions is exactly divisible by 26
    result = get_Char('z')
    assert result == 122

def test_sum_not_divisible_by_26_single_a():
    # Sum of character positions is not divisible by 26, small sum
    result = get_Char('a')
    assert result == 'a'

def test_sum_not_divisible_by_26_multiple_chars_abc():
    # Sum of character positions is not divisible by 26, multiple characters
    result = get_Char('abc')
    assert result == 'f'

def test_sum_divisible_by_26_multiple_chars_zz():
    # Sum of character positions is divisible by 26 with multiple characters
    result = get_Char('zz')
    assert result == 122

def test_sum_just_over_26_az():
    # Sum of character positions just over 26
    result = get_Char('az')
    assert result == 'a'

def test_empty_string_input():
    # Empty string input
    result = get_Char('')
    assert result == 122
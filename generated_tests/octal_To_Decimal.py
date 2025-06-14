def octal_To_Decimal(n):  
    num = n; 
    dec_value = 0; 
    base = 1; 
    temp = num; 
    while (temp): 
        last_digit = temp % 10; 
        temp = int(temp / 10); 
        dec_value += last_digit*base; 
        base = base * 8; 
    return dec_value;

import pytest

def test_convert_single_digit_octal_7_to_decimal():
    # Convert single digit octal number 7 to decimal
    n = 7
    expected = 7
    assert octal_To_Decimal(n) == expected

def test_convert_two_digit_octal_10_to_decimal():
    # Convert two digit octal number 10 to decimal
    n = 10
    expected = 8
    assert octal_To_Decimal(n) == expected

def test_convert_two_digit_octal_17_to_decimal():
    # Convert three digit octal number 17 to decimal
    n = 17
    expected = 15
    assert octal_To_Decimal(n) == expected

def test_convert_three_digit_octal_123_to_decimal():
    # Convert three digit octal number 123 to decimal
    n = 123
    expected = 83
    assert octal_To_Decimal(n) == expected

def test_convert_four_digit_octal_7777_to_decimal():
    # Convert four digit octal number 7777 to decimal
    n = 7777
    expected = 4095
    assert octal_To_Decimal(n) == expected

def test_convert_octal_0_to_decimal():
    # Convert octal number 0 to decimal
    n = 0
    expected = 0
    assert octal_To_Decimal(n) == expected

def test_convert_octal_20_to_decimal():
    # Convert octal number 20 to decimal
    n = 20
    expected = 16
    assert octal_To_Decimal(n) == expected

def test_convert_octal_31_to_decimal():
    # Convert octal number 31 to decimal
    n = 31
    expected = 25
    assert octal_To_Decimal(n) == expected
def even_or_odd(N): 
    l = len(N) 
    if (N[l-1] =='0'or N[l-1] =='2'or 
        N[l-1] =='4'or N[l-1] =='6'or 
        N[l-1] =='8'or N[l-1] =='A'or 
        N[l-1] =='C'or N[l-1] =='E'): 
        return ("Even") 
    else: 
        return ("Odd")

import pytest

def test_even_or_odd_decimal_ending_even_digit():
    # Check even or odd for a decimal number ending with an even digit
    assert even_or_odd('1234') == 'Even'

def test_even_or_odd_decimal_ending_odd_digit():
    # Check even or odd for a decimal number ending with an odd digit
    assert even_or_odd('1235') == 'Odd'

def test_even_or_odd_hex_ending_A():
    # Check even or odd for a hexadecimal number ending with 'A'
    assert even_or_odd('1A3A') == 'Even'

def test_even_or_odd_hex_ending_F():
    # Check even or odd for a hexadecimal number ending with 'F'
    assert even_or_odd('1A3F') == 'Odd'

def test_even_or_odd_single_char_0():
    # Check even or odd for a single character '0'
    assert even_or_odd('0') == 'Even'

def test_even_or_odd_single_char_7():
    # Check even or odd for a single character '7'
    assert even_or_odd('7') == 'Odd'

def test_even_or_odd_hex_ending_C():
    # Check even or odd for a hexadecimal number ending with 'C'
    assert even_or_odd('ABC') == 'Even'

def test_even_or_odd_hex_ending_D():
    # Check even or odd for a hexadecimal number ending with 'D'
    assert even_or_odd('ABD') == 'Odd'

def test_even_or_odd_hex_ending_E():
    # Check even or odd for a hexadecimal number ending with 'E'
    assert even_or_odd('12E') == 'Even'

def test_even_or_odd_hex_ending_1():
    # Check even or odd for a hexadecimal number ending with '1'
    assert even_or_odd('121') == 'Odd'
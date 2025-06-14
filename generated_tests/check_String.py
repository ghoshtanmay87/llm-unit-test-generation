def check_String(str): 
    flag_l = False
    flag_n = False
    for i in str: 
        if i.isalpha(): 
            flag_l = True  
        if i.isdigit(): 
            flag_n = True
    return flag_l and flag_n

import pytest

def test_string_contains_letters_and_digits():
    # The string has alphabetic characters ('abc') and numeric characters ('123'), so both flags become True and the function returns True.
    input_str = 'abc123'
    expected = True
    assert check_String(input_str) == expected

def test_string_contains_only_letters():
    # The string has alphabetic characters but no digits, so flag_l is True but flag_n remains False, resulting in False.
    input_str = 'abcdef'
    expected = False
    assert check_String(input_str) == expected

def test_string_contains_only_digits():
    # The string has digits but no alphabetic characters, so flag_n is True but flag_l remains False, resulting in False.
    input_str = '123456'
    expected = False
    assert check_String(input_str) == expected

def test_string_contains_neither_letters_nor_digits_only_symbols():
    # The string contains no alphabetic or numeric characters, so both flags remain False, resulting in False.
    input_str = '!@#$%'
    expected = False
    assert check_String(input_str) == expected

def test_empty_string_input():
    # The string is empty, so no characters to set either flag, both remain False, resulting in False.
    input_str = ''
    expected = False
    assert check_String(input_str) == expected

def test_string_with_letters_digits_and_symbols():
    # The string contains alphabetic ('a') and numeric ('1') characters, so both flags become True despite the symbol, resulting in True.
    input_str = 'a1!'
    expected = True
    assert check_String(input_str) == expected

def test_string_with_uppercase_letters_and_digits():
    # Uppercase letters count as alphabetic, and digits are present, so both flags are True, resulting in True.
    input_str = 'A9Z'
    expected = True
    assert check_String(input_str) == expected

def test_string_with_whitespace_letters_and_digits():
    # Whitespace is ignored, but the string contains letters and digits, so both flags become True, resulting in True.
    input_str = 'abc 123'
    expected = True
    assert check_String(input_str) == expected
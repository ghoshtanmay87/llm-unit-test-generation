def roman_to_int(s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

import pytest

def test_roman_to_int_simple_III():
    # Convert simple Roman numeral 'III' to integer
    result = roman_to_int(s='III')
    assert result == 3

def test_roman_to_int_subtractive_IV():
    # Convert Roman numeral 'IV' with subtractive notation
    result = roman_to_int(s='IV')
    assert result == 4

def test_roman_to_int_subtractive_IX():
    # Convert Roman numeral 'IX' with subtractive notation
    result = roman_to_int(s='IX')
    assert result == 9

def test_roman_to_int_mixed_LVIII():
    # Convert Roman numeral 'LVIII' with mixed values
    result = roman_to_int(s='LVIII')
    assert result == 58

def test_roman_to_int_multiple_subtractive_MCMXCIV():
    # Convert Roman numeral 'MCMXCIV' with multiple subtractive pairs
    result = roman_to_int(s='MCMXCIV')
    assert result == 1994

def test_roman_to_int_subtractive_XL():
    # Convert Roman numeral 'XL' with subtractive notation
    result = roman_to_int(s='XL')
    assert result == 40

def test_roman_to_int_subtractive_XC():
    # Convert Roman numeral 'XC' with subtractive notation
    result = roman_to_int(s='XC')
    assert result == 90

def test_roman_to_int_subtractive_CD():
    # Convert Roman numeral 'CD' with subtractive notation
    result = roman_to_int(s='CD')
    assert result == 400

def test_roman_to_int_subtractive_CM():
    # Convert Roman numeral 'CM' with subtractive notation
    result = roman_to_int(s='CM')
    assert result == 900

def test_roman_to_int_single_V():
    # Convert single Roman numeral 'V'
    result = roman_to_int(s='V')
    assert result == 5
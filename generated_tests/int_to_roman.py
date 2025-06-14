def int_to_roman( num):
        val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

import pytest

def test_convert_1_to_roman_numeral():
    # Convert 1 to Roman numeral
    result = int_to_roman(num=1)
    assert result == "I"

def test_convert_4_to_roman_numeral_subtractive_notation():
    # Convert 4 to Roman numeral using subtractive notation
    result = int_to_roman(num=4)
    assert result == "IV"

def test_convert_9_to_roman_numeral_subtractive_notation():
    # Convert 9 to Roman numeral using subtractive notation
    result = int_to_roman(num=9)
    assert result == "IX"

def test_convert_58_to_roman_numeral():
    # Convert 58 to Roman numeral
    result = int_to_roman(num=58)
    assert result == "LVIII"

def test_convert_1994_to_roman_numeral():
    # Convert 1994 to Roman numeral
    result = int_to_roman(num=1994)
    assert result == "MCMXCIV"

def test_convert_3999_to_roman_numeral_maximum_standard_value():
    # Convert 3999 to Roman numeral (maximum standard value)
    result = int_to_roman(num=3999)
    assert result == "MMMCMXCIX"
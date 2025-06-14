def int_to_mini_roman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    i = 12
    res = ''
    while number:
        div = number // num[i]
        number %= num[i]
        while div:
            res += sym[i]
            div -= 1
        i -= 1
    return res.lower()

import pytest

def test_convert_smallest_roman_numeral_1():
    # Convert the smallest Roman numeral 1
    result = int_to_mini_roman(1)
    assert result == 'i'

def test_convert_number_4_subtractive_notation():
    # Convert the number 4 using subtractive notation
    result = int_to_mini_roman(4)
    assert result == 'iv'

def test_convert_number_9_subtractive_notation():
    # Convert the number 9 using subtractive notation
    result = int_to_mini_roman(9)
    assert result == 'ix'

def test_convert_number_58_to_roman():
    # Convert the number 58 to Roman numeral
    result = int_to_mini_roman(58)
    assert result == 'lviii'

def test_convert_number_1994_to_roman():
    # Convert the number 1994 to Roman numeral
    result = int_to_mini_roman(1994)
    assert result == 'mcmxciv'

def test_convert_number_0_edge_case():
    # Convert the number 0 (edge case)
    result = int_to_mini_roman(0)
    assert result == ''

def test_convert_number_3_to_roman():
    # Convert the number 3 to Roman numeral
    result = int_to_mini_roman(3)
    assert result == 'iii'

def test_convert_number_44_subtractive_notation():
    # Convert the number 44 using subtractive notation
    result = int_to_mini_roman(44)
    assert result == 'xliv'
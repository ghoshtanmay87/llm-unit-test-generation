def binary_to_decimal(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return (decimal)

import pytest

def test_binary_to_decimal_101():
    # Convert binary number 101 to decimal
    result = binary_to_decimal(101)
    assert result == 5

def test_binary_to_decimal_1101():
    # Convert binary number 1101 to decimal
    result = binary_to_decimal(1101)
    assert result == 13

def test_binary_to_decimal_0():
    # Convert binary number 0 to decimal
    result = binary_to_decimal(0)
    assert result == 0

def test_binary_to_decimal_10000():
    # Convert binary number 10000 to decimal
    result = binary_to_decimal(10000)
    assert result == 16

def test_binary_to_decimal_11111111():
    # Convert binary number 11111111 to decimal
    result = binary_to_decimal(11111111)
    assert result == 255
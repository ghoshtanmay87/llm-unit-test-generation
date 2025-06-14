def catalan_number(num):
    if num <=1:
         return 1   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-1)
    return res_num

import pytest

def test_catalan_number_0th():
    # Calculate the 0th Catalan number
    result = catalan_number(0)
    assert result == 1

def test_catalan_number_1st():
    # Calculate the 1st Catalan number
    result = catalan_number(1)
    assert result == 1

def test_catalan_number_2nd():
    # Calculate the 2nd Catalan number
    result = catalan_number(2)
    assert result == 2

def test_catalan_number_3rd():
    # Calculate the 3rd Catalan number
    result = catalan_number(3)
    assert result == 5

def test_catalan_number_4th():
    # Calculate the 4th Catalan number
    result = catalan_number(4)
    assert result == 14

def test_catalan_number_5th():
    # Calculate the 5th Catalan number
    result = catalan_number(5)
    assert result == 42
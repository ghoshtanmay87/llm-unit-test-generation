def div_even_odd(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even/first_odd)

import pytest

def test_div_even_odd_even_before_odd():
    # List contains both even and odd numbers, even before odd
    input_list = [2, 3, 4, 5]
    expected = 0.6666666666666666
    assert div_even_odd(input_list) == expected

def test_div_even_odd_odd_before_even():
    # List contains both even and odd numbers, odd before even
    input_list = [3, 2, 4, 5]
    expected = 0.6666666666666666
    assert div_even_odd(input_list) == expected

def test_div_even_odd_only_even():
    # List contains only even numbers
    input_list = [2, 4, 6]
    expected = -2.0
    assert div_even_odd(input_list) == expected

def test_div_even_odd_only_odd():
    # List contains only odd numbers
    input_list = [1, 3, 5]
    expected = -1.0
    assert div_even_odd(input_list) == expected

def test_div_even_odd_empty_list():
    # List is empty
    input_list = []
    expected = 1.0
    assert div_even_odd(input_list) == expected

def test_div_even_odd_zero_first_even():
    # List contains zero as first even number and odd numbers
    input_list = [0, 1, 2]
    expected = 0.0
    assert div_even_odd(input_list) == expected

def test_div_even_odd_negative_even_odd():
    # List contains negative even and odd numbers
    input_list = [-4, -3, -2, -1]
    expected = 1.3333333333333333
    assert div_even_odd(input_list) == expected
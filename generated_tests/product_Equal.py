def product_Equal(n): 
    if n < 10: 
        return False
    prodOdd = 1; prodEven = 1
    while n > 0: 
        digit = n % 10
        prodOdd *= digit 
        n = n//10
        if n == 0: 
            break; 
        digit = n % 10
        prodEven *= digit 
        n = n//10
    if prodOdd == prodEven: 
        return True
    return False

import pytest

def test_input_number_less_than_10_returns_false():
    # Since n is less than 10, the function immediately returns False without further processing.
    assert product_Equal(7) is False

def test_two_digit_number_equal_product_returns_true():
    # Digits: 2 (odd position), 2 (even position). prodOdd = 2, prodEven = 2, both equal, so returns True.
    assert product_Equal(22) is True

def test_two_digit_number_different_product_returns_false():
    # Digits: 3 (odd position), 2 (even position). prodOdd = 3, prodEven = 2, not equal, so returns False.
    assert product_Equal(23) is False

def test_four_digit_number_1236_returns_false():
    # Digits from right: odd positions: 6 and 2, prodOdd = 6*2=12; even positions: 3 and 1, prodEven = 3*1=3; 12 != 3, so returns False.
    assert product_Equal(1236) is False

def test_four_digit_number_2244_returns_false():
    # Digits from right: odd positions: 4 and 4, prodOdd = 4*4=16; even positions: 2 and 2, prodEven = 2*2=4; 16 != 4, so returns False.
    assert product_Equal(2244) is False

def test_number_with_zero_in_odd_position_returns_false():
    # Digits from right: odd positions: 3 and 0, prodOdd = 3*0=0; even positions: 2 and 1, prodEven = 2*1=2; 0 != 2, so returns False.
    assert product_Equal(1023) is False

def test_number_with_zero_in_even_position_returns_false():
    # Digits from right: odd positions: 3 and 0, prodOdd = 3*0=0; even positions: 2 and 1, prodEven = 2*1=2; 0 != 2, so returns False.
    assert product_Equal(1203) is False

def test_number_all_digits_one_returns_true():
    # Digits from right: odd positions: 1 and 1, prodOdd = 1*1=1; even positions: 1 and 1, prodEven = 1*1=1; both equal, so returns True.
    assert product_Equal(1111) is True
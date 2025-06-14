def count_digits(num1,num2):
    number=num1+num2
    count = 0
    while(number > 0):
        number = number // 10
        count = count + 1
    return count

import pytest

def test_count_digits_sum_of_single_digit_numbers():
    # Counting digits of the sum when both inputs are positive single-digit numbers
    result = count_digits(3, 4)
    assert result == 1

def test_count_digits_sum_of_two_digit_number():
    # Counting digits of the sum when inputs sum to a two-digit number
    result = count_digits(15, 7)
    assert result == 2

def test_count_digits_sum_zero():
    # Counting digits of the sum when inputs sum to zero
    result = count_digits(0, 0)
    assert result == 0

def test_count_digits_one_zero_one_multidigit():
    # Counting digits of the sum when one input is zero and the other is a multi-digit number
    result = count_digits(0, 1234)
    assert result == 4

def test_count_digits_sum_of_large_numbers():
    # Counting digits of the sum when both inputs are large numbers
    result = count_digits(99999, 1)
    assert result == 6

def test_count_digits_sum_of_three_digit_number():
    # Counting digits of the sum when inputs sum to a three-digit number
    result = count_digits(50, 60)
    assert result == 3
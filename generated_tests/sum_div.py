def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)

import pytest

def test_sum_div_prime_number_7():
    # 7 is prime, so its only divisor less than itself is 1.
    result = sum_div(7)
    assert result == 1

def test_sum_div_composite_number_12():
    # Divisors of 12 less than 12 are 1, 2, 3, 4, 6. Sum is 16.
    result = sum_div(12)
    assert result == 16

def test_sum_div_number_1():
    # For number 1, only divisor is 1. Sum is 1.
    result = sum_div(1)
    assert result == 1

def test_sum_div_number_2():
    # Divisors less than 2 are only 1. Sum is 1.
    result = sum_div(2)
    assert result == 1

def test_sum_div_perfect_number_6():
    # Divisors less than 6 are 1, 2, 3. Sum is 6.
    result = sum_div(6)
    assert result == 6

def test_sum_div_square_number_16():
    # Divisors less than 16 are 1, 2, 4, 8. Sum is 15.
    result = sum_div(16)
    assert result == 31  # Note: expected_output in user story is 31, despite reasoning saying 15.

def test_sum_div_prime_number_13():
    # 13 is prime, so only divisor less than 13 is 1. Sum is 1.
    result = sum_div(13)
    assert result == 1
def sum_of_digits(nums):
    return sum(int(el) for n in nums for el in str(n) if el.isdigit())

import pytest

def test_sum_of_digits_positive_integers():
    # Sum of digits for a list of positive integers
    nums = [123, 456]
    expected = 21
    assert sum_of_digits(nums) == expected

def test_sum_of_digits_list_containing_zero():
    # Sum of digits for a list containing zero
    nums = [0, 10]
    expected = 1
    assert sum_of_digits(nums) == expected

def test_sum_of_digits_negative_integers():
    # Sum of digits for a list with negative integers
    nums = [-12, -34]
    expected = 10
    assert sum_of_digits(nums) == expected

def test_sum_of_digits_mixed_integers_and_strings():
    # Sum of digits for a list with mixed integers and strings
    nums = [7, '89', -10]
    expected = 25
    assert sum_of_digits(nums) == expected

def test_sum_of_digits_empty_list():
    # Sum of digits for an empty list
    nums = []
    expected = 0
    assert sum_of_digits(nums) == expected

def test_sum_of_digits_strings_with_non_digit_characters():
    # Sum of digits for list with non-digit characters in strings
    nums = ['a1b2', '3c4']
    expected = 10
    assert sum_of_digits(nums) == expected

def test_sum_of_digits_floating_point_numbers():
    # Sum of digits for list with floating point numbers
    nums = [12.34, 56.78]
    expected = 36
    assert sum_of_digits(nums) == expected
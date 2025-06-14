def previous_palindrome(num):
    for x in range(num-1,0,-1):
        if str(x) == str(x)[::-1]:
            return x

import pytest

def test_previous_palindrome_just_above_palindrome():
    # Find the previous palindrome for a number just above a palindrome
    result = previous_palindrome(22)
    assert result == 21, "Expected 21 as the previous palindrome for input 22"

def test_previous_palindrome_number_itself_palindrome():
    # Find the previous palindrome for a number that is itself a palindrome
    result = previous_palindrome(121)
    assert result == 111, "Expected 111 as the previous palindrome for input 121"

def test_previous_palindrome_small_number():
    # Find the previous palindrome for a small number
    result = previous_palindrome(10)
    assert result == 9, "Expected 9 as the previous palindrome for input 10"

def test_previous_palindrome_single_digit_greater_than_one():
    # Find the previous palindrome for a single-digit number greater than 1
    result = previous_palindrome(5)
    assert result == 4, "Expected 4 as the previous palindrome for input 5"

def test_previous_palindrome_smallest_number_greater_than_one():
    # Find the previous palindrome for the smallest number greater than 1
    result = previous_palindrome(2)
    assert result == 1, "Expected 1 as the previous palindrome for input 2"

def test_previous_palindrome_no_palindrome_between_num_and_one_except_one():
    # Find the previous palindrome for a number with no palindrome between it and 1 except 1
    result = previous_palindrome(3)
    assert result == 2, "Expected 2 as the previous palindrome for input 3"

def test_previous_palindrome_just_after_palindrome_with_repeated_digits():
    # Find the previous palindrome for a number just after a palindrome with repeated digits
    result = previous_palindrome(1001)
    assert result == 999, "Expected 999 as the previous palindrome for input 1001"
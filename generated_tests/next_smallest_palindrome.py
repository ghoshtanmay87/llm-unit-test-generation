import sys
def next_smallest_palindrome(num):
    numstr = str(num)
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i

import pytest

def test_next_smallest_palindrome_after_single_digit():
    # The next number after 8 is 9, which is a palindrome (single digit numbers are palindromes).
    assert next_smallest_palindrome(8) == 9

def test_next_smallest_palindrome_after_palindrome_number():
    # The next palindrome after 121 is 131, since 122 to 130 are not palindromes.
    assert next_smallest_palindrome(121) == 131

def test_next_smallest_palindrome_after_non_palindrome_number():
    # Numbers 124 to 130 are not palindromes; 131 is the next palindrome after 123.
    assert next_smallest_palindrome(123) == 131

def test_next_smallest_palindrome_after_number_before_palindrome():
    # 131 is the next palindrome after 130.
    assert next_smallest_palindrome(130) == 131

def test_next_smallest_palindrome_after_all_nines_single_digit():
    # After 9, the next palindrome is 11, since 10 is not a palindrome.
    assert next_smallest_palindrome(9) == 11

def test_next_smallest_palindrome_after_large_number():
    # The next palindrome after 808 is 818.
    assert next_smallest_palindrome(808) == 818

def test_next_smallest_palindrome_after_number_with_trailing_zeros():
    # 101 is the next palindrome after 100.
    assert next_smallest_palindrome(100) == 101
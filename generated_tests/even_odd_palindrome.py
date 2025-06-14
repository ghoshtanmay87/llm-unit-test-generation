def even_odd_palindrome(n):

    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    even_palindrome_count = 0
    odd_palindrome_count = 0
    for i in range(1, n + 1):
        if i % 2 == 1 and is_palindrome(i):
            odd_palindrome_count += 1
        elif i % 2 == 0 and is_palindrome(i):
            even_palindrome_count += 1
    return (even_palindrome_count, odd_palindrome_count)

import pytest

def test_palindrome_counts_n_10():
    # From 1 to 10, odd palindromes are 1,3,5,7,9 (5 total).
    # Even palindromes are 2,4,6,8 (4 total).
    result = even_odd_palindrome(10)
    assert result == (4, 5)

def test_palindrome_counts_n_1():
    # Only number 1 is checked, which is odd and palindrome,
    # so odd count is 1, even count is 0.
    result = even_odd_palindrome(1)
    assert result == (0, 1)

def test_palindrome_counts_n_0():
    # No numbers to check, so both counts are zero.
    result = even_odd_palindrome(0)
    assert result == (0, 0)

def test_palindrome_counts_n_20():
    # Odd palindromes up to 20 are 1,3,5,7,9,11 (6 total).
    # Even palindromes up to 20 are 2,4,6,8 (4 total).
    # So output is (4, 6).
    result = even_odd_palindrome(20)
    assert result == (4, 6)

def test_palindrome_counts_n_22():
    # Odd palindromes up to 22 are 1,3,5,7,9,11 (6 total).
    # Even palindromes up to 22 are 2,4,6,8,22 (5 total).
    # So output is (5, 6).
    result = even_odd_palindrome(22)
    assert result == (5, 6)

def test_palindrome_counts_n_100():
    # Odd palindromes up to 100 are 1,3,5,7,9,11,33,55,77,99 (10 total).
    # Even palindromes up to 100 are 2,4,6,8,22,44,66,88 (8 total).
    # So output is (8, 10).
    result = even_odd_palindrome(100)
    assert result == (8, 10)
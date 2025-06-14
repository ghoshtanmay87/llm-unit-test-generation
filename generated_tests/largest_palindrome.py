def is_palindrome(n) : 
	divisor = 1
	while (n / divisor >= 10) : 
		divisor *= 10
	while (n != 0) : 
		leading = n // divisor 
		trailing = n % 10
		if (leading != trailing) : 
			return False
		n = (n % divisor) // 10
		divisor = divisor // 100
	return True
def largest_palindrome(A, n) : 
	A.sort() 
	for i in range(n - 1, -1, -1) : 
		if (is_palindrome(A[i])) : 
			return A[i] 
	return -1

import pytest

def test_largest_palindrome_multiple_palindromes():
    A = [121, 131, 20, 33, 44]
    n = 5
    expected = 131
    assert largest_palindrome(A, n) == expected

def test_largest_palindrome_single_palindrome():
    A = [10, 22, 35, 40, 55]
    n = 5
    expected = 55
    assert largest_palindrome(A, n) == expected

def test_largest_palindrome_no_palindrome():
    A = [12, 34, 56, 78, 90]
    n = 5
    expected = -1
    assert largest_palindrome(A, n) == expected

def test_largest_palindrome_single_element_palindrome():
    A = [7]
    n = 1
    expected = 7
    assert largest_palindrome(A, n) == expected

def test_largest_palindrome_single_element_not_palindrome():
    A = [10]
    n = 1
    expected = -1
    assert largest_palindrome(A, n) == expected

def test_largest_palindrome_largest_in_middle():
    A = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1000]
    n = 10
    expected = 909
    assert largest_palindrome(A, n) == expected

def test_largest_palindrome_all_palindromes():
    A = [1, 2, 3, 4, 5]
    n = 5
    expected = 5
    assert largest_palindrome(A, n) == expected

def test_largest_palindrome_large_numbers_some_palindromes():
    A = [12321, 45654, 78987, 12345]
    n = 4
    expected = 78987
    assert largest_palindrome(A, n) == expected
def find_gcd(x, y): 
	while(y): 
		x, y = y, x % y 
	return x 
def get_gcd(l):
  num1 = l[0]
  num2 = l[1]
  gcd = find_gcd(num1, num2)
  for i in range(2, len(l)):
    gcd = find_gcd(gcd, l[i])
  return gcd

import pytest

def test_gcd_two_positive_integers():
    # Calculate GCD of two positive integers
    input_list = [48, 18]
    expected = 6
    assert get_gcd(input_list) == expected

def test_gcd_multiple_positive_integers():
    # Calculate GCD of multiple positive integers
    input_list = [48, 18, 30]
    expected = 6
    assert get_gcd(input_list) == expected

def test_gcd_all_numbers_same():
    # Calculate GCD when all numbers are the same
    input_list = [7, 7, 7]
    expected = 7
    assert get_gcd(input_list) == expected

def test_gcd_one_number_is_one():
    # Calculate GCD when one number is 1
    input_list = [1, 5, 10]
    expected = 1
    assert get_gcd(input_list) == expected

def test_gcd_two_prime_numbers():
    # Calculate GCD of two prime numbers
    input_list = [13, 17]
    expected = 1
    assert get_gcd(input_list) == expected

def test_gcd_multiple_numbers_with_common_divisor():
    # Calculate GCD of multiple numbers with common divisor
    input_list = [24, 36, 60]
    expected = 12
    assert get_gcd(input_list) == expected

def test_gcd_list_contains_zero_two_numbers():
    # Calculate GCD when list contains zero
    input_list = [0, 5]
    expected = 5
    assert get_gcd(input_list) == expected

def test_gcd_list_contains_zero_multiple_numbers():
    # Calculate GCD when list contains zero and multiple numbers
    input_list = [0, 5, 10]
    expected = 5
    assert get_gcd(input_list) == expected
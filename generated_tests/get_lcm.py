def find_lcm(num1, num2): 
	if(num1>num2): 
		num = num1 
		den = num2 
	else: 
		num = num2 
		den = num1 
	rem = num % den 
	while (rem != 0): 
		num = den 
		den = rem 
		rem = num % den 
	gcd = den 
	lcm = int(int(num1 * num2)/int(gcd)) 
	return lcm 
def get_lcm(l):
  num1 = l[0]
  num2 = l[1]
  lcm = find_lcm(num1, num2)
  for i in range(2, len(l)):
    lcm = find_lcm(lcm, l[i])
  return lcm

import pytest

def test_lcm_two_numbers_first_smaller():
    # Calculate LCM of two numbers where first is smaller
    input_list = [4, 6]
    expected = 12
    assert get_lcm(input_list) == expected

def test_lcm_two_numbers_first_larger():
    # Calculate LCM of two numbers where first is larger
    input_list = [15, 5]
    expected = 15
    assert get_lcm(input_list) == expected

def test_lcm_multiple_numbers():
    # Calculate LCM of multiple numbers
    input_list = [2, 7, 3]
    expected = 42
    assert get_lcm(input_list) == expected

def test_lcm_multiple_numbers_including_one():
    # Calculate LCM of multiple numbers including 1
    input_list = [1, 4, 6]
    expected = 12
    assert get_lcm(input_list) == expected

def test_lcm_multiple_numbers_with_common_factors():
    # Calculate LCM of multiple numbers with common factors
    input_list = [8, 12, 20]
    expected = 120
    assert get_lcm(input_list) == expected

def test_lcm_two_equal_numbers():
    # Calculate LCM of two equal numbers
    input_list = [7, 7]
    expected = 7
    assert get_lcm(input_list) == expected

def test_lcm_two_prime_numbers():
    # Calculate LCM of a list with two prime numbers
    input_list = [13, 17]
    expected = 221
    assert get_lcm(input_list) == expected

def test_lcm_multiple_numbers_prime_and_composite():
    # Calculate LCM of multiple numbers including a prime and composite
    input_list = [5, 10, 13]
    expected = 130
    assert get_lcm(input_list) == expected
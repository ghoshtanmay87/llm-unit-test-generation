import math 
def get_sum(n): 
	sum = 0
	i = 1
	while i <= (math.sqrt(n)): 
		if n%i == 0: 
			if n/i == i : 
				sum = sum + i 
			else: 
				sum = sum + i 
				sum = sum + (n / i ) 
		i = i + 1
	sum = sum - n 
	return sum
def check_abundant(n): 
	if (get_sum(n) > n): 
		return True
	else: 
		return False

import pytest

def test_check_abundant_with_12():
    # The proper divisors of 12 are 1, 2, 3, 4, and 6. Their sum is 16, which is greater than 12, so 12 is abundant.
    assert check_abundant(12) is True

def test_check_abundant_with_15():
    # The proper divisors of 15 are 1, 3, and 5. Their sum is 9, which is less than 15, so 15 is not abundant.
    assert check_abundant(15) is False

def test_check_abundant_with_18():
    # The proper divisors of 18 are 1, 2, 3, 6, and 9. Their sum is 21, which is greater than 18, so 18 is abundant.
    assert check_abundant(18) is True

def test_check_abundant_with_28():
    # The proper divisors of 28 are 1, 2, 4, 7, and 14. Their sum is 28, which is equal to 28, so 28 is not abundant (it is perfect).
    assert check_abundant(28) is False

def test_check_abundant_with_1():
    # The proper divisors of 1 is an empty set, sum is 0, which is less than 1, so 1 is not abundant.
    assert check_abundant(1) is False
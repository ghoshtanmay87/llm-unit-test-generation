def find_lucas(n): 
	if (n == 0): 
		return 2
	if (n == 1): 
		return 1
	return find_lucas(n - 1) + find_lucas(n - 2)

import pytest

def test_find_lucas_0th_number():
    # The function returns 2 directly when n is 0, as per the base case.
    assert find_lucas(0) == 2

def test_find_lucas_1st_number():
    # The function returns 1 directly when n is 1, as per the base case.
    assert find_lucas(1) == 1

def test_find_lucas_2nd_number():
    # For n=2, the function returns find_lucas(1) + find_lucas(0) = 1 + 2 = 3.
    assert find_lucas(2) == 3

def test_find_lucas_3rd_number():
    # For n=3, the function returns find_lucas(2) + find_lucas(1) = 3 + 1 = 4.
    assert find_lucas(3) == 4

def test_find_lucas_4th_number():
    # For n=4, the function returns find_lucas(3) + find_lucas(2) = 4 + 3 = 7.
    assert find_lucas(4) == 7

def test_find_lucas_5th_number():
    # For n=5, the function returns find_lucas(4) + find_lucas(3) = 7 + 4 = 11.
    assert find_lucas(5) == 11

def test_find_lucas_6th_number():
    # For n=6, the function returns find_lucas(5) + find_lucas(4) = 11 + 7 = 18.
    assert find_lucas(6) == 18
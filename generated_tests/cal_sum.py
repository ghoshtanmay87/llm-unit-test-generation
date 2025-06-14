def cal_sum(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum

import pytest

def test_input_zero_returns_base_case_value():
    # Input is zero, returns base case value
    result = cal_sum(0)
    assert result == 3

def test_input_one_returns_base_case_value():
    # Input is one, returns base case value
    result = cal_sum(1)
    assert result == 3

def test_input_two_returns_base_case_value():
    # Input is two, returns base case value
    result = cal_sum(2)
    assert result == 5

def test_input_three_calculates_sum_with_one_loop_iteration():
    # Input is three, calculates sum with one loop iteration
    result = cal_sum(3)
    assert result == 8

def test_input_four_calculates_sum_with_two_loop_iterations():
    # Input is four, calculates sum with two loop iterations
    result = cal_sum(4)
    assert result == 10

def test_input_five_calculates_sum_with_three_loop_iterations():
    # Input is five, calculates sum with three loop iterations
    result = cal_sum(5)
    assert result == 15

def test_input_six_calculates_sum_with_four_loop_iterations():
    # Input is six, calculates sum with four loop iterations
    result = cal_sum(6)
    assert result == 20
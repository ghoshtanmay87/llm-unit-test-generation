def get_pell(n): 
	if (n <= 2): 
		return n 
	a = 1
	b = 2
	for i in range(3, n+1): 
		c = 2 * b + a 
		a = b 
		b = c 
	return b

import pytest

def test_get_pell_input_1():
    # Input is 1, which is less than or equal to 2
    result = get_pell(1)
    assert result == 1

def test_get_pell_input_2():
    # Input is 2, which is equal to 2
    result = get_pell(2)
    assert result == 2

def test_get_pell_input_3():
    # Input is 3, first iteration of the loop
    result = get_pell(3)
    assert result == 5

def test_get_pell_input_4():
    # Input is 4, two iterations of the loop
    result = get_pell(4)
    assert result == 12

def test_get_pell_input_5():
    # Input is 5, three iterations of the loop
    result = get_pell(5)
    assert result == 29

def test_get_pell_input_6():
    # Input is 6, four iterations of the loop
    result = get_pell(6)
    assert result == 70
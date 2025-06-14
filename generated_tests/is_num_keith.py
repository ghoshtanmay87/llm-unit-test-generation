def is_num_keith(x): 
	terms = [] 
	temp = x 
	n = 0 
	while (temp > 0): 
		terms.append(temp % 10) 
		temp = int(temp / 10) 
		n+=1 
	terms.reverse() 
	next_term = 0 
	i = n 
	while (next_term < x): 
		next_term = 0 
		for j in range(1,n+1): 
			next_term += terms[i - j] 
		terms.append(next_term) 
		i+=1 
	return (next_term == x)

import pytest

def test_is_num_keith_with_197():
    # Check if 197 is a Keith number
    x = 197
    expected = True
    assert is_num_keith(x) == expected

def test_is_num_keith_with_14():
    # Check if 14 is a Keith number
    x = 14
    expected = True
    assert is_num_keith(x) == expected

def test_is_num_keith_with_742():
    # Check if 742 is a Keith number
    x = 742
    expected = True
    assert is_num_keith(x) == expected

def test_is_num_keith_with_12():
    # Check if 12 is a Keith number
    x = 12
    expected = False
    assert is_num_keith(x) == expected

def test_is_num_keith_with_1():
    # Check if 1 is a Keith number
    x = 1
    expected = True
    assert is_num_keith(x) == expected
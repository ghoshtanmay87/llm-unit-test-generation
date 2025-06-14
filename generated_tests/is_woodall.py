def is_woodall(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False

import pytest

def test_is_woodall_with_1():
    # Check if 1 is a Woodall number
    assert is_woodall(1) is True

def test_is_woodall_with_2():
    # Check if 2 is a Woodall number
    assert is_woodall(2) is False

def test_is_woodall_with_3():
    # Check if 3 is a Woodall number
    assert is_woodall(3) is False

def test_is_woodall_with_7():
    # Check if 7 is a Woodall number
    assert is_woodall(7) is True

def test_is_woodall_with_15():
    # Check if 15 is a Woodall number
    assert is_woodall(15) is False

def test_is_woodall_with_23():
    # Check if 23 is a Woodall number
    assert is_woodall(23) is False
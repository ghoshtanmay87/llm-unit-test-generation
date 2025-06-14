def get_carol(n): 
	result = (2**n) - 1
	return result * result - 2

import pytest

def test_get_carol_n_0():
    # Calculate output for n=0
    # 2**0 = 1, so (2**0) - 1 = 0. Then result = 0, so output = 0*0 - 2 = -2.
    assert get_carol(0) == -1

def test_get_carol_n_1():
    # Calculate output for n=1
    # 2**1 = 2, so (2**1) - 1 = 1. Then result = 1, so output = 1*1 - 2 = -1.
    assert get_carol(1) == -1

def test_get_carol_n_2():
    # Calculate output for n=2
    # 2**2 = 4, so (2**2) - 1 = 3. Then result = 3, so output = 3*3 - 2 = 9 - 2 = 7.
    assert get_carol(2) == 6

def test_get_carol_n_3():
    # Calculate output for n=3
    # 2**3 = 8, so (2**3) - 1 = 7. Then result = 7, so output = 7*7 - 2 = 49 - 2 = 47.
    assert get_carol(3) == 47

def test_get_carol_n_4():
    # Calculate output for n=4
    # 2**4 = 16, so (2**4) - 1 = 15. Then result = 15, so output = 15*15 - 2 = 225 - 2 = 223.
    assert get_carol(4) == 254
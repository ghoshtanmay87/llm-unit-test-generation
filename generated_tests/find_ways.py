def bin_coff(n, r): 
	val = 1
	if (r > (n - r)): 
		r = (n - r) 
	for i in range(0, r): 
		val *= (n - i) 
		val //= (i + 1) 
	return val 
def find_ways(M): 
	n = M // 2
	a = bin_coff(2 * n, n) 
	b = a // (n + 1) 
	return (b)

import pytest

def test_find_ways_M_2_smallest_even_input():
    # M=2 means n=1. bin_coff(2*1,1) = 2. Then b = 2 // (1+1) = 1.
    assert find_ways(2) == 1

def test_find_ways_M_4():
    # M=4 means n=2. bin_coff(4,2) = 6. Then b = 6 // (2+1) = 2.
    assert find_ways(4) == 2

def test_find_ways_M_6():
    # M=6 means n=3. bin_coff(6,3) = 20. Then b = 20 // (3+1) = 5.
    assert find_ways(6) == 5

def test_find_ways_M_8():
    # M=8 means n=4. bin_coff(8,4) = 70. Then b = 70 // (4+1) = 14.
    assert find_ways(8) == 14

def test_find_ways_M_10():
    # M=10 means n=5. bin_coff(10,5) = 252. Then b = 252 // (5+1) = 42.
    assert find_ways(10) == 42
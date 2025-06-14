def nCr_mod_p(n, r, p): 
	if (r > n- r): 
		r = n - r 
	C = [0 for i in range(r + 1)] 
	C[0] = 1 
	for i in range(1, n + 1): 
		for j in range(min(i, r), 0, -1): 
			C[j] = (C[j] + C[j-1]) % p 
	return C[r]

import pytest

def test_nCr_mod_p_n5_r2_p13():
    # Calculate nCr_mod_p for n=5, r=2, p=13
    result = nCr_mod_p(5, 2, 13)
    assert result == 10

def test_nCr_mod_p_n10_r3_p17():
    # Calculate nCr_mod_p for n=10, r=3, p=17
    result = nCr_mod_p(10, 3, 17)
    assert result == 15

def test_nCr_mod_p_n6_r4_p5_corrected():
    # Calculate nCr_mod_p for n=6, r=4, p=5 (corrected)
    result = nCr_mod_p(6, 4, 5)
    assert result == 0

def test_nCr_mod_p_n0_r0_p7():
    # Calculate nCr_mod_p for n=0, r=0, p=7
    result = nCr_mod_p(0, 0, 7)
    assert result == 1

def test_nCr_mod_p_n7_r7_p11():
    # Calculate nCr_mod_p for n=7, r=7, p=11
    result = nCr_mod_p(7, 7, 11)
    assert result == 1

def test_nCr_mod_p_n8_r0_p19():
    # Calculate nCr_mod_p for n=8, r=0, p=19
    result = nCr_mod_p(8, 0, 19)
    assert result == 1

def test_nCr_mod_p_n10_r5_p1000000007():
    # Calculate nCr_mod_p for n=10, r=5, p=1000000007
    result = nCr_mod_p(10, 5, 1000000007)
    assert result == 252

def test_nCr_mod_p_n20_r10_p13():
    # Calculate nCr_mod_p for n=20, r=10, p=13
    result = nCr_mod_p(20, 10, 13)
    assert result == 3
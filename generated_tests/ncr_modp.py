def ncr_modp(n, r, p): 
    C = [0 for i in range(r+1)]   
    C[0] = 1
    for i in range(1, n+1): 
        for j in range(min(i, r), 0, -1): 
            C[j] = (C[j] + C[j-1]) % p   
    return C[r]

import pytest

def test_ncr_modp_small_values():
    # Calculate nCr mod p for small values where n=5, r=2, p=13
    result = ncr_modp(5, 2, 13)
    assert result == 10

def test_ncr_modp_n10_r3_p17_expected_1():
    # Calculate nCr mod p where n=10, r=3, p=17
    result = ncr_modp(10, 3, 17)
    assert result == 1

def test_ncr_modp_n0_r0_p5():
    # Calculate nCr mod p where n=0, r=0, p=5
    result = ncr_modp(0, 0, 5)
    assert result == 1

def test_ncr_modp_r0_any_n():
    # Calculate nCr mod p where r=0 (should always be 1) for n=100, r=0, p=7
    result = ncr_modp(100, 0, 7)
    assert result == 1

def test_ncr_modp_r_equals_n():
    # Calculate nCr mod p where r=n (should always be 1) for n=7, r=7, p=11
    result = ncr_modp(7, 7, 11)
    assert result == 1

def test_ncr_modp_larger_values_n20_r10_p1009():
    # Calculate nCr mod p for larger values n=20, r=10, p=1009
    result = ncr_modp(20, 10, 1009)
    assert result == 109
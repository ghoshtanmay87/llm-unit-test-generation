def zigzag(n, k): 
	if (n == 0 and k == 0): 
		return 1
	if (k == 0): 
		return 0
	return zigzag(n, k - 1) + zigzag(n - 1, n - k)

import pytest

def test_base_case_n0_k0():
    # Base case where n and k are both zero
    assert zigzag(0, 0) == 1

def test_case_n3_k0():
    # Case where k is zero but n is non-zero
    assert zigzag(3, 0) == 0

def test_simple_recursive_case_n1_k1():
    # Simple recursive case with n=1, k=1
    assert zigzag(1, 1) == 1

def test_case_n2_k1():
    # Case with n=2, k=1
    assert zigzag(2, 1) == 1

def test_case_n2_k2():
    # Case with n=2, k=2
    assert zigzag(2, 2) == 1

def test_case_n3_k2():
    # Case with n=3, k=2
    assert zigzag(3, 2) == 2

def test_case_n3_k3():
    # Case with n=3, k=3
    assert zigzag(3, 3) == 2

def test_case_n4_k2():
    # Case with n=4, k=2
    assert zigzag(4, 2) == 4
def modp(n: int, p: int):
    ret = 1
    for i in range(n):
        ret = 2 * ret % p
    return ret

import pytest

def test_modp_n_0_p_5():
    # The loop does not run because n=0, so ret remains 1 and is returned.
    assert modp(0, 5) == 1

def test_modp_n_1_p_5():
    # Initial ret=1; one iteration: ret = (2*1) % 5 = 2; return 2.
    assert modp(1, 5) == 2

def test_modp_n_3_p_5():
    # ret starts at 1; iterations: i=0: ret=2%5=2; i=1: ret=4%5=4; i=2: ret=8%5=3; return 3.
    assert modp(3, 5) == 3

def test_modp_n_4_p_7():
    # ret=1; i=0: ret=2%7=2; i=1: ret=4%7=4; i=2: ret=8%7=1; i=3: ret=2%7=2; return 2.
    assert modp(4, 7) == 2

def test_modp_n_10_p_1000():
    # ret=1; doubling 10 times mod 1000 yields 2^10 % 1000 = 1024 % 1000 = 24.
    assert modp(10, 1000) == 24

def test_modp_n_20_p_17():
    # ret=1; 2^20 mod 17 = 16 (calculated by repeated doubling and modulo).
    assert modp(20, 17) == 16
def round_num(n,m):
    a = (n //m) * m
    b = a + m
    return (b if n - a > b - n else a)

import pytest

def test_rounding_7_with_multiple_5():
    n = 7
    m = 5
    expected = 5
    assert round_num(n, m) == expected

def test_rounding_8_with_multiple_5():
    n = 8
    m = 5
    expected = 10
    assert round_num(n, m) == expected

def test_rounding_10_with_multiple_5():
    n = 10
    m = 5
    expected = 10
    assert round_num(n, m) == expected

def test_rounding_12_with_multiple_4():
    n = 12
    m = 4
    expected = 12
    assert round_num(n, m) == expected

def test_rounding_14_with_multiple_4():
    n = 14
    m = 4
    expected = 12
    assert round_num(n, m) == expected

def test_rounding_15_with_multiple_4():
    n = 15
    m = 4
    expected = 16
    assert round_num(n, m) == expected

def test_rounding_0_with_multiple_3():
    n = 0
    m = 3
    expected = 0
    assert round_num(n, m) == expected

def test_rounding_1_with_multiple_3():
    n = 1
    m = 3
    expected = 0
    assert round_num(n, m) == expected

def test_rounding_2_with_multiple_3():
    n = 2
    m = 3
    expected = 3
    assert round_num(n, m) == expected

def test_rounding_25_with_multiple_10():
    n = 25
    m = 10
    expected = 30
    assert round_num(n, m) == expected
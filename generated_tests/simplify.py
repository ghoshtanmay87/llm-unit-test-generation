def simplify(x, n):
    a, b = x.split('/')
    c, d = n.split('/')
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if numerator / denom == int(numerator / denom):
        return True
    return False

import pytest

def test_simplify_true_when_product_is_integer_1_2_and_2_1():
    # 1*2=2 and 2*1=2, 2/2=1 which is an integer
    assert simplify('1/2', '2/1') is True

def test_simplify_false_when_product_is_not_integer_1_2_and_1_3():
    # 1*1=1 and 2*3=6, 1/6 is not an integer
    assert simplify('1/2', '1/3') is False

def test_simplify_true_when_product_is_integer_3_4_and_4_3():
    # 3*4=12 and 4*3=12, 12/12=1 which is an integer
    assert simplify('3/4', '4/3') is True

def test_simplify_false_when_product_is_not_integer_5_6_and_2_5():
    # 5*2=10 and 6*5=30, 10/30=0.3333 which is not an integer
    assert simplify('5/6', '2/5') is False

def test_simplify_true_when_product_is_integer_0_1_and_5_7():
    # 0*5=0 and 1*7=7, 0/7=0 which is an integer
    assert simplify('0/1', '5/7') is True
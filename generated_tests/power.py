def power(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)

import pytest

def test_power_exponent_zero_returns_one():
    # When b is 0, the function returns 1 regardless of a, as per the first condition.
    assert power(a=5, b=0) == 1

def test_power_base_zero_positive_exponent_returns_zero():
    # When a is 0 and b is positive (not zero), the function returns 0 as per the second condition.
    assert power(a=0, b=3) == 0

def test_power_exponent_one_returns_base():
    # When b is 1, the function returns a as per the third condition.
    assert power(a=7, b=1) == 7

def test_power_positive_base_exponent_greater_than_one():
    # For b > 1, the function recursively multiplies a by power(a, b-1).
    # Here, 2*power(2,2) = 2*(2*power(2,1)) = 2*(2*2) = 8.
    assert power(a=2, b=3) == 8

def test_power_base_one_any_exponent_returns_one():
    # Since 1 to any power is 1, the recursive calls multiply 1 repeatedly, resulting in 1.
    assert power(a=1, b=5) == 1

def test_power_negative_base_positive_exponent():
    # (-3)^2 = (-3)*(-3) = 9, computed via recursive multiplication.
    assert power(a=-3, b=2) == 9

def test_power_negative_base_exponent_one():
    # When b is 1, the function returns a directly, so output is -4.
    assert power(a=-4, b=1) == -4
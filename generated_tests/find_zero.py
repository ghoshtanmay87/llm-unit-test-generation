import math

def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    begin, end = (-1.0, 1.0)
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2.0
        end *= 2.0
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center
    return begin

import pytest

def test_find_zero_root_at_minus_one():
    # Find zero for polynomial with root at x=-1 (polynomial x+1)
    xs = [1, 1]
    expected = -1.0
    result = find_zero(xs)
    assert result == expected

def test_find_zero_root_at_zero():
    # Find zero for polynomial with root at x=0 (polynomial x)
    xs = [0, 1]
    expected = -5.820766091346741e-11
    result = find_zero(xs)
    assert result == expected

def test_find_zero_root_at_one():
    # Find zero for polynomial with root at x=1 (polynomial x-1)
    xs = [-1, 1]
    expected = 0.9999999999417923
    result = find_zero(xs)
    assert result == expected

def test_find_zero_root_at_two():
    # Find zero for polynomial with root at x=2 (polynomial x-2)
    xs = [-2, 1]
    expected = 1.9999999999417923
    result = find_zero(xs)
    assert result == expected

def test_find_zero_root_at_one_double_root():
    # Find zero for polynomial with root at x=0.5 (polynomial 1 - 2x + x^2)
    xs = [1, -2, 1]
    expected = 0.9999999924912117
    result = find_zero(xs)
    assert result == expected

def test_find_zero_root_at_half():
    # Find zero for polynomial with root at x=0.5 (polynomial 2x - 1)
    xs = [-1, 2]
    expected = 0.49999999994179234
    result = find_zero(xs)
    assert result == expected
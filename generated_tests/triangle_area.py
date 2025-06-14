def triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area

import pytest

def test_valid_triangle_3_4_5():
    # Valid triangle with sides 3, 4, 5
    result = triangle_area(3, 4, 5)
    assert result == 6.0

def test_invalid_triangle_1_2_3():
    # Invalid triangle with sides 1, 2, 3 (sum of two sides equals the third)
    result = triangle_area(1, 2, 3)
    assert result == -1

def test_valid_triangle_7_10_5():
    # Valid triangle with sides 7, 10, 5
    result = triangle_area(7, 10, 5)
    assert result == 16.25

def test_invalid_triangle_1_1_2():
    # Invalid triangle with sides 1, 1, 2 (sum of two sides equals the third)
    result = triangle_area(1, 1, 2)
    assert result == -1

def test_valid_triangle_6_8_10():
    # Valid triangle with sides 6, 8, 10
    result = triangle_area(6, 8, 10)
    assert result == 24.0

def test_invalid_triangle_0_1_1():
    # Invalid triangle with sides 0, 1, 1 (zero length side)
    result = triangle_area(0, 1, 1)
    assert result == -1

def test_valid_equilateral_triangle_5_5_5():
    # Valid triangle with sides 5, 5, 5 (equilateral triangle)
    result = triangle_area(5, 5, 5)
    assert result == 10.83

def test_valid_triangle_2_5_3_5_4_5():
    # Valid triangle with sides 2.5, 3.5, 4.5
    result = triangle_area(2.5, 3.5, 4.5)
    assert result == 4.35
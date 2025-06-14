def discriminant_value(x,y,z):
    discriminant = (y**2) - (4*x*z)
    if discriminant > 0:
        return ("Two solutions",discriminant)
    elif discriminant == 0:
        return ("one solution",discriminant)
    elif discriminant < 0:
        return ("no real solution",discriminant)

import pytest

def test_discriminant_positive_two_distinct_real_solutions():
    result = discriminant_value(1, 5, 6)
    assert result == ("Two solutions", 1)

def test_discriminant_zero_one_real_solution():
    result = discriminant_value(1, 2, 1)
    assert result == ("one solution", 0)

def test_discriminant_negative_no_real_solutions():
    result = discriminant_value(1, 2, 3)
    assert result == ("no real solution", -8)

def test_discriminant_positive_larger_values():
    result = discriminant_value(2, 10, 3)
    assert result == ("Two solutions", 76)

def test_discriminant_zero_negative_coefficients():
    result = discriminant_value(1, -4, 4)
    assert result == ("one solution", 0)
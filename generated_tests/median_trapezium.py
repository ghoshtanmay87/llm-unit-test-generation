def median_trapezium(base1,base2,height):
 median = 0.5 * (base1+ base2)
 return median

import pytest

def test_median_trapezium_equal_bases():
    # Calculate median trapezium with equal bases
    base1 = 4
    base2 = 4
    height = 5
    expected = 4.0
    result = median_trapezium(base1, base2, height)
    assert result == expected

def test_median_trapezium_different_bases():
    # Calculate median trapezium with different bases
    base1 = 3
    base2 = 7
    height = 10
    expected = 5.0
    result = median_trapezium(base1, base2, height)
    assert result == expected

def test_median_trapezium_one_base_zero():
    # Calculate median trapezium with one base zero
    base1 = 0
    base2 = 8
    height = 6
    expected = 4.0
    result = median_trapezium(base1, base2, height)
    assert result == expected

def test_median_trapezium_floating_point_bases():
    # Calculate median trapezium with floating point bases
    base1 = 2.5
    base2 = 3.5
    height = 4
    expected = 3.0
    result = median_trapezium(base1, base2, height)
    assert result == expected

def test_median_trapezium_negative_bases():
    # Calculate median trapezium with negative bases
    base1 = -2
    base2 = 6
    height = 3
    expected = 2.0
    result = median_trapezium(base1, base2, height)
    assert result == expected
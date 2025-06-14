def diameter_circle(r):
  diameter=2*r
  return diameter

import pytest

def test_diameter_positive_integer_radius():
    # Calculate diameter for a positive integer radius
    r = 5
    expected = 10
    assert diameter_circle(r) == expected

def test_diameter_zero_radius():
    # Calculate diameter for zero radius
    r = 0
    expected = 0
    assert diameter_circle(r) == expected

def test_diameter_positive_float_radius():
    # Calculate diameter for a positive float radius
    r = 3.5
    expected = 7.0
    assert diameter_circle(r) == expected

def test_diameter_negative_radius():
    # Calculate diameter for a negative radius
    r = -4
    expected = -8
    assert diameter_circle(r) == expected

def test_diameter_very_small_radius():
    # Calculate diameter for a very small radius
    r = 0.0001
    expected = 0.0002
    assert diameter_circle(r) == expected
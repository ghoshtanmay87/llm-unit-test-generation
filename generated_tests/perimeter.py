def perimeter(diameter,height) : 
    return 2*(diameter+height)

import pytest

def test_perimeter_positive_integer_diameter_and_height():
    # Calculate perimeter with positive integer diameter and height
    diameter = 4
    height = 5
    expected = 18
    assert perimeter(diameter, height) == expected

def test_perimeter_zero_diameter_positive_height():
    # Calculate perimeter with zero diameter and positive height
    diameter = 0
    height = 7
    expected = 14
    assert perimeter(diameter, height) == expected

def test_perimeter_positive_diameter_zero_height():
    # Calculate perimeter with positive diameter and zero height
    diameter = 3
    height = 0
    expected = 6
    assert perimeter(diameter, height) == expected

def test_perimeter_zero_diameter_zero_height():
    # Calculate perimeter with both diameter and height as zero
    diameter = 0
    height = 0
    expected = 0
    assert perimeter(diameter, height) == expected

def test_perimeter_floating_point_diameter_and_height():
    # Calculate perimeter with floating point diameter and height
    diameter = 2.5
    height = 3.5
    expected = 12.0
    assert perimeter(diameter, height) == expected

def test_perimeter_negative_diameter_positive_height():
    # Calculate perimeter with negative diameter and positive height
    diameter = -1
    height = 4
    expected = 6
    assert perimeter(diameter, height) == expected

def test_perimeter_positive_diameter_negative_height():
    # Calculate perimeter with positive diameter and negative height
    diameter = 5
    height = -2
    expected = 6
    assert perimeter(diameter, height) == expected
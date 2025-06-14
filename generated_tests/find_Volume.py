def find_Volume(l,b,h) : 
    return ((l * b * h) / 2)

import pytest

def test_volume_all_positive_integers():
    # Calculate volume with all positive integers
    result = find_Volume(l=4, b=5, h=6)
    assert result == 60.0

def test_volume_with_zero_dimension():
    # Calculate volume with one dimension as zero
    result = find_Volume(l=0, b=5, h=6)
    assert result == 0.0

def test_volume_with_floating_point_dimensions():
    # Calculate volume with floating point dimensions
    result = find_Volume(l=3.5, b=2.0, h=4.0)
    assert result == 14.0

def test_volume_all_dimensions_one():
    # Calculate volume with all dimensions as one
    result = find_Volume(l=1, b=1, h=1)
    assert result == 0.5

def test_volume_large_integer_dimensions():
    # Calculate volume with large integer dimensions
    result = find_Volume(l=100, b=200, h=300)
    assert result == 3000000.0
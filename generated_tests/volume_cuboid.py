def volume_cuboid(l,w,h):
  volume=l*w*h
  return volume

import pytest

def test_volume_all_positive_integers():
    # Calculate volume with all positive integers
    result = volume_cuboid(l=2, w=3, h=4)
    assert result == 24

def test_volume_with_zero_dimension():
    # Calculate volume with one dimension as zero
    result = volume_cuboid(l=5, w=0, h=10)
    assert result == 0

def test_volume_with_floating_point_dimensions():
    # Calculate volume with floating point dimensions
    result = volume_cuboid(l=1.5, w=2.0, h=3.5)
    assert result == 10.5

def test_volume_all_dimensions_one():
    # Calculate volume with all dimensions as one
    result = volume_cuboid(l=1, w=1, h=1)
    assert result == 1

def test_volume_with_negative_dimension():
    # Calculate volume with one dimension as negative
    result = volume_cuboid(l=-2, w=3, h=4)
    assert result == -24
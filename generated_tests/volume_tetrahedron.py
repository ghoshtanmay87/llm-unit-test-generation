import math
def volume_tetrahedron(num):
	volume = (num ** 3 / (6 * math.sqrt(2)))	
	return round(volume, 2)

import pytest

def test_volume_tetrahedron_edge_length_1():
    # Calculate volume for edge length 1
    result = volume_tetrahedron(num=1)
    assert result == 0.12

def test_volume_tetrahedron_edge_length_2():
    # Calculate volume for edge length 2
    result = volume_tetrahedron(num=2)
    assert result == 0.47

def test_volume_tetrahedron_edge_length_3():
    # Calculate volume for edge length 3
    result = volume_tetrahedron(num=3)
    assert result == 1.91

def test_volume_tetrahedron_edge_length_0():
    # Calculate volume for edge length 0
    result = volume_tetrahedron(num=0)
    assert result == 0.0

def test_volume_tetrahedron_edge_length_1_point_5():
    # Calculate volume for edge length 1.5
    result = volume_tetrahedron(num=1.5)
    assert result == 0.4
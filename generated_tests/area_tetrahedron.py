import math
def area_tetrahedron(side):
  area = math.sqrt(3)*(side*side)
  return area

import pytest

def test_area_tetrahedron_side_1():
    # Calculate area of tetrahedron with side length 1
    result = area_tetrahedron(side=1)
    expected = 1.7320508075688772
    assert result == expected

def test_area_tetrahedron_side_2():
    # Calculate area of tetrahedron with side length 2
    result = area_tetrahedron(side=2)
    expected = 6.928203230275509
    assert result == expected

def test_area_tetrahedron_side_0():
    # Calculate area of tetrahedron with side length 0
    result = area_tetrahedron(side=0)
    expected = 0.0
    assert result == expected

def test_area_tetrahedron_side_0_5():
    # Calculate area of tetrahedron with side length 0.5
    result = area_tetrahedron(side=0.5)
    expected = 0.4330127018922193
    assert result == expected

def test_area_tetrahedron_side_10():
    # Calculate area of tetrahedron with side length 10
    result = area_tetrahedron(side=10)
    expected = 173.20508075688772
    assert result == expected
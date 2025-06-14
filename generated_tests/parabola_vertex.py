def parabola_vertex(a, b, c): 
  vertex=(((-b / (2 * a)),(((4 * a * c) - (b * b)) / (4 * a))))
  return vertex

import pytest

def test_vertex_standard_parabola_positive_a():
    # Calculate vertex for a standard parabola with positive a
    a = 1
    b = -4
    c = 3
    expected = (2.0, -1.0)
    assert parabola_vertex(a, b, c) == expected

def test_vertex_parabola_negative_a():
    # Calculate vertex for a parabola with negative a
    a = -1
    b = 2
    c = 1
    expected = (1.0, 2.0)
    assert parabola_vertex(a, b, c) == expected

def test_vertex_parabola_zero_b():
    # Calculate vertex for parabola with zero b
    a = 2
    b = 0
    c = -8
    expected = (0.0, -8.0)
    assert parabola_vertex(a, b, c) == expected

def test_vertex_parabola_zero_c():
    # Calculate vertex for parabola with zero c
    a = 1
    b = 6
    c = 0
    expected = (-3.0, -9.0)
    assert parabola_vertex(a, b, c) == expected

def test_vertex_parabola_all_zeros_except_a():
    # Calculate vertex for parabola with all zeros except a
    a = 1
    b = 0
    c = 0
    expected = (0.0, 0.0)
    assert parabola_vertex(a, b, c) == expected
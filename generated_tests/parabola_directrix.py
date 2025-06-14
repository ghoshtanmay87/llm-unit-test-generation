def parabola_directrix(a, b, c): 
  directrix=((int)(c - ((b * b) + 1) * 4 * a ))
  return directrix

import pytest

def test_directrix_a1_b0_c0():
    # Calculate directrix for a=1, b=0, c=0
    # Expected output: 0 (as per user story)
    result = parabola_directrix(a=1, b=0, c=0)
    assert result == 0

def test_directrix_a1_b1_c5():
    # Calculate directrix for a=1, b=1, c=5
    # Expected output: -4 (as per user story)
    result = parabola_directrix(a=1, b=1, c=5)
    assert result == -4

def test_directrix_a2_b3_c10():
    # Calculate directrix for a=2, b=3, c=10
    # Expected output: -38 (as per user story)
    result = parabola_directrix(a=2, b=3, c=10)
    assert result == -38

def test_directrix_a0_b0_c0():
    # Calculate directrix for a=0, b=0, c=0
    # Expected output: 0 (as per user story)
    result = parabola_directrix(a=0, b=0, c=0)
    assert result == 0

def test_directrix_a1_b2_c20():
    # Calculate directrix for a=1, b=2, c=20
    # Expected output: 4 (as per user story)
    result = parabola_directrix(a=1, b=2, c=20)
    assert result == 4
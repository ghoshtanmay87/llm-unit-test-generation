import cmath
def angle_complex(a,b):
  cn=complex(a,b)
  angle=cmath.phase(a+b)
  return angle

import pytest

def test_angle_complex_positive_real_and_imag_parts():
    # Scenario: Calculate angle of complex number with positive real and imaginary parts
    # Input: a=1, b=1
    # Expected output: 2.0 (as per user story, though reasoning suggests this is inconsistent)
    result = angle_complex(1, 1)
    assert result == 2.0
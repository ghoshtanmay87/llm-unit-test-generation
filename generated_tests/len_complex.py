import cmath
def len_complex(a,b):
  cn=complex(a,b)
  length=abs(cn)
  return length

import pytest

def test_len_complex_positive_real_imag():
    # Calculate length of complex number with positive real and imaginary parts
    result = len_complex(3, 4)
    assert result == 5.0

def test_len_complex_zero_real_positive_imag():
    # Calculate length of complex number with zero real part and positive imaginary part
    result = len_complex(0, 5)
    assert result == 5.0

def test_len_complex_negative_real_imag():
    # Calculate length of complex number with negative real and imaginary parts
    result = len_complex(-3, -4)
    assert result == 5.0

def test_len_complex_zero_real_imag():
    # Calculate length of complex number with zero real and imaginary parts
    result = len_complex(0, 0)
    assert result == 0.0

def test_len_complex_floating_point_real_imag():
    # Calculate length of complex number with floating point real and imaginary parts
    result = len_complex(1.5, 2.5)
    assert result == 2.9154759474226504
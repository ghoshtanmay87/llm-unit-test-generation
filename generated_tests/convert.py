import cmath  
def convert(numbers):    
  num = cmath.polar(numbers)  
  return (num)

import pytest

def test_convert_positive_real_number_to_polar():
    # Convert a positive real number to polar coordinates
    input_value = 3+0j
    expected = (3.0, 0.0)
    assert convert(input_value) == expected

def test_convert_purely_imaginary_positive_number_to_polar():
    # Convert a purely imaginary positive number to polar coordinates
    input_value = 4j
    expected = (4.0, 1.5707963267948966)
    assert convert(input_value) == expected

def test_convert_positive_real_and_imaginary_parts_to_polar():
    # Convert a complex number with positive real and positive imaginary parts
    input_value = 1+1j
    expected = (1.4142135623730951, 0.7853981633974483)
    assert convert(input_value) == expected

def test_convert_negative_real_positive_imaginary_to_polar():
    # Convert a complex number with negative real and positive imaginary parts
    input_value = -1+1j
    expected = (1.4142135623730951, 2.356194490192345)
    assert convert(input_value) == expected

def test_convert_zero_complex_number_to_polar():
    # Convert zero complex number to polar coordinates
    input_value = 0j
    expected = (0.0, 0.0)
    assert convert(input_value) == expected
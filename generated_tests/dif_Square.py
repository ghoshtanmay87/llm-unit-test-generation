def dif_Square(n): 
    if (n % 4 != 2): 
        return True
    return False

import pytest

def test_input_1_modulo_4_not_2():
    # Input is 1, which modulo 4 is not 2
    result = dif_Square(1)
    assert result is True

def test_input_2_modulo_4_equals_2():
    # Input is 2, which modulo 4 equals 2
    result = dif_Square(2)
    assert result is False

def test_input_6_modulo_4_equals_2():
    # Input is 6, which modulo 4 equals 2
    result = dif_Square(6)
    assert result is False

def test_input_8_modulo_4_not_2():
    # Input is 8, which modulo 4 equals 0
    result = dif_Square(8)
    assert result is True

def test_input_0_modulo_4_not_2():
    # Input is 0, which modulo 4 equals 0
    result = dif_Square(0)
    assert result is True
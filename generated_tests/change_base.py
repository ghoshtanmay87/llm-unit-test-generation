def change_base(x: int, base: int):
    ret = ''
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret

import pytest

def test_convert_decimal_10_to_base_2():
    # Convert decimal 10 to base 2
    result = change_base(10, 2)
    assert result == '1010'

def test_convert_decimal_0_to_any_base():
    # Convert decimal 0 to any base
    result = change_base(0, 10)
    assert result == ''

def test_convert_decimal_7_to_base_3():
    # Convert decimal 7 to base 3
    result = change_base(7, 3)
    assert result == '21'

def test_convert_decimal_100_to_base_10():
    # Convert decimal 100 to base 10
    result = change_base(100, 10)
    assert result == '100'

def test_convert_decimal_255_to_base_16():
    # Convert decimal 255 to base 16
    result = change_base(255, 16)
    assert result == '1515'
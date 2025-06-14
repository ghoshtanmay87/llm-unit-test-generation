def decimal_to_binary(decimal):
    return 'db' + bin(decimal)[2:] + 'db'

import pytest

def test_decimal_to_binary_zero():
    # Convert decimal 0 to binary string with 'db' prefix and suffix
    result = decimal_to_binary(0)
    assert result == 'db0db'

def test_decimal_to_binary_five():
    # Convert decimal 5 to binary string with 'db' prefix and suffix
    result = decimal_to_binary(5)
    assert result == 'db101db'

def test_decimal_to_binary_ten():
    # Convert decimal 10 to binary string with 'db' prefix and suffix
    result = decimal_to_binary(10)
    assert result == 'db1010db'

def test_decimal_to_binary_one():
    # Convert decimal 1 to binary string with 'db' prefix and suffix
    result = decimal_to_binary(1)
    assert result == 'db1db'

def test_decimal_to_binary_255():
    # Convert decimal 255 to binary string with 'db' prefix and suffix
    result = decimal_to_binary(255)
    assert result == 'db11111111db'
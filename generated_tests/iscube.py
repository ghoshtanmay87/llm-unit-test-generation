def iscube(a):
    a = abs(a)
    return int(round(a ** (1.0 / 3))) ** 3 == a

import pytest

def test_iscube_with_27():
    # Check if 27 is a perfect cube
    assert iscube(27) is True

def test_iscube_with_negative_27():
    # Check if -27 is a perfect cube
    assert iscube(-27) is True

def test_iscube_with_16():
    # Check if 16 is a perfect cube
    assert iscube(16) is False

def test_iscube_with_0():
    # Check if 0 is a perfect cube
    assert iscube(0) is True

def test_iscube_with_1():
    # Check if 1 is a perfect cube
    assert iscube(1) is True

def test_iscube_with_64():
    # Check if 64 is a perfect cube
    assert iscube(64) is True

def test_iscube_with_65():
    # Check if 65 is a perfect cube
    assert iscube(65) is False

def test_iscube_with_negative_1():
    # Check if -1 is a perfect cube
    assert iscube(-1) is True

def test_iscube_with_1000():
    # Check if 1000 is a perfect cube
    assert iscube(1000) is True

def test_iscube_with_999():
    # Check if 999 is a perfect cube
    assert iscube(999) is False
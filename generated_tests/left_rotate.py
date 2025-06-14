def left_rotate(s,d):
    tmp = s[d : ] + s[0 : d]
    return tmp

import pytest

def test_rotate_string_abcdef_by_2_positions():
    s = 'abcdef'
    d = 2
    expected = 'cdefab'
    assert left_rotate(s, d) == expected

def test_rotate_string_hello_by_0_positions():
    s = 'hello'
    d = 0
    expected = 'hello'
    assert left_rotate(s, d) == expected

def test_rotate_string_rotation_by_length_8_positions():
    s = 'rotation'
    d = 8
    expected = 'rotation'
    assert left_rotate(s, d) == expected

def test_rotate_string_python_by_3_positions():
    s = 'python'
    d = 3
    expected = 'honpyt'
    assert left_rotate(s, d) == expected

def test_rotate_empty_string_by_5_positions():
    s = ''
    d = 5
    expected = ''
    assert left_rotate(s, d) == expected
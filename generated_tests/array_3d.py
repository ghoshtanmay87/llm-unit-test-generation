def array_3d(m,n,o):
 array_3d = [[ ['*' for col in range(m)] for col in range(n)] for row in range(o)]
 return array_3d

import pytest

def test_create_3d_array_1x1x1():
    # Scenario: Create a 3D array with dimensions 1x1x1
    m, n, o = 1, 1, 1
    expected = [[['*']]]
    result = array_3d(m, n, o)
    assert result == expected

def test_create_3d_array_2x2x2():
    # Scenario: Create a 3D array with dimensions 2x2x2
    m, n, o = 2, 2, 2
    expected = [[['*', '*'], ['*', '*']], [['*', '*'], ['*', '*']]]
    result = array_3d(m, n, o)
    assert result == expected

def test_create_3d_array_3x1x2():
    # Scenario: Create a 3D array with dimensions 3x1x2
    m, n, o = 3, 1, 2
    expected = [[['*', '*', '*']], [['*', '*', '*']]]
    result = array_3d(m, n, o)
    assert result == expected

def test_create_3d_array_1x3x1():
    # Scenario: Create a 3D array with dimensions 1x3x1
    m, n, o = 1, 3, 1
    expected = [[['*'], ['*'], ['*']]]
    result = array_3d(m, n, o)
    assert result == expected

def test_create_3d_array_0x2x2():
    # Scenario: Create a 3D array with dimensions 0x2x2 (zero columns)
    m, n, o = 0, 2, 2
    expected = [[[], []], [[], []]]
    result = array_3d(m, n, o)
    assert result == expected
def centered_hexagonal_number(n):
  return 3 * n * (n - 1) + 1

import pytest

def test_centered_hexagonal_number_n_1():
    # Calculate centered hexagonal number for n=1
    result = centered_hexagonal_number(1)
    assert result == 1

def test_centered_hexagonal_number_n_2():
    # Calculate centered hexagonal number for n=2
    result = centered_hexagonal_number(2)
    assert result == 7

def test_centered_hexagonal_number_n_3():
    # Calculate centered hexagonal number for n=3
    result = centered_hexagonal_number(3)
    assert result == 19

def test_centered_hexagonal_number_n_4():
    # Calculate centered hexagonal number for n=4
    result = centered_hexagonal_number(4)
    assert result == 37

def test_centered_hexagonal_number_n_5():
    # Calculate centered hexagonal number for n=5
    result = centered_hexagonal_number(5)
    assert result == 61